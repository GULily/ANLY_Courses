top1k = top1m.take(1000)
top1k = sc.parallelize(top1k)
domains = top1k.map(lambda line: line[line.find(',')+1:])
results = domains.filter(google_analytics)
results.collect()




