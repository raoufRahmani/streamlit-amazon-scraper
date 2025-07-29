import streamlit as st
from backend import get_urls, scrap_infos

# Sidebar 
st.sidebar.markdown("### Contact Me")
st.sidebar.markdown("**Email:** [rahmani.abderraouff@gmail.com](mailto:rahmani.abderraouff@gmail.com)")

github_link = "https://github.com/raoufRahmani"
linkedin_link = "https://www.linkedin.com/in/raoufrhm/"


st.sidebar.markdown(
    f"""
    <style>
    .icon-link {{
        display: flex;
        align-items: center;
        margin-bottom: 8px;
        font-size: 16px;
        text-decoration: none;
        color: #000;
    }}
    .icon-link:hover {{
        text-decoration: underline;
        color: #0077b5;  /* LinkedIn blue on hover */
    }}
    .icon {{
        width: 20px;
        height: 20px;
        margin-right: 8px;
    }}
    </style>

    <a href="{github_link}" target="_blank" class="icon-link">
        <img class="icon" src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/github.svg" alt="GitHub" />
        GitHub
    </a>

    <a href="{linkedin_link}" target="_blank" class="icon-link">
        <img class="icon" src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/linkedin.svg" alt="LinkedIn" />
        LinkedIn
    </a>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1 style='text-align: center;'>Amazon App Scraper</h1>", unsafe_allow_html=True)
st.caption("Created by Abderraouf RAHMANI")

st.write("Welcome to the Amazon app scraper, this web application will allow you to collect data about Amazon products.")
st.markdown("- Go to amazon.fr")
st.markdown("- Choose a product")
st.markdown("- Copy the link of the page and paste it here")

# step1: Get links from URL
with st.form(key='form1'):
    link = st.text_area("Enter the URL")
    st.write("Choose the number of pages to scrape (from 1 to 7):")
    num_pages = st.slider("",1, 7)
    button1 = st.form_submit_button("Submit")

if button1:
    with st.spinner("Scraping product links, please wait..."):
        liens = get_urls(link, num_pages)

    if liens:
        st.success(f"{len(liens)} product links found!")
        st.session_state["product_links"] = liens
        st.session_state["step1_done"] = True
    else:
        st.error("No product links found. Check the URL and try again.")
        st.session_state["step1_done"] = False

# move to step2 after submitting step 1
# STEP 2: Only show this if step 1 is done
if st.session_state.get("step1_done", False) and not st.session_state.get("step2_done", False):
    if not st.session_state.get("creating_file", False):
        with st.form(key="file_form"):
            file = st.text_area("Choose a name for your file")
            button2 = st.form_submit_button("Submit")

        if button2:
            st.session_state["creating_file"] = True
            st.session_state["file_name_input"] = file.strip().replace('\n', '').replace('\r', '')
            st.rerun()

# Run scraper only once when creating_file is True
if st.session_state.get("creating_file", False) and not st.session_state.get("step2_done", False):
    with st.spinner("Creating your file, this may take a few minutes..."):
        filename_with_ext = scrap_infos(st.session_state["product_links"], st.session_state["file_name_input"])
        st.session_state["generated_file"] = filename_with_ext
        st.session_state["step2_done"] = True
        st.session_state["creating_file"] = False
    st.success("File created successfully!")

# Show download button after file creation
if st.session_state.get("step2_done", False):
    filename_with_ext = st.session_state.get("generated_file", None)
    if filename_with_ext:
        with open(filename_with_ext, "rb") as f:
            st.download_button("Download file", f, file_name=filename_with_ext)







