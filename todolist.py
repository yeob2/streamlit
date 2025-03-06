import streamlit as st

# 세션 상태에 할 일 목록 초기화
if 'todos' not in st.session_state:
    st.session_state.todos = []

# 할 일 추가 함수
def add_todo():
    if st.session_state.new_todo:
        st.session_state.todos.append(st.session_state.new_todo)
        st.session_state.new_todo = ""  # 입력창 초기화

st.title("To Do List 앱")

# 할 일 입력창
st.text_input("할 일을 입력하세요:", key="new_todo")
st.button("추가", on_click=add_todo)

st.write("## 할 일 목록")
for i, todo in enumerate(st.session_state.todos):
    st.write(f"{i+1}. {todo}")
