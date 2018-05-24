#치환문 예
a=1
b=a+1
print(a, b)

#변수값 할당 오류
#1+a=c

#세미콜론으로 치환문 구분가능(비권장)
a=3.5; f=5.3

#여러 개를 한 번에 치환
e, f = 3.5, 5.3
print(e, f)

#여러 개를 같은 값으로 치환
x=y=z=10
print(x,y,z)

#값 교환
f, e = e, f
print(e, f)



#동적 타이핑: 변수에 새로운 값이 할당되면 기존의 값을 버리고 새로운 값으로 치환된다.
a=1
print(type(a))
a="hello"
print(type(a))

#확장 치환문
a = 10
a += 10
print(a)

a-=3
print(a)


print(~4)
