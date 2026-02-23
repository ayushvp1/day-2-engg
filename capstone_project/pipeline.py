from retriever import load_documents, retrieve_context
from agent_layer import build_agent_prompt
from llm_layer import generate_response

def run_pipeline(question):

    documents = load_documents()
    context = retrieve_context(question, documents)

    # Guardrail: Don't call LLM if no relevant context found
    if context == "No relevant context found.":
        return "❌ Sorry, this question is outside my domain knowledge. Please ask something related to the available knowledge base."

    agent_prompt = build_agent_prompt(context, question)

    response = generate_response(agent_prompt)

    return response
