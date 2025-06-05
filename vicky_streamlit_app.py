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

