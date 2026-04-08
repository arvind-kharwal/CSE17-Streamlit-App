import streamlit as st;
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng
st.title('Home')
df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])
st.line_chart(df)