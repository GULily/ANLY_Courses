import sys
import os,datetime,re

# We are giving you the regular expression!

CLR_RE = re.compile(r'^(\S+) (\S+) (\S+) \[([^\]]+)\] "(\S+) (\S+) \S+" (\S+) (\S+) "([^"]*)" "([^"]*)"')
log_re = re.compile(CLR_RE)

class LogLine():
    __slots__ = ['ipaddr','path','method','datetime','result','bytes','refer','agent']
    def __init__(self,line):
        # Parse line with the regular expression
        m = log_re.search(line)
        if not m:
            self.ipaddr   = None
            self.method   = None
            self.path     = None
            self.datetime = None
            self.result   = None
            self.bytes    = None
            self.refer    = None
            self.agent    = None
            return
        self.ipaddr     = m.group(1)
        self.datetime   = datetime.datetime.strptime(m.group(4),"%d/%b/%Y:%H:%M:%S %z")
        self.method = m.group(5)
        self.path = m.group(6)
        self.result = m.group(7)
        self.bytes = m.group(8)
        self.refer = m.group(9)
        self.agent = m.group(10)


    def __str__(self):
        return "{} {} {} {} {} {} {} {}".format(self.ipaddr,self.method,self.path,self.datetime.isoformat(),self.result,self.bytes,self.refer,self.agent)

    def __repr__(self):
        return "<LogLine: {} {} {} {} {} {} {} {}>".format(self.ipaddr,self.method,self.path,self.datetime.isoformat(),self.result,self.bytes,self.refer,self.agent)

    def row(self):
        from pyspark.sql import Row
        # You need to fill in the rest:
        return Row(ipaddr=self.ipaddr, datetime=self.datetime, method=self.method, path=self.path,
                   result=self.result, bytes=self.bytes, refer=self.result, agent=self.agent)
