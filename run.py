import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import glob
import frontmatter  # pip install python-frontmatter
from datetime import datetime
from dateutil import parser
import plotly.express as px
import plotly.graph_objects as go

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
            padding: 1rem 1rem;
            color: var(--text-color);
            margin-bottom: 1rem;
            text-align: center;
            border-radius: 15px;
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

        /* Error/Success Messages */
        .stAlert {{
            margin-top: 1rem !important;
            border-radius: 12px !important;
        }}

        .stAlert .st-emotion-cache-1m7p7fa {{
            background-color: #ff444430 !important;
            border: 1px solid #ff4444 !important;
            color: var(--text-color) !important;
        }}

        .stAlert .st-emotion-cache-1vzeuhh {{
            background-color: #00C85130 !important;
            border: 1px solid #00C851 !important;
            color: var(--text-color) !important;
        }}

        /* Blog specific styling */
        .stExpander {{
            background: var(--card-bg) !important;
            border: 1px solid var(--card-border) !important;
            border-radius: 12px !important;
            margin-bottom: 1rem;
        }}

        .stExpander .st-emotion-cache-1qg05tj {{
            color: var(--text-color) !important;
            font-size: 1.2rem !important;
        }}

        .post-date {{
            color: var(--text-muted) !important;
            font-size: 0.9rem !important;
        }}

        .post-tag {{
            background: var(--tag-bg) !important;
            border: 1px solid var(--tag-border) !important;
            padding: 4px 12px !important;
            border-radius: 20px !important;
            font-size: 0.8rem !important;
        }}

        .stCodeBlock pre {{
            border-radius: 12px !important;
            background: var(--card-bg) !important;
            border: 1px solid var(--card-border) !important;
        }}

        /* Radar chart styling */
        .js-plotly-plot .plotly .main-svg {{
            border-radius: 18px;
            padding: 20px;
            border: 1px solid var(--card-border);
        }}

        .js-plotly-plot .plotly .polar-radialaxis-tick {{
            fill: var(--text-color) !important;
        }}

        /* TimelineJS Customization */
        .tl-timeline {{
            background: var(--card-bg) !important;
            border-radius: 18px !important;
            padding: 20px !important;
            border: 1px solid var(--card-border) !important;
        }}

        .tl-text {{
            color: var(--text-color) !important;
            background: var(--card-bg) !important;
        }}

        .tl-timemarker-media-container {{
            background: var(--button-bg) !important;
        }}

        .tl-menubar {{
            background: var(--card-bg) !important;
        }}

        /* Certification Card */
        .certification-card {{
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 18px;
            padding: 1.5rem;
            margin: 1rem 0;
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        }}

        .certification-card:hover {{
            transform: translateY(-3px);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
        }}

        /* Certification Header */
        .cert-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1.5rem;
            margin-bottom: 1rem;
        }}

        /* Certification Badge */
        .cert-badge {{
            flex-shrink: 0;
        }}

        .cert-badge img {{
            width: 100px;
            height: 100px;
            border-radius: 12px;
            border: 2px solid var(--card-border);
            padding: 5px;
            background: white;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }}

        /* Certification Info */
        .cert-info {{
            flex: 1;
        }}

        .cert-header h3 {{
            margin: 0;
            font-size: 1.2rem;
            color: var(--text-color);
        }}

        /* Certification Meta */
        .cert-meta {{
            display: flex;
            gap: 1rem;
            align-items: center;
            margin: 0.5rem 0;
        }}

        .cert-issuer {{
            font-weight: 500;
            color: var(--text-color);
            background: var(--tag-bg);
            padding: 0.25rem 0.8rem;
            border-radius: 20px;
            font-size: 0.9rem;
        }}

        .cert-id {{
            font-size: 0.9rem;
            color: var(--text-muted) !important;
            margin: 0.5rem 0 !important;
        }}

        /* Certification Date */
        .cert-date {{
            background: var(--tag-bg);
            color: var(--text-color);
            padding: 0.3rem 0.8rem;
            border-radius: 20px;
            font-size: 0.9rem;
        }}

        /* Certification Description */
        .cert-body p {{
            margin: 0.5rem 0;
            color: var(--text-muted);
        }}

        /* Certification Button */
        .certification-button {{
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: var(--button-bg);
            color: white !important;
            padding: 0.6rem 1.2rem;
            border-radius: 25px;
            text-decoration: none !important;
            margin-top: 1rem;
            transition: all 0.3s ease;
        }}

        .certification-button:hover {{
            background: var(--button-hover);
            transform: scale(1.02);
            color: white !important;
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

def send_email(name, email, message):
    """Send email using SMTP (Gmail example)"""
    try:
        # Create message
        msg = MIMEMultipart()
        msg['Subject'] = f"New message from {name} - Data Portfolio Contact"
        msg['From'] = st.secrets["email"]["smtp_user"]
        msg['To'] = st.secrets["email"]["recipient"]
        
        # Create HTML body
        html = f"""
        <html>
            <body>
                <h3>New Contact Form Submission</h3>
                <p><strong>Name:</strong> {name}</p>
                <p><strong>Email:</strong> {email}</p>
                <p><strong>Message:</strong></p>
                <p>{message}</p>
            </body>
        </html>
        """
        
        msg.attach(MIMEText(html, 'html'))
        
        # Connect to SMTP server
        with smtplib.SMTP_SSL(
            st.secrets["email"]["smtp_server"],
            st.secrets["email"]["smtp_port"]
        ) as server:
            server.login(
                st.secrets["email"]["smtp_user"],
                st.secrets["email"]["smtp_password"]
            )
            server.send_message(msg)
        
        return True
    except Exception as e:
        st.error(f"Error sending email: {str(e)}")
        return False

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
    
    # Add to navigation radio in sidebar
    nav = st.radio("Navigation", ["Home", "Professional Experience",  "Projects", "Skills", "Certifications", "Contact", "Blog"])
    if nav != st.session_state.page:
        st.session_state.page = nav
        st.rerun()

    # Resume Download Button
    with open("Resume_Raghuveera_N.pdf", "rb") as f:
        resume_bytes = f.read()
    
    st.download_button(
        label="📄 Download Resume",
        data=resume_bytes,
        file_name="John_Doe_Data_Scientist_Resume.pdf",
        mime="application/pdf",
        key="resume-download",
        help="Download my full resume in PDF format"
    )
    
    # Social Links
    st.markdown("""
    <div style="margin-top: 5px; display: flex; gap: 10px;">
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
        st.image("raghu.jpg")
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
    
    # Radar Chart Data
    skill_categories = {
        'Python': 90,
        'Data Analysis': 85,
        'Machine Learning': 88,
        'Data Visualization': 82,
        'Cloud Technologies': 75,
        'Big Data': 70
    }
    
    # Create radar chart
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=list(skill_categories.values()),
        theta=list(skill_categories.keys()),
        fill='toself',
        name='Skill Level',
        fillcolor='rgba(0, 113, 227, 0.4)',
        line=dict(color='#0071e3')
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont=dict(color='var(--text-color)'),
                gridcolor='var(--card-border)'
            ),
            angularaxis=dict(
                gridcolor='var(--card-border)',
                linecolor='var(--card-border)',
                tickfont=dict(color='var(--text-color)')
            )
        ),
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=500,
        margin=dict(l=50, r=50, b=50, t=50)
    )
    
    # Display radar chart
    st.plotly_chart(fig, use_container_width=True)
    
    # Existing skill bars
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

# Remove the About page handler and add Certifications
elif st.session_state.page == 'Certifications':
    st.title("Professional Certifications")
    
    # Update the certifications data structure
    certs = [
        {
            "title": "AWS Certified Machine Learning - Specialty",
            "issuer": "Amazon Web Services",
            "date": "2023",
            "credential_id": "AWS123456",
            "verify_url": "https://www.credly.com/cert/...",
            "badge_url": "https://images.credly.com/size/680x680/images/...aws.png"  # New field
        },
        {
            "title": "Google Cloud Professional Data Engineer",
            "issuer": "Google Cloud",
            "date": "2022",
            "credential_id": "GCP789012",
            "verify_url": "https://www.credential.net/...",
            "badge_url": "https://www.credly.com/sharer/...gcp-badge.png"
        },
    ]

    # Update the certification card HTML
    for cert in certs:
        with st.container():
            st.markdown(f"""
            <div class="certification-card">
                <div class="cert-header">
                    <div class="cert-badge">
                        <img src="{cert['badge_url']}" alt="{cert['title']} badge">
                    </div>
                    <div class="cert-info">
                        <h3>{cert['title']}</h3>
                        <div class="cert-meta">
                            <span class="cert-issuer">{cert['issuer']}</span>
                            <span class="cert-date">{cert['date']}</span>
                        </div>
                        <p class="cert-id">Credential ID: {cert['credential_id']}</p>
                    </div>
                </div>
                <a href="{cert['verify_url']}" target="_blank" class="certification-button">
                    Verify Credential
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
                        <path fill-rule="evenodd" d="M4 8a.5.5 0 0 1 .5-.5h5.793L8.146 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708-.708L10.293 8.5H4.5A.5.5 0 0 1 4 8z"/>
                    </svg>
                </a>
            </div>
            """, unsafe_allow_html=True)

    

elif st.session_state.page == 'Contact':
    st.title("Get in Touch")

    # Email validation regex pattern
    EMAIL_PATTERN = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    # Initialize session state keys
    if 'contact_submitted' not in st.session_state:
        st.session_state.contact_submitted = False
        st.session_state.form_data = {
            'name': '',
            'email': '',
            'message': ''
        }

    # Reset form after successful submission
    if st.session_state.contact_submitted:
        st.session_state.form_data = {'name': '', 'email': '', 'message': ''}
        st.session_state.contact_submitted = False
        st.rerun()  # Force UI refresh after clearing

    with st.form("contact_form"):
        # Create form fields with dedicated keys
        name = st.text_input(
            "Name",
            placeholder="John Smith",
            key="form_name",
            value=st.session_state.form_data['name']
        )
        email = st.text_input(
            "Email", 
            placeholder="john@example.com",
            key="form_email",
            value=st.session_state.form_data['email']
        )
        message = st.text_area(
            "Message", 
            height=150,
            key="form_message",
            value=st.session_state.form_data['message']
        )
        
        submitted = st.form_submit_button("Send Message", type="primary")
        
        if submitted:
            # Store values in temporary session state
            st.session_state.form_data.update({
                'name': name,
                'email': email,
                'message': message
            })
            
            # Validate inputs
            validation_passed = True
            if not name.strip():
                st.error("🚨 Please enter your name")
                validation_passed = False
            if not email.strip() or not re.match(EMAIL_PATTERN, email):
                st.error("📧 Please enter a valid email address")
                validation_passed = False
            if not message.strip():
                st.error("💬 Please enter your message")
                validation_passed = False

            if validation_passed:
                # Attempt to send email
                with st.spinner("Sending message..."):
                    if send_email(name, email, message):
                        st.success("🚀 Message sent successfully!")
                        st.balloons()
                        # Set flag and clear form data
                        st.session_state.contact_submitted = True
                    else:
                        st.error("❌ Failed to send message. Please try again later.")
    
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

elif st.session_state.page == 'Blog':
    st.title("Technical Writings")
    
    # Load blog posts with proper path handling
    posts = []
    blog_dir = os.path.join(os.path.dirname(__file__), "blog_posts")
    
    try:
        for file in glob.glob(os.path.join(blog_dir, "*.md")):
            try:
                post = frontmatter.load(file)
                # Convert date string to datetime object if needed
                post_date = post.metadata.get('date', datetime.now())
                if isinstance(post_date, str):
                    from dateutil import parser
                    post_date = parser.parse(post_date)
                
                posts.append({
                    "title": post.metadata.get('title', 'Untitled'),
                    "date": post_date,
                    "category": post.metadata.get('category', 'General'),
                    "tags": post.metadata.get('tags', []),
                    "content": post.content,
                    "interactive": post.metadata.get('interactive', False),
                    "metadata": post.metadata
                })
            except Exception as e:
                st.error(f"Error loading post {os.path.basename(file)}: {str(e)}")
                
    except Exception as e:
        st.error(f"Could not access blog directory: {str(e)}")
    
    # Sort posts by date
    posts.sort(key=lambda x: x['date'], reverse=True)
    
    # Blog layout
    col1, col2 = st.columns([3, 1])
    
    with col2:
        st.subheader("Filter Posts")
        selected_category = st.selectbox(
            "Category",
            ["All"] + list(sorted({p['category'] for p in posts}))
        )
        search_query = st.text_input("Search posts")
        
    with col1:
        if not posts:
            st.info("📭 No blog posts found. Check back later!")
            st.stop()  # This will stop further execution of the blog section

        for post in posts:
            if selected_category != "All" and post['category'] != selected_category:
                continue
                
            if search_query.lower() not in post['content'].lower():
                continue
            
            with st.expander(f"{post['title']} ({post['date'].strftime('%b %Y')})"):
                st.markdown(f"""
                **{post['category']}** · {", ".join(post['tags'])}
                """)
                
                # Render Markdown content with proper image paths
                st.markdown(post['content'].replace('](images/', '](blog_posts/images/'))
                
                # Add interactive elements
                if post['interactive']:
                    st.divider()
                    if "plot" in post['metadata']:
                        try:
                            fig = px.line(**post['metadata']['plot'])
                            st.plotly_chart(fig)
                        except Exception as e:
                            st.error(f"Could not render plot: {str(e)}")
                            
                    if "code" in post['metadata']:
                        try:
                            st.code(
                                post['metadata']['code']['content'], 
                                language=post['metadata']['code'].get('language', 'python')
                            )
                        except Exception as e:
                            st.error(f"Could not render code block: {str(e)}")

# Add experience page handler
elif st.session_state.page == 'Professional Experience':
    st.title("Professional Journey")
    
    # Timeline data
    timeline_data = [
        {
            "start_date": "2020-07",
            "end_date": "Present",
            "title": "Senior Data Scientist",
            "company": "Tech Corp Inc",
            "description": """Led ML initiatives across 3 product teams. 
            - Scaled real-time recommendation system to 1M+ users
            - Reduced inference latency by 40% through model optimization
            - Mentored 5 junior data scientists""",
            "icon": "🚀"
        },
        {
            "start_date": "2018-06",
            "end_date": "2020-06",
            "title": "Data Scientist",
            "company": "Data Insights LLC",
            "description": """Built predictive maintenance models for IoT devices.
            - Developed anomaly detection system with 92% accuracy
            - Automated ETL pipelines serving 100+ daily reports
            - Implemented CI/CD for ML models""",
            "icon": "📈"
        },
        {
            "start_date": "2016-09",
            "end_date": "2018-05",
            "title": "Junior Data Analyst",
            "company": "StartUp Ventures",
            "description": """Created business intelligence dashboards.
            - Reduced reporting time by 70% through automation
            - Performed customer segmentation analysis
            - Developed SQL training program for team""",
            "icon": "🔍"
        }
    ]
    
    # Generate TimelineJS HTML
    # Update the timeline data generation section
    timeline_html = f"""
    <link href="https://cdn.knightlab.com/libs/timeline3/latest/css/timeline.css" rel="stylesheet">
    <script src="https://cdn.knightlab.com/libs/timeline3/latest/js/timeline.js"></script>

    <div id='timeline-embed' style="width: 95%; height: 600px; margin: 0 auto"></div>

    <script>
        var timelineData = {{
            "title": {{
                "media": {{
                    "url": "",
                    "caption": "",
                    "credit": ""
                }},
                "text": {{
                    "headline": "Professional Timeline",
                    "text": "<p>Career progression and key achievements</p>"
                }}
            }},
            "events": [
                {','.join([f"""
                {{
                    "start_date": {{"year": "{e['start_date'].split('-')[0]}", "month": "{e['start_date'].split('-')[1]}"}},
                    "end_date": {{"year": "{datetime.now().year if e['end_date'] == 'Present' else e['end_date'].split('-')[0]}", "month": "{datetime.now().month if e['end_date'] == 'Present' else e['end_date'].split('-')[1] if '-' in e['end_date'] else '01'}"}},
                    "text": {{
                        "headline": "{e['icon']} {e['title']} · {e['company']}",
                        "text": "<p>{e['description'].replace('\n', '<br>')}</p>"
                    }},
                    "background": {{"color": "#ffffff"}}
                }}
                """ for e in timeline_data])}
            ]
        }};
        
        window.timeline = new TL.Timeline('timeline-embed', timelineData);
    </script>
    """
    
    # Render timeline
    components.html(timeline_html, height=650)
    
    # Add downloadable resume section
    st.markdown("---")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("Detailed Experience")
        st.markdown("""
        **Senior Data Scientist** @ Tech Corp Inc (2020-Present)  
        - Led cross-functional ML initiatives impacting 1M+ users
        - Optimized model serving infrastructure reducing costs by 35%
        - Introduced MLOps practices across 3 product teams
        
        **Data Scientist** @ Data Insights LLC (2018-2020)  
        - Developed predictive maintenance system with 92% accuracy
        - Automated ETL pipelines processing 10TB+ daily
        - Implemented model monitoring framework
        
        **Junior Data Analyst** @ StartUp Ventures (2016-2018)  
        - Built BI dashboards used by 50+ executives
        - Performed customer segmentation analysis
        - Reduced reporting time by 70% through automation
        """)
    
    with col2:
        st.subheader("Download Resume")
        with open("Resume_Raghuveera_N.pdf", "rb") as f:
            resume_bytes = f.read()
            st.download_button(
                label="📄 Download Full Resume",
                data=f,
                file_name="Resume_Raghuveera_N.pdf",
                mime="application/pdf"
            )
        st.markdown("""
        **Core Competencies:**
        - Machine Learning Engineering
        - Data Pipeline Architecture
        - Cloud Infrastructure (AWS/GCP)
        - Team Leadership & Mentoring
        """)