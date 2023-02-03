# <pythonfile>.ipynb notebook
# 프로그램 작성시에는 pythonfile.py
# python3 <pythonfile>.py
# streamlit run <streamlitapp>.py

import streamlit as st
import pandas as pd 

st.title("First_APP")
def main():
    df = pd.DataFrame({
        "first_col":[1,2,3,4],
         "second_col":[10,20,30,40]
})
    st.write(df)

if __name__ == "__main__":
    main()