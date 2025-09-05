import streamlit as st

st.title('Counter')

# customer_count = 0

# if st.button('손님 한 명 추가요~!'):
#     customer_count += 1
# st.write(f'지금까지 온 손님 수: {customer_count}')

# 버튼 누르기 전 : 0
# 버튼 누르면 : 1
# 버튼 다시 누르면 페이지를 전체 reload 하기 때문에 다시 customer_count 는 0이 되어 customer_count 는 += 1 연산되어 1 값으로 머문다.
# 그래서 우리는 session_state를 활용해서 streamlit에서 변수를 공유하는 방법을 해야한다.


if "customer_count" not in st.session_state:    # st.session_state 에 customer_count 가 없다면,
    st.session_state.customer_count = 0         # 버튼 누르기 전에는 st.session_state 공간에는 customer_count 가 존재하지 않음.
                                                # 버튼을 누르면서 session_state.custormer 공간이 생기면서 0으로 받는다.
if st.button('손님 한 명 추가요~!'):             # 버튼을 추가로 누르면 기존에 st.session_state 공간에는 customer_count 공간이 있으므로,
    st.session_state.customer_count += 1        # st.session_state.customer_count = 0 초기화를 하지 않고 증가 시킨다.
                                                # 하지만 'page 새로고침'을 하는 경우는 전체 page 코드가 reload 되면서 customer_count 공간은 없어진다.
if st.button('오늘 장사 끝! 손님 수 초기화'):
    st.session_state.customer_count = 0

st.write(f'지금까지 온 손님 수: {st.session_state.customer_count}')