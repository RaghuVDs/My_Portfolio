import streamlit as st
import pandas as pd

# --- Data and Assets (Replace with your actual data) ---
# Example Project Data
df_projects = pd.DataFrame({
    'project_name': ['Customer Churn Prediction', 'Sales Forecasting', 'Sentiment Analysis of Product Reviews'],
    'description': [
        'Developed a machine learning model to predict customer churn for a telecommunications company.',
        'Built a time series model to forecast future sales.',
        'Performed sentiment analysis on customer reviews.'
    ],
    'technologies': ['Python, scikit-learn', 'Python, Statsmodels', 'Python, NLTK'],
    'year': [2023, 2022, 2023],
    'project_page_link': ['project_1', 'project_2', 'project_3'],
    'case_study_link': ['case_study_1', 'case_study_2', 'case_study_3']
})

# Simplified other data for example
df_skills = pd.DataFrame({
    'skill_category': ['Programming Languages', 'Machine Learning'],
    'skills': [
        ['Python', 'SQL'],
        ['Supervised Learning', 'Deep Learning']
    ]
})

# --- Page Configuration ---
st.set_page_config(
    page_title="Data Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Session State Management ---
if 'page' not in st.session_state:
    st.session_state.page = 'Home'  # Match case with navigation options

# --- Sidebar Navigation ---
with st.sidebar:
    st.image("raghu.jpg", width=250)  # Ensure this image exists
    st.title("Navigation")
    
    # Define navigation options with consistent casing
    nav_options = ["Home", "Portfolio", "About Me", "Skills", "Contact"]
    page = st.radio("Go to", nav_options)
    
    # Update session state if navigation changes
    if page != st.session_state.page:
        st.session_state.page = page
        st.rerun()
    
    # Resume download
    with open("Resume_Raghuveera_N.pdf", "rb") as f:
        st.download_button(
            "📄 Download Resume",
            f.read(),
            "Your_Resume.pdf",
            "application/pdf"
        )

# --- Page Content ---

# Home Page
if st.session_state.page == 'Home':
    st.title("Welcome to My Data Portfolio")
    st.write("### John Doe - Data Scientist")
    
    st.write("""
    I'm a data professional with expertise in machine learning and data analysis.
    This portfolio showcases my projects and skills.
    """)
    
    # Use column layout for better organization
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("raghu.jpg", use_column_width=True)
    with col2:
        st.write("""
        **Key Expertise:**
        - Machine Learning
        - Data Visualization
        - Predictive Modeling
        """)
    
    if st.button("View My Work →", type="primary"):
        st.session_state.page = "Portfolio"
        st.rerun()

# Portfolio Page
elif st.session_state.page == 'Portfolio':
    st.title("Project Portfolio")
    
    # Project filtering
    tech_options = list(set(df_projects['technologies'].str.split(', ').sum()))
    selected_tech = st.multiselect("Filter by technologies:", tech_options)
    
    # Filter projects
    filtered_projects = df_projects
    if selected_tech:
        filtered_projects = df_projects[
            df_projects['technologies'].apply(
                lambda techs: any(t in techs for t in selected_tech)
            )
        ]
    
    # Display projects
    for _, project in filtered_projects.iterrows():
        with st.expander(project['project_name'], expanded=False):
            st.write(f"**Description:** {project['description']}")
            st.write(f"**Technologies:** {project['technologies']}")
            st.write(f"**Year:** {project['year']}")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"Details: {project['project_name']}"):
                    st.session_state.page = project['project_page_link']
                    st.rerun()
            with col2:
                if st.button(f"Case Study: {project['project_name']}"):
                    st.session_state.page = project['case_study_link']
                    st.rerun()

# Project Details Pages
elif st.session_state.page in df_projects['project_page_link'].values:
    project = df_projects[df_projects['project_page_link'] == st.session_state.page].iloc[0]
    
    st.title(project['project_name'])
    st.image(f"projects/{project['project_page_link']}.jpg", use_column_width=True)
    
    st.header("Project Overview")
    st.write(project['description'])
    
    st.write("**Technologies Used:**")
    st.write(project['technologies'])
    
    if st.button("← Back to Portfolio"):
        st.session_state.page = "Portfolio"
        st.rerun()

# About Me Page
elif st.session_state.page == 'About Me':
    st.title("About Me")
    
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("raghu.jpg", width=200)
    with col2:
        st.write("""
        ## John Doe
        **Data Scientist** with 5+ years of experience...
        """)
    
    st.write("""
    ### Professional Journey
    - MSc in Data Science
    - Certified Machine Learning Specialist
    - Experience in multiple industries
    """)

# Skills Page
elif st.session_state.page == 'Skills':
    st.title("Technical Skills")
    
    for _, category in df_skills.iterrows():
        st.subheader(category['skill_category'])
        cols = st.columns(4)
        for i, skill in enumerate(category['skills']):
            cols[i % 4].markdown(f"- {skill}")

# Contact Page
elif st.session_state.page == 'Contact':
    st.title("Get in Touch")
    
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        
        if st.form_submit_button("Send Message"):
            # Add your email handling logic here
            st.success("Message sent successfully!")

    st.write("""
    **Alternative Contact Methods:**
    - 📧 email@example.com
    - 🔗 [LinkedIn Profile](https://linkedin.com)
    - 📍 Location: City, Country
    """)

# Handle unknown pages
else:
    st.error("Page not found")
    if st.button("Return to Home"):
        st.session_state.page = "Home"
        st.rerun()