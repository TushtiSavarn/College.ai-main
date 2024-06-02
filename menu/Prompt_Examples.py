import streamlit as st
#Main function
def main():
    st.write("<h1><center>Prompt Examples</center></h1>", unsafe_allow_html=True)
    
    st.write("<h2>Example Prompts</h2>", unsafe_allow_html=True)

    # Summarization
    st.write("<h3>1. Summarization</h3>", unsafe_allow_html=True)
    st.text_area(
        'Summarize in 50 words',
        placeholder="Summarize the topic provided below in 50 words."
    )
    st.write("<p><i>Example: Summarize the impact of climate change on global agriculture.</i></p>", unsafe_allow_html=True)

    # Contextual Explanation
    st.write("<h3>2. Contextual Explanation</h3>", unsafe_allow_html=True)
    st.text_area(
        'Explain the context',
        placeholder="Explain the given context in detail."
    )
    st.write("<p><i>Example: Explain the historical context of the Renaissance period in Europe.</i></p>", unsafe_allow_html=True)

    # Question Generation
    st.write("<h3>3. Question Generation</h3>", unsafe_allow_html=True)
    st.text_area(
        'Generate questions',
        placeholder="Make 10 questions with answers based on the given context."
    )
    st.write("<p><i>Example: Create 10 questions with answers about the water cycle.</i></p>", unsafe_allow_html=True)

    # Resume Analysis
    st.write("<h3>4. Resume Analysis</h3>", unsafe_allow_html=True)
    st.text_area(
        'Analyze resume',
        placeholder="Analyze the provided resume and give recommendations."
    )
    st.write("<p><i>Example: Provide feedback on the resume of a software engineer with 5 years of experience.</i></p>", unsafe_allow_html=True)

    # ATS Matching
    st.write("<h3>5. ATS Matching</h3>", unsafe_allow_html=True)
    st.text_area(
        'Match job descriptions',
        placeholder="Match the given job description with resumes and provide feedback."
    )
    st.write("<p><i>Example: Match the job description of a Data Scientist position with the given resumes.</i></p>", unsafe_allow_html=True)

    # PDF Querying
    st.write("<h3>6. PDF Querying</h3>", unsafe_allow_html=True)
    st.text_area(
        'Query PDF',
        placeholder="Upload a PDF and ask questions about its content."
    )
    st.write("<p><i>Example: Upload a research paper on machine learning and ask about the key findings.</i></p>", unsafe_allow_html=True)

    # Creative Writing
    st.write("<h3>7. Creative Writing</h3>", unsafe_allow_html=True)
    st.text_area(
        'Write a story',
        placeholder="Write a short story based on the given prompt."
    )
    st.write("<p><i>Example: Write a short story about a time traveler who accidentally lands in the future.</i></p>", unsafe_allow_html=True)

    # Exploring ChatGPT-4 Features
    st.write("<h3>8. Exploring ChatGPT-4 Features</h3>", unsafe_allow_html=True)
    st.text_area(
        'Explore ChatGPT-4',
        placeholder="Describe how ChatGPT-4 can be used for natural language understanding tasks."
    )
    st.write("<p><i>Example: Explain the capabilities of ChatGPT-4 in understanding and generating human-like text, with tasks like summarization, translation, and question-answering.</i></p>", unsafe_allow_html=True)

    # Training/Uploading PDFs
    st.write("<h3>9. Training/Uploading PDFs</h3>", unsafe_allow_html=True)
    st.text_area(
        'Train/Upload PDF',
        placeholder="How can I upload and query a PDF document in College.ai's Ask_To_PDF feature?"
    )
    st.write("<p><i>Example: Provide step-by-step instructions on uploading a PDF and querying it for information.</i></p>", unsafe_allow_html=True)

    # Using AI Lens
    st.write("<h3>10. Using AI Lens</h3>", unsafe_allow_html=True)
    st.text_area(
        'Use AI Lens',
        placeholder="How does the AI Lens feature work for image analysis and chatbot functionality?"
    )
    st.write("<p><i>Example: Overview of AI Lens capabilities, and instructions on using it for image recognition and chatbot interaction.</i></p>", unsafe_allow_html=True)

    st.write("<h5><center>Keep Learning, keep exploring 😉!!</center></h5>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
