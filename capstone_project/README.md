# 🌟 Capstone Project: Domain-Specific GenAI Assistant

A working AI Assistant prototype featuring **RAG + Agent + Evaluation Framework**.

## 🏗 Architecture

```
User Input → Input Layer → Retriever (RAG) → Agent Reasoning → LLM → Evaluation → Final Output
```

## 🧠 Domain Options

- 🎓 Academic Assistant
- 💼 Placement AI Assistant
- 📄 Research Paper Explainer
- 💻 Coding Debug Assistant
- 🚀 Startup Idea Evaluator

## Setup

1. Copy `.env.example` to `.env` and add your Groq API key.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your domain-specific documents to `knowledge_base/`.
4. Run:
   ```bash
   python main.py
   ```

## Structure

| File | Purpose |
|------|---------|
| `input_layer.py` | Handles user input |
| `retriever.py` | RAG — loads docs & retrieves relevant context |
| `agent_layer.py` | Structures reasoning with step-by-step prompts |
| `llm_layer.py` | LLM interaction via Groq + LiteLLM |
| `evaluation_layer.py` | Self-evaluation of output quality |
| `pipeline.py` | Orchestrates the full RAG → Agent → LLM flow |
| `main.py` | CLI entry point |
| `knowledge_base/` | Domain documents for retrieval |
