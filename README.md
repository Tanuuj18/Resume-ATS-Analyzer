ATS Resume Analyzer using Gemini AI
This is a Streamlit-based web application that leverages Google's Gemini AI to evaluate resumes against job descriptions. It mimics the behavior of an Applicant Tracking System (ATS) and provides feedback on resume relevance, strengths, weaknesses, and percentage match for tech roles such as Data Science, Full Stack Development, DevOps, and more.

🔍 Features
📄 Upload resume in PDF format

🧠 Evaluate resume against job description using Gemini 1.5 Flash

✅ HR-style analysis of resume fit

📊 ATS-style percentage match and keyword suggestions

🚀 Tech Stack
Streamlit

Google Generative AI (Gemini)

pdf2image

python-dotenv

📁 Project Structure
bash
Copy
Edit
├── app.py               # Main Streamlit app
├── requirements.txt     # Python dependencies
├── .env                 # Contains Google API key (DO NOT share publicly)
🛠️ Setup Instructions
Clone the repository

bash
Copy
Edit
git clone https://github.com/Tanuuj18/Resume-ATS-Analyzer.git
cd ats-resume-analyzer
Create and activate a virtual environment (optional but recommended)

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Add your Google API key

Create a .env file (already present if cloned) and add:

Copy
Edit
GOOGLE_API_KEY

⚠️ Never share your API key in public repositories.

Install Poppler for PDF conversion

Windows: Download from Poppler for Windows and set the correct poppler_path in app.py

Linux/macOS: Use sudo apt install poppler-utils or brew install poppler

Run the app

bash
Copy
Edit
streamlit run app.py
📸 App Preview
(Optional: Add screenshots or GIFs showing the interface)

📌 Future Improvements
Multi-page resume analysis

Skill gap suggestions

Upload job description via PDF

Resume formatting tips

🧑‍💻 Author
Tanuuj vardhan reddy – Full Stack + GenAI Enthusiast
