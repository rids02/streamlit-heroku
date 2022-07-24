import streamlit as st

st.title('Simple Streamlit Web App Week8')
st.write('UseCase : Multiplication of 2 given numbers.')
st.subheader('Submitted by Riddhi Bhogaonkar 21f1004802')
option1 = st.selectbox('Select type of first number', ('float', 'integer'))
if (option1=='float'):
    m = st.number_input('Enter first number: ', step=0.01)
else:
    m = st.number_input('Enter first number: ', step=1)

option2 = st.selectbox('Select type of second number', ('float', 'integer'))
if (option2=='float'):
    n = st.number_input('Enter second number: ', step=0.01)
else:
    n = st.number_input('Enter second number: ', step=1)
st.write(f'{m}*{n} = {m*n}')
