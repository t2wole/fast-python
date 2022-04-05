# 데이터 타입

v_str1 = "niceman"
v_bool = True
v_str2 = "goodboy"
v_float = 10.3
v_int = 9
v_dict = {
    "name" : "kim",
    "age" : 11
}

v_list = [3, 5, 7]
v_tuple = 3, 5, 6
v_set = {7, 8, 9}

print(type(v_list))
print(type(v_tuple))
print(type(v_set))

# 연산 실습
i1 = 39
i2 = 939
big_int1 = 123456789123456789012345678901234567890
big_int2 = 999999999999999999999999999999999999999
f1 = 1.234
f2 = 3.939
print("============================================================================")

# / -> 소수까지 모두 출력
print("##### / #####")
print("big_int2 / big_int1: ", big_int2 / big_int1)
print("i1 / f1: ", i1 / f1)
print("f1 / i1: ", f1 / i1)

print("============================================================================")

# // -> 정수부분.0 으로 출력
print("##### // #####")
print("big_int2 // big_int1: ", big_int2 // big_int1)
print("i1 // f1: ", i1 // f1)
print("f1 // i1: ", f1 // i1)
print("============================================================================")

# %
print("##### % #####")
print("big_int1 % big_int2 :", big_int1 % big_int2)
print("i1 % f1 :", i1 % f1)
print("f1 % i1 :", f1 % i1)
print("============================================================================")

# **
print("##### ** #####")
print("2 ** 3: ", 2 ** 3)
print("i1 ** i2: ", i1 ** i2) 
print("f1 ** f2: ", f1 ** f2)
print("i1 ** f1: ", i1 ** f1)
print("f1 ** i1: ", f1 ** i1)
print("============================================================================")

# 형 변환 실습
a = 5.
b = 4
c = .4
d = 7.7

# 타입 출력
print(type(a), type(b), type(c), type(d))

# 형 변환
print(float(b))  # 정수 -> 실수
print(int(c))  # 실수 -> 정수
print(int(d))  # 실수 -> 정수
print(int(True))  # Bool -> 정수
print(float(True))  # Bool -> 정수
print(int(False))  # Bool -> 정수
print(float(False))  # Bool -> 정수
print("============================================================================")

# 수치 연산 함수
print(abs(-7))
x, y = divmod(100, 8)
print(x, y)
print(pow(5, 3))

#외부 모듈
import math

#ceil
print(math.ceil(5.1))   # x 이상의 수 중에서 가장 작은 정수
print(math.ceil(8.999))

#floor
print(math.floor(3.874)) # x 이하의 수 중에서 가장 큰 정수
print(math.floor(-25.5))

#pi
print(math.pi)