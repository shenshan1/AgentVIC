import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Meet VICKY – Your Vocal Intelligence Coach",
    page_icon="🎙️",
    layout="centered"
)

# --- HEADER ---
st.title("🎙️ Meet VICKY – Your Vocal Intelligence Coach")
st.subheader("Also known as VIC")

# --- INTRO ---
st.markdown("""
VICKY (short for **Vocal Intelligence Coach**) is your AI-powered voice mentor.

Whether you're a singer, speaker, student, or performer, **VIC** helps you unlock your vocal potential with smart, personalized guidance.
""")

# --- WHAT VICKY CAN DO ---
st.markdown("---")
st.header("🔥 What VICKY Can Do")

st.markdown("""
### 🗣️ Real-Time & Asynchronous Coaching
Join live sessions or send in your recordings for feedback anytime.

### 🎯 Feedback on Key Vocal Elements
- **Pitch**: Stay in tune and hit every note with confidence  
- **Tone**: Discover your signature sound and polish your resonance  
- **Breath**: Learn to support your voice with powerful, relaxed breathing  
- **Diction**: Improve clarity and pronunciation  
- **Delivery**: Connect emotionally and stylistically with your audience  

### 🎵 Guided Warmups & Vocal Exercises
- Daily warmups tailored to your voice
- Custom drills based on your progress
- Smart suggestions for your vocal type

### 📈 Progress Tracking & Personalized Goals
- Weekly reports
- Vocal journals
- Motivational feedback to keep you growing

### 💡 Encouragement & Education
- Learn how your voice works
- Tips for confidence, performance, and healthy habits
""")

# --- CTA BUTTONS ---
st.markdown("---")
st.header("🚀 Ready to Train with VICKY?")
col1, col2, col3 = st.columns(3)

with col1:
    st.button("🎤 Start Vocal Session", help="Coming soon")

with col2:
    st.button("📤 Upload Recording", help="Feature under development")

with col3:
    st.button("📚 Browse Exercises", help="Feature under development")

# --- FOOTER ---
st.markdown("---")
st.caption("VICKY is part of the Nrth Eydn Ltd. creative development platform. Powered by AI. Guided by purpose.")



        

      
