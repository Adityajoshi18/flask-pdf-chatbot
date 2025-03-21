from flask import Flask, request, jsonify
from utils import PDFChatBot

app = Flask(__name__)

# Initialize the PDFChatBot instance
pdf_chatbot = PDFChatBot()
pdf_chatbot.create_vector_db()

# Define route for handling queries
@app.route('/answer', methods=['POST'])
def answer_query():
    try:
        data = request.get_json()
        if not data or 'query' not in data:
            return jsonify({'error': 'Query parameter "query" missing in request body.'}), 400
        
        # Call search_similar_documents method of PDFChatBot
        response = pdf_chatbot.search_similar_documents(data['query'])
        return jsonify({'answer': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
