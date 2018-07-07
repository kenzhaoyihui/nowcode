#!/usr/bin/env python
import argparse
import sys
 
try:
    import json
except ImportError:
    import simplejson as json

def RFile():
    with open('hostlist.txt', 'r+') as f:
        result=[]
        for line in f.readlines():
            host = line.strip().split()
            if host:
                result.append(host)
    return result

host_list = RFile()
#print host_list
 
def groupList():
    group_list = []
    for host in host_list:
        group_list.append(host[1])
    print (json.dumps({"all":group_list},indent=4))
 
def hostList(key):
    host_dict = {}
    for host in host_list:
        host_dict[host[1]] = {"ansible_ssh_host": host[1],"ansible_ssh_port":22, "ansible_ssh_user":"root","ansible_ssh_pass":
"redhat","hostname":host[0]}
    print (json.dumps(host_dict[key], indent=4))
 
if len(sys.argv) == 2 and (sys.argv[1] == '--list'):
    groupList()
elif len(sys.argv) == 3 and (sys.argv[1] == '--host'):
    hostList(sys.argv[2])
else:
    print "Usage: %s --list or --host <hostname>" % sys.argv[0]
    sys.exit(1)
