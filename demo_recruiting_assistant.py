import streamlit as st
from datetime import datetime
import requests
from PIL import Image

# --- Page Setup ---
st.set_page_config(page_title="East Coast Sports Recruiting", layout="wide")

# --- Branding Header ---
st.markdown("""
    <div style="background-color:#002244;padding:10px 20px;border-radius:8px;margin-bottom:20px;">
        <h1 style="color:white;margin-bottom:0;">🏈 East Coast Sports Group</h1>
        <p style="color:#FFCC00;font-weight:bold;margin-top:5px;">Student-Athlete Recruiting Made Personal</p>
    </div>
""", unsafe_allow_html=True)

# --- Static Data ---
CONTACT_INFO = {
    "email": "ripley@eastcoastsportsgroup.com",
    "phone": "772‑201‑5093",
    "hours": "7 AM–5 PM ET"
}

def send_to_gohighlevel(name, sport, gpa, grad_year, email, phone):
    url = "https://your-gohighlevel-webhook-or-form-endpoint.com"  # Replace with actual GHL endpoint
    payload = {
        "full_name": name,
        "sport": sport,
        "gpa": gpa,
        "grad_year": grad_year,
        "email": email,
        "phone": phone
    }
    try:
        response = requests.post(url, json=payload)
        return response
    except Exception as e:
        return None

# --- UI Sections ---
def show_banner():
    st.markdown("""
        <style>
        .banner {
            background-image: url('https://yourdomain.com/banner.jpg');
            background-size: cover;
            background-position: center;
            padding: 60px 20px;
            border-radius: 10px;
            text-align: center;
            color: white;
        }
        .cta-button {
            background-color: #FFCC00;
            color: #000;
            padding: 12px 24px;
            font-weight: bold;
            border-radius: 5px;
            text-decoration: none;
        }
        </style>
        <div class="banner">
            <h2>Get Recruited. Stay Ready. Be Seen.</h2>
            <p>Join the top athletes taking control of their recruiting journey</p>
            <a class="cta-button" href="https://eastcoastsportsgrouprecruiting.com" target="_blank">Start Your Profile</a>
        </div>
    """, unsafe_allow_html=True)

def profile_builder():
    st.markdown("## 📝 Create Your Profile")
    name = st.text_input("Full Name")
    sport = st.selectbox("Sport", [
        "Football", "Basketball", "Baseball", "Soccer", "Track & Field", "Wrestling",
        "Girls Flag Football", "Esports"
    ])
    gpa = st.slider("GPA", 0.0, 4.0, step=0.1)
    grad_year = st.date_input("Graduation Year")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")

    st.markdown("## 🎥 Upload Highlight Video")
    video_url = st.text_input("YouTube or Hudl Link")
    if video_url:
        st.video(video_url)

    st.markdown("## 🧭 Track Your Recruiting Journey")
    st.progress(60)
    st.markdown("You are 60% through your recruiting profile setup.")

    st.markdown("## 🏆 Coach Notifications")
    st.checkbox("Notify me when a coach views my profile")
    st.checkbox("Text me when my video is opened")

    st.info("To fully experience this app, you must subscribe to a service plan. Notification features like coach alerts only work through the dedicated student-athlete site after login.")

    if st.button("Submit Profile"):
        if name and email and phone:
            res = send_to_gohighlevel(name, sport, gpa, str(grad_year), email, phone)
            if res and res.status_code == 200:
                st.success("Profile submitted! You’re now in our recruiting system.")
            else:
                st.error("Something went wrong. Please try again.")
        else:
            st.warning("Please complete name, email, and phone to proceed.")

def contact_info():
    st.header("📞 Contact Coach Rip")
    st.write(f"📧 Email: {CONTACT_INFO['email']}")
    st.write(f"📱 Phone: {CONTACT_INFO['phone']}")
    st.write(f"🕘 Hours: {CONTACT_INFO['hours']}")

def show_footer():
    st.markdown("""
        <hr style="margin-top: 2em; margin-bottom: 1em;">
        <center>
        <small>
            © 2025 East Coast Sports Group<br>
            Powered by <a href="https://your-placeholder-url.com" target="_blank" style="color: inherit; text-decoration: underline;">
            28 Foot Marketing</a>
        </small>
        </center>
    """, unsafe_allow_html=True)

# --- Main ---
def main():
    show_banner()
    st.markdown("### 👇 Choose a section to get started:")
    section = st.radio("", [
        "Build Your Profile",
        "Contact Coach"
    ])

    if section == "Build Your Profile":
        profile_builder()
    elif section == "Contact Coach":
        contact_info()

    st.markdown("---")
    st.markdown("### ⏳ Ready to Get Recruited?")
    st.markdown("> Join today and get alerts when coaches view your profile – even while you're asleep.")
    st.markdown("""
        <a href="https://eastcoastsportsgrouprecruiting.com" target="_blank">
            <button style="background-color:#FFCC00;border:none;color:black;padding:12px 24px;
            text-align:center;text-decoration:none;display:inline-block;
            font-size:16px;border-radius:6px;font-weight:bold;">
            Start My Recruiting Profile
            </button>
        </a>
    """, unsafe_allow_html=True)

    show_footer()

if __name__ == "__main__":
    main()


