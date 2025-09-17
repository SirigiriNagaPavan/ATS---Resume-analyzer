from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
from streamlit_extras import add_vertical_space as avs
import os
import PyPDF2

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(input):
    response = model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ''
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += str(page.extract_text())
    return text

input_prompt="""
As an experienced ATS (Applicant Tracking System), proficient in the technical domain 
encompassing Software Engineering, Data Science, Data Analysis, Big Data Engineering, 
Web Developer, Mobile App Developer, DevOps Engineer, Machine Learning Engineer, 
Cybersecurity Analyst, Cloud Solutions Architect, Database Administrator, Network Engineer, 
AI Engineer, Systems Analyst, Full Stack Developer, UI/UX Designer, IT Project Manager, 
and additional specialized areas, your objective is to meticulously assess resumes against 
provided job descriptions. In a fiercely competitive job market, your expertise is crucial 
in offering top-notch guidance for resume enhancement. Assign precise matching percentages 
based on the JD (Job Description) and meticulously identify any missing keywords with 
utmost accuracy.
resume:{text}
description:{jd}

I want the response in the following structure:
The first line indicates the percentage match with the job description (JD). 
The second line presents a list of missing keywords.
The third section provides a profile summary.

Mention the title for all the three sections.
While generating the response put some space to separate all the three sections.
"""

# Page configuration
st.set_page_config(page_title="Resume ATS Tracker", layout="wide")

avs.add_vertical_space(6)

# Introduction Section
def introduction():
    col1, col2 = st.columns([3, 2])

    with col1:
        st.title("CareerCraft")
        st.header("Navigate the Job Market with Confidence!")
        st.markdown("""
        <p style="text-align: justify;">
        Introducing CareerCraft, an ATS-Optimized Resume Analyzer - your ultimate solution for optimizing job applications and accelerating career growth. 
        Our innovative platform leverages advanced ATS technology to provide job seekers with valuable insights into their resumes' compatibility with job descriptions. 
        From resume optimization and skill enhancement to career progression guidance, CareerCraft empowers users to stand out in today's competitive job market.
        Streamline your job application process, enhance your skills, and navigate your career path with confidence. Join CareerCraft today and unlock new opportunities for professional success!
        </p>
        """, unsafe_allow_html=True)

    with col2:
        st.image('images/image1.webp', use_container_width=True)
    avs.add_vertical_space(10)

# Offerings Section
def offerings():
    col1, col2 = st.columns([3, 2])

    with col1:
        st.image('images/image2.webp', use_container_width=True)

    with col2:
        st.header("Wide Range of Offerings")
        st.write("""
        - **ATS-Optimized Resume Analysis**
        - **Resume Optimization**
        - **Skill Enhancement**
        - **Career Progression Guidance**
        - **Interview Preparation**
        - **Job Application Strategy**
        """)
    avs.add_vertical_space(10)

# Resume ATS Tracking Application Section
def resume_ats_tracking():
    col1, col2 = st.columns([3, 2]) 
    with col1: 
        st.markdown("<h1 style='text-align: center;'>Embark on Your Career Adventure</h1>", unsafe_allow_html=True) 
        jd=st.text_area("Paste the Job Description") 
        uploaded_file=st.file_uploader("Upload Your Resume", type="pdf", help="Please uplaod the pdf") 
        submit = st.button("Submit") 
        if submit: 
            if uploaded_file is not None: 
                text=input_pdf_text(uploaded_file) 
                response=get_gemini_response (input_prompt) 
                st.subheader(response) 

    with col2: 
        st.image("./images/image3.webp", use_container_width=True) 
    avs.add_vertical_space(10)

# FAQ Section
def faq():
    col1, col2 = st.columns([2, 3]) 
    with col2: 
        st.markdown("<h1 style='text-align: center;'>FAQ</h1>", unsafe_allow_html=True) 
        st.write("Question: How does CareerCraft analyze resumes and job descriptions?") 
        st.write("""Answer: CareerCraft uses advanced algorithms to analyze resumes and job descriptions, identifying key keywords and assessing compatibility between the two.""") 
        st.write("")
        st.write("Question: Can CareerCraft suggest improvements for my resume?") 
        st.write("""Answer: Yes, CareerCraft provides personalized recommendations to optimize your resume for specific job openings, including suggestions for missing keywords and alignment with desired job roles.""") 
        st.write("") 
        st.write("Question: Is CareerCraft suitable for both entry-level and experienced professionals?") 
        st.write("""Answer: Absolutely! CareerCraft caters to job seekers at all career stages, offering tailored insights and guidance to enhance their resumes and advance their careers.""") 
    
    with col1: 
        st.image("./images/image4.webp", use_container_width=True)

# Render the sections
introduction()
offerings()
resume_ats_tracking()
faq()
