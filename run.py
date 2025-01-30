import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# --- Custom CSS ---
def inject_custom_css():
    st.markdown("""
    <style>
        /* Base styling */
        .stApp {
            background:rgb(106, 166, 251);
        }
        
        /* Project cards */
        .project-card {
            background: white;
            border-radius: 10px;
            padding: 20px;
            margin: 10px 0;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s;
        }
        .project-card:hover {
            transform: translateY(-5px);
        }
        
        /* Skill bars */
        .skill-bar {
            background:rgba(247, 121, 115, 0);
            border-radius: 20px;
            margin: 10px 0;
        }
        .skill-progress {
            background: #4CAF50;
            height: 20px;
            border-radius: 20px;
            text-align: center;
            color: white;
        }
        
        /* Custom header */
        .hero-header {
            background: linear-gradient(135deg, #6366f1, #8b5cf6);
            padding: 4rem 2rem;
            border-radius: 15px;
            color: white;
            margin-bottom: 2rem;
        }
    </style>
    """, unsafe_allow_html=True)

# --- Data and Assets ---
# (Keep your existing data, but add more details)
df_projects = pd.DataFrame({
    'project_name': ['Customer Churn Prediction', 'Sales Forecasting', 'Sentiment Analysis'],
    'description': ['...', '...', '...'],
    'technologies': ['Python, scikit-learn, XGBoost', 'Python, Prophet, ARIMA', 'Python, BERT, Transformers'],
    'year': [2023, 2022, 2023],
    'complexity': ['Advanced', 'Intermediate', 'Advanced'],
    'impact': ['Reduced churn by 15%', 'Improved forecast accuracy by 20%', 'Automated review analysis']
})

# --- Helper Components ---
def project_card(project):
    card = f"""
    <div class="project-card">
        <h3>{project['project_name']}</h3>
        <p>{project['description']}</p>
        <div style="margin: 10px 0;">
            {" ".join([f'<span class="badge" style="background: #4CAF50; color: white; padding: 5px 10px; border-radius: 20px; margin: 2px;">{tech}</span>' for tech in project['technologies'].split(', ')])}
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <span style="color: #666;">📅 {project['year']}</span>
                <span style="margin-left: 15px; color: #666;">🏆 {project['complexity']}</span>
            </div>
            <button onclick="alert('Coming soon!')" style="background: #6366f1; color: white; border: none; padding: 8px 20px; border-radius: 5px; cursor: pointer;">
                View Case Study →
            </button>
        </div>
    </div>
    """
    st.markdown(card, unsafe_allow_html=True)

