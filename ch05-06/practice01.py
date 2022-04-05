v1 = 1

while v1 < 11:
    print("v1 is : ", v1)
    v1 += 1
print('-----------------------------------------------------')

for v2 in range(11):
    print("v2 is : ", v2)
print('-----------------------------------------------------')

for v3 in range(1, 11):
    print("v3 is : ", v3)
print('-----------------------------------------------------')

for v4 in range(1, 11, 2):
    print("v4 is : ", v4)
print('-----------------------------------------------------')

sum1 = 0
count1 = 1

while count1 <= 100:
    sum1 += count1
    count1 += 1

print('1 ~ 100 합 : ', sum1)
print('1 ~ 100 합 : ', sum(range(1, 101)))
print('1 ~ 100 안에 3의 배수의 합 : ', sum(range(1, 101, 3)))
print('-----------------------------------------------------')

names = ["Kim", "Park", "Cho", "Lee", "Choi", "Yoo"]

for name in names:
    print("You are", name)
print('-----------------------------------------------------')

lotto_numbers = [11, 19, 21, 28, 36, 37]
for number in lotto_numbers:
    print("Your number is", number)
print('-----------------------------------------------------')

word = 'dreams'
for i in word:
    print("word :", i)
print('-----------------------------------------------------')

myInfo = {
    "name": "kim",
    "age": 13,
    "city": "seoul"
}

for key in myInfo:
    print(key, ":", myInfo[key])

for val in myInfo.values():
    print(val)
print('-----------------------------------------------------')

name = 'KennRY'

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())
print('-----------------------------------------------------')

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 33:
        print("found!")
        break
    else:
        print("not found!", num)
print('-----------------------------------------------------')

lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is float:
        continue

    print("type:", type(v))
    print("multiply by 2:", v*3)
print('-----------------------------------------------------')

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 39:
        print("found!")
        break
    else:
        print("not found", num)
else:
    print("not found ...")
print('-----------------------------------------------------')

flag = True
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

while flag:
    for v in numbers:
        if v == 33:
            print("found!")
            flag = False
        print("not found!", v)
print('-----------------------------------------------------')

i = 1
while i <= 10:
    print('i : ', i)
    if i == 6:
        break
    i += 1
print('-----------------------------------------------------')

for i in range(1, 11):
    for j in range(1, 11):
        print('{:4d}'.format(i * j), end=" ")
    print()
print('-----------------------------------------------------')




