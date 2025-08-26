import streamlit as st

st.title('오늘은 화요일😎 st.title()')
st.header('오늘은 streamlit 배우는 날😉 st.header()')
st.header('8501번 포트, 포트는 프로그램의 주소 번호, st.header()')
st.subheader('Streamlit으로 나만의 데모 페이지 만들기!!, st.subheader()')

my_site = st.text_input('오늘 내가 만들어보고 싶은 사이트는?! my_site = st.text_input()')
st.write(my_site + "  st.wirte(my_site) 를 통해 출력된 결과")
# print(my_site)

if st.button(f'{my_site} 접속하기'): # click = True, unclick = False 로 반환
    if len(my_site) != 0:
        st.success(f'{my_site} 접속 중')
    else:
        st.success(f'올바른 주소를 입력하세요!')

# 명령어를 쓸 때, 앞에다가 경로를 덧붙여서 쓰는 방법
# 명령어를 실행하려고 하는 위치로 이동해서 사용하는 밥법

# streamlit run [파일명.확장자]

