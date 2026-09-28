# 🧠 RecallDesk

## Persistent Support & Incident Intelligence

RecallDesk is an AI-powered customer support assistant that remembers previous customer interactions and uses that context to provide more relevant, continuous, and intelligent support.

Instead of treating every customer message as a completely new conversation, RecallDesk retrieves relevant historical interactions and gives that context to an AI support agent before generating a response.

---

## 🚨 Problem

Traditional customer support systems often lose context between interactions.

When a customer reports the same issue again, support representatives may have to:

- Search through previous conversations
- Ask the customer the same questions again
- Repeat troubleshooting steps
- Determine what solutions were already attempted
- Manually reconstruct the history of an incident

This creates unnecessary work for support teams and can lead to a frustrating customer experience.

---

## 💡 Our Solution

RecallDesk combines **persistent memory** with an **AI customer support agent**.

When a customer sends a message, RecallDesk:

1. Identifies the customer and current issue.
2. Searches persistent memory for relevant previous interactions.
3. Retrieves previous troubleshooting information.
4. Provides the relevant history to the AI agent.
5. Generates a context-aware response.
6. Stores the new interaction for future conversations.

This allows the system to continuously learn from previous support interactions.

---

## 🧠 Key Idea

> RecallDesk doesn't just answer the current question — it remembers what happened before.

For example:

A customer previously reported:

> "The dashboard freezes when uploading large CSV files."

The support team already tried:

- Clearing the browser cache
- Reducing the file size

The customer later returns and says:

> "I'm still having the dashboard freezing problem."

Instead of starting from scratch, RecallDesk retrieves the previous interaction and can respond with the next appropriate troubleshooting steps.

---

# ✨ Features

### 🧠 Persistent Memory

RecallDesk stores previous customer interactions using Hindsight so that important context can be retrieved later.

### 🔎 Relevant Memory Retrieval

The system searches stored customer interactions and retrieves information relevant to the current issue.

### 🤖 Context-Aware AI Support

The retrieved history is provided to the AI agent before it generates a response.

### 🔄 Continuous Learning From Interactions

New customer messages and generated responses are stored back into memory.

### 🛠️ Previous Troubleshooting Awareness

The AI can recognize troubleshooting steps that were already attempted and avoid unnecessarily repeating them.

### 💬 Simple Support Interface

A Streamlit interface allows a support representative to enter:

- Customer name
- Customer message

and receive:

- Retrieved customer history
- AI-generated support response

---

# 🏗️ How It Works

```text
                    ┌───────────────────┐
                    │     Customer      │
                    │      Message      │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │    Streamlit UI   │
                    │      app.py       │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │   Hindsight       │
                    │ Memory Retrieval  │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Relevant Customer │
                    │     History       │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │    AI Agent       │
                    │     agent.py      │
                    │                   │
                    │      Groq         │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Context-Aware     │
                    │     Response      │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Store Interaction │
                    │    in Hindsight   │
                    └───────────────────┘



---

# 🛠️ Tech Stack

- **Python** — Core application logic
- **Streamlit** — Web interface
- **Hindsight** — Persistent AI memory
- **Groq** — LLM inference
- **GPT-OSS-120B** — AI response generation
- **python-dotenv** — Environment variable management
- **Git & GitHub** — Version control

---

# 📁 Project Structure

```text
RecallDesk/
│
├── app.py              # Streamlit web application
├── agent.py            # AI customer support agent
├── memory.py           # Hindsight memory integration
├── test_agent.py       # Agent testing
├── test_memory.py      # Memory testing
├── requirements.txt    # Python dependencies
├── run_app.bat         # Windows application launcher
├── .gitignore          # Files excluded from Git
└── README.md           # Project documentation
