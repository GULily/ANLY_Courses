## ANLY 502 Assignment 1: Getting started with AWS

The purpose of this assignment is for you to become familiar with
Amazon Web Services (AWS) and to run your first map/reduce job.

## Required skills and technologies

* Git (command line)

* SSH (makeing keys and logging in to remote systems)

* AWS (creating VMs)

* S3  (Fetching data, creating a bucket, storing data).

Note: The code has only been tested on MacOS and Linux. If you are
using Windows, we recommend that you exclusively solve the homework in
a virtual machine at Amazon, and that you only use your Windows
computer for logging in to the remote server.

## Preparation 

Start by making a [***fork***](https://confluence.atlassian.com/bitbucket/forking-a-repository-221449527.html) or a [***clone***](https://confluence.atlassian.com/bitbucket/clone-a-repository-223217891.html) of the course repository. (Note: We
recommend forking the [BitBucket Repository][1] so that you can have a
private repository, and then that you clone your forked repository to the computer on which
you are working.) Enter the `/A1` directory of the repository (where
this file is located).

[1]: https://ANLY502@bitbucket.org/ANLY502/anly502_2017_spring.git

## Question 1

Provide the URL of your git repository in a file called `q1.txt`. We will verify this repository to make sure that it is not publicly available.

Note: you should be able to create the output with the following command:

    git config --get remote.origin.url > q1.txt

If you are interested, we will verify that the repository cannot be accessed by running this command:

    curl `cat q1.txt` 

