import streamlit as st
import pandas as pd
from text_generator import question_generator

def main():
    st.title(" 🤖 AI Assist for Educators ")
    st.header("Question Variant Generator", divider="gray")

    with st.sidebar:
        st.title("🤖 AI Assist for Educators")
        st.markdown(
            """This app transforms your original quiz questions into 
multiple variants with just a TSV file upload. 
            This app is  built using:
- [Streamlit](https://streamlit.io/) 
- [OpenAI](https://openai.com/)
- [Langchain](https://python.langchain.com/)
             """  
        st.text("")
        st.write("Please enter your OpenAI API key")
        OPENAI_API_KEY = st.text_input("OpenAI API Key", 
                                   key="file_qa_api_key", 
                                   type="password")       

        "[View the source code of the app](https://github.com/swethag04/question_variant_generator)"
        )

    # File Uploader
    uploaded_file = st.file_uploader("Upload a TSV file with questions", type="tsv")

    if uploaded_file is not None:
        # Read CSV
        df = pd.read_csv(uploaded_file, sep="\t")

        # Display Original Data
        st.subheader("Original Data")
        st.write(df)

        # Data Processing 
        output = question_generator(df, OPENAI_API_KEY)

        # Display Processed Data
        st.subheader("Output with 2 variants of each question")
        st.write(output)

        # Download Processed Data
        st.download_button(
            label="Download Processed Data as CSV",
            data=output.to_csv(index=False),
            file_name="processed_data.csv",
            mime="text/csv",
        )

if __name__ == "__main__":
    main()
