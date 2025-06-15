import streamlit as st
from datetime import datetime
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
            <h2>Get Recruited. Stay Ready. Be Seen.</h2>
            <p>Join the top athletes taking control of their recruiting journey</p>
            <a class="cta-button" href="https://eastcoastsportsgrouprecruiting.com" target="_blank">Start Your Profile</a>
        </div>
    """, unsafe_allow_html=True)

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

    st.info("To fully experience this app, you must subscribe to a service plan. Notification features like coach alerts only work through the dedicated student-athlete site after login.")

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

def testimonials():
    st.header("💬 Real Stories from Athletes and Parents")
    st.success("“Coach Rip helped my daughter land three D2 offers in one month!” – Parent, Florida")
    st.info("“The timeline helped me stay on track. I signed my NLI last week!” – Senior WR, Maryland")
    st.warning("“We were lost before using the app. Now we feel like we are ahead of the game.” – Family from Texas")

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

# --- Navigation Flow ---
def main():
    show_banner()
    st.markdown("### 👇 Choose a section to get started:")
    section = st.radio("", [
        "Build Your Profile",
        "Recruiting Timeline",
        "Membership Advisor",
        "Success Stories",
        "Contact Coach"
    ])

    if section == "Build Your Profile":
        profile_builder()
    elif section == "Recruiting Timeline":
        timeline_generator()
    elif section == "Membership Advisor":
        membership_advisor()
    elif section == "Success Stories":
        testimonials()
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

