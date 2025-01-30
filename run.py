import streamlit as st
import pandas as pd
import plotly.express as px

# --- Data and Assets (Replace with your actual data) ---
# Example Project Data
df_projects = pd.DataFrame({
    'project_name': ['Customer Churn Prediction', 'Sales Forecasting', 'Sentiment Analysis of Product Reviews', 'Image Classification for E-commerce', 'Website Click-Through Rate Prediction', 'Fraud Detection in Financial Transactions'],
    'description': [
        'Developed a machine learning model to predict customer churn for a telecommunications company, achieving 90% accuracy.',
        'Built a time series model to forecast future sales, improving forecast accuracy by 25% compared to the previous model.',
        'Performed sentiment analysis on customer reviews to identify key areas for product improvement, leading to a 15% increase in positive sentiment.',
        'Created an image classification model to automatically categorize products for an e-commerce platform, reducing manual effort by 80%.',
        'Built a predictive model to estimate website click-through rates, optimizing ad campaigns and increasing conversion by 20%.',
        'Developed a real-time fraud detection system for a financial institution, reducing fraudulent transactions by 40%.'
    ],
    'technologies': ['Python, scikit-learn, Pandas, Machine Learning', 'Python, Statsmodels, Time Series Analysis', 'Python, NLTK, Sentiment Analysis', 'Python, TensorFlow, Deep Learning, Computer Vision', 'Python, scikit-learn, Feature Engineering, Machine Learning', 'Python, PySpark, Machine Learning, Anomaly Detection'],
    'year': [2023, 2022, 2023, 2022, 2023, 2022],
    'project_page_link': ['project_1', 'project_2', 'project_3', 'project_4', 'project_5', 'project_6'],
    'case_study_link': ['case_study_1', 'case_study_2', 'case_study_3', 'case_study_4', 'case_study_5', 'case_study_6']
})

# Example Skills Data
df_skills = pd.DataFrame({
    'skill_category': ['Programming Languages', 'Machine Learning', 'Data Visualization', 'Databases', 'Cloud Computing', 'Big Data Technologies'],
    'skills': [
        ['Python', 'R', 'SQL', 'Java', 'JavaScript'],
        ['Supervised Learning', 'Unsupervised Learning', 'Deep Learning', 'Natural Language Processing', 'Computer Vision'],
        ['Tableau', 'Power BI', 'Seaborn', 'Matplotlib', 'Plotly'],
        ['MySQL', 'PostgreSQL', 'MongoDB', 'SQLite'],
        ['AWS (S3, EC2, Lambda)', 'Azure', 'Google Cloud Platform'],
        ['Hadoop', 'Spark', 'Kafka']
    ]
})

# Example Testimonials Data
df_testimonials = pd.DataFrame({
    'client': ['John Doe', 'Jane Smith', 'Peter Jones', 'Acme Corporation'],
    'role': ['CEO, Company X', 'Marketing Manager, Company Y', 'Data Scientist, Company Z', 'Project Manager'],
    'testimonial': [
        'Working with [Your Name] was a game-changer for our business. Their insights helped us increase sales by 20%.',
        '[Your Name] is a highly skilled data analyst who consistently delivers high-quality work.',
        'I was impressed by [Your Name]\'s ability to explain complex data concepts in a clear and concise way.',
        '[Your Name] helped us implement a critical data analytics project on time and on budget. Highly recommend.'
    ]
})

profile_image = "My_portfolio/raghu.jpg"
resume_file = "My_portfolio/Resume_Raghuveera_N.pdf"

