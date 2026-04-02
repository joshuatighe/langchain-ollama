from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="tinyllama:latest")

answer = llm.invoke("Say hello in one short sentence.")
print(answer)