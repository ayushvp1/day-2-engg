import os

def load_documents():
    documents = {}
    base_path = "knowledge_base"

    if not os.path.exists(base_path):
        base_path = os.path.join(os.path.dirname(__file__), "knowledge_base")

    for file in os.listdir(base_path):
        with open(os.path.join(base_path, file), "r", encoding="utf-8") as f:
            documents[file] = f.read()

    return documents


def retrieve_context(question, documents):
    STOP_WORDS = {"what", "is", "are", "the", "a", "an", "and", "or", "in", "on", "of", "to", "for", "with", "about", "it", "how", "me", "tell", "explain"}

    question_lower = question.lower()
    keywords = [word for word in question_lower.split() if word not in STOP_WORDS and len(word) > 1]

    if not keywords:
        keywords = question_lower.split()

    scored_docs = []

    for name, content in documents.items():
        content_lower = content.lower()
        score = sum(1 for keyword in keywords if keyword in content_lower)

        if score > 0:
            scored_docs.append((score, content))

    scored_docs.sort(key=lambda x: x[0], reverse=True)

    if not scored_docs:
        return "No relevant context found."

    top_contexts = [doc[1] for doc in scored_docs[:2]]
    return "\n\n---\n\n".join(top_contexts)
