import streamlit as st
from src.guide_creator_flow.main import run_guide_flow

st.set_page_config(page_title="Guide Creator", layout="wide")
st.title("📘 Guide Creator")

# Inputs
topic = st.text_input("Enter the topic for your guide")
audience = st.selectbox("Select the audience level", ["beginner", "intermediate", "advanced"])

# When user clicks button
if st.button("Generate Guide"):
    if topic and audience:
        with st.spinner("Generating your guide..."):
            guide_md = run_guide_flow(topic, audience)
        st.success("✅ Guide generated successfully!")

        # Render guide in clean markdown format
        st.markdown("---")
        st.subheader("📄 Generated Guide")
        st.markdown(guide_md, unsafe_allow_html=True)  # render markdown content
        st.download_button("📥 Download Guide as Markdown", data=guide_md, file_name="complete_guide.md")
    else:
        st.warning("Please enter both the topic and audience level.")
