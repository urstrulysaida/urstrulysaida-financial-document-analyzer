# 🚀 Financial Document Analyzer (CrewAI Debug Challenge)

## 📌 Project Overview

This project is an AI-powered **Financial Document Analysis System** built using **CrewAI** and **FastAPI**.

The system allows users to upload financial PDF documents and performs:

- Financial metric extraction
- Financial health summarization
- Risk analysis
- Neutral investment insights
- Structured analysis reporting

This project was developed as part of an **AI Internship Debug Assignment**, where the original codebase contained deterministic bugs and inefficient prompts that were identified and fixed.

---

## 🧠 Key Features

### ✔ AI Agent Architecture

The system uses specialized CrewAI agents:

| Agent | Responsibility |
|---|---|
| Financial Analyst | Extracts financial insights from documents |
| Document Verifier | Validates financial document relevance |
| Risk Assessor | Identifies realistic financial risks |

---

### ✔ FastAPI Backend

- Upload financial PDFs
- Submit analysis query
- Receive structured AI-generated analysis

---

### ✔ CrewAI Orchestration

- Task-based agent execution
- Tool integration (PDF reader)
- Structured output generation

---

## 🏗️ System Architecture
```
Client
↓
FastAPI API
↓
CrewAI Orchestrator
↓
AI Agents
↓
PDF Processing Tool
↓
Structured Analysis Output
```

---

## 🐛 Bugs Found & Fixes

### 1️⃣ Undefined LLM Initialization
**Issue:** LLM object was not defined.  
**Fix:** Added proper CrewAI LLM initialization.

---

### 2️⃣ Incorrect Agent Parameter
**Issue:** `tool=` used instead of `tools=`.  
**Fix:** Updated to correct CrewAI syntax.

---

### 3️⃣ Missing PDF Loader
**Issue:** PDF loader was not imported.  
**Fix:** Added `PyPDFLoader` for reliable PDF parsing.

---

### 4️⃣ Async Tool Misconfiguration
**Issue:** Async tool incompatible with CrewAI execution.  
**Fix:** Converted tools to synchronous functions.

---

### 5️⃣ File Path Not Passed
**Issue:** Uploaded file path was ignored during analysis.  
**Fix:** Passed `file_path` into Crew kickoff context.

---

### 6️⃣ Inefficient / Unsafe Prompts
**Issue:** Prompts encouraged hallucinated outputs.  
**Fix:** Rewritten prompts to enforce factual, document-based analysis.

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/urstrulysaida/urstrulysaida-financial-document-analyzer.git
```

## 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```
## ▶️ Run Application

```
uvicorn main:app --reload
```
#### API will start at:

```
http://127.0.0.1:8000
```

## 📡 API Documentation

FastAPI automatically generates interactive docs:

```
http://127.0.0.1:8000/docs
```

## 📂 API Endpoint
POST /analyze

| Field | Type   | Description        |
| ----- | ------ | ------------------ |
| file  | PDF    | Financial document |
| query | string | Analysis request   |

#### Example Response

```json
{
  "status": "success",
  "query": "Analyze this financial document",
  "analysis": "Structured financial report...",
  "file_processed": "report.pdf"
}
```

### 🧩 Tech Stack

Python

FastAPI

CrewAI

LangChain

PyPDF

Pandas

NumPy

### 📁 Project Structure
```
financial-document-analyzer/
│
├── agents.py
├── main.py
├── task.py
├── tools.py
├── requirements.txt
├── README.md
│
└── data/
    ├── sample.pdf
    └── .gitkeep
```

### 🧪 Future Improvements

Multi-agent parallel execution

Structured JSON outputs

Database storage for analysis history

Queue-based async processing

Cloud deployment

### 👨‍💻 Assignment Goal

This project demonstrates:

Debugging and bug fixing

Prompt engineering improvements

AI agent orchestration

Backend API development

Clean software design practices

### 📄 License

This project is created for educational and internship evaluation purposes.

---


## 🧪 Quick Test

After starting the server, open:

http://127.0.0.1:8000/docs



Upload a PDF and verify the analysis response.

