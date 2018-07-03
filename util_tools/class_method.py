"""
def get_no_of_instances(cls_obj):
    return cls_obj.no_inst

class Kls(object):
    no_inst = 0
    def __init__(self):
        Kls.no_inst = Kls.no_inst + 1

print (get_no_of_instances(Kls))
ik1 = Kls()
ik2 = Kls()

print (get_no_of_instances(Kls))

"""

"""
def iget_no_of_instance(ins_obj):
    return ins_obj.__class__.no_inst

class Kls(object):
    no_inst = 0
    def __init__(self):
        Kls.no_inst = Kls.no_inst + 1


ik1 = Kls()
ik2 = Kls()
print (iget_no_of_instance(ik1))
print (iget_no_of_instance(ik2))
"""

"""
class Kls(object):
    no_inst = 0
    def __init__(self):
        Kls.no_inst = Kls.no_inst + 1
    
    @classmethod
    def get_no_of_instances(cls_obj):
        return cls_obj.no_inst

ik1 = Kls()
ik2 = Kls()
print ik1.get_no_of_instances()
print ik2.get_no_of_instances()
print Kls.get_no_of_instances()
"""

"""
IND = 'ON'
class Kls(object):
    def __init__(self, data):
        self.data = data
    @staticmethod
    def checkind():
        return (IND == 'ON')
    def do_reset(self):
        if self.checkind():
            print('Reset done for:', self.data)
    def set_db(self):
        if self.checkind():
            self.db = 'New db connection'
        print('DB connection made for: ', self.data)
ik1 = Kls(12)
ik1.do_reset()
ik1.set_db()
"""

"""
import math
class Circle:
    def __init__(self,radius):
        self.radius=radius

    @property
    def area(self):
        return math.pi * self.radius**2

    @property
    def perimeter(self):
        return 2*math.pi*self.radius

c=Circle(10)
print(c.radius)
print(c.area)
print(c.perimeter)
"""

class People:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return '<name:%s,age:%s>' %(self.name,self.age)

p1=People('egon',18)
print(p1)
#p1.__str__()
#str(p1) #----->p1.__str__()