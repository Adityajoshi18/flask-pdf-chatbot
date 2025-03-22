# AI-Powered PDF Chatbot

This project is a Flask-based AI chatbot that processes PDF documents, extracts relevant information using FAISS vector search, and generates responses using LLaMA-2. The chatbot uses Hugging Face embeddings and LangChain to retrieve and answer user queries based on the PDF content.

## Features

- Upload and process PDF documents for information retrieval
- Query the chatbot for contextual answers based on PDF content
- Uses FAISS vector database for efficient similarity search
- LLaMA-2 integrated for generating relevant responses
- API-based architecture for seamless integration

## Tech Stack

- **Backend**: Flask, Python
- **Machine Learning/NLP**: LLaMA-2, Hugging Face Embeddings, LangChain
- **Vector Search**: FAISS
- **Document Processing**: PyPDFLoader
- **API Testing**: Requests

## Installation & Setup

1. **Clone the Repository**

```bash
   git clone git@github.com:Adityajoshi18/flask-pdf-chatbot.git
   cd <your-project-folder>
```

2. **Create a Virtual Environment**

```bash
   python -m venv env
   source env/bin/activate   # For macOS/Linux
   env\Scripts\activate      # For Windows
```

3. **Install Dependencies** 

```bash
   pip install -r requirements.txt
```

4. **Run the Application**

```bash
   cd bot/src
   python app.py
```

The Flask app will start at http://localhost:5000/.

## Testing the API

Run the test script:

```bash
   python test_api.py
```

## Contributing

Feel free to fork the repository, create a branch, and submit a pull request.
