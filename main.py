import streamlit as st

st.set_page_config(page_title="jordans webpage",
                   page_icon=":folded_hands",
                   layout="wide")
st.subheader("Hello, my name is jordan")
st.title(" An Aspiring Software Engineer")
st.write(
    "I currently work part time in audio visual I.T. and enjoy solving complex problems using technology."
)
st.write(
    "[Here is my linkedin>](https://www.linkedin.com/in/jordan-cameron-788232323/)"
)
with st.container():
  st.write("---")
  left_column, right_column = st.columns(2)
  with left_column:
    st.subheader("I am a audio visual support specialist")
    st.write("""
    - implamented visual solutions by running and maintaining visual signal cables such as HDMI, SDi, and rj45
    - handle lighting solutions through digital and analog DMX programming
    
    - handle DMX network programming and configurtions to handle lighting solutions
    
    - configured lan and wlan network through router and switcher configuration"""
             )
    with right_column:
      st.image("IMG_1883.jpg", width=300)

with st.container():
  st.write("---")
  st.subheader("My Certifications")
  st.write("---")
  left_column, right_column = st.columns((1, 2))
  with left_column:
    st.image("cbre.png")
  with right_column:
    st.write("**CBRE - Project Management**")
    st.write("""
    - I manage projects by compartmentalizing tasks and assigning them to team members
    - I use gaant charts to manage and prioritize assignments
    - I keep track of the hours worked for each portion of the project
    - I make sure to utilize all resources efficiently to complete the project"""
             )
