from mtr_fix import *
import re
# LINE0 = 'Start: Wed Dec 28 23:37:02 2016'
LINE0 = 'Start: Sun Jan 15 19:01:28 2017'
LINE1 = ' 1.|-- 192.168.10.1               0.0%     1    1.3   1.3   1.3   1.3   0.0'
# LINE1 = '6.|-- hu-0-10-0-1-pe07.ashburn.  0.0%     1   11.7  11.7  11.7  11.7   0.0'
TS = "2017-01-15T19:01:28"


def test_parse_timestamp():
    assert parse_timestamp(LINE0)==TS

# LINE1 = LINE1.strip()
# m = re.search("(\d+)\..*\s(\?+|\d+\.\d+\.\d+\.\d+|[a-z]+.*)\s+(\d+)\.0.*\s+(\d+\.\d|\d+\.)\s+(\d+\.\d|\d+\.)\s+(\d+\.\d|\d+\.)\s+(\d+\.\d|\d+\.)\s+(\d+\.\d)", LINE1)
# # x = mtr_line_exp.search(LINE1)
# print(m.group(1))
# print(m.group(2))
# print(m.group(3))
# print(m.group(4))
# print(m.group(5))
# print(m.group(6))
# print(m.group(7))
# print(m.group(8))

def test_MtrLine():
    current_timestamp = parse_timestamp(LINE0)
    m = MtrLine(current_timestamp,LINE1)

    # print(m.hostname)
    assert m.timestamp == TS
    assert m.hop_number == '1'
    # assert m.ipaddr == ''
    # assert m.hostname == 'bu-101-ur21-d.west'
    assert m.pct_loss == '0'
    assert m.time == '1.3'
    #
    # host = 'bu-101-ur21-d.west'

    # assert m.hostname == 'bu-101-ur21-d.west'

    # f = open("mtr.www.comcast.com.2016.txt", "r")
    # for line in f:
    #     line = line.strip().split(";")
    #     for string in line:
    #         # print(string)
    #         if string.startswith(m.hostname):
    #             # print(string)
    #             m.hostname = string
    #             if string.find('('):
    #                 i = string.find('(')
    #                 m.hostname = string[:i]
    #                 m.ipaddr = string[i + 1:-1]
    #                 # print(m.hostname)
    #                 # print(m.ipaddr)
    #             break
    #     else:
    #         continue
    #     break








    print(m.timestamp)
    print(m.hop_number)
    print(m.ipaddr)
    print(m.hostname)
    print(m.pct_loss)
    print(m.time)


test_parse_timestamp()
test_MtrLine()




# hostname = 'bu-101-ur21-d.west'
# ipaddr =""
# with open("mtr.www.comcast.com.2016.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         line = line.strip().split(";")
#         for string in line:
#             if string.startswith(hostname):
#                 hostname = string
#                 if string.find('('):
#                     i = string.find('(')
#                     hostname = string[:i]
#                     ipaddr = string[i + 1:-1]
# print(hostname)
# print(ipaddr)

