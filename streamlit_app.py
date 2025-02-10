import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
from datetime import datetime
import time

# Cấu hình trang
st.set_page_config(
    page_title="My Responsive Website",
    page_icon="🌟",
    layout="wide"
)

# Custom CSS cho responsive design
st.markdown("""
<style>
/* Main container */
.main {
    padding: 20px;
}

/* Responsive text */
@media (max-width: 768px) {
    .big-font {
        font-size: 20px !important;
    }
    .medium-font {
        font-size: 16px !important;
    }
}

@media (min-width: 769px) {
    .big-font {
        font-size: 30px !important;
    }
    .medium-font {
        font-size: 20px !important;
    }
}

/* Card style */
.card {
    padding: 20px;
    border-radius: 10px;
    background-color: #ffffff;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
}

/* Navigation style */
.nav-link {
    text-decoration: none;
    color: #333;
    padding: 10px;
    border-radius: 5px;
    transition: background-color 0.3s;
}

.nav-link:hover {
    background-color: #f0f2f6;
}

/* Button styles */
.stButton>button {
    width: 100%;
    border-radius: 5px;
    background-color: #4CAF50;
    color: white;
    transition: all 0.3s;
}

.stButton>button:hover {
    background-color: #45a049;
    transform: translateY(-2px);
}

/* Form styles */
.stTextInput>div>div>input {
    border-radius: 5px;
}

/* Custom header */
.custom-header {
    background-color: #f8f9fa;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 20px;
}

/* Footer style */
.footer {
    position: fixed;
    bottom: 0;
    width: 100%;
    background-color: #f8f9fa;
    padding: 10px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Tạo class cho quản lý session state
class SessionState:
    def __init__(self):
        self.logged_in = False
        self.current_page = "home"

# Khởi tạo session state
if 'session_state' not in st.session_state:
    st.session_state.session_state = SessionState()

# Components
def header():
    st.markdown('<div class="custom-header">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown('<h1 class="big-font" style="text-align: center;">My Responsive Website</h1>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def navigation():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("🏠 Home"):
            st.session_state.session_state.current_page = "home"
    with col2:
        if st.button("📊 Dashboard"):
            st.session_state.session_state.current_page = "dashboard"
    with col3:
        if st.button("📝 Profile"):
            st.session_state.session_state.current_page = "profile"
    with col4:
        if st.button("ℹ️ About"):
            st.session_state.session_state.current_page = "about"

def login_form():
    with st.form("login_form"):
        st.markdown('<h2 class="medium-font">Login</h2>', unsafe_allow_html=True)
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")
        
        if submit and username == "admin" and password == "admin":
            st.session_state.session_state.logged_in = True
            st.success("Login successful!")
            time.sleep(1)
            st.experimental_rerun()

def home_page():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h2 class="medium-font">Welcome to our Website</h2>', unsafe_allow_html=True)
    
    # Featured content
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### Latest Updates
        - New features added
        - Improved performance
        - Bug fixes
        """)
    with col2:
        st.markdown("""
        ### Quick Links
        - Documentation
        - Support
        - Contact Us
        """)
    st.markdown('</div>', unsafe_allow_html=True)

def dashboard_page():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h2 class="medium-font">Dashboard</h2>', unsafe_allow_html=True)
    
    # Sample data
    data = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        'Sales': [100, 120, 80, 150, 130]
    })
    
    # Interactive charts
    fig = px.line(data, x='Month', y='Sales', title='Monthly Sales')
    st.plotly_chart(fig, use_container_width=True)
    
    # Stats in columns
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Sales", "$580", "+12%")
    with col2:
        st.metric("Customers", "1,234", "+5%")
    with col3:
        st.metric("Satisfaction", "98%", "+2%")
    
    st.markdown('</div>', unsafe_allow_html=True)

def profile_page():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h2 class="medium-font">Profile</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://via.placeholder.com/150", width=150)
        st.markdown("### John Doe")
        st.markdown("Software Developer")
    with col2:
        st.markdown("### Contact Information")
        st.markdown("📧 john@example.com")
        st.markdown("📱 +1234567890")
    
    st.markdown('</div>', unsafe_allow_html=True)

def about_page():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h2 class="medium-font">About Us</h2>', unsafe_allow_html=True)
    st.markdown("""
    We are a company dedicated to providing the best services to our customers.
    Our mission is to make technology accessible to everyone.
    
    ### Our Values
    - Innovation
    - Quality
    - Customer Focus
    - Integrity
    """)
    st.markdown('</div>', unsafe_allow_html=True)

def footer():
    st.markdown(
        '<div class="footer">© 2024 My Responsive Website. All rights reserved.</div>',
        unsafe_allow_html=True
    )

def main():
    header()
    
    if not st.session_state.session_state.logged_in:
        login_form()
    else:
        navigation()
        
        if st.session_state.session_state.current_page == "home":
            home_page()
        elif st.session_state.session_state.current_page == "dashboard":
            dashboard_page()
        elif st.session_state.session_state.current_page == "profile":
            profile_page()
        elif st.session_state.session_state.current_page == "about":
            about_page()
        
        footer()

if __name__ == "__main__":
    main()