import json
import urllib.request

data = json.loads(urllib.request.urlopen("http://data.consumerfinance.gov/api/views/7zpz-7ury/rows.json").read().decode('utf-8'))
# print(type(data))
# print(type(data["meta"]))
# print(type(data["data"]))
#
# print(len(data))
# print(len(data["meta"]))
# print(len(data["data"]))

# print(data["data"][0][15])
# print(data["data"][1][15])
# print(data["data"][86634][15])

if __name__ == "__main__":
    # Get your sparkcontext and make a dataframe
    from pyspark.sql import SparkSession

    spark = SparkSession.builder.appName("complaints").getOrCreate()
    sc = spark.sparkContext  # get the context

    import json
    import urllib.request
    data = json.loads(
        urllib.request.urlopen("http://data.consumerfinance.gov/api/views/7zpz-7ury/rows.json").read().decode('utf-8'))
    lines = data["data"]
    original = sc.parallelize(lines)
    # original = sc.textFile(data["data"])
    # parts = original.map(lambda l: l.split(','))
    from pyspark.sql import Row
    rows = original.map(lambda p: Row(year=p[8][0:4], company=p[15]))
    df = spark.createDataFrame(rows)
    df.cache()
    df.createOrReplaceTempView("complaints")

    # Print how many rows we have
    print("2013\t{}".format(spark.sql("select count(*) from complaints where year=='2013'").collect()))
    print("2014\t{}".format(spark.sql("select count(*) from complaints where year=='2014'").collect()))
    print("2015\t{}".format(spark.sql("select count(*) from complaints where year=='2015'").collect()))
    print("2016\t{}".format(spark.sql("select count(*) from complaints where year=='2016'").collect()))
    print("2017\t{}".format(spark.sql("select count(*) from complaints where year=='2017'").collect()))


