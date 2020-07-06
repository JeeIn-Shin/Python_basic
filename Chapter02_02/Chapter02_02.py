#Chapter02-2
#파이썬 완전 기초
#파이썬 기초
# --------------------------------------------------------------------------
#들어가기 앞서...
#파이썬에서는 객체(object) 라는 단위로 메모리 정보를 관리
#객체에는 값(value) 유형(type) 정체성(identity)라는 세가지 특성이 존재
#값 = 메모리에 기록된 내용
#유형 = 데이터의 종류, 유형에 따라 그 값을 어떻게 읽고 다루어야 할지가 결정됨
#정체성 = 각각의 객체를 식별하기 위한 고유번호, 객체가 메모리 속에 위치한 주소값

#즉, 값과 유형이 동일한 데이터가 데이터가 메모리 공간에 여러 개 존재할 수 있지만
#이들은 서로 별개의 객체이며 정체성이 서로 다르다.
#그렇다면 아래 예제를 통하면 이건 틀린 말 아닌가??????
# --------------------------------------------------------------------------
#기본선언
#오른쪽에 있는 걸 왼쪽에 할당
n = 700

#n이 있는 주소를 방문해서 ...
#print(n)

#출력
#type (자료형)
print(type(n))

#동시 선언
x = y = z = 700
print(x, y, z)
print()

#선언 , 내가 선언한 변수를 정확하게 알고 있어야함
var = 75
#재선언
var = "change value"
print(type(var))
print(var)
print()

#object Reference
#변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

#ex1)
print(type(300))
print(int(300))
print(300)


#ex2)
#n -> 777
n = 777
#print(n) , print(type(n)) 한 줄로 끝내기
print(n, type(n))

# m -> 777 <- n
m = n
print(m, type(m), n, type(n))
print()

#재할당
m = n
print(m, type(m), n, type(n))
m = 400
print(m, type(m), n, type(n))
print()

#id(identity)확인 : 객체의 고유값 확인
m = 800
n = 655
print(id(m))
print(id(n))
print(id(m) == id(n))
print()

#예상 결과값 실제 결과값
#True		True
#True		True
#False		Treu		<< 어째서 이런 결과가 나오는가?
#어차피 800을 나중에 복사해서 써도 되는데
#지금부터 똑같은 값을 할당해서 쓰는 것이
#비효율적이라고 판단
#따라서 m, n 모두 똑같은 인스턴스
#겉보기에는 2개지만, 실제로는 하나만 존재하는 것
m = 800
n = 800
print(m == n)
print(type(m) == type(n))
print(id(m) == id(n))
print()

#다양한 변수 선언
#CameL case : numberOfCollegeGraduates -> Method
#Pascal case : NumberOfCollegeGraduates -> class
#Snake case : number_of_college_graduates -> var
#ex) student_grade = 3

#허용하는 변수 선언 법
#특수문자(_ , $ 제외), 숫자로 시작되는 변수는 사용할 수 없음
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_agE = 8

#예약어는 변수명으로 사용 불가능
# ex
# for = 3, class = 3 .......
# 참고 https://www.programiz.com/python-programming/keyword-list
