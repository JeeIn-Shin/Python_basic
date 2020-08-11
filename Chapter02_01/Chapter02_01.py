#Chapter02-1.
#파이썬 완전기초
#print 사용법
#일반적으로 ''를 더 많이 사용함

#기본 출력
print('python start')
print("python start")
print('''python start''')
print("""python start""")

#그냥 print()를 하면 개행문자가 출력됨
print()

#seperator 옵션, sep이 뭐냐에 따라 출력이 달리됨 (구분자)
print('P', 'Y', 'T', 'H', 'O', 'N', sep='	')
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')
print('P', 'Y', 'T', 'H', 'O', 'N', sep=',')
print('010', '1234', '5678', sep='-')
print()

#end 옵션, 마지막 부분을 어떻게 처리할건지?
#default는 개행문자,
print('welcom to', end=' ')
print('IT News', end=' ')
print('Web site')
print()

#file 옵션, import 예약어(?), 첫번째 인자를 외부(두번째 인자)에 작성하겠다 ?
import sys
print('Learn Python', file=sys.stdout)
print()
#format 사용(d, s, f) d = digit, s = string, f = float
# %s
print('%s %s' % ('one', 'two'))

print('%10s' % ('nice'))
print('{:>10}'. format('nice'))

print('%-10s' % ('nice'))
print('{:10}'. format('nice'))

print('{:_>10}'. format('nice'))
print('{:^10}'. format('nice'))

#공간을 5개를 확보, .를 붙이면 확보한 공간만큼만 !, 붙이지 않으면 확보한 공간을 오버해도 받아줌
print('%.5s' % ('pythonstudy'))
print('%5s' % ('pythonstudy'))
#공간을 10개를 확보, 왼쪽부터 5개만 출력하겠음
print('{:10.5}'.format('pythonstudy'))
print()
# %d
print('%d %d' % (1, 2))
print('{1} {0}'. format(1, 2))

print('%4d' % (42))
print('{:4d}'.format(42))
# %f
# %f의 default는 소수부 6자리임.
print('%f' % (3.143434343434343434))

print('%20.2f' % (34.14343434))
print('%20.10f' % (34.14343434))
print('%20.15f' % (34.14343434))

print('{:f}'.format(3.143434343434343434))
print('%06.2f' % (3.141592653589793))
