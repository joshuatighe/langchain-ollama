from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="tinyllama:latest")

prompt = PromptTemplate.from_template(
    "Explain {topic} in simple words and give one example."
)

text = prompt.format(topic="vector databases")
print(llm.invoke(text))