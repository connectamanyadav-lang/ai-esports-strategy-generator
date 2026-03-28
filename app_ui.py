import streamlit as st
import openai

openai.api_key = "YOUR_API_KEY"

st.set_page_config(page_title="AI Esports Strategy Generator", layout="centered")

st.title("🎮 AI Esports Strategy Generator")

st.markdown("Generate pro-level strategies for your matches.")

game = st.text_input("Enter Game (e.g., Free Fire)")
map_name = st.text_input("Enter Map (e.g., Bermuda)")
playstyle = st.selectbox("Select Playstyle", ["Aggressive", "Passive", "Balanced"])

if st.button("Generate Strategy"):
    if game and map_name:
        with st.spinner("Generating strategy..."):
            prompt = f"""
            You are a professional esports coach.

            Game: {game}
            Map: {map_name}
            Playstyle: {playstyle}

            Give a competitive strategy including:
            - Early game plan
            - Mid game positioning
            - End game tactics
            """

            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            strategy = response['choices'][0]['message']['content']
            st.success("Strategy Generated!")
            st.write(strategy)
    else:
        st.warning("Please fill all fields.")
