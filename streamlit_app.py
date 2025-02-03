import streamlit as st
import re
import time
from datetime import datetime

# Custom CSS for animations
st.markdown("""
<style>
@keyframes slideIn {
    0% {
        transform: translateX(-100%);
        opacity: 0;
    }
    100% {
        transform: translateX(0);
        opacity: 1;
    }
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

.sliding-element {
    animation: slideIn 1s ease-out;
}

.fading-element {
    animation: fadeIn 1.5s ease-in-out;
}

.stButton>button {
    transition: all 0.3s ease;
}

.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}

.success-message {
    padding: 20px;
    border-radius: 10px;
    background-color: #d4edda;
    border: 1px solid #c3e6cb;
    animation: fadeIn 1s ease-in-out;
}
</style>
""", unsafe_allow_html=True)

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def is_valid_phone(phone):
    # Accept international format
    pattern = r'^\+?1?\d{9,15}$'
    return re.match(pattern, phone) is not None

def main():
    # Add a loading animation
    with st.spinner('Loading...'):
        time.sleep(1)
    
    st.markdown('<div class="sliding-element">', unsafe_allow_html=True)
    st.title("✨ Registration Form")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Progress bar for form completion
    progress = st.progress(0)
    
    with st.form("registration_form"):
        st.markdown('<div class="fading-element">', unsafe_allow_html=True)
        
        # Personal Information
        st.subheader("📝 Personal Information")
        full_name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        birth_date = st.date_input("Date of Birth", 
                                 min_value=datetime(1900, 1, 1),
                                 max_value=datetime.now())
        
        # Additional Information
        st.subheader("🔍 Additional Information")
        gender = st.selectbox("Gender", ["Select...", "Male", "Female", "Other", "Prefer not to say"])
        occupation = st.text_input("Occupation")
        
        # Interests with animated selection
        interests = st.multiselect(
            "Interests",
            ["Reading", "Sports", "Travel", "Music", "Cooking", "Art", "Technology", "Gaming", "Other"],
            help="Select multiple interests"
        )
        
        # Address Information
        st.subheader("📍 Address Information")
        country = st.selectbox("Country", ["Select...", "United States", "United Kingdom", "Canada", "Australia", "Other"])
        city = st.text_input("City")
        
        # About Me
        st.subheader("👤 About Me")
        about_me = st.text_area("Tell us about yourself")
        
        # File upload with preview
        st.subheader("📎 Profile Picture")
        profile_pic = st.file_uploader("Upload your profile picture", type=["jpg", "png", "jpeg"])
        
        # Terms and Newsletter
        st.subheader("📜 Terms & Preferences")
        terms = st.checkbox("I agree to the Terms and Conditions")
        newsletter = st.checkbox("Subscribe to our newsletter")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Submit button with animation
        submitted = st.form_submit_button("Register ✨")
        
        if submitted:
            # Update progress bar
            progress.progress(50)
            
            # Validation
            error = False
            
            if not full_name:
                st.error("❌ Please enter your full name")
                error = True
                
            if not email or not is_valid_email(email):
                st.error("❌ Invalid email address")
                error = True
                
            if not phone or not is_valid_phone(phone):
                st.error("❌ Invalid phone number")
                error = True
                
            if gender == "Select...":
                st.error("❌ Please select your gender")
                error = True
                
            if country == "Select...":
                st.error("❌ Please select your country")
                error = True
                
            if not terms:
                st.error("❌ Please agree to the Terms and Conditions")
                error = True
                
            if not error:
                # Complete progress bar
                progress.progress(100)
                
                # Success animation and message
                with st.spinner('Processing your registration...'):
                    time.sleep(1)
                
                st.markdown('<div class="success-message">', unsafe_allow_html=True)
                st.success("🎉 Registration Successful!")
                
                # Display registration information with animations
                st.write("### Registration Details:")
                st.write(f"**Name:** {full_name}")
                st.write(f"**Email:** {email}")
                st.write(f"**Phone:** {phone}")
                st.write(f"**Date of Birth:** {birth_date}")
                st.write(f"**Gender:** {gender}")
                st.write(f"**Occupation:** {occupation}")
                st.write(f"**Interests:** {', '.join(interests)}")
                st.write(f"**Country:** {country}")
                st.write(f"**City:** {city}")
                st.write(f"**About Me:** {about_me}")
                st.write(f"**Newsletter Subscription:** {'Yes' if newsletter else 'No'}")
                st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()