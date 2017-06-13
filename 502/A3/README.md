# ANLY 502 Assignment 3 Version 1.0
# Due Sunday, February 19th, 12:01pm


_Note: Read this assignment online at [https://bitbucket.org/ANLY502/anly502_2017_spring/src/HEAD/A3/?at=master](https://bitbucket.org/ANLY502/anly502_2017_spring/src/HEAD/A3/?at=master)_

In this problem set, you will analyze a network flow dataset that was created for this course. 

This dataset is based on the [`mtr`](https://en.wikipedia.org/wiki/MTR_(software)) command, a popular open source _traceroute_ command that has an interactive, character-based display. The program performs multiple traceroute operations over time and displays the results.  One of the common uses of the `mtr` command is to diagnose network problems.  Take a moment now and [review the Wikipedia page for the mtr command](https://en.wikipedia.org/wiki/MTR_(software)).

The `mtr` command has an option to produce output as a text file.  Here is an example of the output:

    MTR.0.85;1482973562;OK;www.comcast.com;1;192.168.10.1;1669
    MTR.0.85;1482973562;OK;www.comcast.com;2;96.120.104.177;16404
    MTR.0.85;1482973562;OK;www.comcast.com;3;68.87.130.233;11504
    MTR.0.85;1482973562;OK;www.comcast.com;4;ae-53-0-ar01.capitolhghts.md.bad.comcast.net (68.86.204.217);14874
    MTR.0.85;1482973562;OK;www.comcast.com;5;be-33657-cr02.ashburn.va.ibone.comcast.net (68.86.90.57);13030
    MTR.0.85;1482973562;OK;www.comcast.com;6;be-10102-cr01.newark.nj.ibone.comcast.net (68.86.85.162);19641
    MTR.0.85;1482973562;OK;www.comcast.com;7;be-10203-cr02.newyork.ny.ibone.comcast.net (68.86.85.186);18920
    MTR.0.85;1482973562;OK;www.comcast.com;8;be-10305-cr02.350ecermak.il.ibone.comcast.net (68.86.85.202);40477
    MTR.0.85;1482973562;OK;www.comcast.com;9;be-7922-ar02-d.northlake.il.ndcchgo.comcast.net (68.86.87.70);40555
    MTR.0.85;1482973562;OK;www.comcast.com;10;69.139.178.142;59072
    MTR.0.85;1482973562;OK;www.comcast.com;11;???;0

In this example, `mtr` has been used from a home to the host `www.comcast.com`. The fields are separated by semicolons. The fields are:

1. Version number, in this case `MTR.0.85`
2. The [Unix timestamp](https://en.wikipedia.org/wiki/Unix_time) of when the `mtr` command was started.
3. An `OK` indicating that the command terminated successfully.
4. The number of hops out that the [ICMP](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol) [PING](https://en.wikipedia.org/wiki/Ping_(networking_utility)) packet traveled before it returned.
5. If the `mtr` command can resolve the hostname of the remote system, the line contains the host name of the remote system that the PING packet reached, and its IP address in parenthesis. Otherwise, `mtr` outputs simply the IP address. If the packet is not returned, `mtr` outputs three question marks (i.e. `???`).
6. The number of microseconds that the packet required for the round-trip. If the ECHO packet was not received, this number is zero.

From July 1, 2016 through Dec 28, 2016, we ran `mtr` every minute, generating _traceroute_ results from a [Raspberry PI](https://en.wikipedia.org/wiki/Raspberry_Pi) computer to the host `www.comcast.com`. The Raspberry PI is connected by Ethernet to a Apple Airport Extreme Router, that is connected to a Comcast cable modem. Thus, all of the variability between subsequent runs of the `mtr` command are the result of congestion and other network issues within the Comcast network.  

In this assignment, you will develop software to help analyze this dataset. A truism of data science is that it is always easier to collect data than to analyze it. For example, if you scour the Internet you will find many resources for _generating_ `traceroute` data, but you will find practically no resources for _analyzing_ `traceroute` data.

We set up the $35 Raspberry PI to collect this data because we observed that the Comcast performance was inconsistent. But why was it inconsistent? Network congestion? Is it worse on different days, or at different times of the day? Is the problem congestion, or is it reliability---are there links that are going down?  In this problem set, you'll perform an analysis that can help answer these questions.


## Understanding the dataset

The Raspberry PI was configured to run a traceroute every minute from the home network to `www.comcast.com`. The rational of choosing `www.comcast.com` is that the host was likely to be inside the Comcast network, so we weren't looking at problems that might originate elsewhere. We have uploaded the output of the `mtr` command to [s3://gu-anly502/A3/mtr.www.comcast.com.2016.txt](s3://gu-anly502/A3/mtr.www.comcast.com.2016.txt). This 206MB output file has 2,397,086 lines resulting from  a total of 260,499 invocations of the `mtr` command. 

This output is not very large, and you could easily analyze it on your laptop. However, in this class, we ask that you analyze it on Amazon using MRJOB and Hadoop.

Here are some questions that we will try to answer:

* How consistent is the Comcast network? 
* How often are there changes within the Comcast network? 
* How much redundancy is there within the Comcast network?

Here are some questions we will not be answering:

* Are the changes in the Comcast network a response to network problems? (You could tell this if the changes happen after a network problem, and then the problem goes away.)
* Can you distinguish network outages from outages at the end-user location where the Raspberry PI was running?  (Yes, you can: a power failure will result in a gap between subsequent `mtr` invocations. We aren't looking for them in this problem set, but you can!)
* Are we getting the service that we are paying for?

We won't be able to answer all of these questions in **A3**, but you might think about answering them in a final project. Also, note that that analyzing this dataset is a *passive analysis* project, but for your final project you could carry out your own measurements.

## Getting Started

As collected, the dataset is hard to analyze, because each time we invoke the `mtr` command the result may be one or more lines.  So the first thing to do is to turn the multi-line format into a new format where each invocation results in a single line. This single line will be easier to analyze. 

To help you get started, you will find in the repository a file called [`A3/mtr.www.comcast.com.2016.subset.txt`](mtr.www.comcast.com.2016.subset.txt) that contains a subset of the dataset, and a program called [`ingest_mtr.py`](ingest_mtr.py) that reads any `mtr`-formatted text file and outputs complete records. The record consists of a timestamp and one or more quads, all separated by commas, where each quad consists of:

* Step number (1..N)
* Hostname of the remote system (or null)
* IP address of the remote system
* The number of microseconds for the response

The splitting of the name returned by `mtr` into a hostname and IP address is done with a regular expression. You should examine the source code of the `ingest_mtr.py` program to see how this is done.

The first record looks like this:

    2016-07-01T00:01:01,1,,192.168.10.1,1798,2,,96.120.104.177,9739,3,,68.87.130.233,11766,4,ae-53-0-ar01.capitolhghts.md.bad.comcast.net,68.86.204.217,11203,5,be-33657-cr02.ashburn.va.ibone.comcast.net,68.86.90.57,14575,6,he-0-2-0-0-ar01-d.westchester.pa.bo.comcast.net,68.86.94.226,17923,7,bu-101-ur21-d.westchester.pa.bo.comcast.net,68.85.137.213,16070,8,,68.87.29.59,16761

Even with our preprocessing script, this is a challenging assignment because every input line has a (potentially) different length. 

The dataset represents a series of paths through the Internet at different times. The first four hops of the line above are shown again below:

    1,,192.168.10.1,1798,2,,96.120.104.177,9739,3,,68.87.130.233,11766,4,ae-53-0-ar01.capitolhghts.md.bad.comcast.net,68.86.204.217,11203,...
    
This extract represents three hops:

    192.168.10.1 -> 96.120.104.177      (9739 usec from 192.168.10.1)
    96.120.104.177 -> 68.87.130.233     (11766 usec from 192.168.10.1)
    68.87.130.233 -> 68.86.204.217      (11203 usec from 192.168.10.1)
    
Schematically, we can call this:

    A->B->C->D

Where A is `192.168.10.1`, B is `96.120.104.177`, C is `68.87.130.233` and D is `68.86.204.217`

**How is it possible that it took longer to reach C (11766 usec) than D (11203 usec), given that C is closer than D?** The answer is that these were separate ICMP ECHO (ping) packets that were sent out, and the amount of time that it takes for the response to come back is not always the same---it depends on network congestion. 
        
Sometimes you might want to look for a link that goes down and comes back up. Of course, if a link goes down, the _traceroute_ done by `mtr` will stop. So you might end up seeing data that looks like this:

    1: A->B->C->D->E
    2: A->B->C->D->E
    3: A->B->C->D->E
    4: A->B->C->D->E
    5: A->B->C;    
    6: A->B->C;    
    7: A->B->C;    
    8: A->B->C->D->E
    9: A->B->C->D->E

In this example, the link between C and D went down at time 5 and came back up at time 8. The link between D and E may have been up at times 5, 6 and 7, but it may not have been. We have no way of telling for sure.

Note: there are some IP addresses in this dataset that have more than one hostname!

## Question 1: Rough Characterization

Start by creating an EMR cluster that has a single Master node and no Core or Task nodes (you won't need them).  Do not forget to use the bootstrap code! Log into the Master node and clone the course git repository. We will be working in the `A3/` directory.

In Question 1 we are asking that you characterize the data. You should answer all of these questions by using `ingest_mtr.py` to process the dataset into single records and store this as a file in your  and then storing the results either in S3 or HDFS. 

Start by copying the MTR data in S3 to your local computer and use the `ingest_mtr.py` program to transform the data into a local file. You will use this file as the input to `mrjob` and will store the results in output files. 

1. We have given you a [MRJOB](https://github.com/Yelp/mrjob) prototype called `q1_ipaddresses.py`. You need to modify this program so that it will compute how many different IP addresses are in the dataset.  Store the output of your program in a file called `q1_ipaddresses.txt`. Each line of the file should have the format:

    _ipaddress_`\t`_count_ 
    
    (Where `\t` is the TAB character.) The file does not need to be sorted.

2. Create a mapper and reducer with MRJOB called `q1_hostnames.py` that computes how many different hostnames are in the dataset.  Store the output of your program in a file called `q1_hostnames.txt`. Each line of the file should have the format:

    _hostname_`\t`_count_
    
    The file does not need to be sorted.
    
## Question 2: Multiple Names per IP address

Find the IP addresses that have more than one hostname.  

1. Create a program that does this called `q2_multiple.py` and store the results in an output called `q2_multiple.txt`. Your output file should have this format:

    _ipaddress_`\t`_hostname1_ , _hostname2_
    
    
If you feel particularly motivated, you can determine the time for each hostname, and see if the two names overlap in time or if the name changes from one name to the other. 

## Question 3: Link Analysis

For this question, we define a _link_ as the connection from one host to another host. You can compute the time associated with the first host from the time associated with the second host. So if the highest step number on a line is 5, that line describes 4 links.

1. Create a link analysis program with MRJOB named `q3_links.py` that will analyze the dataset for *every link in the dataset*. Run this program and pipe the output into a file `q3_links.txt` that contains, *for each link*, a line in the following format:

     IPADDRESS1`->`IPADDRESS2`\t`COUNT
     
There will be many lines in this file, one for each different link taken by a packet.

2. Modify `q3_links.py` so that it calculates the [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation) for the time taken by each hop. Run this program and pipe the output into a file called `q3_linksdev.txt` that has this format:

     IPADDRESS1`->`IPADDRESS2`\t`COUNT`\t`STDDEV
     
     The file does not need to be sorted.
     
Turn in `q3_links.py` and `q3_linksdev.txt`.      
     
## Question 4: Time Analysis      

Finally, let's look at how Comcast's residential distribution network might be impacted by people watching videos in the evenings. That is, we're going to look for the "Netflix" effect. To do this, we will restrict our analysis of the standard deviation of the link from the 2nd hop to the 3rd hop (Comcast's residential distribution network), and see how it changes for different times of the day.  

1. Create a new program using MRJOB called `q4_hop23.py` that computes the standard deviation between the 2nd and 3rd hop of the dataset by time of day. Generate an output file `q4_hop23.txt` that has this form:

     HOUR`\t`STDDEV
     
For example, if the standard deviation was 2.0 between 3pm and 3:59pm and 3.0 between 4pm and 4:59pm, your output file would look like this:

    15  2.0
    16  3.0
    
     
## Extra Credit

1. For extra credit, create a program called `q4_grapher.py` that reads the file `q4_hop23.txt`, and makes a graph of this dataset with matplotlib, saving the result in a file called  `q4_graph.png`.

## Other ideas

Here are some other things that you could do with the dataset:

* Figure out which links are the least reliable. 
* When does Comcast change the topology of the network? Is it correlated with network outages?
* When are the names associated with IP addresses changed? Does it correlate with other network changes?

Is there a better way to do this analysis?  There are graph-oriented databases. Are they better for doing this kind of analysis?


