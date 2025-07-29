import streamlit as st
from backend import get_urls, scrap_infos

st.header("Amazon App Scraper")
st.caption("Created by Abderraouf RAHMANI")
st.write("Welcome to Amazon app scraper, this web application will allow you to collect data about amazon products")
st.markdown("- Go to amazon.fr")
st.markdown("- Choose a product")
st.markdown("- Copy the link of the page and paste it here")

# STEP 1: Get links from URL
with st.form(key='form1'):
    link = st.text_area("Enter the URL")
    num_pages = st.slider("Number of pages to scrap", 1, 7)
    button1 = st.form_submit_button("Submit")

if button1:
    st.info("Scraping product links...")
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
        st.info('Creating your file...')
        st.info("This can take few minutes, thank you for your patience.")

        # Sanitize filename
        file = file.strip().replace('\n', '').replace('\r', '')
        filename_with_ext = scrap_infos(st.session_state["product_links"], file)

        # Download button
        with open(filename_with_ext, "rb") as f:
            st.download_button("Download file", f, file_name=filename_with_ext)

st.markdown("---")
st.markdown("###  Contact Me")
st.markdown(" [rahmani.abderraouff@gmail.com](mailto:rahmani.abderraouff@gmail.com)")

st.markdown(
    """
    <a href="https://github.com/raoufRahmani" target="_blank">
        <button style="padding:8px 16px; background-color:#24292e; color:white; border:none; border-radius:5px;">GitHub</button>
    </a>
    <a href="https://www.linkedin.com/in/raoufrhm/" target="_blank" style="margin-left:10px;">
        <button style="padding:8px 16px; background-color:#0077b5; color:white; border:none; border-radius:5px;">LinkedIn</button>
    </a>
    """,
    unsafe_allow_html=True
)






