# import streamlit as st
#
# st.title("Welcome to Wscube tech ")
# st.header("Python")
# st.subheader("Java")
# st.markdown(" I love Python")
# st.code("""for i in range(1,5,1):
#                 print("Hello")
#          """)
#
# import streamlit as st
# import pandas as pd
#
# dataset = pd.read_csv("List of College.csv")
# st.dataframe(dataset)

import streamlit as st
import pandas as pd
name = st.text_input("Enter your Name :- ")
fname = st.text_input("Enter your Father Name :-")
adr = st.text_area("Enter your Address :-")
classdata = st.selectbox("Enter your class :",(1,2,3,4,5,6,7,8,9,10,11,12,"DIPLOLA"))

button = st.button("Done")
if button:
    st.markdown(f"""
Name : {name}
f_name : {fname}
Adr : {adr}
class : {classdata}
""")