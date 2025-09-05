import streamlit as st
import pandas as pd

st.title('게임 캐릭터의 인지도')

data = pd.DataFrame({
    "캐릭터": ["전사", "법사", "힐러", "탱커", "랜덤"],
    "선택횟수": [120, 95, 150, 80, 111],
    "승률 (%)": [52, 48, 56, 60, 49],
    "인지도 (%)": [25, 20, 30, 15, 22]
})

st.dataframe(data)

edited_data = st.data_editor(data)
# st.write(edited_data)

st.bar_chart(data.set_index('캐릭터')['선택횟수'])     # '캐릭터' 컬럼을 인덱스로 쓴다
st.line_chart(data.set_index('캐릭터')['승률 (%)'])

#pip install matplotlib
fig = data.plot.pie(           # Pandas가 제공하는 plot 기능을 이용
    y='인지도 (%)',            # 무엇을 그릴지
    labels=data['캐릭터'],     # 달아주는 것
    autopct='%1.1f%%',         # 파이차트를 그려줄때 %지 형식을 지정
    figsize=(6, 6),            # 가로 세로 크기를 지정
    legend=False               # 범례? 표시
).get_figure()                 # get_figure() 만들어진 데이터를 반환한다. 그럼 받아줘야겠네?
st.pyplot(fig)                 # pyplot() Pandas 에서 만들어진 데이터를 출력한다.