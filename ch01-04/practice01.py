# 입.출력 모두 utf-8
import sys

print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 출력문
print('My name is Nana')

# 변수 선언
myName = 'Nana'

# 조건문
if myName == 'Nana':
    print('Good')
else:
    print('Bad')

# 반복문
for i in range(1, 10):
    for j in range(1, 10):
        print("%d * %d = " % (i, j), i*j)

# 함수
def greeting():
    print('안녕')

greeting()

# 클래스
class cookie:
    pass

# 객체 생성
cookie = cookie()

print(id(cookie))
print(dir(cookie))
