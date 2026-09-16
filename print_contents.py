"""
streamlit에서 텍스트를 사용하는 방법

title()
subtitle()
header()
write()
text()
code()
markdown()
"""

import streamlit as st
import pandas as pd
import numpy as np

MAIN_TITLE = 'Hello, Streamlit'

st.title(MAIN_TITLE)
st.header('데이터 애플리케이션')
st.subheader('대시보드 페이지 구성')
st.write('streamlit은 대시보드를 쉽게 구성할 수 있습니다.')

st.caption('쉽게 만들수 있어요!')

st.markdown('---')

st.markdown("""
### 매출 분석 결과

이번달 주요 지표입니다.

* 총 주문수: **1000건**
- 총 매출: 3500000만원
- 평균 주문 금액: 28000원

매출은 지난달 보다 *8.2%* 증가 했습니다.
""")

st.markdown('---')

scores = [ 78, 85, 92, 88, 95 ]
score_avg = sum(scores) / len(scores)

st.subheader('학생 평균')
st.markdown(f'현재 학생들의 평균점수는 **{score_avg:.2f}** 점입니다.')

st.markdown('---')

example_sql = """
SELECT
  category, product_name, unit_price
FROM
  orders
GROUP BY
  category
"""


st.code(
    example_sql,
    language='sql'
)

st.markdown('---')

sales = pd.DataFrame({
    '월': [
        '1월',
        '2월',
        '3월',
        '4월',
    ],
    '가격': [
        1200,
        1500,
        1350,
        1800,
    ],
    '판매량': [
        3,
        8,
        15,
        20
    ]
})

sales['매출'] = sales['가격'] * sales['판매량']

st.title('월별 매출')

st.dataframe(
    sales,
    hide_index=True,
)

st.write('---')

st.table(sales)

st.write('---')

image = np.zeros(
    (200, 400, 3),
    dtype=np.uint8,
)

image[:, :200] = [
    80,140,220
]

image[:, 200:] = [
    1,
    200,
    150
]

st.image(
    image,
    caption='Numpy 배열로 그린 멋진 그림'
)
# st.caption('Numpy 배열로 그린 멋진 그림')

st.write('---')

st.image(
    'pizza.jpg',
    width=200,
    caption='맛있는_피자.jpg'
)

st.write('---')

st.title('수식')
st.latex(r'p = 3.141592')

st.latex(r"""
\bar{x}
=
\frac{1}{n}
\sum_{i=1}^{n} x_i
""")

st.write('---')

st.title('코드 실행 과정 확인')

with st.echo():
    numbers = [ 10, 20, 30 ]

    total = sum(numbers)

    st.write(f'합계: {total}')

st.write('---')

st.info('데이터는 매일 오전 9시에 갱신됩니다.')
st.success('데이터는 매일 오전 9시에 갱신됩니다.')
st.warning('데이터는 매일 오전 9시에 갱신됩니다.')
st.error('데이터는 매일 오전 9시에 갱신됩니다.')

st.write('---')

score = 100

st.title('학생 성적 확인')
st.write(
    f'점수: {score}'
)

if score >= 90:
    st.success('멋져')
elif score >= 80:
    st.info('괜찮아요')
else:
    st.warning('힘내세요')