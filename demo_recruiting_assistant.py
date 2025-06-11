# demo_recruiting_assistant.py
import streamlit as st
from datetime import datetime
from typing import Dict

# --- Assist logic ---
MEMBERSHIP_TIERS = {
    "Player": {"price": "$30/mo", "features": ["Platform access", "Timeline tracker", "Resume & video", "Real-time alerts", "Unlimited messaging"]},
    "All-Star": {"price": "$50/mo or $500/yr", "features": ["Everything in Player", "Scholarship search assistance", "Monthly coaching call"]},
    "All-Star Extra": {"price": "$99.95/mo or $1000/yr", "features": ["Everything in All-Star", "Free film evaluation", "Twice-monthly calls", "Recruiting video help"]}
}
CONTACT_INFO = {"email": "[email protected]", "phone": "772‑201‑5093", "hours": "7 AM–5 PM ET"}

def show_intro():
    st.title("East Coast Sports Group Recruiting Assistant")
    st.write("I can help with membership guidance, timelines, coach messaging, and more.")

def membership_advisor():
    st.header("Choose the Best Membership Tier")
    sport = st.text_input("What sport do you play?")
    grad_year = st.selectbox("Graduation year", [2025, 2026, 2027, 2028])
    need = st.selectbox("Biggest need", ["Platform access", "Scholarship help", "Film evaluation"])
    for tier, info in MEMBERSHIP_TIERS.items():
        if need == "Platform access" and tier == "Player":
            recommend = tier
        elif need == "Scholarship help" and "Scholarship search assistance" in info["features"]:
            recommend = tier
        elif need == "Film evaluation" and "Free film evaluation" in info["features"]:
            recommend = tier
    st.write(f"**Recommended plan**: {recommend} — {MEMBERSHIP_TIERS[recommend]['price']}")
    st.write("Features:", ", ".join(MEMBERSHIP_TIERS[recommend]["features"]))

def timeline_tool():
    st.header("Recruiting Timeline Generator")
    sport = st.text_input("Sport (same as before)", key="sport2")
    if st.button("Generate Timeline"):
        year = int(st.date_input("Enter your high school graduation date").year)
        now = datetime.now().year
        years_left = year - now
        st.write(f"You have {years_left} years left before graduation.")
        st.write("Suggested milestones:")
        st.markdown(f"""
        - **{now+0}**: Build profile & video  
        - **{now+1}**: Start messaging coaches  
        - **{year-1}**: Visit schools & apply
        - **{year}**: Thrive on campus!
        """)

def contact():
    st.header("Contact & Support")
    st.write(f"📧 {CONTACT_INFO['email']}")
    st.write(f"📞 {CONTACT_INFO['phone']} ({CONTACT_INFO['hours']})")
    if st.button("Get Coach Rip"):
        st.write("Coach Ripley will contact you within 24 hours to discuss your goals.")

def main():
    show_intro()
    membership_advisor()
    timeline_tool()
    contact()

if __name__ == "__main__":
    import streamlit as st_cli
    st_cli.run()
