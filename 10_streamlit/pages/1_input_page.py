import streamlit as st

st.title('사용자 입력 받는 페이지, st.title')
st.header('This is st.header')

col1, _, col2 = st.columns(3)

with col1:
    nickname = st.text_input('닉네임 입력, st.text_input')
    age = st.number_input('나이 입력, st.number_input으로 min_value=13, max_value=100', min_value=13, max_value=100)
    options = ['한국', '중국', '미국', '일본', '우주', '영국']
    national = st.selectbox('국적, st.selectbox(options)', options)

    r_options = ['맛집 탐방', '영화 감상', '음악 감상', '유투브 보기', '뜨개질']
    hobby = st.radio('취미 st.radio(r_options)', r_options)

    is_checked = st.checkbox('개인정보 제공 동의')

with col2:
    if st.button('✅ 입력 완료, 입력을 바꾸면 새롭게 Reload 됩니다.'):
        st.write(f'이름이 무엇인가요? {nickname}')
        st.write(f'몇 살인가요? {age}')
        st.write(f'어디서 오셨나요? {national}')
        st.write(f'취미를 알려주세요 {hobby}')
        st.write(f'개인정보 동의하시나요? {is_checked}')