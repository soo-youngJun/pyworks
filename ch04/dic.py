# 딕셔너리

person = {}
print(person)

person['name'] = '이순신'
person['age'] = 40
print(person)

person['address'] = '전라도'
print(person)

# 딕셔너리 value값 출력
for key in person:
    print(person[key]) 

# 요소 삭제 : person.pop(address)와 같음
del person['address']
print(person)
