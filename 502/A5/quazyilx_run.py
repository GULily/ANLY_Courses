#!/usr/bin/env python3
#
# Run this program with spark-submit

import sys,os,datetime,re,operator
from pyspark import SparkContext, SparkConf


QUERIES = [["total_rows", "select count(*) from quazyilx"],
           ["total_errors", "SELECT count(*) FROM quazyilx WHERE fnard == -1 AND fnok == -1 AND cark == -1 AND gnuck == -1"],  # 3
           ["one_error_others_gt5", "SELECT count(*) FROM quazyilx WHERE fnard == -1 AND fnok>5 AND cark>5"],  # 21141
           ["first_date", "SELECT FIRST(datetime) FROM quazyilx"],            # 2000-01-01T00:00:03
           ["last_date", "SELECT LAST(datetime) FROM quazyilx"],              # 2000-03-04T14:51:25
           ["first_error_date", "SELECT FIRST(datetime) FROM quazyilx WHERE fnard == -1 AND fnok == -1 AND cark == -1 AND gnuck == -1"],  # 2000-01-28T03:07:44
           ["last_error_date", "SELECT LAST(datetime) FROM quazyilx WHERE fnard == -1 AND fnok == -1 AND cark == -1 AND gnuck == -1"]     # 2000-03-01T17:31:22
]


if __name__=="__main__":
    # Get your sparkcontext and make a dataframe
    from pyspark.sql import SparkSession
    spark = SparkSession.builder.appName("quazyilx").getOrCreate()
    sc    = spark.sparkContext      # get the context
    
    # Replace this code with your own
    # print("*** Verifying that Spark works ***",file=sys.stderr)
    # res = sc.parallelize(range(1,1000)).reduce(operator.add)
    # print("*** Result = {}  (should be 499500) ***".format(res),file=sys.stderr)
    # assert res==499500

    # Create an RDD from s3://gu-anly502/A1/quazyilx1.txt
    # NOTE: Do this with 1 master m3.xlarge, 2 core m3.xlarge, and 4 task m3.xlarge
    # otherwise it will take forever...
    # ipyspark --files quazyilx.py
    original = sc.textFile("s3://gu-anly502/A1/quazyilx0.txt")
    import quazyilx
    parts = original.map(lambda l: quazyilx.Quazyilx(l))
    from pyspark.sql import Row
    rows = parts.map(lambda q: Row(datetime=q.datetime.isoformat(), fnard=q.fnard, fnok=q.fnok, cark=q.cark, gnuck=q.gnuck))
    # register your dataframe as the SQL table quazyilx
    # You probably want to cache it, also!
    df = spark.createDataFrame(rows)
    df.cache()
    df.createOrReplaceTempView("quazyilx")

    # Print how many rows we have
    print("rows: {}".format(spark.sql("select count(*) from quazyilx").collect()))

    # Now do the queries
    for (var,query) in QUERIES:
        print("{}-query: {}".format(var,query))
        if query:
            query_result = spark.sql(query).collect()
            print("{}: {}".format(var,query_result))
