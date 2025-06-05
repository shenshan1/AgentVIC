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



import streamlit as st
from audio_recorder_streamlit import audio_recorder
import librosa
import soundfile as sf
import numpy as np
import io

st.title("Audio Recorder with Streamlit")

# Audio recorder component
audio_bytes = audio_recorder(
    text="Click to record",
    recording_color="#e8b62c",
    neutral_color="#6aa36f",
    icon_name="microphone",
    icon_size="2x",
)

if audio_bytes:
    st.audio(audio_bytes, format="audio/wav")
    
    # Convert bytes to numpy array for processing
    try:
        # Write bytes to a temporary file-like object
        audio_buffer = io.BytesIO(audio_bytes)
        
        # Load audio data using soundfile
        audio_data, sample_rate = sf.read(audio_buffer)
        
        st.write(f"Audio sample rate: {sample_rate} Hz")
        st.write(f"Audio duration: {len(audio_data) / sample_rate:.2f} seconds")
        st.write(f"Audio shape: {audio_data.shape}")
        
        # Use librosa for audio analysis
        if len(audio_data.shape) > 1:
            # Convert stereo to mono if needed
            audio_data = librosa.to_mono(audio_data.T)
        
        # Extract some audio features
        tempo, beats = librosa.beat.beat_track(y=audio_data, sr=sample_rate)
        mfccs = librosa.feature.mfcc(y=audio_data, sr=sample_rate, n_mfcc=13)
        
        st.write(f"Estimated tempo: {tempo:.2f} BPM")
        st.write(f"Number of beats detected: {len(beats)}")
        st.write(f"MFCC features shape: {mfccs.shape}")
        
        # Display waveform
        st.subheader("Audio Waveform")
        st.line_chart(audio_data)
        
    except Exception as e:
        st.error(f"Error processing audio: {str(e)}")

st.write("Record audio using the button above to see analysis results!")


# --- FOOTER ---
st.divider()
st.caption("VICKY is part of the Nrth Eydn Ltd. creative development platform. Streamlit-only prototype.")
