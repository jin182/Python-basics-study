'''식권수를 입력받은 다음 입력 받은 숫자 만큼
식권을 다음 형태로 출력하느 프로그맮
[식권] # 번호
'''

식권수 = int(input("식권이 몇 장 필요한가요?"))# 식권개수 입력

for 출석된식권 in range(식권수):
    print('[식권] #', 출석된식권 + 1)