from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="tinyllama:latest")

for chunk in llm.stream("Explain what an LLM is in very simple words."):
    print(chunk, end="", flush=True)
print()