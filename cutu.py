import streamlit as st
import random

# ✨ Affirmations
affirmations = [
    "You are strong 💪",
    "You are loved 💕",
    "You make people smile 🌞",
    "You are doing great 🌸",
    "You are unstoppable 🚀"
]

# 💌 Sweet messages
sweet_messages = [
    "No matter what, I’ll always believe in you 💖",
    "Forever proud of you 🌹",
    "You’re my favorite person in the whole world 🌍💞",
    "With you, every day feels magical ✨"
]

# Romantic GIFs or Images
gifs = [
    "https://media.giphy.com/media/l0MYEqEzwMWFCg8rm/giphy.gif",
    "https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif",
    "https://media.giphy.com/media/xT0xezQGU5xCDJuCPe/giphy.gif",
    "https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif"
]

# --- Streamlit App ---
st.set_page_config(page_title="💕 Personalized App", page_icon="💌")
st.title("💌 A Little Something for You")

# Cute heart banner
st.markdown("<h3 style='text-align: center;'>❤️🌸💖✨💞💌💕✨💖🌸❤️</h3>", unsafe_allow_html=True)

# Step 1: Name
name = st.text_input("Hey love 💕 What's your name?")

if name:
    st.image(random.choice(gifs), caption="For you 💖", use_container_width=True)
    st.success(f"Hi {name}! 🌸 Here’s a little motivation for you today:")
    st.info("✨ Keep shining, keep smiling, and never forget how amazing you are ✨")

    # Step 2: Next Button
    if st.button("Next ➡️"):
        st.subheader("🌟 Affirmations just for you:")
        for aff in affirmations:
            st.write("✔️ " + aff)

        st.balloons()  # 🎈 surprise animation
        st.success(random.choice(sweet_messages))

        # Signature from you
        st.markdown("<h4 style='text-align: center; color: pink;'>💖 By Saisha 💖</h4>", unsafe_allow_html=True)
