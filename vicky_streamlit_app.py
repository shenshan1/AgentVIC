import streamlit as st
from audio_recorder_streamlit import audio_recorder
import librosa
import soundfile as sf
import numpy as np
import io

st.set_page_config(page_title="VICKY - Vocal Intelligence Coach", layout="centered")
st.title("🎙️ VICKY - Your Vocal Intelligence Coach")

# Guided Warmups and Breathing
with st.expander("🧘 Guided Breathing and Vocal Warmups"):
    st.markdown("**Breathing Exercise:**")
    st.markdown("1. Inhale deeply through your nose for 4 counts\n2. Hold for 4 counts\n3. Exhale gently through your mouth for 6 counts\n4. Repeat 4 times")
    st.markdown("**Pitch Glide:** Glide from low to high pitch on 'oooo' and back down. Helps stretch your range.")
    st.markdown("**Lip Trills:** Try lip trills on a simple scale. This warms up pitch and airflow.")
    st.markdown("**Sirens:** Start from your lowest note and slide to your highest and back.")

# Ask user what song they're singing
song_title = st.text_input("🎵 What song are you singing today?", placeholder="e.g., 'Halo by Beyoncé'")
if song_title:
    st.markdown(f"🎤 Singing: **{song_title}**")

# Audio Recorder
audio_bytes = audio_recorder(
    text="🎤 Click to record your voice",
    recording_color="#e8b62c",
    neutral_color="#6aa36f",
    icon_name="microphone",
    icon_size="2x",
)

if audio_bytes:
    st.audio(audio_bytes, format="audio/wav")

    try:
        # Load audio
        audio_buffer = io.BytesIO(audio_bytes)
        audio_data, sample_rate = sf.read(audio_buffer)

        if len(audio_data.shape) > 1:
            audio_data = librosa.to_mono(audio_data.T)

        duration = len(audio_data) / sample_rate
        st.write(f"🎧 Sample Rate: {sample_rate} Hz")
        st.write(f"🕒 Duration: {duration:.2f} seconds")

        # Audio Features
        tempo, beats = librosa.beat.beat_track(y=audio_data, sr=sample_rate)
        pitch = librosa.yin(audio_data, fmin=80, fmax=1000, sr=sample_rate)
        pitch_mean = np.mean(pitch)
        pitch_std = np.std(pitch)
        energy = np.mean(librosa.feature.rms(y=audio_data))
        mfccs = librosa.feature.mfcc(y=audio_data, sr=sample_rate, n_mfcc=13)

        # Plot waveform
        st.subheader("📈 Waveform")
        st.line_chart(audio_data)

        # VICKY Feedback
        st.markdown("---")
        st.subheader("🧠 VICKY's Feedback")

        feedback = ""

        if pitch_std < 20:
            feedback += "✅ Pitch was stable — great control!\n\n"
        else:
            feedback += "🎯 Try working on pitch accuracy — some variation noted.\n\n"

        if energy < 0.02:
            feedback += "💤 Soft delivery — could work well for emotional or intimate songs.\n\n"
        elif energy > 0.1:
            feedback += "🔥 Strong projection — this suits powerful or belting songs.\n\n"
        else:
            feedback += "🎵 Balanced energy — works for most genres.\n\n"

        if tempo < 70:
            feedback += "🕊️ Slow tempo — great for soul, R&B, or ballads.\n"
        elif tempo > 120:
            feedback += "💃 Fast tempo — consider pop or upbeat gospel.\n"
        else:
            feedback += "🎶 Mid-tempo — flexible genre range.\n"

        st.success("Here's what VIC says:")
        st.markdown(f"**{feedback}**")

    except Exception as e:
        st.error(f"⚠️ Error processing audio: {e}")

else:
    st.info("Click the microphone above to record your voice.")

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

st.header("🎵 Learn With VICKY")

exercise = st.selectbox(
    "Choose an area to practice:",
    ["Breathing", "Pitch Accuracy", "Voice Control", "Stretching Vocal Range"]
)

if exercise == "Breathing":
    st.subheader("🫁 Breathing Exercises")
    st.markdown("""
- **Hiss Exercise:** Inhale deeply for 4 seconds, exhale with a long steady “ssss” sound. Repeat 5 times.  
- **Box Breathing:** Inhale 4s → Hold 4s → Exhale 4s → Hold 4s. Repeat 4 cycles.  
- **Belly Breathing:** Place a hand on your stomach, inhale deeply so your hand rises, then exhale slowly.

Try 5 minutes of focused breathing before singing.
""")

elif exercise == "Pitch Accuracy":
    st.subheader("🎯 Pitch Exercises")
    st.markdown("""
- **5-Tone Scale:** Sing Do-Re-Mi-Fa-So (C-D-E-F-G), then back down. Use a piano app or tuner to match.  
- **Pitch Matching:** Play a single note (e.g. C4) and hold it. Check against a piano or digital tuner.  
- **Lip Trill Scales:** Sing scales while doing a lip trill (like a motorboat).

Daily repetition improves pitch control.
""")

elif exercise == "Voice Control":
    st.subheader("🎤 Voice Control Drills")
    st.markdown("""
- **Volume Swells:** Sustain a note and gradually increase/decrease volume without cracking.  
- **Staccato vs. Legato:** Sing short bursts (staccato) vs smooth long notes (legato).  
- **Breath Tap-outs:** Sing “ha ha ha” on one breath to build diaphragm coordination.

These will build vocal agility and balance.
""")

elif exercise == "Stretching Vocal Range":
    st.subheader("📈 Stretch Your Vocal Range")
    st.markdown("""
- **Octave Slides:** Glide from low to high pitch on “ng” or “woo” — like a siren.  
- **Semi-Tone Steps:** Go up a half step each time you repeat a short phrase.  
- **Yawning Warmup:** Do light yawns while humming to gently open your throat.

Stretch slowly. Never push too hard past your comfortable range.
""")

st.info("💡 TIP: Use a keyboard app or tuner to track pitch and range as you practice.")




# --- FOOTER ---
st.divider()
st.caption("VICKY is part of the Nrth Eydn Ltd. creative development platform. Streamlit-only prototype.")
