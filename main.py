import streamlit as st;
# st.title('Streamlit App')

home_page = st.Page(
    page = 'views\home.py',
    title='Home',
    icon=':material/home:'
)
profile_page = st.Page(
    page = 'views\profile.py',
    title='Profile',
    icon=':material/person:',
    default=True
)
contact_page = st.Page(
    page = 'views\contact.py',
    title='Contact us',
    icon=':material/thumb_up:',
)

# nb = st.navigation(pages=[home_page, profile_page,contact_page])
nb= st.navigation(
    {
        'info':[home_page,profile_page],
        'Useful Link':[contact_page]
    }
)
st.logo('assets\moon.png')
st.sidebar.text("Powered by: Arvind")
nb.run()