# 변수 (Variable)
# -> Ctrl + / 로 주석 처리
# 어떤 값(Literal) 하나를 담기 위한 이름, 지어진 메모리 공간

# date 변수에 오늘 날짜를 대입해주세요.
date = 20250818
name = '오흥재'

print(date)
print(name)

# 대입연산자 : 좌항의 공간에 우항의 값을 대입

num = 10 # num 변수에 10을 대입
num = 50 # num 변수에 50을 대입
print(num)

# 10 = num (X) 좌항에 값은 대입할 수 없음, 변수명은 숫자로 시작할 수 없음
# num + 1 = 20 (X) 변수명에는 다른 특수 기호를 사용할 수 없음

m = 100
n = m + 10
m = 200 
print(n) # n은 m의 값이 바뀌어도 바뀌지 않음, n은 110을 담고 있음

"""
변수명 작성요령
1. 대소문자를 구분한다.
2. 변수명은 snake casing을 사용한다. (단어와 단어사이를 _로 연결)
3. 한글 변수명을 지정할 수 있다. (하지만 인코딩 등의 문제를 야기할 수 있으므로 사용을 지양한다.)
4. 언더바(_)를 제외한 특수문자를 사용할 수 없고, 숫자로 시작할 수 없다.
5. 파이썬 예약어(if, elif, else, for, while, …)를 사용할 수 없다.
6. **직관적인 변수명**을 사용한다. 짧고 간편하다고, a, b, c와 같은 변수명을 사용하지 않는다.
"""

team_name = "Ohgiraffers"
Team_name = "오지라퍼스"
print(team_name, Team_name) # 결과값 : Ohgiraffers 오지라퍼스
print(team_name + Team_name) # 결과값 : Ohgiraffers오지라퍼스

역이름 = '독산역'
print(역이름) # 결과값 : 독산역

# 사용자 아이디
user_id = 'vfxpedia'
# 상품 가격
product_price = 10000


 
