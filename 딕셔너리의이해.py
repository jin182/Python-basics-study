성적 = {'승준':60, '은희':'결석', '태호':60,'지영':70}

#print(성적[1]) 오류 발생 딕셔너리는 인덱스번호로 값 불러오기 x

print(성적['은희'])#결석출력
for 안의값 in 성적:
    print(안의값) #key값출력

print("-------------------")

for 값 in 성적.values():
    print(값) #value출력


