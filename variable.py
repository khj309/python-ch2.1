import keyword

# 변수 이름은 문자, 숫자, _로 구성된다.

friend=1
a   =   10
my_name = '김형주'
myName = '김형주'
_yourName='둘리'
member1="또치"

#에러 : 다른 구성의 변수이름은 사용불가
#1a='dont start number'
#def = 'reserved';

print(keyword.kwlist)
print(len(keyword.kwlist))

#한글 이름의 변수도 사용 가능
가격1=5000
할인율1=0.3
할인된가격1=가격1*(1-할인율1)
print(할인된가격1)

