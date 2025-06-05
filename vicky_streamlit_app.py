import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="🎙️ VICKY – Vocal Intelligence Coach",
    page_icon="🎤",
    layout="centered"
)

# --- HEADER ---
st.title("🎙️ Meet VICKY – Your Vocal Intelligence Coach")
st.subheader("Also known as VIC")

st.markdown("""
VICKY (short for **Vocal Intelligence Coach**) is your AI-powered voice mentor.  
Get help with pitch, tone, breath control, diction, delivery, and more.
""")

st.divider()

# --- VOCAL GOALS ---
st.header("✍️ What's your vocal goal today?")
user_goal = st.text_input("Enter your vocal focus (e.g. 'improve pitch', 'project better', 'build breath control')")

if user_goal:
    st.success(f"✅ Goal saved: *{user_goal}*")

# --- AUDIO UPLOAD ---
st.header("🎧 Upload Your Vocal Sample")
audio_file = st.file_uploader("Choose a vocal recording (MP3 or WAV)", type=["mp3", "wav"])

if audio_file:
    st.audio(audio_file, format='audio/wav')
    st.success("✅ Audio uploaded successfully!")

# --- CHAT INTERFACE ---
st.header("💬 Chat with VICKY")

# Initialize chat history if not already
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input
user_input = st.text_input("Type your question here (e.g. 'How do I improve my tone?')", key="chat_input")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Simulated intelligent reply based on keywords
    reply = "That's a great question! Let's explore that together."

    if "pitch" in user_input.lower():
        reply = "Try practicing slow scales and matching a piano or tuner note-for-note."
    elif "tone" in user_input.lower():
        reply = "Your tone improves with good breath support and relaxed throat. Try humming exercises!"
    elif "breath" in user_input.lower():
        reply = "Use a 'hiss' exercise: inhale fully, then exhale slowly on a hiss to strengthen control."
    elif "diction" in user_input.lower():
        reply = "Practice tongue twisters slowly and clearly, focusing on consonants."
    elif "confidence" in user_input.lower():
        reply = "Confidence builds with routine and self-encouragement. Practice in front of a mirror."

    st.session_state.chat_history.append({"role": "vicky", "content": reply})

# Display the chat
for msg in st.session_state.chat_history:
    speaker = "🧑 You" if msg["role"] == "user" else "🎙️ VICKY"
    st.markdown(f"**{speaker}:** {msg['content']}")

# --- FOOTER ---
st.divider()
st.caption("VICKY is part of the Nrth Eydn Ltd. creative development platform. Streamlit-only prototype.")
