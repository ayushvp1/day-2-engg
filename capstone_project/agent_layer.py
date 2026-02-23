def build_agent_prompt(context, question):

    return f"""
You are a Domain-Specific AI Assistant.

Step 1: Analyze the question.
Step 2: Use retrieved context.
Step 3: Provide structured response.

Context:
{context}

Question:
{question}

Provide:
- Explanation
- Example
- Key Insights
- Final Recommendation
"""
