#!/usr/bin/env python35
#
# Parse an MTR file in text mode and turn it into a tinydata file.
#
import sys
if sys.version < "3.4":
    raise RuntimeError("requires Pyton 3.4 or above")

<<<<<<< HEAD

# "Return an ISO8601-formatted timestamp from an input line"
def parse_timestamp(line):
    assert line.startswith("Start:")
<<<<<<< HEAD
    ts = datetime.datetime.strptime(line[7:], "%a %b %d %H:%M:%S %Y")  # Wed Dec 28 23:37:02 2016
    ts = ts.isoformat()
    return ts
=======
import os,datetime,re
>>>>>>> 8979994f06d4767949c60727878ca9780be3faae


mtr_line_exp = re.compile("")   # put something here

<<<<<<< HEAD

class MtrLine:
    def __init__(self, ts, line):
=======
=======
def parse_timestamp(line):
    assert line.startswith("Start:")
>>>>>>> 8979994f06d4767949c60727878ca9780be3faae
    return "Return an ISO8601-formatted timestamp from an input line"

class MtrLine():
    def __init__(self,ts,line):
<<<<<<< HEAD
>>>>>>> remotes/ANLY502/anly502_2017_spring/master
=======
>>>>>>> 8979994f06d4767949c60727878ca9780be3faae
        # Parse line and fill these in.
        # ts is the timestamp that we previously found
        line = line.strip()
        self.timestamp = ''
        self.hop_number = ''
        self.ipaddr = ''
        self.hostname = ''
        self.pct_loss = ''
        self.time = ''
    
def fix_mtr(infile,outfile):
    count = 0
    current_timestamp = None
    for line in infile:
        line = line.strip()     # remove leading and trailing white space
        if line.startswith('Start:'):
            # Beginning of a new record...
            print("Replace this print statement with new code. Probably need to set a variable with the time...")
            continue
        if line.startswith('HOST:'):
            # This can be ignored, since we always start at the same location
            continue
        
        m= MtrLine(line)
        if m.timestamp:
            print("Regular expression matched. Replace this with code...")
            outfile.write("OUTPUT RECORD GOES HERE!")
            count += 1
    return count

        

if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--infile",help="input file",default="mtr.www.comcast.com.2016.subset.txt")
    parser.add_argument("--outfile",help="output file",default="mtr.records.2016.subset.txt")
    args = parser.parse_args()

    if os.path.exists(args.outfile):
        raise RuntimeError(args.outfile + " already exists. Please delete it.")

    print("{} -> {}".format(args.infile,args.outfile))

    count = fix_mtr(open(args.infile,"rU"), open(args.outfile,"w"))
    print("{} records converted".format(count))