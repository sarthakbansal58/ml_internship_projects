import streamlit as st
from chains.story_chains import generateStory
from utils.story_pdf import generate_pdf



st.set_page_config(
    page_title="AI Story Generator",
    page_icon="📖",
    layout="wide"
)

st.title("📖 AI Story Generator")
st.write("Generate amazing stories using Generative AI.")

# Sidebar

st.sidebar.header("Story Settings")

genre = st.sidebar.selectbox(
    "Genre",
    ["Fantasy", "Mystery", "Horror", "Sci-Fi", "Adventure"]
)

tone = st.sidebar.selectbox(
    "Tone",
    ["Funny", "Serious", "Dark", "Emotional", "Suspenseful"]
)

length = st.sidebar.selectbox(
    "Story Length",
    ["Short", "Medium", "Long"]
)
language = st.sidebar.selectbox(
    "Select Language",
    ["English", "Hindi", "Hinglish", "Spanish", "French"]
)

# Main Inputs

character = st.text_input("Character Name")

setting = st.text_input("Story Setting")

user_prompt = st.text_area("Enter Story Prompt")

generate = st.button("🚀 Generate Story")

if generate:
    st.success("UI Working Successfully!")

    st.write("### User Inputs")

    st.write(f"Genre: {genre}")
    st.write(f"Tone: {tone}")
    st.write(f"Length: {length}")
    st.write(f"language:{language}")
    st.write(f"Character: {character}")
    st.write(f"Setting: {setting}")
    st.write(f"Prompt: {user_prompt}")
    story = generateStory(
        genre,
        tone,
        length,
        language,
        character,
        setting,
        user_prompt
    )
    pdf=generate_pdf(
        title="AI generated story",
        genre=genre,
        tone=tone,
        character=character,
        language=language,
        setting=setting,
        story=story
        ) 
    
    st.download_button(
        label="📄 Download Story PDF",
        data=pdf,
        file_name="story.pdf",
        mime="application/pdf"
        )
