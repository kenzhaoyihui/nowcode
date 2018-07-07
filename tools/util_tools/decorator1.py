"""
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print ("func name is  %s" % func.__name__)
        return func(*args, **kw)
    return wrapper


def log1(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print ("func name is %s: --> %s" % (func.__name__, text))
            return func(*args, **kw)
        return wrapper
    return decorator


@log
def now():
    print ("2017-08-10")

@log1('yzhaosherry')
def now1():
    print("2017-08-11,yzhao")

if __name__ == '__main__':
    now()
    now1()

    print (now.__name__)
    print (now1.__name__)
"""

class Student(object):
    __slots__ = ('__name', '__score')
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
        self.age = 12

    def print_score(self):
        print ("%s: %s" % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def __get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score

