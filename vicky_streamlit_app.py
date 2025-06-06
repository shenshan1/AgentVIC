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


import requests

st.markdown("---")
st.header("💬 Chat with VICKY")

user_input = st.text_input("Ask VICKY anything about your voice, warmups, or singing tips:")

if user_input:
    with st.spinner("VICKY is thinking..."):
        headers = {
            "Authorization": "Bearer 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",
            "Content-Type": "application/json"
        }

        payload = {
            "inputs": {
                "text": f"You are VIC, a gentle and supportive vocal coach helping a singer. Answer this: {user_input}"
            }
        }

        response = requests.post(
            "https://api-inference.huggingface.co/models/Qwen/Qwen1.5-1.8B-Chat",
            headers=headers,
            json=payload
        )

        if response.status_code == 200:
            try:
                output = response.json()
                if isinstance(output, list) and len(output) > 0:
                    reply = output[0]['generated_text'].split(user_input)[-1].strip()
                    st.markdown(f"🗣️ **VICKY:** {reply}")
                else:
                    st.warning("⚠️ No valid response from VIC.")
            except Exception as e:
                st.error(f"🔧 Error parsing response: {e}")
        else:
            st.error(f"❌ Error: {response.status_code} - {response.text}")

# --- FOOTER ---
st.markdown("---")
st.caption("VICKY is part of the Nrth Eydn Ltd. creative development platform. Powered by AI. Guided by purpose.")



        

      
