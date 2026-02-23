from retriever import load_documents, retrieve_context
from agent_layer import build_agent_prompt
from llm_layer import generate_response

def run_pipeline(question):

    documents = load_documents()
    context = retrieve_context(question, documents)

    agent_prompt = build_agent_prompt(context, question)

    response = generate_response(agent_prompt)

    return response
