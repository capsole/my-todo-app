import streamlit as st
from modules import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    print(todo)


st.title("My Todo App")
st.subheader("this is a basic to do app")
st.write("this app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="add here", label_visibility="hidden", placeholder="Enter something needed to be done...",
              on_change=add_todo, key='new_todo')
#st.button("Add")
#st.button("Completed")
#st.session_state