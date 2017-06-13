#!/usr/bin/env python3
#
# Run this program with spark-submit

import sys,os,datetime,re,operator
from pyspark import SparkContext, SparkConf



if __name__=="__main__":
    # Get your sparkcontext and make a dataframe
    from pyspark.sql import SparkSession
    spark = SparkSession.builder.appName("fwiki").getOrCreate()
    sc    = spark.sparkContext      # get the context
    
    # Create an RDD from s3://gu-anly502/logs/forensicswiki.2012.txt
    url = "s3://gu-anly502/logs/forensicswiki.2012.txt"
    # NOTE: Do this with 1 master m3.xlarge, 2 core m3.xlarge, and 4 task m3.xlarge
    # otherwise it will take forever...
    # ipyspark --files quazyilx.py
    loglines = sc.textFile(url)
    import fwiki
    logs = loglines.map(lambda l: fwiki.LogLine(l))
    logs = logs.map(lambda l: fwiki.LogLine.row(l))
    df = spark.createDataFrame(logs)
    df.cache()
    # Register the dataframe as an SQL table called 'log'
    df.createOrReplaceTempView("log")
    # Print how many log lines there are
    print("Total Log Lines: {}".format(spark.sql("select count(*) from log").collect()))

    # Figure out when it started and ended
    (start,end) = spark.sql("select min(datetime),max(datetime) from log").collect()[0]
    print("Date range: {} to {}".format(start,end))

    # Now generate the requested output
    output = spark.sql("SELECT SUBSTR(datetime, 1, 7), COUNT(1) FROM log GROUP BY 1").collect()
    for i in range(14):
        (month, hits) = output[i]
        print("{}\t{}".format(month, hits))

