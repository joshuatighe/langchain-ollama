from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="tinyllama:latest")

while True:
    q = input("You: ").strip()

    if q == "-1":
        print("Bye!")
        break

    print("AI:", llm.invoke(q))