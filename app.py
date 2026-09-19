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


#-- Load ASSETS --
lottie_coding = load_local_lottie("coding.json")
# find the https://www.webfx.com/tools/emoji-cheat-sheet/ the icons
st.set_page_config(page_title="Streamlit webpage", page_icon=":tada:", layout="wide")
#---HEADER SECTION ----
with st.container():
    st.subheader("HI, I am tensaye :wave: ")
    st.title("A software enginer from Ethiopia")
    st.write("I am passionate about finding ways to use python and VBA to be more effective and efficient in business settings.")
    st.write("[Learn more >](https://portfolio2-six-flax.vercel.app/)")

#--- WHAT I DO ---
with st.container():
    st.write("---")
    left_col, right_col = st.columns(2)
    with left_col:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I create practical, efficient digital solutions that help businesses save time,
            reduce manual work, and improve daily operations.

            My focus is on using Python, VBA, and automation tools to simplify repetitive
            tasks, organize data, and build smarter workflows.

            I help businesses with:
            - Python automation and script development
            - Excel and VBA solutions for reporting and data processing
            - Data cleaning, analysis, and dashboard creation
            - Workflow optimization and process improvement
            - Turning complex tasks into simple, reliable systems
            """
        )
        with right_col:
            if lottie_coding is not None:
                st_lottie.st_lottie(lottie_coding, height=300, key="Coding")

