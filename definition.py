def 인사말만들기(이름):
    인사말 = '안녕하세요?' + 이름 + "님"
    return 인사말

def 인사말_바로하기(이름): 
    인사말 = '안녕하세요?' + 이름 + "님"
    print(인사말)
    
    
인사말 = 인사말만들기('준이')
print(인사말)

인사말_바로하기('정국')