from openai import OpenAI
import os 

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_ai(question, context):

    prompt = f"""
Use this web information to answer the question.

Context:
{context}

Question:
{question}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text