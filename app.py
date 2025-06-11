
import streamlit as st
from datetime import datetime

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

# --- Functions ---
def show_intro():
    st.title("🏈 East Coast Sports Recruiting Assistant")
    st.write("Get guidance on memberships, recruiting timelines, and support from Coach Rip.")

def membership_advisor():
    st.header("📋 Membership Recommendation")
    sport = st.text_input("What sport do you play?")
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
        st.write("🏅 Features:")
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

def contact_info():
    st.header("📞 Contact Coach Rip")
    st.write(f"Email: {CONTACT_INFO['email']}")
    st.write(f"Phone: {CONTACT_INFO['phone']}")
    st.write(f"Hours: {CONTACT_INFO['hours']}")

# --- App Layout ---
def main():
    show_intro()
    membership_advisor()
    timeline_generator()
    contact_info()

if __name__ == "__main__":
    main()
