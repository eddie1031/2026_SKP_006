import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='부산항만',
    page_icon='👍',
    layout='centered',
    initial_sidebar_state='locked',
)

st.title('스마트 항만 대시보드')

data = pd.DataFrame({
    '상품': [
        '노트북',
        '모니터',
        '키보드',
        '마우스',
    ],
    '판매량': [
        15,
        28,
        42,
        51
    ]
})

# st.dataframe(data)

st.write('A')
st.write('B')
st.write('C')