# from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Load environment variables
# load_dotenv()

# Define Your Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL queries!
    The SQL database is named STUDENT and contains columns for NAME, CLASS, SECTION and MARKS. 

    For instance:
    Example 1 - To find the count of records, the SQL command should resemble:
    "How many entries of records are present?"
    SQL: SELECT COUNT(*) FROM STUDENT;

    Example 2 - To retrieve all students in the Data Science class, the question is:
    "Tell me all the students studying in Data Science class?"
    SQL: SELECT * FROM STUDENT WHERE CLASS='Data Science';

    Note: The SQL code should not have triple backticks (```) in the beginning or end, and the word 'sql' should not appear in the output.
    """
]

def main():

    # Streamlit App
    st.set_page_config(page_title="Gemini SQL Query Data Retrieval App", page_icon="✨")

    # Configure Google API Key
    st.write(
        "Has environment variables been set:",
        os.environ["ST_GOOGLE_API_KEY"] == st.secrets["ST_GOOGLE_API_KEY"])

    genai.configure(api_key=os.getenv("ST_GOOGLE_API_KEY"))

    # Function to load Google Gemini Model and provide queries as response
    def generate_gemini_response(question, prompt):
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content([prompt[0], question])
        return response.text

    # Function to retrieve query from the database
    def execute_sql_query(sql, db):
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return rows

    

    # App header
    st.title("🔮 Gemini App: Retrieve SQL Data with Magic ✨")

    # User input for the question
    question = st.text_input("🤔 ✨ Ask me a question about the STUDENT database:", key="input")

    # Button to submit the question
    submit = st.button("🚀 Ask me the question")

    # Handle submit action
    if submit:
        # Get response from Gemini model
        gemini_response = generate_gemini_response(question, prompt)
        
        # Execute SQL query based on the response
        sql_query_response = execute_sql_query(gemini_response, "student.db")
        
        # Display the SQL query response
        st.subheader("🌈 The SQL Query Response is:")
        for row in sql_query_response:
            st.success(row)

if __name__ == '__main__':
    main()
