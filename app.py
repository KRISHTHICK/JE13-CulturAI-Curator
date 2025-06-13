import streamlit as st
from PIL import Image
from utils.classify_art import identify_artifact
from artifact_agent import cultural_chat
from rag_culture import rag_query

st.set_page_config(page_title="CulturAI Curator", layout="wide")
st.title("🏛️ CulturAI Curator – Explore Cultural Artifacts with AI")

uploaded = st.file_uploader("📸 Upload an artifact image", type=["jpg", "png", "jpeg"])
if uploaded:
    img = Image.open(uploaded)
    st.image(img, caption="Uploaded Artifact", use_column_width=True)

    with st.spinner("Analyzing Artifact..."):
        result = identify_artifact(img)
        st.success(f"🎨 Identified: {result['style']} from {result['region']}")
        st.markdown(f"**Cultural Insight**: {result['description']}")

    st.subheader("🧠 Ask AI about this culture:")
    q = st.text_input("Type your cultural question")
    if q:
        response = cultural_chat(q)
        st.info(response)

    with st.expander("📚 Ask RAG from Local Knowledge Base"):
        query = st.text_input("Enter your specific cultural question")
        if query:
            answer = rag_query(query)
            st.success(answer)
