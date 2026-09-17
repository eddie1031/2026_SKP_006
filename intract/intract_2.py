import streamlit as st
import pandas as pd


sales = pd.DataFrame({
    "지역": [
        "서울",
        "서울",
        "대전",
        "대전",
        "부산",
        "부산",
    ],
    "상품": [
        "노트북",
        "모니터",
        "노트북",
        "키보드",
        "모니터",
        "키보드",
    ],
    "판매량": [
        3,
        8,
        4,
        15,
        10,
        18,
    ],
    "매출": [
        4_500_000,
        2_800_000,
        6_000_000,
        1_800_000,
        3_500_000,
        2_160_000,
    ],
})


region = st.selectbox(
    '지역',
    [
        '전체',
        '서울',
        '대전',
        '부산'
    ]
)

if region == '전체':
    filtered = sales.copy()
else:
    filtered = sales[sales['지역'] == region]

row_count = len(filtered)

# 총매출(KPI)
total_sales = filtered['매출'].sum()

# 총판매량(KPI)
total_quantity = filtered['판매량'].sum()

st.title(f'{region}지역 매출 대시보드')

col1, col2, col3 = st.columns(3)

col1.metric(
    '총 매출',
    value=f'{total_sales:,}원'
)

col2.metric(
    '총 판매량',
    value=f'{total_quantity:,}개'
)

col3.metric(
    '조회 건수',
    value=f'{row_count:,}건'
)

st.dataframe(filtered, hide_index=True)