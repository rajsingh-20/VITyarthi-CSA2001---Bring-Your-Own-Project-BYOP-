import streamlit as st
import pickle

# Load model
with open("stress_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🎓 Student Exam Stress Detector")
st.write("Tell me how you're feeling about your exams...")

user_input = st.text_area("Enter your thoughts here:")

if st.button("Analyze"):
    if user_input.strip():
        prediction = model.predict([user_input])[0]
        
        if prediction == "stressed":
            st.error("😟 You seem STRESSED. Take a deep breath — you've got this!")
        elif prediction == "neutral":
            st.warning("😐 You seem NEUTRAL. Stay focused and keep going!")
        else:
            st.success("😊 You seem RELAXED. Great mindset — keep it up!")
    else:
        st.warning("Please enter some text first.")