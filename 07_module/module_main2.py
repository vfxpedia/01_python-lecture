# from-import 구문을 사용

# 1. our_class.py 모듈을 가져와서 
from our_class import teacher_name, student_count, study, lecture, go_lunch

# teacher_name = hi
# 2. 선생님 이름과 학생 수를 출력
print(teacher_name, student_count)
# 3. study() 함수와 lecture() 함수 호출
study()
lecture()
# 4.먹고 싶은 메뉴명이 5개 담긴 menus 배열을 만들어서
menus = [1, 2, 3, 4, 5]

# 5. go_lunch() 함수를 호출해 점심 메뉴를 출력

print(go_lunch(menus))