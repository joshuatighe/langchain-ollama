from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="tinyllama:latest")

prompt = PromptTemplate.from_template(
    "You are a tutor. Explain {topic} in 3 short bullet points."
)

chain = prompt | llm | StrOutputParser()

print(chain.invoke({"topic": "embeddings"}))