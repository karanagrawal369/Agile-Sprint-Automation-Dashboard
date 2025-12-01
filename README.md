
# 🤖 Enterprise Agile Automation Agent (Kaggle Capstone)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-WebSockets-green)
![Architecture](https://img.shields.io/badge/Architecture-Multi--Agent-orange)

## 📖 Project Overview
This project is a submission for the **Google AI Agents Intensive Capstone**, specifically for the **Enterprise Agents** track. 

It demonstrates a **Multi-Agent System** designed to automate the handoff between QA teams (using Jira) and Development teams (using Zoho Projects). It features a real-time **Cyberpunk-style Dashboard** that visualizes the agents' "thought process" via WebSockets.

## ⚡ Key Features (Competition Criteria)
* **Multi-Agent Architecture:** Uses a Manager agent to orchestrate specialized sub-agents (Jira, Triage, Zoho, QA).
* **Sequential Logic:** Data flows structurally from ingestion -> filtering -> execution -> verification.
* **Observability:** Custom logging system that streams "Thoughts" vs "Actions" to a web UI.
* **Tool Use:** Custom async Python tools simulating API interactions with Jira and Zoho.
* **Session Management:** Maintains state context across the lifecycle of the request.

## 🛠️ Architecture
The workflow follows a strict enterprise logic:
1.  **Manager Agent:** Receives user intent.
2.  **Jira Agent:** Connects to issue tracking to fetch raw data.
3.  **Triage Agent:** Applies business logic (Filters only 'Critical/High' priority).
4.  **Zoho Agent:** Automates task creation in the project management tool.
5.  **QA Agent:** Verifies integrity (Input count == Output count).

## 📂 Project Structure
```text
KAGGLE_PROJECT/
├── agents/             # Specialized Agent Logic
│   ├── jira_agent.py
│   ├── triage_agent.py
│   ├── zoho_agent.py
│   └── ...
├── tools/              # Mock API Wrappers
├── templates/          # HTML/CSS Dashboard
├── main.py             # FastAPI Server & Entry Point
├── stream_logger.py    # WebSocket Log Bridge
└── session_service.py  # State Management
