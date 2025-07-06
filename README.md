

# 🧠 WhatsApp Personal Assistant using Ollama on Raspberry Pi

This project is a private, local LLM-powered WhatsApp assistant that runs entirely on a Raspberry Pi using [Ollama](https://ollama.com) for language model inference. It uses `whatsapp-web.js` to receive and send messages, and a Python backend powered by Flask to interface with the local LLM.

## ✨ Features

- Responds only when tagged using `@ollama` in a WhatsApp message.
- Supports both individual and group chats.
- Handles and processes image/files (sent as base64) along with messages.
- Uses local LLM (e.g. LLaMA3) via Ollama — no cloud API or internet dependency.
- Fully customizable assistant prompt.
- Runs on Raspberry Pi or any local server.

## 🧰 Technologies Used

- [Ollama](https://ollama.com) (local LLM runtime)
- Python (Flask API backend)
- Node.js (`whatsapp-web.js` for WhatsApp connectivity)
- Raspberry Pi (or any Linux server)

## ⚙️ Installation & Setup

### 1. Install Ollama and run a model
```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3
ollama run llama3
```

### 2. Setup Python Backend
```bash
pip install flask requests
python3 bot.py
```

### 3. Setup WhatsApp Bridge
```bash
npm install
node whatsapp-bridge.js
```

Scan the QR code from your WhatsApp and you're live!

## 📂 File Structure

```
├── bot.py                # Python Flask backend
├── whatsapp-bridge.js    # WhatsApp bridge using whatsapp-web.js
├── readme.md             # Project documentation
└── ...
```

## 🧪 Example Usage

**User Message:**  
`@ollama What's the weather like on Mars?`  

**Bot Response:**  
> The weather on Mars is extremely cold with average temperatures around -80°F (-62°C). Dust storms are also common. Let me know if you want more on that! 😊

## 🔐 Privacy & Security

- All processing happens locally on your Raspberry Pi.
- No third-party servers or APIs are involved.
- Media files are processed only when tagged and never stored.

## 🚀 Roadmap

- [ ] OCR for image-based queries
- [ ] PDF summarization
- [ ] Telegram and Signal integration
- [ ] Voice-to-text support

## 📬 Connect

If you’d like to replicate this or have ideas to improve it, feel free to connect or drop a message!

---

Made with ❤️ and a Raspberry Pi.