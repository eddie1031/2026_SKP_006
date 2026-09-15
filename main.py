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

# streamlit run <실행하고자 하는 파이썬 파일>

# 가장 큰 제목
# st.title('온라인 쇼핑몰 매출 분석')
# # 주요 영역 제목
# st.header('2026년 매출 현황')
# # 세부 영역 제목
# st.subheader('8월 매출')
# # 일반적인 내용
# st.write('8월 매출 데이터를 분석합니다.')

price = 1000
amount = 5

st.write(f'총 가격은 {price * amount}원입니다')

st.title('쇼핑몰 운영 대시보드')
st.header('매출 현황')
st.subheader('금일 매출 현황')
st.write('오늘 발생한 주문의 매출을 확인합니다.')
st.subheader('월간 매출')
st.write('이번달 누적 매출을 확인합니다.')
st.header('고객 현황')
st.subheader('신규 가입자')
st.write('오늘 가입한 신규 고객을 확인합니다.')

st.title('이것은 title이구요')
st.write('**판매량** : 120개')
st.text('**매출액** : 3500000')

st.caption('매출 데이터는 매일 오전 9시에 갱신됩니다.')
st.caption('기준일: 2026-09-15')
st.caption('단위: 1TEU')


st.markdown(
    "이번달 매출은 **무려** **35000000** 이며"
    "*전월보다 많이 증가했습니다 :)*"
)

st.markdown("""
### 매출 분석 결과

이번 달 주요 지표입니다.

- 총 주문수: 30건
- 총 매출: 10만원
- 평균 주문 금액: 3만원

매출은 지난달보다 32.5%증가했습니다.
""")

st.code(
    """
    """
)