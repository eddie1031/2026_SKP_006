import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.title('Matplotlib 그래프')

sales = pd.DataFrame({
    'month': [
        'jan',
        'feb',
        'mar',
        'apr',
        'may',
        'jun'
    ],
    'sales': [
        12.5,
        14.2,
        13.8,
        16.4,
        18.1,
        19.7,
    ]
})

fig, ax = plt.subplots(figsize = (8,6))

ax.plot(
    sales['month'],
    sales['sales'],
    marker='o',
)

ax.set_title('Monthly Sales')

ax.set_xlabel('Month')
ax.set_ylabel('Sales')

st.pyplot(fig)

plt.close(fig)

st.title('Seaborn 그래프')

fig, ax = plt.subplots(figsize = (8,6))

sns.barplot(
    data=sales,
    x='month',
    y='sales',
    ax=ax,
)

ax.set_title('Monthly Sales')
ax.set_xlabel('Month')
ax.set_ylabel('Sales')

st.pyplot(fig)

plt.close(fig)
