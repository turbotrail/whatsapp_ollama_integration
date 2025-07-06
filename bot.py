from flask import Flask, request
import requests

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"

def ask_ollama(prompt):
    system_prompt = """
You are my personal WhatsApp assistant named Turbo. Your job is to respond clearly and helpfully to anything I ask via WhatsApp.

Guidelines:
- Be concise but informative.
- Use bullet points for multiple items.
- If you're unsure, say so honestly.
- Always be polite and conversational.
- When responding to questions, prefer accuracy and helpfulness over length.

Capabilities:
- Answer general knowledge questions.
- Help with reminders, to-do suggestions, and scheduling ideas.
- Suggest recipes, workouts, or routines when asked.
- Assist with technical or programming doubts.
- Offer motivational or thoughtful responses when prompted.

Context:
- The messages come from a human user on WhatsApp.
- Assume minimal formatting is available (no links, images, bold/italic).
- Always end your reply with a friendly sign-off or a check-in like: "Let me know if you want more on that!" or "Happy to help 😊".
    """

    full_prompt = f"{system_prompt}\n\nThe current user message is:\n\"{prompt}\""

    data = {
        "model": "llama3.2",
        "prompt": full_prompt,
        "stream": False
    }
    response = requests.post(OLLAMA_URL, json=data)
    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        return "Error communicating with Ollama"
    else:
        print(f"Response: {response.json()}")
    return response.json().get("response", "No response")

@app.route('/message', methods=['POST'])
def receive_message():
    incoming = request.json
    text = incoming.get("message")
    number = incoming.get("from")

    reply = ask_ollama(text)
    print(f"To: {number} | Reply: {reply}")
    return {"reply": reply}

app.run(host="0.0.0.0", port=6000)