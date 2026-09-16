from asyncio import start_server

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='부산항만',
    page_icon='👍',
    layout='wide',
    initial_sidebar_state='locked',
)

# st.sidebar.title('신항1')
# st.sidebar.title('신항2')

sales_df = pd.DataFrame({
        '지역': [
            '서울',
            '서울',
            '대전',
            '대전',
            '부산',
            '부산',
        ],
        '상품': [
            '노트북',
            '모니터',
            '노트북',
            '키보드',
            '모니터',
            '키보드',
        ],
        '매출': [
            4_500_000,
            3_500_000,
            2_500_000,
            1_500_000,
            2_500_000,
            5_500_000,
        ]
    })

with st.sidebar:
    st.title('북항')
    st.write('북항 대시보드')


    st.title('신항')
    st.write('신항 대시보드')
    selected_port = st.selectbox(
        '부두를 선택해주세요',
        [
            '신항 1부두',
            '신항 2부두',
            '신항 3부두',
            '신항 4부두',
        ]
    )
    st.write(f'선택된 부두: {selected_port}')

    st.header('조회조건')
    region = st.selectbox(
        '지역 선택',
        [
            '전체',
            '서울',
            '대전',
            '부산',
        ]
    )

    if region == '전체':
        filtered = sales_df.copy()
    else:
        filtered = sales_df[sales_df['지역'] == region]

st.title('스마트 항만 대시보드')

df_area = st.container(border=True)

with df_area:
    st.dataframe(filtered, hide_index=True)


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
# fig, ax
col1, col2, col3 = st.columns(3)

with col1:
    st.write('왼쪽')

with col2:
    st.write('가운데')

with col3:
    st.write('오른쪽')

sales_kpi, orders_kpi, customers_kpi = st.columns(3)

with sales_kpi:
    with st.container(border=True):
        st.subheader('매출 KPI')
        st.metric(
            label='오늘 매출',
            value='35,000,000원'
        )

with orders_kpi:
    with st.container(border=True):
        st.subheader('주문 KPI')
        st.metric(
            label='오늘 주문 수',
            value='1,250건'
        )

with customers_kpi:
    with st.container(border=True):
        st.subheader('고객 KPI')
        st.metric(
            label='누적 고객수',
            value='874명'
        )

left, right = st.columns([2, 1])

with left:
    st.subheader('넓은 영역')
    st.write('해당 영역은 상대적으로 넓게 표시됩니다.')

with right:
    st.subheader('좁은 영역')
    st.write('해당 영역은 상대적으로 좁게 표시됩니다.')

st.write('컨테이너 밖')

container1 = st.container(
    border=True
)

with container1:
    st.subheader('매출 정보')
    st.write('총매출: 35,000,000원')
    st.write('1,250건')

st.write('컨테이너 밖')

result_area = st.container(border=True)

result_area.subheader('분석결과')
result_area.metric(label='분석 결과', value='평균 매출: 1,520건')

with st.expander('자세히보기'): # , expanded=True):
    st.subheader('평균 계산')
    st.write('Super Ultra Mega Alpha detailed description')
    st.latex(r'\bar{x} = 10')

