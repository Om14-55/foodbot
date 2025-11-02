from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI
from foodbot.ingest import ingestdata
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def generation(vstore):
    retriever = vstore.as_retriever(search_kwargs={"k": 3})

    FOOD_BOT_TEMPLATE = """
    You are a Food Recipe Bot.
    You are an expert in suggesting recipes based on ingredients.
    You analyze recipe data to provide relevant recipe names, ingredient quantities, and instructions.
    Be clear, helpful, and accurate in your response.

    CONTEXT:
    {context}

    QUESTION: {question}

    YOUR ANSWER:
    """

    prompt = ChatPromptTemplate.from_template(FOOD_BOT_TEMPLATE)

    # Initialize Gemini model
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro", api_key=os.getenv("GOOGLE_API_KEY"))

    # Create the chain
    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain


if __name__ == "__main__":
    vstore, _ = ingestdata("done")  # unpack only the vstore
    chain = generation(vstore)
    query = "egg, green chili, onion, oil"
    response = chain.invoke(query)
    print("\n Suggested Recipe:\n", response)
