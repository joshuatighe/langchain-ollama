from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="tinyllama:latest")

context = """
LangChain is a Python library for building applications with LLMs.
LCEL is a modern way to create chains using the pipe operator.
Ollama lets you run models locally, like tinyllama.
""".strip()


prompt = PromptTemplate.from_template(
    """Answer the question using ONLY the context.

Context:
{context}

Question: {question}

If the answer is not in the context, say: "I don't know."
"""
)

question = "What is LCEL?"
final_prompt = prompt.format(context=context, question=question)

print(llm.invoke(final_prompt))