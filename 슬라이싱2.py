점수A = [60, '결석', 60, 70]
점수B = 점수A[:]

print(점수B[2])#슬라이싱으로 참조x 복사됨

점수A[2] = 100
print(점수B[2])