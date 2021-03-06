#!/usr/bin/env python3
#
# ingest the TXT file generated by "mtr" and read it as records

import sys
import os,datetime,re


QUAZYILX_RE = "(\S+\s\S+)\sfnard:(\S+)\sfnok:(\S+)\scark:(\S+)\sgnuck:(\S+)"
quazyilx_re = re.compile(QUAZYILX_RE)

class Quazyilx():
    __slots__ = ['datetime','fnard','fnok','cark','gnuck']
    def __init__(self,line):
        # Parse line with the regular expression
        line = line.strip()
        m = quazyilx_re.search(line)
        if not m:
            self.datetime = None
            self.fnard    = None
            self.fnok     = None
            self.cark     = None
            self.gnuck    = None
            return
        # Put your code here:
        self.datetime = datetime.datetime.strptime(m.group(1), "%Y-%m-%d %H:%M:%S")
        self.fnard = m.group(2)
        self.fnok = m.group(3)
        self.cark = m.group(4)
        self.gnuck = m.group(5)
    def __str__(self):
        return "{} fnard:{} fnok:{} cark:{} gnuck:{}".format(self.datetime,self.fnard,self.fnok,self.cark,self.gnuck)
    def __repr__(self):
        return "{} fnard:{} fnok:{} cark:{} gnuck:{}".format(self.datetime,self.fnard,self.fnok,self.cark,self.gnuck)

        

