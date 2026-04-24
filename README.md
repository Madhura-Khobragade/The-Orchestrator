# 🛡️ Sovereign AI Orchestrator: Multi-Agent Privacy Shield

A "Local-First" AI Agent system built for high-security sectors (Banking, Healthcare) that performs complex data analysis without ever sending sensitive user data to a public cloud.

## 🚀 Project Overview
In 2026, data sovereignty is the top barrier to AI adoption in the EU. This project solves the "Privacy Paradox" by implementing a Multi-Agent system that resides entirely on local hardware using **Ollama** and **Llama 3.2**.

### Key Features:
* **Privacy-as-Code:** A dedicated "Privacy Auditor" agent uses NLP to redact PII (Personally Identifiable Information) before any output is displayed.
* **Explainable AI (XAI):** An "XAI Transparency" agent provides the legal and logical basis for every redaction, meeting **EU AI Act** standards.
* **Local-First Architecture:** Zero byte egress to the public cloud.
* **Product Strategy:** Includes a RICE prioritization matrix and GTM strategy for the German banking market.

## 🛠️ Tech Stack
* **Orchestration:** LangGraph (State Machine Agents)
* **LLM Engine:** Ollama (Llama 3.2 3B)
* **Frontend:** Streamlit
* **Language:** Python 3.10+

## 📂 Project Structure
* `orchestrator.py`: The core agent logic and graph definition.
* `app.py`: The Streamlit dashboard and PM documentation layer.
* `requirements.txt`: Project dependencies.

## ⚙️ Installation & Execution

1.  **Install Ollama:** [ollama.com](https://ollama.com/)
2.  **Pull the Model:**
    ```bash
    ollama pull llama3.2
    ```
3.  **Clone & Install Dependencies:**
    ```bash
    pip install langgraph langchain_community ollama streamlit
    ```
4.  **Run the Application:**
    ```bash
    streamlit run app.py
    ```

## 📊 PM Vision (2026)
This project is designed as a **High-Risk AI System** compliant with Article 13 of the EU AI Act. By prioritizing **Data Minimization (GDPR Art. 5)** over cloud-scale latency, it achieves a high RICE score for enterprise security adoption.

---
**Developed by:** Madhura Santosh Khobragade