# --- Helper Functions ---
def load_project_page(project_name):
    """Loads the content for an individual project page."""
    project_details = df_projects[df_projects['project_name'] == project_name].iloc[0]

    st.title(project_details['project_name'])

    # High-quality visuals (replace with your actual images/videos)
    st.image(f"{project_name.lower().replace(' ', '_')}.jpg", use_column_width=True)

    st.header("Project Overview")
    st.write(project_details['description'])

    st.header("Problem/Challenge")
    st.write("Describe the specific problem you were trying to solve with this project.")  # Customize this

    st.header("Your Role and Contributions")
    st.write("Explain your specific role and what you did in this project.")  # Customize this

    st.header("Process/Methodology")
    st.write("Detail the steps you took, the methods you used, and the rationale behind your choices.")  # Customize this

    st.header("Results/Outcome")
    st.write("Showcase the positive impact of your project. Use metrics and data to quantify the results.")  # Customize this

    st.header("Technologies/Tools Used")
    st.write(project_details['technologies'])

    # Optional: Testimonial related to the project
    # if project_details['testimonial_id']:
    #     st.header("Testimonial")
    #     # ... (fetch and display testimonial)

    # Call to Action
    col1, col2, col3 = st.columns(3)
    with col2:
        if st.button("Contact Me", key=f"contact_from_{project_name}"):
            st.session_state.page = "contact"
            st.experimental_rerun()

def load_case_study_page(project_name):
    project_details = df_projects[df_projects['project_name'] == project_name].iloc[0]

    st.title(f"Case Study: {project_details['project_name']}")

    st.write(f"This is a more detailed case study for the {project_name} project.")
    st.header("Project Overview")
    st.write(project_details['description'])

    st.header("Research and Process")
    st.write("Here, you will go into depth about the research phase, user interviews, data collection methods, analysis techniques, iterations, and the overall process you followed.")
    
    st.header("Technologies/Tools Used")
    st.write(project_details['technologies'])

    # Call to Action
    col1, col2, col3 = st.columns(3)
    with col2:
        if st.button("Contact Me", key=f"contact_from_case_study_{project_name}"):
            st.session_state.page = "contact"
            st.experimental_rerun()

# --- Page Navigation ---
# Use session state to manage page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'home'

#--- Sidebar Navigation (Improved) ---
with st.sidebar:
    st.image(profile_image, width=250)
    st.sidebar.title("Navigation")
    page = st.radio("Go to", [
        "Home", "Portfolio", "About Me", "Skills", "Testimonials", "Blog", "Contact"
    ])

    if page != st.session_state.page:
        st.session_state.page = page
        st.experimental_rerun()

    # --- Add Download Resume Button in Sidebar ---
    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.sidebar.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name="Your_Name_Resume.pdf",
        mime="application/octet-stream",
    )

# --- Page Content ---

# --- Homepage ---
if st.session_state.page == 'home':
    st.title("Welcome to My Data Portfolio")
    st.write("### [Your Name] - Data Scientist | Data Analyst | Machine Learning Engineer")

    # Introduction
    st.write("""
    I am a passionate data professional with a strong analytical background and a proven ability to extract valuable insights from complex datasets. 
    I excel at developing and implementing machine learning models to solve business problems and improve decision-making. 
    I am always eager to learn new technologies and techniques to stay at the forefront of the data field.
    """)

    # Visual (replace with a relevant image or video)
    st.image("home_page_visual.jpg", use_column_width=True)

    # Call to Action
    col1, col2, col3 = st.columns(3)
    with col2:
        if st.button("View Portfolio"):
            st.session_state.page = "portfolio"
            st.experimental_rerun()

# --- Portfolio Page ---
elif st.session_state.page == 'portfolio':
    st.title("Portfolio")
    st.write("### Explore my data-driven projects.")

    # Filter by Technologies (Optional)
    selected_technologies = st.multiselect(
        "Filter Projects by Technologies:",
        options=list(set(df_projects['technologies'].str.split(', ').sum()))
    )

    filtered_projects = df_projects
    if selected_technologies:
        filtered_projects = df_projects[
            df_projects['technologies'].apply(lambda techs: any(tech in techs for tech in selected_technologies))
        ]

    # Display Projects
    for index, row in filtered_projects.iterrows():
        col1, col2 = st.columns([1, 3])  # Adjust column ratio for better layout

        with col1:
            # Thumbnail (replace with actual project images)
            st.image(f"{row['project_name'].lower().replace(' ', '_')}.jpg", width=150)

        with col2:
            st.subheader(row['project_name'])
            st.write(row['description'])
            with st.expander("Learn More", expanded=False):
                if st.button(f"View Project Details", key=f"project_{index}"):
                    st.session_state.page = row['project_page_link']
                    st.experimental_rerun()
                if st.button(f"View Case Study", key=f"case_study_{index}"):
                    st.session_state.page = row['case_study_link']
                    st.experimental_rerun()
                

