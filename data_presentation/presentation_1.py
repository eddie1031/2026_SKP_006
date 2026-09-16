import streamlit as st
import pandas as pd


data = pd.DataFrame({
    '번호': range(1, 51),
    '점수': range(1, 51),
    '단가': range(1, 51),
    '입출항횟수': range(1, 51),
    '수출횟수': range(1, 51),
    '수입횟수': range(1, 51),
})

display_df = data[
    [
        '입출항횟수',
        '수출횟수',
        '수입횟수'
    ]
]

st.dataframe(
    display_df,
    height=300,
)

products = pd.DataFrame({
    '상품': [
        '노트북',
        '모니터',
        '키보드'
    ],
    '단가': [
        150_000_000,
        350_000,
        1_020_000
    ]
})

st.dataframe(
    products,
    column_config={
        '단가': st.column_config.NumberColumn(
            '단가(원)',
            format='%,d원'
        )
    }
)
