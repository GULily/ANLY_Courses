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

paypal = 0
count2013, count2014, count2015, count2016, count2017 = 0, 0, 0, 0, 0
for i in range(len(data["data"])):
    if data["data"][i][8][0:4] == "2013":
        count2013 += 1
    elif data["data"][i][8][0:4] == "2014":
        count2014 += 1
    elif data["data"][i][8][0:4] == "2015":
        count2015 += 1
    elif data["data"][i][8][0:4] == "2016":
        count2016 += 1
    elif data["data"][i][8][0:4] == "2017":
        count2017 += 1

    if data["data"][i][15] == "PayPal Holdings, Inc.":
        paypal += 1

print("2013\t", count2013)
print("2014\t", count2014)
print("2015\t", count2015)
print("2016\t", count2016)
print("2017\t", count2017)
print("Paypal\t", paypal)

with open('complaints.txt','w') as f:
    f.write("2013\t" + str(count2013) + "\n")
    f.write("2014\t" + str(count2014) + "\n")
    f.write("2015\t" + str(count2015) + "\n")
    f.write("2016\t" + str(count2016) + "\n")
    f.write("2017\t" + str(count2017) + "\n")

with open('paypal.txt','w') as f:
    f.write("Paypal\t" + str(paypal) + "\n")