# --- Individual Project Pages ---
elif st.session_state.page in df_projects['project_page_link'].tolist():
    load_project_page(df_projects[df_projects['project_page_link'] == st.session_state.page]['project_name'].iloc[0])

# --- Case Study ---
elif st.session_state.page in df_projects['case_study_link'].tolist():
    load_case_study_page(df_projects[df_projects['case_study_link'] == st.session_state.page]['project_name'].iloc[0])

# --- About Me Page ---
elif st.session_state.page == 'about':
    st.title("About Me")

    # Professional Photo
    st.image(profile_image, width=250)

    st.header("My Story")
    st.write("""
    Write your story here. Talk about your background, experience, how you got into data science, and what motivates you.
    """)

    st.header("My Expertise")
    st.write("""
    Highlight your key skills and areas of expertise. What makes you unique as a data professional?
    """)

    # Optional: Values/Mission
    st.header("My Values")
    st.write("""
    (Optional) Share your values and your mission. What do you stand for? What impact do you want to make?
    """)

# --- Skills Page ---
elif st.session_state.page == 'skills':
    st.title("Skills and Services")

    # Display Skills using st.chips (or custom HTML for chips)
    for index, row in df_skills.iterrows():
        st.subheader(row['skill_category'])
        for skill in row['skills']:
            st.markdown(f"<span style='display: inline-block; margin: 5px; padding: 5px 10px; background-color: #e0f2f7; border-radius: 15px;'>{skill}</span>", unsafe_allow_html=True)
    
    st.header("Services")
    st.write("""
    Describe the services you offer to clients or employers. Be specific about what you can do and how you can help them.
    """)

# --- Testimonials Page ---
elif st.session_state.page == 'testimonials':
    st.title("Testimonials")
    st.write("### What others say about my work")

    for index, row in df_testimonials.iterrows():
        st.subheader(f"{row['client']} - {row['role']}")
        st.write(f"> {row['testimonial']}")
        st.markdown("---")  # Add a separator between testimonials

    # Optional: Client Logos
    # st.header("Clients I've Worked With")
    # ... (display client logos)

# --- Blog Page ---
elif st.session_state.page == 'blog':
    st.title("Blog/Articles")
    st.write("### Insights, tutorials, and more")

    # Example Blog Posts (replace with your actual blog data)
    blog_posts = [
        {'title': 'Data Cleaning Tips for Beginners', 'date': '2023-10-26', 'content': '...'},
        {'title': 'Introduction to Time Series Analysis', 'date': '2023-10-15', 'content': '...'},
        {'title': 'My Favorite Data Visualization Tools', 'date': '2023-09-28', 'content': '...'}
    ]

    for post in blog_posts:
        with st.expander(f"**{post['title']}** ({post['date']})", expanded=False):
            st.write(post['content'])

# --- Contact Page ---
elif st.session_state.page == 'contact':
    st.title("Contact Me")
    st.write("### Let's connect! I'm always open to discussing new opportunities.")

    # Contact Form
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Send Message")

        if submit_button:
            # Handle form submission (e.g., send email, store in database)
            st.success("Thank you for your message! I'll get back to you soon.")

    # Other Contact Information
    st.write("📧 **Email:** your.email@example.com")
    st.write("🔗 **LinkedIn:** [Your LinkedIn Profile](https://www.linkedin.com/in/yourprofile)")
    # ... (add other social media links if applicable)