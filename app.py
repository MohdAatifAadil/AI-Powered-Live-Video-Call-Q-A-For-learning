from flask import Flask, request, jsonify
from pymongo import MongoClient
from transformers import pipeline
from scraper import scrape_content

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["ai_learning_db"]

# Initialize the QA model
qa_model = pipeline("question-answering")

@app.route("/ask", methods=["POST"])
def ask_question():
    question = request.json.get("question")
    
    # Get content from the database
    context_docs = db.content.find()  # Gather all context docs
    context = " ".join([doc['content'] for doc in context_docs])

    # Answer the question based on the context
    answer = qa_model(question=question, context=context)
    db.qa_pairs.insert_one({"question": question, "answer": answer['answer']})
    
    return jsonify({"answer": answer['answer']})

@app.route("/scrape", methods=["GET"])
def scrape():
    scrape_content()
    return jsonify({"status": "Content scraped and stored"})

if __name__ == "__main__":
    app.run(debug=True)
