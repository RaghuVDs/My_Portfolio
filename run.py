import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# --- Custom CSS ---
def inject_custom_css():
    theme = st.session_state.get('theme', 'dark')
    
    if theme == 'dark':
        css_vars = {
            '--background': '#121212',
            '--text-color': '#ffffff',
            '--card-bg': '#1e1e1e',
            '--card-border': '#333333',
            '--skill-bar-bg': '#333333',
            '--skill-progress-bg': 'linear-gradient(90deg, #0071e3 0%, #00a1e4 100%)',
            '--hero-bg': 'linear-gradient(135deg, #2c2c2e 0%, #1c1c1e 100%)',
            '--button-bg': '#0071e3',
            '--button-hover': '#0063c7',
            '--metric-bg': '#1e1e1e',
            '--metric-border': '#333333',
            '--input-bg': '#1e1e1e',
            '--input-border': '#333333',
            '--text-muted': '#cccccc',
            '--text-metric': '#ffffff',
            '--tag-bg': '#333333',
            '--tag-border': '#444444',
            '--social-icon': '#cccccc',
        }
    else:
        css_vars = {
            '--background': '#ffffff',
            '--text-color': '#000000',
            '--card-bg': '#f5f5f5',
            '--card-border': '#e0e0e0',
            '--skill-bar-bg': '#e0e0e0',
            '--skill-progress-bg': 'linear-gradient(90deg, #0071e3 0%, #00a1e4 100%)',
            '--hero-bg': 'linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%)',
            '--button-bg': '#0071e3',
            '--button-hover': '#0063c7',
            '--metric-bg': '#f8f9fa',
            '--metric-border': '#dee2e6',
            '--input-bg': '#ffffff',
            '--input-border': '#ced4da',
            '--text-muted': '#6c757d',
            '--text-metric': '#000000',
            '--tag-bg': '#e9ecef',
            '--tag-border': '#dee2e6',
            '--social-icon': '#495057',
        }
    
    css = f"""
    <style>
        :root {{
            --background: {css_vars['--background']};
            --text-color: {css_vars['--text-color']};
            --card-bg: {css_vars['--card-bg']};
            --card-border: {css_vars['--card-border']};
            --skill-bar-bg: {css_vars['--skill-bar-bg']};
            --skill-progress-bg: {css_vars['--skill-progress-bg']};
            --hero-bg: {css_vars['--hero-bg']};
            --button-bg: {css_vars['--button-bg']};
            --button-hover: {css_vars['--button-hover']};
            --metric-bg: {css_vars['--metric-bg']};
            --metric-border: {css_vars['--metric-border']};
            --input-bg: {css_vars['--input-bg']};
            --input-border: {css_vars['--input-border']};
            --text-muted: {css_vars['--text-muted']};
            --text-metric: {css_vars['--text-metric']};
            --tag-bg: {css_vars['--tag-bg']};
            --tag-border: {css_vars['--tag-border']};
            --social-icon: {css_vars['--social-icon']};
        }}
        
        /* Base styling */
        .stApp {{
            background: var(--background);
            color: var(--text-color);
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
        }}
        
        /* Project cards */
        .project-card {{
            background: var(--card-bg);
            border-radius: 18px;
            padding: 25px;
            margin: 15px 0;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
            border: 1px solid var(--card-border);
        }}
        
        .project-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
        }}
        
        /* Skill bars */
        .skill-bar {{
            background: var(--skill-bar-bg);
            border-radius: 12px;
            margin: 15px 0;
            height: 24px;
            overflow: hidden;
        }}
        
        .skill-progress {{
            background: var(--skill-progress-bg);
            height: 100%;
            border-radius: 12px;
            display: flex;
            align-items: center;
            padding-left: 15px;
            color: white;
            font-weight: 500;
            transition: width 1s ease-in-out;
        }}
        
        /* Hero header */
        .hero-header {{
            background: var(--hero-bg);
            padding: 6rem 2rem;
            color: var(--text-color);
            margin-bottom: 2rem;
            text-align: center;
            border-radius: 18px;
            border: 1px solid var(--card-border);
        }}
        
        /* Buttons */
        .apple-button {{
            background: var(--button-bg);
            color: white !important;
            border: none;
            padding: 12px 28px;
            border-radius: 25px;
            font-size: 1rem;
            font-weight: 500;
            transition: all 0.3s ease;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }}
        
        /* Form elements */
        .stTextInput>div>div>input, 
        .stTextArea>div>textarea {{
            background: var(--input-bg) !important;
            color: var(--text-color) !important;
            border-radius: 12px !important;
            padding: 12px 16px !important;
            border: 1px solid var(--input-border) !important;
        }}
        
        /* Metrics */
        .stMetric {{
            background: var(--metric-bg);
            color: var(--text-metric) !important;
            padding: 20px;
            border-radius: 18px;
            border: 1px solid var(--metric-border);
        }}
        
        /* Text styling */
        h1, h2, h3, h4, h5, h6 {{
            color: var(--text-color) !important;
        }}
        
        p, div {{
            color: var(--text-muted) !important;
        }}
        
        /* Technology tags */
        .tech-tag {{
            background: var(--tag-bg);
            color: var(--text-color);
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 0.9rem;
            border: 1px solid var(--tag-border);
        }}
        
        /* Social links */
        .social-link {{
            color: var(--social-icon) !important;
            transition: color 0.3s ease;
            text-decoration: none;
        }}
        
        .social-link:hover {{
            color: var(--button-bg) !important;
        }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

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

# --- Interactive Components ---
def create_3d_card(content):
    return components.html(f"""
    <div style="perspective: 1000px;">
        <div style="
            transition: transform 0.3s;
            transform-style: preserve-3d;
            &:hover {{ transform: rotateY(10deg) rotateX(5deg); }}
        ">
            {content}
        </div>
    </div>
    """, height=300)

# --- Updated Project Card ---
def project_card(project):
    card = f"""
    <div class="project-card">
        <h3>{project['project_name']}</h3>
        <p class="project-description">{project['description']}</p>
        <div class="tech-tags">
            {" ".join([f'<span class="tech-tag">{tech}</span>' 
                      for tech in project['technologies'].split(', ')])}
        </div>
        <div class="project-footer">
            <div class="project-meta">
                <div>📅 {project['year']}</div>
                <div>⭐ {project['complexity']}</div>
                <div>🚀 {project['impact']}</div>
            </div>
            <button class="apple-button">
                View Details
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M4 8a.5.5 0 0 1 .5-.5h5.793L8.146 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708-.708l2.147-2.146H4.5A.5.5 0 0 1 4 8z"/>
                </svg>
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
    
    # Theme Toggle
    current_theme = st.session_state.get('theme', 'dark')
    theme_emoji = '🌙' if current_theme == 'dark' else '☀️'
    toggle_label = f"({current_theme.capitalize()})"
    if st.toggle(f'{theme_emoji} {toggle_label}'):
        st.session_state.theme = 'light' if current_theme == 'dark' else 'dark'
        st.rerun()
    
    # Navigation
    nav = st.radio("Navigation", ["Home", "Projects", "Skills", "About", "Contact"])
    if nav != st.session_state.page:
        st.session_state.page = nav
        st.rerun()
    
    # Social Links
    st.markdown("""
    <div style="margin-top: 50px; display: flex; gap: 15px;">
        <a href="https://linkedin.com" target="_blank" class="social-link">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
        </a>
        <a href="https://github.com" target="_blank" class="social-link">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
        </a>
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
    
    cols = st.columns(3)
    with cols[0]:
        st.subheader("Contact Info", anchor=False)
        st.markdown("""
        📍 **Location**  
        San Francisco Bay Area  
        California, USA
        
        📧 **Email**  
        [john.doe@dataportfolio.com](mailto:john.doe@dataportfolio.com)
        
        📱 **Phone**  
        +1 (555) 123-4567
        """)
    
    with cols[1]:
        st.subheader("Social", anchor=False)
        st.markdown("""
        <div style="display: flex; gap: 15px; margin-top: 20px;">
            <a href="https://linkedin.com" target="_blank" style="color: #0077b5; text-decoration: none; display: flex; align-items: center; gap: 8px;">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
                </svg>
                LinkedIn
            </a>
            <a href="https://github.com" target="_blank" style="color: #333; text-decoration: none; display: flex; align-items: center; gap: 8px;">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                </svg>
                GitHub
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    with cols[2]:
        st.subheader("Location", anchor=False)
        components.html(
            """<iframe src="https://www.google.com/maps/embed?pb=..."></iframe>""",
            height=300
        )