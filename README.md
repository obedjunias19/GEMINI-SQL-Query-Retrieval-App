 Gemini SQL Query Data Retrieval App

Welcome to the Gemini SQL Query Data Retrieval App repository. This application leverages the Gemini model to translate English questions into SQL queries for a hypothetical SQL database named STUDENT.

## Overview

The app is designed to provide users with a user-friendly interface to input questions and retrieve the corresponding SQL queries. It uses the Google Gemini model for natural language understanding and generation.

## Features

- Translate English questions into SQL queries and then Query the Database
- Hypothetical SQL database named STUDENT with columns: NAME, CLASS, SECTION and MARKS
- Clean and precise SQL code Output generated

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/gemini-sql-query-retrieval-app.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure your Google API Key in a `.env` file:

    ```env
    GOOGLE_API_KEY=your_google_api_key
    ```

4. Run the app:

    ```bash
    streamlit run app.py
    ```

## Usage

1. Input your English question in the provided text box.
2. Click the "Ask me the question" button.
3. View the generated SQL query response.
