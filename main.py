# 환경변수 사용하기 위한 라이브러리 로드
# from dotenv import load_dotenv
# load_dotenv()
from langchain_openai import ChatOpenAI
import streamlit as st
# OpenAI 와 ChatOpenAI 는 다르다. OpenAI -> LLM , ChatOpenAI -> Chat 



chat_model = ChatOpenAI()

st.title("인공지능 시인")

content = st.text_input("시의 주제를 제시해주세요.")

if st.button("시 작성 요청하기"):

    with st.spinner('시 작성 중...'):
        result = chat_model.invoke(content + "에 대한 시를 써줘.")
        st.write(result.content)


# print(result.content)


# front end 는 streamlit 으로 한다.