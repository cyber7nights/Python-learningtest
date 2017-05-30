import functools

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print('2015-3-25')
a=now
print(a)

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print ('begin call')
        return func(*args,**kw)
    return wrapper
@log
def sum(x,y):
    return x+y
print(sum(3,5))

def log(*test):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print ('begin:',func.__name__,test)
            return func(*args,**kw)
        return wrapper
    return decorator
@log ()
def sum(x,y):
    return x+y
print(sum(3,5))
