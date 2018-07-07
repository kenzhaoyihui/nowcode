#!/usr/bin/env python
import argparse
import sys
 
try:
    import json
except ImportError:
    import simplejson as json

class MyInventory(object):
    def __init__(self):
        self.host_list = self.RFile()

        if len(sys.argv) == 2 and (sys.argv[1] == '--list'):
            print self.groupList()
        elif len(sys.argv) == 3 and (sys.argv[1] == '--host'):
            print self.hostList(sys.argv[2])
        else:
            print "Usage: %s --list or --host <hostname>" % sys.argv[0]
            sys.exit(1)

    @staticmethod
    def RFile():
        with open('../library/hostlists', 'r+') as f:
            result = []
            for line in f.readlines():
                host = line.strip().split()
                if host:
                    result.append(host)
        return result

    def groupList(self):
        group_list = []
        for host in self.host_list:
            group_list.append(host[1])
        return json.dumps({"all":group_list},indent=4)
 
    def hostList(self, key):
        host_dict = {}
        for host in self.host_list:
            host_dict[host[1]] = {"ansible_ssh_host": host[1],"ansible_ssh_port":22, "ansible_ssh_user":"root","ansible_ssh_pass":
    "redhat","hostname":host[0]}
        return json.dumps(host_dict[key], indent=4)

MyInventory()
