import streamlit as st
import pandas as pd

st.set_page_config(
    layout='wide',
)

sales_df = pd.DataFrame({
    '상품': [
        '노트북',
        '모니터',
        '키보드',
        '마우스',
    ],
    '판매량': [
        3,
        8,
        15,
        20
    ],
    '매출': [
        4_500_000,
        2_800_000,
        1_800_000,
        1_600_000,
    ]
})

total_sales = sales_df['매출'].sum()
total_quantity = sales_df['판매량'].sum()
average_sales = sales_df['매출'].mean()

max_product = sales_df.loc[
    sales_df['매출'].idxmax(),
    '상품'
]

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    label='총 매출',
    value=f'{total_sales:,}원',
    # border=True
)

col2.metric(
    label='총 판매량',
    value=f'{total_quantity:,}개',
    # border=True
)

col3.metric(
    label='평균 매출',
    value=f'{average_sales:,.0f}원',
    # border=True
)

col4.metric(
    label='최고 매출 상품',
    value=max_product,
    # border=True
)
