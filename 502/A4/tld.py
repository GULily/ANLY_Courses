#!/usr/bin/env python3.4
#
# Insert your tld.py function below.


def tld(s):
    import re
    m = re.search(".*\.(\w+)", s)
    if m:
        return m.group(1)
    else:
        return s


tlds = top1m.map(tld)
tlds_and_counts = tlds.countByValue()
counts_and_tlds = [(count, domain) for (domain, count) in tlds_and_counts.items()]
counts_and_tlds.sort(reverse=True)
counts_and_tlds[0:50]
open("q3_counts.txt","w").write(str(counts_and_tlds[0:50]))
