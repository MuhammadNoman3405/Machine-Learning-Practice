import streamlit as st
import numpy as np
import pandas as pd

st.title("Hello Noman How are you?")

st.write("This is the simple text")

df=pd.DataFrame({
    'First Column':[1,2,3,4],
    'Second Column':[10,20,30,40]
})
df.set_index('First Column')
st.write("Here is the dataframe Data")
st.write(df)

# creating the line chart data
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)

st.write("Streamlit text input")
name=st.text_input("Enter your name")
if name:
    user_response=st.text_input(f'Hello {name} How are you?')
    if user_response:
        st.write(f"oky mean you are {user_response}")
# slider
age=st.slider('Select you age:',0,100,25)
st.write(f'you are {age} old')

# Select Box
options=['C++','Java','Python','Matplotlib','Seaborn']
choice=st.selectbox('Choose your favourite Langauge:',options)
st.write(f"You choose {choice}")


student_data = {
    "student_id": "23-CS-68",
    "personal_info": {
        "full_name": "Muhammad Noman",
        "age": 22,
        "languages": ["English", "Urdu", "Saraiki"],
        "education_background": "FSc Pre-Engineering"
    },
    "academic_info": {
        "institution": "University of Engineering and Technology (UET) Taxila",
        "degree_program": "Bachelor of Science in Computer Science (BS CS)",
        "session": "2023 - 2027",
        "graduation_year": 2027,
        "current_status": "Undergraduate Student",
        "final_year_project_focus": "Federated Learning"
    },
    "technical_skills": {
        "programming_languages": ["Python", "C++", "SQL", "x86 Assembly (NASM)", "JavaScript", "HTML", "CSS"],
        "machine_learning_and_data_science": [
            "Pandas", "NumPy", "Matplotlib", "Seaborn", 
            "Scikit-Learn", "TensorFlow", "Keras", "PySpark", "OpenCV"
        ],
        "generative_ai": ["LangChain", "Hugging Face APIs", "Vector Embeddings", "LLM Workflows"],
        "web_frameworks": ["Streamlit", "Flask"],
        "tools_and_platforms": [
            "VS Code", "Jupyter Notebook", "Google Colab", 
            "MySQL Workbench", "XAMPP", "Power BI", "Git", "GitHub", "Vercel"
        ]
    },
    "experience_and_certifications": {
        "internship": {
            "role": "Machine Learning Engineering Intern",
            "company": "FlyRank AI",
            "duration": "8 weeks"
        },
        "certifications": [
            "IBM Data Science Professional Certificate (Coursera)",
            "Data Science Bootcamp by Krish Naik (Udemy)"
        ]
    },
    "major_projects": [
        {
            "title": "Pneumonia Detection AI Web Application",
            "tech_stack": ["TensorFlow", "Keras", "OpenCV", "Streamlit"],
            "description": "Deep learning chest X-ray classification web app using CLAHE ROI preprocessing."
        },
        {
            "title": "Fake Job Detector",
            "tech_stack": ["Python", "Machine Learning", "Streamlit"],
            "description": "Classification model to detect fraudulent online job postings."
        },
        {
            "title": "Bank Management System",
            "tech_stack": ["C++", "OOP", "File Handling"],
            "description": "Console-based banking application automating account and transaction management."
        },
        {
            "title": "Bus Reservation System",
            "tech_stack": ["x86 Assembly (NASM)", "Linux System Calls"],
            "description": "Low-level seat booking and reservation routine."
        },
        {
            "title": "Superstore Sales & Profit Analysis",
            "tech_stack": ["Power BI", "Microsoft Excel"],
            "description": "Interactive business intelligence dashboard with custom calculated fields and pivot analysis."
        },
        {
            "title": "Compiler Token Analyzer",
            "tech_stack": ["C++"],
            "description": "Lexical analysis tool for custom `.wpp` source files."
        }
    ]
}

# df=pd.DataFrame(student_data)
# st.write(df)

# st.json(student_data)

df=pd.json_normalize(student_data)
st.dataframe(df)

student_data2 = {
    "Student ID": ["23-CS-68", "23-CS-69", "23-CS-70"],
    "Name": ["Muhammad Noman", "Ali Raza", "Hamza Ahmed"],
    "Degree": ["BS Computer Science", "BS Computer Science", "BS Software Engineering"],
    "Semester": [7, 7, 7],
    "Domain": ["Machine Learning", "Cybersecurity", "Cloud Computing"],
    "Status": ["Enrolled", "Enrolled", "Enrolled"]
}

st.title("Student Data 2")
df=pd.DataFrame(student_data2)
st.write(df)

# file upload code

file_upload=st.file_uploader('Upload your csv file:',type='csv')
if file_upload is not None:
    df=pd.read_csv(file_upload)
    st.write(df)
else:
    st.write('You upload the wrong file')