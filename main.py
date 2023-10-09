import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
# Create a two-column layout
col1, col2 = st.columns(2)  # Use beta_columns instead of columns

# Add content to the first column
with col1:
    st.image("images/profilepic.jpg", width=400)

# Add content to the second column
with col2:
    st.title("Greg")
    content = """Hello, I'm Greg, and at the age of 36, I bring a unique blend of experience to the table. With a strong background in Marketing Management and an extensive 13-year journey as a Medical Coder, I'm currently in the process of embarking on a transformative journey into the world of self-taught programming.
    This transition is a testament to my unwavering passion for technology, coding, and the boundless possibilities they offer. In my portfolio, you'll discover a curated collection of innovative projects that reflect my dedication to exploring new horizons a"""
    st.write(content)

content2 = """Below you can find some of the apps i have built in python. Feel free to contact me."""
st.write(content2)

# Load data from a CSV file with the correct delimiter
data = pd.read_csv("data.csv", sep=";")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    # Display the titles from the data
    for index, row in data[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row['image'])
        st.write(f'[Source]({row["url"]})')

with col4:
    # Display the titles from the data
    for index, row in data[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row['image'])
        st.write(f'[Source]({row["url"]})')