def skill_bar(name, level):
    st.markdown(f"""
    <div class="skill-bar">
        <div class="skill-progress" style="width: {level}%;">
            {name} - {level}%
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- Page Config ---
st.set_page_config(
    page_title="Data Portfolio | John Doe",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Session State ---
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

# --- Sidebar ---
with st.sidebar:
    st.image("raghu.jpg", width=250)
    st.title("John Doe")
    st.caption("Data Scientist | ML Engineer")
    
    nav = st.radio("Navigation", ["Home", "Projects", "Skills", "About", "Contact"])
    if nav != st.session_state.page:
        st.session_state.page = nav
        st.rerun()
    
    # Social Links
    st.markdown("""
    <div style="margin-top: 50px;">
        <a href="https://linkedin.com" target="_blank" style="margin-right: 15px; color: #0A66C2;">LinkedIn</a>
        <a href="https://github.com" target="_blank" style="margin-right: 15px; color: #333;">GitHub</a>
        <a href="https://medium.com" target="_blank" style="color: #000;">Blog</a>
    </div>
    """, unsafe_allow_html=True)

# --- Main Content ---
inject_custom_css()

if st.session_state.page == 'Home':
    # Hero Section
    st.markdown("""
    <div class="hero-header">
        <h1 style="color: white; margin: 0;">Turning Data Into Decisions</h1>
        <p style="font-size: 1.2rem;">Data Scientist specializing in Machine Learning & Business Intelligence</p>
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns([1, 2])
    with cols[0]:
        st.image("raghu.jpg", use_column_width=True)
    with cols[1]:
        st.subheader("About Me")
        st.write("""
        Experienced data professional with 5+ years in delivering impactful ML solutions.
        Passionate about solving complex business problems through data-driven approaches.
        """)
        st.metric("Years Experience", "5+", "+3 certifications")
        st.metric("Projects Completed", "27", "8 active")
        
    st.subheader("Featured Projects")
    for _, proj in df_projects.iterrows():
        project_card(proj)

elif st.session_state.page == 'Projects':
    st.title("Project Portfolio")
    
    # Filters
    col1, col2 = st.columns(2)
    with col1:
        tech_filter = st.multiselect("Filter by Technology", 
                                   options=['Python', 'scikit-learn', 'Prophet', 'BERT'])
    with col2:
        search_query = st.text_input("Search Projects")
    
    # Filtered projects
    filtered = df_projects.copy()
    if tech_filter:
        filtered = filtered[filtered['technologies'].apply(lambda x: any(t in x for t in tech_filter))]
    if search_query:
        filtered = filtered[filtered['project_name'].str.contains(search_query, case=False)]
    
    # Display projects
    for _, proj in filtered.iterrows():
        project_card(proj)

elif st.session_state.page == 'Skills':
    st.title("Technical Expertise")
    
    st.subheader("Machine Learning")
    skill_bar("Python", 90)
    skill_bar("TensorFlow", 80)
    skill_bar("Natural Language Processing", 75)
    
    st.subheader("Data Engineering")
    skill_bar("SQL", 85)
    skill_bar("Spark", 70)
    skill_bar("Airflow", 65)
    
    st.subheader("Visualization")
    skill_bar("Tableau", 88)
    skill_bar("Power BI", 75)
    skill_bar("Matplotlib", 82)

elif st.session_state.page == 'About':
    st.title("About Me")
    
    cols = st.columns([1, 2])
    with cols[0]:
        st.image("raghu.jpg", use_column_width=True)
    with cols[1]:
        st.subheader("Professional Journey")
        st.write("""
        - 🎓 MSc in Data Science, Stanford University (2018)
        - 💼 Senior Data Scientist @ TechCorp (2020-Present)
        - 🏆 AWS Machine Learning Certified
        - 📈 Built predictive models serving 1M+ users
        """)
    
    st.subheader("Certifications")
    cert_cols = st.columns(3)
    with cert_cols[0]:
        st.image("raghu.jpg", caption="AWS ML Specialty")
    with cert_cols[1]:
        st.image("raghu.jpg", caption="Google Cloud Professional")
    with cert_cols[2]:
        st.image("raghu.jpg", caption="Databricks Engineer")

elif st.session_state.page == 'Contact':
    st.title("Get in Touch")
    
    with st.form("contact_form"):
        cols = st.columns(2)
        with cols[0]:
            name = st.text_input("Name", placeholder="John Smith")
            email = st.text_input("Email", placeholder="john@example.com")
        with cols[1]:
            message = st.text_area("Message", height=150)
        
        if st.form_submit_button("Send Message", type="primary"):
            st.success("🚀 Message sent successfully!")
            st.balloons()
    
    st.divider()
    st.subheader("Direct Contact")
    st.write("📧 john.doe@dataportfolio.com")
    st.write("📱 +1 (555) 123-4567")
    st.write("📍 San Francisco, CA")
    
    # Embed Map
    components.html("""
    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d100940.17073741354!2d-122.50764081392592!3d37.75767927538934!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80859a6d00690021%3A0x4a501367f076adff!2sSan%20Francisco%2C%20CA!5e0!3m2!1sen!2sus!4v1718146464298!5m2!1sen!2sus" 
        width="100%" height="300" style="border:0; border-radius: 10px;" allowfullscreen="" loading="lazy"></iframe>
    """)