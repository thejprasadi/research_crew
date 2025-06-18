import streamlit as st
from main import GuideCreatorFlow, GuideCreatorState

def run_guide_flow(topic, audience_level):
    flow = GuideCreatorFlow()
    flow.state.topic = topic
    flow.state.audience_level = audience_level
    flow.kickoff()
    # after kickoff, flow.state will be updated with the outline and sections
    return flow.state

st.title("Comprehensive Guide Creator")

topic = st.text_input("Topic for your guide:")
audience = st.selectbox("Audience level:", ["beginner", "intermediate", "advanced"])

if st.button("Create Guide"):
    if topic and audience:
        with st.spinner("Creating guide..."):
            state = run_guide_flow(topic, audience)
        st.success("Guide created!")
        st.write("Guide Title:", state.guide_outline.title)
        st.write("Introduction:", state.guide_outline.introduction)
        for section in state.guide_outline.sections:
            st.subheader(section.title)
            st.write(section.description)
            st.write(state.sections_content.get(section.title, ""))
        st.write("Conclusion:", state.guide_outline.conclusion)
    else:
        st.error("Please enter a topic and select audience level.")
