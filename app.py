import json
import os

import streamlit as st
import streamlit_lottie as st_lottie


def load_local_lottie(file_name):
    file_path = os.path.join(os.path.dirname(__file__), "assets", file_name)
    if not os.path.exists(file_path):
        return None

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


# -- Page setup --
st.set_page_config(page_title="Tensaye | Software Engineer", page_icon="✨", layout="wide")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');
    :root { --ink: #18232d; --muted: #60717d; --cream: #f7f5ef; --mint: #dcefe8; --coral: #e87961; --line: #d9e1dc; }
    .stApp { background: var(--cream); color: var(--ink); }
    [data-testid="stHeader"] { background: transparent; }
    .block-container { max-width: 1120px; padding: 3rem 3rem 4rem; }
    h1, h2, h3 { font-family: 'Space Grotesk', sans-serif !important; color: var(--ink); }
    p, li, a, div { font-family: 'DM Sans', sans-serif; }
    h1 { font-size: clamp(2.8rem, 6vw, 5.6rem) !important; line-height: .98 !important; letter-spacing: -2px; }
    h2 { font-size: 2.1rem !important; }
    .eyebrow { color: var(--coral); font-weight: 700; letter-spacing: 2px; text-transform: uppercase; font-size: .78rem; }
    .hero-copy { color: var(--muted); font-size: 1.15rem; line-height: 1.7; max-width: 600px; }
    .tag { display: inline-block; background: var(--mint); padding: .5rem .8rem; border-radius: 999px; margin: .2rem .25rem .2rem 0; color: var(--ink); font-size: .85rem; }
    .section-rule { border-top: 1px solid var(--line); margin: 3.5rem 0 2.5rem; }
    .project-card { border: 1px solid var(--line); border-radius: 12px; padding: 1.4rem; background: rgba(255,255,255,.35); min-height: 175px; }
    .project-card h3 { margin-top: 0; font-size: 1.25rem; }
    .project-card p { color: var(--muted); line-height: 1.6; }
    .contact { background: var(--ink); border-radius: 16px; padding: 2rem 2.2rem; color: white; }
    .contact h2, .contact p { color: white !important; }
    .contact p { opacity: .8; }
    @media (max-width: 700px) { .block-container { padding: 2rem 1.2rem 3rem; } h1 { font-size: 3.2rem !important; } }
    </style>
    """,
    unsafe_allow_html=True,
)

# -- Load assets --
lottie_coding = load_local_lottie("coding.json")

# -- Header --
with st.container():
    st.markdown('<p class="eyebrow">Software engineer · Ethiopia</p>', unsafe_allow_html=True)
    hero_text, hero_art = st.columns([1.2, .8], gap="large")
    with hero_text:
        st.title("I turn repetitive work into simple systems.")
        st.markdown('<p class="hero-copy">I build practical tools with Python and VBA that help businesses save time, work with better data, and move with confidence.</p>', unsafe_allow_html=True)
        st.link_button("Explore my work →", "https://portfolio2-six-flax.vercel.app/")
        st.markdown('<span class="tag">Python</span><span class="tag">VBA</span><span class="tag">Automation</span>', unsafe_allow_html=True)
    with hero_art:
        if lottie_coding is not None:
            st_lottie.st_lottie(lottie_coding, height=320, key="Coding")

# -- What I do --
with st.container():
    st.markdown('<div class="section-rule"></div>', unsafe_allow_html=True)
    st.markdown('<p class="eyebrow">How I help</p>', unsafe_allow_html=True)
    st.header("What I do")
    st.write("I create efficient digital solutions that reduce manual work and make everyday business operations easier to manage.")
    service_cols = st.columns(3)
    services = [
        ("01 / Automate", "I replace repetitive tasks with reliable Python scripts and workflows."),
        ("02 / Organize", "I clean, structure, and transform data into something useful."),
        ("03 / Improve", "I build Excel and VBA tools that make reporting faster and clearer."),
    ]
    for column, (title, description) in zip(service_cols, services):
        with column:
            st.markdown(f'<div class="project-card"><h3>{title}</h3><p>{description}</p></div>', unsafe_allow_html=True)

# -- Projects --
with st.container():
    st.markdown('<div class="section-rule"></div>', unsafe_allow_html=True)
    st.markdown('<p class="eyebrow">Selected work</p>', unsafe_allow_html=True)
    st.header("My projects")
    project_cols = st.columns(2)
    projects = [
        ("Business automation", "Scripts that remove repetitive steps and give teams more time for meaningful work."),
        ("Data and reporting tools", "Clear Excel dashboards and VBA solutions for faster, more confident decisions."),
    ]
    for column, (title, description) in zip(project_cols, projects):
        with column:
            st.markdown(f'<div class="project-card"><h3>{title}</h3><p>{description}</p></div>', unsafe_allow_html=True)

# -- Contact --
with st.container():
    st.markdown('<div class="section-rule"></div>', unsafe_allow_html=True)
    st.markdown('<div class="contact"><h2>Have a process worth improving?</h2><p>Let’s turn the slow, manual parts of your work into something simpler.</p></div>', unsafe_allow_html=True)
    st.write("[Get in touch →](https://portfolio2-six-flax.vercel.app/)")

