

import streamlit as st
from datetime import datetime
from PIL import Image

# --- Must come first ---
st.set_page_config(page_title="East Coast Sports Recruiting", layout="wide")

# --- Static Data ---
MEMBERSHIP_TIERS = {
    "Player": {
        "price": "$30/mo",
        "features": [
            "Platform access", "Timeline tracker", "Resume & video upload",
            "Real-time alerts", "Unlimited messaging"
        ]
    },
    "All-Star": {
        "price": "$50/mo or $500/yr",
        "features": [
            "Everything in Player", "Scholarship search assistance",
            "Monthly coaching call"
        ]
    },
    "All-Star Extra": {
        "price": "$99.95/mo or $1000/yr",
        "features": [
            "Everything in All-Star", "Free film evaluation",
            "Twice-monthly calls", "Recruiting video help"
        ]
    }
}

CONTACT_INFO = {
    "email": "ripley@eastcoastsportsgroup.com",
    "phone": "772‑201‑5093",
    "hours": "7 AM–5 PM ET"
}

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
            <h1>Get Recruited. Stay Ready. Be Seen.</h1>
            <p>Join the top athletes who are taking control of their recruiting journey</p>
            <a class="cta-button" href="#profile">Start Your Profile</a>
        </div>
    """, unsafe_allow_html=True)

def membership_advisor():
    st.header("📋 Membership Recommendation")
    sport = st.selectbox("What sport do you play?", [
        "Football", "Basketball", "Baseball", "Soccer", "Track & Field", "Wrestling",
        "Girls Flag Football", "Esports"
    ])
    grad_year = st.selectbox("Graduation year", [2025, 2026, 2027, 2028])
    need = st.selectbox("What is your biggest need?", [
        "Platform access", "Scholarship help", "Film evaluation"
    ])

    recommended = None
    for tier, info in MEMBERSHIP_TIERS.items():
        if need == "Platform access" and tier == "Player":
            recommended = tier
        elif need == "Scholarship help" and "Scholarship search assistance" in info["features"]:
            recommended = tier
        elif need == "Film evaluation" and "Free film evaluation" in info["features"]:
            recommended = tier

    if recommended:
        st.subheader(f"✅ Recommended Plan: {recommended}")
        st.write(f"💰 {MEMBERSHIP_TIERS[recommended]['price']}")
        st.markdown("🏅 **Features:**")
        for feat in MEMBERSHIP_TIERS[recommended]["features"]:
            st.markdown(f"- {feat}")

def timeline_generator():
    st.header("⏳ Generate Your Recruiting Timeline")
    grad_year = st.selectbox("Graduation Year", [2025, 2026, 2027, 2028], key="timeline_year")
    current_year = datetime.now().year
    years_remaining = grad_year - current_year

    if st.button("Generate Timeline"):
        st.success(f"You have {years_remaining} year(s) until graduation.")
        st.markdown("### Suggested Timeline:")
        st.markdown(f"- **{current_year}**: Build profile and upload film")
        st.markdown(f"- **{current_year + 1}**: Message coaches, attend camps")
        st.markdown(f"- **{grad_year - 1}**: Finalize your top schools and apply")
        st.markdown(f"- **{grad_year}**: Commit and prepare for college life")

def profile_builder():
    st.markdown("## 📝 Create Your Profile")
    st.text_input("Full Name")
    st.selectbox("Sport", [
        "Football", "Basketball", "Baseball", "Soccer", "Track & Field", "Wrestling",
        "Girls Flag Football", "Esports"
    ])
    st.slider("GPA", 0.0, 4.0, step=0.1)
    st.date_input("Graduation Year")

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

    st.markdown("---")

    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://yourdomain.com/sample-profile.jpg", caption="Sample Athlete Profile", use_column_width=True)
    with col2:
        st.markdown("### Why Build a Profile?")
        st.write("""
        • Your personal recruiting webpage  
        • Instant alerts when coaches interact  
        • Shareable with high school and club coaches  
        • Tracks your stats, GPA, and eligibility  
        """)

def contact_info():
    st.header("📞 Contact Coach Rip")
    st.write(f"Email: {CONTACT_INFO['email']}")
    st.write(f"Phone: {CONTACT_INFO['phone']}")
    st.write(f"Hours: {CONTACT_INFO['hours']}")

def show_footer():
    st.markdown("""
        <hr>
        <center>
        <small>Powered by <strong>28 Foot Marketing</strong> | © 2025 East Coast Sports Group</small>
        </center>
    """, unsafe_allow_html=True)

# --- Main Layout ---
def main():
    show_banner()
    profile_builder()
    membership_advisor()
    timeline_generator()
    contact_info()
    show_footer()

if __name__ == "__main__":
    main()
