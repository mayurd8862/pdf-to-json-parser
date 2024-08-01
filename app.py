

# import streamlit as st
# from langchain_google_genai import ChatGoogleGenerativeAI
# import os
# import json
# from io import StringIO
# import getpass

# from streamlit_pdf_viewer import pdf_viewer


# # container_pdf, container_chat = st.columns([50, 50])


# # with container_pdf:
# #     pdf_file = st.file_uploader("Upload PDF file", type=('pdf'))

# #     if pdf_file:
# #         binary_data = pdf_file.getvalue()
# #         pdf_viewer(input=binary_data,
# #                    width=700)


# from langchain_community.document_loaders import PyPDFLoader



# GOOGLE_API_KEY = st.secrets.GOOGLE_API_KEY
# llm = ChatGoogleGenerativeAI(model="gemini-pro",google_api_key=GOOGLE_API_KEY)

# # Streamlit UI for uploading resume
# st.title("Resume to JSON Parser")
# uploaded_file = st.file_uploader("Upload your resume", type=["pdf"])

# if uploaded_file is not None:

#     loader = PyPDFLoader(uploaded_file)
#     pages = loader.load_and_split()
    
#     # Define the ChatGPT prompt
#     prompt = f"""
#     You are an AI model that parses resumes. Given the content of a resume, extract and format the information into a JSON object with the following structure:
#     - Name
#     - Contact Information
#       - Email
#       - Phone
#       - LinkedIn
#       - GitHub
#     - Education
#       - Degree
#       - University
#       - Graduation Year
#     - Work Experience
#       - Job Title
#       - Company
#       - Duration
#       - Responsibilities
#     - Projects
#       - Project Name
#       - Description
#       - Technologies
#     - Skills
#     - Certifications
#     - Awards

#     Here is the resume content:
#     {pages}

#     Provide the JSON output.
#     """
    
#     # Invoke the language model
#     result = llm.invoke(prompt)
    
#     # Display the JSON output
#     st.subheader("Parsed Resume JSON")
#     st.json(json.loads(result.content))
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import json
from PyPDF2 import PdfReader
import getpass

# Set up Google API Key
GOOGLE_API_KEY = st.secrets.GOOGLE_API_KEY
llm = ChatGoogleGenerativeAI(model="gemini-pro",google_api_key=GOOGLE_API_KEY)

# llm = ChatGoogleGenerativeAI(model="gemini-pro",google_api_key="Your API key")

# Streamlit UI for uploading resume
st.title("📋 Resume to JSON Parser")
st.subheader("",divider = 'rainbow')
uploaded_file = st.file_uploader("Upload your resume", type=["pdf"])

if uploaded_file is not None:
    # Read the file content using PyPDF2
    pdf_reader = PdfReader(uploaded_file)
    resume_content = ""
    for page in pdf_reader.pages:
        resume_content += page.extract_text()
    
    # Define the ChatGPT prompt
    prompt = f"""
    You are an AI model that parses resumes. Given the content of a resume, extract and format the information into a JSON object with the following structure:
    - Name
    - Contact Information
      - Email
      - Phone
      - LinkedIn
      - GitHub
    - Education
      - Degree
      - University
      - Graduation Year
    - Work Experience
      - Job Title
      - Company
      - Duration
      - Responsibilities
    - Projects
      - Project Name
      - Description
      - Technologies
    - Skills
    - Certifications
    - Awards

    Here is the resume content:
    {resume_content}

    Provide the JSON output.
    """
    
    # Invoke the language model
    result = llm.invoke(prompt)
    

    with open("parsed_resume.json", "w") as json_file:
        json.dump(result.content, json_file)

            # Provide a download link for the JSON file
    with open("parsed_resume.json", "r") as json_file:
        st.download_button(label="💾 Download JSON",
                        data=json_file,
                        file_name="parsed_resume.json",
                        mime="application/json")
        
    st.subheader("🚀 Parsed Resume JSON")
    st.write(result.content)