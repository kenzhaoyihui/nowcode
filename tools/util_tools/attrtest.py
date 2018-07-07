#! /usr/bin/env python2.7

import attr

@attr.s
class Testcase(object):
    zyh = attr.ib(default="zyh")
    lj = attr.ib(default="lj")
    age = attr.ib(default=23)

    def print_zyh(self):
        print self.zyh

    def print_lj(self):
        print self.lj

    def print_age(self):
        print self.age


if __name__ == "__main__":
    instance = Testcase()
    instance.print_zyh()
    instance.print_lj()
    instance.print_age()