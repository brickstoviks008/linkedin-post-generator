import streamlit as st
from few_shots import FewShotPosts
from post_generator import generate_post

# Options for length and language
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]



# Main app layout
def main():
    st.subheader("LinkedIn Post Generator")

    # Create three columns for the dropdowns
    col1, col2, col3 = st.columns(3)

    fs = FewShotPosts()
    tags = fs.get_tags()
    with col1:
        # Dropdown for Topic (Tags)
        selected_tag = st.selectbox("Topic", options=tags)

    with col2:
        # Dropdown for Length
        selected_length = st.selectbox("Length", options=length_options)

    with col3:
        # Dropdown for Language
        selected_language = st.selectbox("Language", options=language_options)

    # Generate Button
    if st.button("Generate"):
        post = generate_post(selected_length, selected_language, selected_tag)
        # Save to session state so it survives the regenerate button's rerun
        st.session_state["generated_post"] = post
        st.session_state["last_inputs"] = (selected_length, selected_language, selected_tag)

        # Show the post (and regenerate/stats) only if one exists
    if "generated_post" in st.session_state:
        post = st.session_state["generated_post"]

        st.write(post)

        # --- Length stats ---
        word_count = len(post.split())
        char_count = len(post)
        st.caption(f"📝 {word_count} words · {char_count} characters")

        if char_count > 3000:
            st.warning("This post exceeds LinkedIn's 3000 character limit.")
        elif char_count > 1300:
            st.info("Posts under ~1300 characters tend to get better engagement on LinkedIn.")

        # --- Regenerate button ---
        if st.button("🔄 Regenerate"):
            last_length, last_language, last_tag = st.session_state["last_inputs"]
            new_post = generate_post(last_length, last_language, last_tag)
            st.session_state["generated_post"] = new_post
            st.rerun()

if __name__ == "__main__":
    main()
