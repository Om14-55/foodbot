from langchain_astradb import AstraDBVectorStore
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os
import pandas as pd
from foodbot.data_converter import dataconveter
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load environment variables
load_dotenv()

# Load API keys correctly
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")  # fixed
ASTRA_DB_KEYSPACE = os.getenv("ASTRA_DB_KEYSPACE")  # fixed

#  Use Gemini embeddings
# embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001", api_key=GOOGLE_API_KEY)


embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


def ingestdata(status=None):
    #  Use AstraDBVectorStore (not AstraDBByteStore)
    vstore = AstraDBVectorStore(
        embedding=embedding,
        collection_name="foodbot_db",
        api_endpoint=ASTRA_DB_API_ENDPOINT,
        token=ASTRA_DB_APPLICATION_TOKEN,
        namespace=ASTRA_DB_KEYSPACE,
    )

    # Data ingestion
    if status is None:
        docs = dataconveter()  # This should return a list of Document objects
        inserted_ids = vstore.add_documents(docs)
        return vstore, inserted_ids
    else:
        return vstore


if __name__ == '__main__':
    vstore, ingested_ids = ingestdata(None)
    if ingested_ids:
        print(f"\n Inserted {len(ingested_ids)} documents successfully!\n")

    #  Perform a similarity search query
    query = "egg greenchilly onion oil"
    results = vstore.similarity_search(query, k=3)

    for res in results:
        print(f" Recipe Name: {res.metadata.get('name', 'N/A')}")
        print(f" Ingredients Quantity: {res.metadata.get('ingredients_quantity', 'N/A')}")
        print(f" Instructions: {res.metadata.get('instructions', 'N/A')}")
        print("-" * 60)

