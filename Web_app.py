import streamlit as st
from backend import get_urls, scrap_infos

# ---------------- Sidebar: Contact Info with Icons ----------------
st.sidebar.markdown("### 📫 Contact Me")
st.sidebar.markdown("**Email:** [rahmani.abderraouff@gmail.com](mailto:rahmani.abderraouff@gmail.com)")

st.sidebar.markdown(
    "[![GitHub](https://img.shields.io/badge/GitHub-raoufRahmani-181717?style=for-the-badge&logo=github)]"
    "(https://github.com/raoufRahmani)"
)
st.sidebar.markdown(
    "[![LinkedIn](https://img.shields.io/badge/LinkedIn-raoufrhm-0A66C2?style=for-the-badge&logo=linkedin)]"
    "(https://www.linkedin.com/in/raoufrhm/)"
)

# ---------------- Main app ----------------
st.markdown("<h1 style='text-align: center;'>Amazon App Scraper</h1>", unsafe_allow_html=True)
st.caption("Created by Abderraouf RAHMANI")

st.write("Welcome to the Amazon app scraper, this web application will allow you to collect data about Amazon products.")
st.markdown("- Go to amazon.fr")
st.markdown("- Choose a product")
st.markdown("- Copy the link of the page and paste it here")

# STEP 1: Get links from URL
with st.form(key='form1'):
    link = st.text_area("Enter the URL")
    st.write("👉 Choose the number of pages to scrape (from 1 to 7):")
    num_pages = st.slider("Number of pages to scrap", 1, 7)
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

# STEP 2: Only show this if step 1 is done
if st.session_state.get("step1_done", False):
    with st.form(key="file"):
        file = st.text_area("Choose a name for your file")
        button2 = st.form_submit_button("Submit")

    if button2:
        with st.spinner("Creating your file, this may take a few minutes..."):
            # Sanitize filename
            file = file.strip().replace('\n', '').replace('\r', '')
            filename_with_ext = scrap_infos(st.session_state["product_links"], file)

        st.success("File created successfully!")

        # Download button
        with open(filename_with_ext, "rb") as f:
            st.download_button("Download file", f, file_name=filename_with_ext)







