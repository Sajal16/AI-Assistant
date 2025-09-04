# 📖 README – AI Assistant (CLI with Ollama)

## 🔹 Project Overview
This project is a **Command-Line AI Assistant** built with Python and Ollama.  
It allows users to interact with an AI model (LLaMA2 or compatible) and perform the following functions:
1. **Answer Questions**  
2. **Summarize Text**  
3. **Generate Creative Content**  
4. **Exit the Assistant**

The assistant also includes:
- **Loading animation** while AI is generating a response  
- **Feedback mechanism** (users can rate if a response was helpful)  
- **Feedback log storage** in `feedback_log.txt` for later analysis  

---

## 🔹 Requirements
- **Python 3.9+** installed  
- **Ollama** installed and added to system PATH → [Download Ollama](https://ollama.ai/download)  
- A compatible **local AI model** (e.g., `llama2`) pulled using:  
  ```bash
  ollama pull llama2
  ```

---

## 🔹 How to Run
1. Open a terminal in the project folder.  
2. Run the program with:
   ```bash
   python app.py
   ```
3. The main menu will appear:
   ```
   Welcome to your AI Assistant!
   1. Answer Questions
   2. Summarize Text
   3. Generate Creative Content
   4. Exit
   ```
4. Enter the number for your desired function and follow the prompts.  

---

## 🔹 Features
- **Answer Questions** – Ask factual or general questions.  
- **Summarize Text** – Paste or type long text, get a concise summary.  
- **Creative Content** – Generate poems, stories, essays, etc.  
- **Feedback Logging** – After each response, you can type `yes` or `no` to log feedback in `feedback_log.txt`.  

---

## 🔹 Example Usage
```
Select an option: 1
Enter your question: What is the capital of France?

🤖 AI Response:
Paris

Was this helpful? (yes/no): yes
👉 Press Enter to return to menu...
```

---

## 🔹 Output Files
- **feedback_log.txt** → Stores user queries, AI responses, and feedback (yes/no).  

---

## 🔹 Exit
Select option `4` from the menu to exit the assistant.  

---

✨ Congratulations! You now have your own **offline AI Assistant** powered by Ollama 🎉  
