숫자 =90
#mutable
print(id(숫자))

숫자 =100
print(id(숫자))

print("-----------------------")
#immutable
리스트 = [1,2,3]
print(리스트)
print(id(리스트))

리스트[2] =6
print(리스트)
print(id(리스트))


#mutable (값을 바꿀수 았는 자료형) : 리스트, 딕셔너리, 집합
#immutable (값을 바꿀수 없는 자료형) : 정수형, 실수형, 문자열, 튜