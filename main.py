import streamlit as st

st.set_page_config(layout="wide")
# Create a two-column layout
col1, col2 = st.columns(2)  # Use beta_columns instead of columns

# Add content to the first column
with col1:
    st.image("images/profilepic.jpg", width=600)

# Add content to the second column
with col2:
    st.title("Greg")
    content = """Hello, I'm Greg, and at the age of 36, I bring a unique blend of experience to the table. With a strong background in Marketing Management and an extensive 13-year journey as a Medical Coder, I'm currently in the process of embarking on a transformative journey into the world of self-taught programming.
    This transition is a testament to my unwavering passion for technology, coding, and the boundless possibilities they offer. In my portfolio, you'll discover a curated collection of innovative projects that reflect my dedication to exploring new horizons a"""
    st.write(content)
