import streamlit as st;
import pandas as pd
st.title('Profile')
col1,col2,col3 = st.columns(3)
col1.image('assets/moon.png',width=100)
col3.subheader("My Name: ")

st.divider()

confusion_matrix = pd.DataFrame(
    {
        "Predicted Cat": [85, 3, 2, 1],
        "Predicted Dog": [2, 78, 4, 0],
        "Predicted Bird": [1, 5, 72, 3],
        "Predicted Fish": [0, 2, 1, 89],
    },
    index=["Actual Cat", "Actual Dog", "Actual Bird", "Actual Fish"],
)
st.table(confusion_matrix)

st.divider()
st.markdown("- Item A")
st.markdown("- Item B")
st.divider()
# st.balloons()
st.snow()
st.divider()
import time

with st.spinner("Wait for it...", show_time=True):
    time.sleep(5)
st.success("Done!")
st.button("Rerun")
st.divider()
st.toast("Your edited image was saved!", icon="😍")