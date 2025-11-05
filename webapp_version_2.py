
import streamlit as st
import random

#Function to load a random quote
def get_quote():
    with open("quotes.txt", "r") as f:
        quotes = f.readlines()
    return random.choice(quotes).strip()

#CSS for background and styling
st.markdown(
    """
    <style>
    body {
        background-color: #ffffff;
    }
    .quote-text {
        font-size: 22px;
        color: #2c3e50;
        font-style: sans-serif;
        text-align: center;
        padding: 20px;
        border-left: 4px solid #4CAF50;
        background-color: #ecf9f1;
        border-radius: 10px;
    }
    .footer {
        text-align: center;
        color: gray;
        font-size: 13px;
        margin-top: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#Title
st.markdown("<h1 style='text-align: center;'> Quote of the Day </h1>", unsafe_allow_html=True)

#Initialize state
if "quote" not in st.session_state:
    st.session_state.quote = get_quote()

#Show quote inside styled box
st.markdown(f"<div class='quote-text'>{st.session_state.quote}</div>", unsafe_allow_html=True)

#Centered button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Inspire Me"):
        st.session_state.quote = get_quote()
        st.markdown(f"<div class='quote-text'>{st.session_state.quote}</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>Built by Kweku</div>", unsafe_allow_html=True)

import streamlit as st
import random

#Function to load a random quote
def get_quote():
    with open("quotes.txt", "r") as f:
        quotes = f.readlines()
    return random.choice(quotes).strip()

#CSS for background and styling
st.markdown(
    """
    <style>
    body {
        background-color: #ffffff;
    }
    .quote-text {
        font-size: 22px;
        color: #2c3e50;
        font-style: sans-serif;
        text-align: center;
        padding: 20px;
        border-left: 4px solid #4CAF50;
        background-color: #ecf9f1;
        border-radius: 10px;
    }
    .footer {
        text-align: center;
        color: gray;
        font-size: 13px;
        margin-top: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#Title
st.markdown("<h1 style='text-align: center;'> Quote of the Day </h1>", unsafe_allow_html=True)

#Initialize state
if "quote" not in st.session_state:
    st.session_state.quote = get_quote()

#Show quote inside styled box
st.markdown(f"<div class='quote-text'>{st.session_state.quote}</div>", unsafe_allow_html=True)

#Centered button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Inspire Me"):
        st.session_state.quote = get_quote()
        st.markdown(f"<div class='quote-text'>{st.session_state.quote}</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>Built by Kweku</div>", unsafe_allow_html=True)
