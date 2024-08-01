
# 📋 Resume to JSON Parser

This project is a Streamlit application that converts a resume in PDF format to a JSON object. It uses the Google Gemini language model for natural language processing and PyPDF2 for reading PDF files.

## AIM
System that takes your Resume as input and parse the content in JSON format.

![image](https://github.com/user-attachments/assets/e398d33b-1e9a-4aaf-9ac8-c4a45acdbb7d)

## Features

- 📄 Upload a resume in PDF format.
- 🔍 Extract and parse the resume content into a structured JSON format.
- 💾 Download the parsed JSON file.

## Technologies Used

- [Streamlit](https://streamlit.io/) for the user interface.
- [Google Gemini](https://ai.google/) as the language model for parsing the resume.
- [PyPDF2](https://pypi.org/project/PyPDF2/) for reading PDF files.

## Requirements

- Python 3.7 or higher
- Google API key for accessing the Google Gemini language model

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/resume-to-json-parser.git
    cd resume-to-json-parser
    ```

2. **Create and activate a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your Google API key:**

    - Create a file named `secrets.toml` in the `.streamlit` directory (create the directory if it doesn't exist).
    - Add your Google API key to `secrets.toml`:

    ```toml
    [general]
    GOOGLE_API_KEY = "your_google_api_key"
    ```

## Usage

1. **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

2. **Upload a resume in PDF format.**

3. **Download the parsed JSON file.**

---
[Click here](https://jsonparsor.streamlit.app/) to use the web application.


