문장 = input("아무 글이나 입력하세요:")
글자수 = 0;

for 한문장 in 문장:
    if 한문장 == " ":
        pass
    else:
        글자수 += 1
print(문장 * 글자수)