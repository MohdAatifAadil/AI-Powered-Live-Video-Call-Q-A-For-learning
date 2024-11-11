from transformers import pipeline
from pymongo import MongoClient

# Load pre-trained question-answering model from Hugging Face
qa_pipeline = pipeline("question-answering")

# Connect to MongoDB to fetch stored content
client = MongoClient('mongodb://localhost:27017/')
db = client['ai_learning']
collection = db['scraped_content']

def get_answer(question):
    # Fetch the most recent scraped content
    latest_content = collection.find().sort("timestamp", -1).limit(1)[0]['content']
    
    # Answer the question using the QA model
    result = qa_pipeline(question=question, context=latest_content)
    return result['answer']

# Test answering a question
if __name__ == "__main__":
    question = input("Ask your question: ")
    answer = get_answer(question)
    print(f"Answer: {answer}")