After you create or modify a file in your clone of the repository and
you want to "save your work," you should commit your changes to the
local repository (e.g. `git commit -m "some message" -a`) and then
push the changes back to your remote repository (e.g. `git push`). If you are using BitBucket, you can make this easier by [configuring the git server to accept your ssh key](https://confluence.atlassian.com/bitbucket/set-up-ssh-for-git-728138079.html). When you log into a remote server
(for example, at AWS), you will use [ssh agent forwarding](https://developer.github.com/guides/using-ssh-agent-forwarding)
so that the public key from your laptop can be used by your remote
virtual machine. This avoids having to store secrets (e.g. your _ssh_ private key) on the remote
server, and also makes is so that you don't have to keep adding new
public keys to BitBucket (or github) to get your work done.
    
While you work on this assignment, you'll likely find that you have a
copy of your git repository checked out on both your laptop and on the
VM at Amazon. You keep them in sync by doing a `pull` and
`push` operations on each as you make changes.
    
## Question 2

With your AWS account, create a [**t2.nano**](https://aws.amazon.com/ec2/instance-types/) or **t2.micro** instance and log into
it. This instance t2.nano instance has 0.5GiB of memory, uses EBS for local storage and costs 0.59 cents/hour ($51/year), but the t2.micro instance is eligible for the _free tier_ while the t2.nano is not. Either works well. 

(Note: if you need more memory but it doesn't need to be fast, you can
add virtual memory to this instance by creating a swap file on the EBS
device. However, for serious work you would want to create a larger
instance.)

Install Python3.5 and the Python package `PyYAML`. Do this with the commands:

    sudo yum -y install python35 python35-pip
    sudo pip-3.5 install PyYAML

Use the `traceroute` command and create a traceroute to the host
ns1.georgetown.edu, one of the Georgetown University Internet name
servers. (Unlikely [www.georgetown.edu](http://www.georgetown.edu),
which is hosted at Akami, and
[cs.georgetown.edu](http://cs.georgetown.edu), which is hosted at
Amazon AWS, ns1.georgetown.edu is hosted at Georgetown itself.) Save
the traceroute in a file called `q2.txt`. You can do that with this
command:

    traceroute ns1.georgetown.edu > q2.txt

In this part of the problem set, we will be working with a text file in the 1-100GB range. The file contains hypothetic measurements of a
scientific instrument called a _quazyilx_ that has been specially
created for this class. Every few seconds the quazyilx makes four measurements: _fnard_, _fnok_, _cark_ and _gnuck_. The output looks like this:

    YYYY-MM-DDTHH:MM:SSZ fnard:10 fnok:4 cark:2 gnuck:9

(This time format is called [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) and it has the advantage that it is both unambigous and that it sorts properly. The Z stands for _Greenwich Mean Time_ or GMT, and is sometimes called _Zulu Time_ because the [NATO Phonetic Alphabet](https://en.wikipedia.org/wiki/NATO_phonetic_alphabet) word for **Z** is _Zulu_.)

When one of the measurements is not present, the result is displayed as negative 1 (e.g. `-1`). 

The quazyilx has been malfunctioning, and occasionally generates output with a `-1` for all four measurements, like this:

    2015-12-10T08:40:10Z fnard:-1 fnok:-1 cark:-1 gnuck:-1

Your job is to find all of the times where the four instruments malfunctioned together. The easy way to do this is with the `grep` command. Unfortunately, as you can see, the file is *big*. We have stored the file in Amazon S3. There are three ways that you can filter to find the bad records:

***Method 1*** - copy the file to your AWS VM (slow!) and use
   `grep`. (If you need to count, you can also use `wc`). 

***Method 2*** - stream the file from S3 to your AWS VM with the AWS steaming command and use `grep` as it goes by. To stream from Amazon S3 to standard out, you use the command:

    aws s3 cp s3://<bucket>/<filename> -

***Method 3*** - Use Hadoop running on one or more VMs to search the file in parallel, with each Hadoop worker starting at a different point.


## Question 3

First, make sure that you are able to run `aws` commands on your instance by trying to list the contents of the course S3 bucket `s3://gu-anly502/`. Below we use the `aws s3 ls` command to do that:

	[ec2-user@ip-172-31-52-185 A1]$ aws s3 ls s3://gu-anly502/
	                           PRE A1/
	                           PRE gutenberg/
	                           PRE maxmind/
	2016-03-05 14:21:58       1150 bootstrap-.bashrc
	2016-03-21 02:58:57       2735 bootstrap.sh
	2016-03-05 02:18:43       1237 startup.sh
	[ec2-user@ip-172-31-52-185 A1]$

In this question we will work with the 4.8GB file `s3://gu-anly502/A1/quazyilx1.txt`.

Determine the amount of time that Method 1 takes by copying the
file `s3://gu-anly502/A1/quazyilx1.txt` from S3 to your instance VM and reporting the amount
of time that it takes to do the copy operation, the amount of time to
takes to do the scan, and the total number of lines that indicate a
malfunction. Store this in a file called
`q3.txt`. Your file should have this format:


    # download and serch to a t2.nano instance
    source: s3://gu-anly502/A1/quazyilx1.txt   # should be proper S3 URL
    date: 2016-02-04T10:10:10                   # Date, in ISO-8601 time
    mode: download
    download: 100                               # in seconds
    search: 200                                 # also in seconds
    malfunctions: 42                            # in lines

(Of course, the numbers will be different in your case.) If you are interested, this file is in [YAML](http://yaml.org/) format. The information after the `#` are comments and ignored.

## Question 4

Determine the amount of time that Method 1 takes by streaming
the file from S3 to your VM and reporting the amount of time that
the search takes and the number of lines indicating a
malfunction. Perform the streaming by using the `aws s3 cp` command and copying from the S3 URL to the device `-`, and then piping the result into a `grep` process. 

Store your report in a file called `q4.txt`. Your file should have the format:

    # streaming to a t2.nano
    date: 2016-02-04T10:10:10   # Date, in ISO-8601 time
    mode: streaming
    streaming: 150 
    malfunctions: 42 

Now, add your files to your local repository, push the changes to your git server, and shut down your VM. 

Extra credit (1 point): Create a program called `streaming-time.py` which performs this benchmark automatically. Your program should take two parameters: the source URL and the destination filename. A skeleton program has been provided.


## Question 5

Create a t2.large instance and repeat the streaming exercise. Store the results in a file called `q5.txt` the results:

    # streaming to a t2.large
    date: 2016-02-04T10:10:10   # Date, in ISO-8601 time
    mode: streaming 
    streaming: 150
    malfunctions: 42

## Question 6

Finally, we want you to give us a list of the malfunction entries. You
will place them in a file and store that file on S3.

Place the malfunction entries in a file called `q6-malfunctions.txt`.

## Question 7

Create an S3 bucket that is world-readable. Enable the S3 web server,
so that the content of the bucket can be read via HTTP. Store the file `q6-malfunctions.txt` in that bucket. 

In a file called `q7.txt`, place the following information:

    s3: **YOUR*S3*URL**
    http: **YOUR*S3*HTTP*URL**

(Where `**YOUR*S3*URL**` is actually the URL from which your file can
be retrieved using S3 protocols, and `**YOUR*S3*HTTP*URL**` is the
URL from which is can be retrieved using any web browser.)

## To Submit
Place all of your files in this directory and type "make submit." Our
validator will check to make sure that each file is in the proper
format, which means that they are ***TEXT FILES*** with [UNIX Line
Discipline](https://en.wikipedia.org/wiki/Line_discipline). The submission program will then make a ZIP file, relying
on the file `user.cfg` in the root of the GIT repository for your configuration information.

Upload this ZIP file to Canvas. (Note: If we can't get auto-grading on
Canvas to work, we will have an alternative submission strategy posted.)




    


