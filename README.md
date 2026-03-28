# VITyarthi-CSA2001---Bring-Your-Own-Project-BYOP-
StressCheck - AI-Powered Student Stress Detector


■ About the Project

The Student Exam Stress Detector is a simple AI-powered web application that analyzes a student's
text input — such as how they are feeling about their exams — and classifies their emotional state as
Stressed, Neutral, or Relaxed. It is built using Python, scikit-learn for the ML model, and Streamlit for
the web interface.
This project was built as part of a Bring Your Own Project (BYOP) assignment for the Artificial
Intelligence and Machine Learning (AIML) course during B.Tech first year.


■ Features

1. Real-time stress detection from plain text input
2. Three-class classification: Stressed / Neutral / Relaxed
3. Interactive web UI — no coding needed to use the app
4. Fast prediction using a trained Naive Bayes classifier
5. Color-coded feedback with motivational messages
6. Lightweight and runs locally on any machine


■ Project Structure

exam-stress-detector/
1. app.py # Streamlit web application
2. model.py # Script to train and save the ML model
3. dataset.csv # Labeled training data
4. stress_model.pkl # Saved trained model (generated after training)
5. requirements.txt # Python dependencies
6. README.md # Project documentation


■ Prerequisites

Make sure you have the following installed on your computer:
• Python 3.10 or higher — https://www.python.org/downloads/
• pip (Python package manager — usually comes with Python)
• A terminal / command prompt
• Git (optional, for cloning the repo) — https://git-scm.com


■ Installation & Setup

Step 1 — Clone the repository
git clone https://github.com/rajsingh-20/exam-stress-detector.git
cd exam-stress-detector
Step 2 — Install required libraries
pip install -r requirements.txt
Step 3 — Train the ML model
Run this once to train the model and save it as stress_model.pkl:
python model.py

* Note: You must run model.py before running app.py. The app loads the saved model file.

Step 4 — Launch the web application
streamlit run app.py
After running this command, Streamlit will open the app automatically in your web browser at
http://localhost:8501


■ How to Use the App

1. Open the app in your browser (it opens automatically after running streamlit run app.py).
2. You will see a text area that says 'Enter your thoughts here'.
3. Type how you are feeling about your exams. For example: 'I am really worried about
tomorrow's paper'.
4. Click the Analyze button.
5. The app will instantly display your stress level with a color-coded message:
Result Color Message
Stressed Red You seem STRESSED. Take a deep breath — you've got this!
Neutral Yellow/Orange You seem NEUTRAL. Stay focused and keep going!
Relaxed Green You seem RELAXED. Great mindset — keep it up!


■ requirements.txt

scikit-learn
pandas
streamlit
nltk


■ How It Works (Technical Overview)

   Step        What Happens
1. Input       User types a sentence describing their exam feelings
2. Vectorize   TF-IDF converts the text into a numerical feature vector
3. Predict     Naive Bayes classifier predicts the label (stressed/neutral/relaxed)
4. Display     Streamlit shows a color-coded result with a supportive message


■ Sample Dataset Format (dataset.csv)

text,label
I am so scared about tomorrow's exam,stressed
I have no idea what to study,stressed
I feel okay about the test,neutral
I think I will manage,neutral
I studied well and feel prepared,relaxed
Everything is going to be fine,relaxed

* Tip: Add at least 20-25 examples per class for better accuracy. More varied data = smarter model.


■ Future Improvements

• Larger and more diverse dataset for better accuracy
• Use BERT or other transformer models for deeper context understanding
• Add a history tracker to monitor stress trends over time
• Support for regional Indian languages (Hindi, Tamil, etc.)
• Deploy online using Streamlit Cloud or Hugging Face Spaces


■ License
This project is licensed under the MIT License — free to use, modify, and distribute.


■ Author
Raj Singh — First Year B.Tech Student
GitHub: https://github.com/rajsingh-20

