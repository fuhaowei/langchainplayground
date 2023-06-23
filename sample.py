import os
import getpass

from langchain.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI

def run(query):
    llm = OpenAI(batch_size=5, temperature=0)

    # loading documents
    loader = PyPDFLoader("filenamehere.pdf")
    pages = loader.load_and_split()

    faiss_index = FAISS.from_documents(pages, OpenAIEmbeddings())
    docs = faiss_index.similarity_search(query, k=2)
    
    chain = load_qa_chain(llm, chain_type="stuff")
    print(chain.run(input_documents=docs, question=query))

if __name__ == "__main__":
    while True:
        query = input('Please provide your query (type "exit" to stop): ')
        if query.lower() == 'exit':
            break
        run(query)