__author__ = "kenzhaoyihui"

import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print "%s are my love" % text
            return func(*args, **kw)
        return wrapper
    return decorator


@log("LJ")
def ins():
    print "Hello , ZYH"

if __name__ == "__main__":
    ins()