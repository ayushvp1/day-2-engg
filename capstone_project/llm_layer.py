import os
from dotenv import load_dotenv
from litellm import completion

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME", "groq/llama-3.1-8b-instant")

SYSTEM_PROMPT = """
Be precise and domain-aware.
If context does not contain answer, say:
'Insufficient domain knowledge.'
"""

def generate_response(prompt):

    response = completion(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=1000
    )

    return response["choices"][0]["message"]["content"]
