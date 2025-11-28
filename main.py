import streamlit as st
import google.generativeai as genai

st.title("我的 AI 聊天室 🤖")

# 1. 取得 API Key
# 這裡告訴程式去 Streamlit 的秘密金庫拿鑰匙
api_key = st.secrets["GOOGLE_API_KEY"]

if not api_key:
    st.error("沒有偵測到 API Key！")
    st.stop()

# 2. 設定模型
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. 簡單的對話框
user_input = st.text_input("你想問什麼？", "你好！")

if st.button("發送"):
    try:
        response = model.generate_content(user_input)
        st.write("Gemini 回答：")
        st.success(response.text)
    except Exception as e:
        st.error(f"發生錯誤：{e}")
