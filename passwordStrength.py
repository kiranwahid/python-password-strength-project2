import streamlit as st
import re

# Set up page configuration
st.set_page_config(page_title="Password Strength", page_icon="🔒", layout="centered")

# Apply custom CSS styles
st.markdown("""
<style>
body, .stApp{
    background-color:#60a3bc;
    color:white;
}
    .main {text-align: center;}
    .stTextInput {width: 60% !important; margin: auto;}
    .stButton button { 
        width: 40%; 
        background-color: #0c2461; 
        color: white; 
        font-size: 18px; 
        margin: auto; 
        display: flex; 
        justify-content: center; 
        align-items: center; 
        padding: 10px 20px; 
        border-radius: 10px; 
        border: none;
    }
    .stButton button:hover {background-color: #0a3d62; color:black}
    .stButton {text-align: center;} /* Ensures button is centered */
</style>
""", unsafe_allow_html=True)

# App title and description
st.title("🔐 Password Strength Checker")
st.write("Enter your password below to check its security level 🔍")

# Function to check password strength
def password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 characters long**")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **both uppercase (A-Z) and lowercase (a-z) letters**")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one digit (0-9)**")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one special character (!@#$%^&*)**")

    if score == 4:
        st.success("☑️ **Strong Password** – Your password is secure!")
    elif score == 3:
        st.warning("⚠️ **Moderate Password** – Consider improving security by adding more features.")
    else:
        st.error("❌ **Weak Password** – Follow the suggestions below to strengthen it.")

    if feedback:
        with st.expander("🔍 Improve Your Password"):
            for item in feedback:
                st.write(item)

# Input for password
password = st.text_input("Enter Your Password:", type="password", help="Make sure your password is strong 🔐")

# Button to check password strength
if st.button("Check Password Strength"):
    if password:
        password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")
