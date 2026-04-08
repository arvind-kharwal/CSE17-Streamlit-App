import streamlit as st;

import streamlit as st
st.title('Contact')
enable = st.checkbox("Enable camera")
picture = st.camera_input("Take a picture", disabled=not enable)

if picture:
    st.image(picture)