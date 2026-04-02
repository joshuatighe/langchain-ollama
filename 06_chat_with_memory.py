from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="tinyllama:latest")

history = []

SYSTEM = "You are a helpful tutor. Keep answers short and simple."

while True:
    user_msg = input("You: ").strip()
    if user_msg == "-1":
        print("Bye!")
        break

    history.append(f"User: {user_msg}")
    prompt = SYSTEM + "\n\n" + "\n".join(history) + "\nAssistant:"
    ai_msg = llm.invoke(prompt)

    history.append(f"Assistant: {ai_msg}")
    print("AI:", ai_msg)