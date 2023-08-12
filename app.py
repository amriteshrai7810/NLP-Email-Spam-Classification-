import streamlit as st

st.title('atul <3 Deependar')

col1, col2 = st.columns(2)
with col1:
    st.image('Untitled.png')
    st.header('Mai hu atul aloo')
    st.header('Mera dost hai lohith kalu')

with col2:
    st.image('Untitled3.png')
    st.header('Mai hu jaise ek jangli bhalu')

st.header('Mai hu atul aloo mera bhai hai jungle ka bhaloo mera dost hai lohith kalu mai khud bhi hu bada chalu')
st.subheader('atul kutta hai bsdk')

st.sidebar.title('Menu')
st.sidebar.markdown('-Home'
                    '-Menu'
                    '-Contact')


