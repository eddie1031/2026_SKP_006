import pandas as pd
import streamlit as st


st.title('버튼 실습')

if st.button('분석시작'):
    st.success('데이터 분석이 성공적으로 시작되었습니다')

st.title('체크박스')

checked = st.checkbox(
    '상세정보 표시'
)

if checked:
    st.write('눌렸다!')

st.write(f'체크박스 상태 : {checked}')

st.title('슬라이더 실습')

score = st.slider(
    label='점수를 선택해주세요.',
    min_value=0,
    max_value=100,
    step=1,
    value=50,
)

st.write(f'선택된 점수: {score}')

score_range = st.slider(
    label='점수 범위',
    min_value=0,
    max_value=100,
    step=1,
    value=(60,90),
)

st.write(f'점수 최소값 = {score_range[0]}')
st.write(f'점수 최대값 = {score_range[1]}')

st.title('Number Input 실습')

age = st.number_input(
    label='나이를 입력하세요',
    min_value=0,
    max_value=120,
    step=2,
    value=19,
)

st.write(f'선택된 나이: {age}')

st.title('Text Input 실습')

name = st.text_input(
    '항만 터미널 검색',
    placeholder='예: 신항-제1터미널'
)

# st.write(f'{age}살 {name} 회원님! 어서오세요!')

st.subheader('스마트 항만 로그인')
st.text_input(
    '사번'
)
st.text_input(
    '비밀번호',
    type='password'
)

products = pd.DataFrame({
    '항만': [
        '감만항',
        '신항1',
        '북항',
        '대포항',
        '덕포항'
    ],
    '환적수': [
        190_000,
        1000,
        170,
        2,
        5
    ]
})

st.title('항만 검색 대시보드')
terminal_name = st.text_input(
    '항만 검색'
)

if terminal_name:

    result = products[products['항만'].str.contains(terminal_name)]
else:
    result = products

st.dataframe(result)