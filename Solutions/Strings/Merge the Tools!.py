''' Date 29-8-2018 '''
from collections import OrderedDict

def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        print "".join(OrderedDict.fromkeys(string[i:i+k]))

if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)