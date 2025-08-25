# import 구문 사용

# 1. our_class.py 모듈을 가져오기
import our_class

# 2. 선생님 이름과 학생 수를 출력
print(f'선생님 이름 : {our_class.teacher_name} \n학생 수 : {our_class.student_count}명')

# 3. study() 함수와 lecture() 함수 호출
our_class.study()
our_class.lecture()

# 4. 먹고 싶은 메뉴명이 5개 담긴 menus 배열 만들기
menus = ['A', 'B', 'C', 'D','E']

# 5. go_lunch() 함수를 호출해 오늘의 점심 메뉴룰 출력해 주세요!
print(our_class.go_lunch(menus))