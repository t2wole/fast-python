def hello(world):
    value = "hello, " + str(world)
    return value

str = hello("niceman")
print(str)
print('---------------------------------------------------')

def functionMul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

val1, val2, val3 = functionMul(5)

print(val1, val2, val3)
print('---------------------------------------------------')

def functionTup(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 6
    return y1,y2,y3

tup = functionTup(4)
print(type(tup), tup, list(tup))
print('---------------------------------------------------')

def functionList(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 6
    return [y1,y2,y3]

list_ = functionList(6)
print(type(list_), list_, set(list_))
print('---------------------------------------------------')

def functionDict(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 6
    return {'rect1': y1, 'rect2': y2, 'rect3': y3}

dict = functionDict(8)
print(type(dict), dict, dict.items())
print('---------------------------------------------------')

# *args
def args_func(*args):   # 매개변수 몇 개가 올지 모를때
    for i, v in enumerate(args):
        print("{}".format(i), v, end=' ')

args_func('Kim')
args_func('Kim', 'Park')
args_func('Kim', 'Park', 'Lee')

print()
print('---------------------------------------------------')

# kwargs
def kwargs_func(**kwargs):
    for v in kwargs.keys():
        print('{}'.format(v), kwargs[v], end=' ')

kwargs_func(name1='Kim')
kwargs_func(name1='Kim', name2='Park')
kwargs_func(name1='Kim', name2='Park', name3='Lee')

print()
print('---------------------------------------------------')

def example(args1, args2, *args, **kwargs):
    print(args1, args2, args, kwargs)

example(10, 20, 'park', 'kim', age1 = 33, age2 = 34, age3 = 35)
print('---------------------------------------------------')

# 중첩함수
def nestedFunc(num):
    def funcInFunc(num):
        print(num)
    print("In func")
    funcInFunc(num + 10000)

nestedFunc(10000)
print('---------------------------------------------------')

def funcMul(x : int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return[y1, y2, y3]

print(funcMul(5))
print('---------------------------------------------------')

def hint(word: str, num: int) -> int:
    return len(word) * num

print('hint exam1 : ', hint('I love you', 10))
print('---------------------------------------------------')

def hint2(word: str, num: int) -> None:
    print('hint exam2 : ', len(word) * num)

hint2("niceman", 10)
print('---------------------------------------------------')

# lambda 

lambda_func = lambda x: x * 10

def func_final(x, y, func):
    print(x * y * func(10))

func_final(10, 10, lambda_func)