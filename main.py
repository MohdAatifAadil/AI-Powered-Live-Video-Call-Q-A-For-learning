import time
from scraper import scrape_and_store
from qa_model import get_answer

def main():
    # Run the scraper and QA system simultaneously
    while True:
        # Scrape new content every 10 minutes
        scrape_and_store()

        # Ask a question and get an answer
        question = input("Ask your question: ")
        answer = get_answer(question)
        print(f"Answer: {answer}")

        # Wait for some time before asking another question or scraping again
        time.sleep(10)  # You can adjust the delay time

if __name__ == "__main__":
    main()
