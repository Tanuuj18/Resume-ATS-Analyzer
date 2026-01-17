from dotenv import load_dotenv
import streamlit as st
import os
import io
import base64
from PIL import Image
import pdf2image
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from Gemini
def get_gemini_response(input_text, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input_text, pdf_content[0], prompt])
    return response.text

# Function to convert uploaded PDF to base64 image content
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Convert PDF to image
        images = pdf2image.convert_from_bytes(
            uploaded_file.read(),
            poppler_path=r"C:\Users\Chirr\OneDrive\Desktop\ATS\poppler-24.08.0\Library\bin"  # Adjust if needed
        )
        first_page = images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        # Encode image to base64
        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode('utf-8')
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

##streamlit app
st.set_page_config(page_title='ATS resume Expert')
st.header("ATS Tracking System")
input_text=st.text_area("Job Description:",key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])


if uploaded_file is not None:
    st.write("PDF Uploaded successfully")


submit1 = st.button("Tell me about the Resume") 

#submit2 = st.button("How can i improve my skills")

submit3 = st.button("Percentage match")   

input_prompt1="""
You are an experienced HR with tech experience in the field of data sceience,full stack
web development,big data engineering,DEVOPS,data analyst,your task is to review 
the provided resume against the job description for these profiles.
 please share your professional evaluation on whether the candidates's profile aligns with the role.
Highlight the strenghts and weeknessesof the applicant in relation to the specified job role
"""
input_prompt3="""
You are an skilled ATS(Application tracking system) scanner with a deep understanding of data science,full stack
web development,big data engineering,DEVOPS,data analyst,and deep ATS functionality
your task is to evaluate the resume against the provided job description.give the percentage match if the resume matches the job description 
first the output should come as percentage and then keywords missing and last final thoughts.
""" 
if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The response is ")
        st.write(response)
    else:
        st.write("please upload the reusme")

    
elif submit3:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The response is ")
        st.write(response)
    else:
        st.write("please upload the reusme")

