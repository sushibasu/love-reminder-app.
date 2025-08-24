import streamlit as st
import random

# 💕 Romantic GIFs
gifs = [
    "https://media.giphy.com/media/l0MYEqEzwMWFCg8rm/giphy.gif",
    "https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif",
    "https://media.giphy.com/media/xT0xezQGU5xCDJuCPe/giphy.gif",
    "https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif"
]

# --- Streamlit App ---
st.set_page_config(page_title="💕 A Little Something for You", page_icon="💌")
st.title("💌 A Little Something for You")

# Cute heart banner
st.markdown("<h3 style='text-align: center;'>❤️🌸💖✨💞💌💕✨💖🌸❤️</h3>", unsafe_allow_html=True)

# Step 1: Ask his name
name = st.text_input("Hey love 💕 What's your name?")

if name:
    # Motivation + GIF
    st.image(random.choice(gifs), caption="For you 💖", use_container_width=True)
    st.success(f"Hi {name}! 🌸 Here’s a little motivation for you today:")
    st.info("✨ Keep shining, keep smiling, and never forget how amazing you are ✨")

    # Step 2: Next Button
    if st.button("Next ➡️"):
        # Personalized affirmations
        affirmations = [
            f"{name}, you make my world brighter 🌞",
            f"You inspire me every day, {name} 💫",
            f"You are my safe place 💕",
            f"I believe in you more than anything, {name} 🌹",
            f"You’re unstoppable, {name} 🚀"
        ]

        st.subheader("🌟 Affirmations just for you:")
        for aff in affirmations:
            st.write("✔️ " + aff)

        st.balloons()  # 🎈 surprise animation

        # Final sweet message
        st.success(f"No matter what, I’ll always believe in you, {name} 💖")

        # --- Fortune Calculator ---
        st.markdown("---")
        st.subheader("🔮 Fortune Calculator")
        st.write("Let’s see if you are truly lucky today...")

        if st.button("Calculate My Good Fortune ✨"):
            st.success(f"YES {name}! 🍀 You are the luckiest because you have me 💕")

        # Signature from you
        st.markdown("<h4 style='text-align: center; color: pink;'>💖 By Saisha 💖</h4>", unsafe_allow_html=True)

