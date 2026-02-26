# 🚀 Financial Document Analyzer (CrewAI Debug Challenge)

## 📌 Project Overview

This project is an AI-powered **Financial Document Analysis System** built using **CrewAI**, **FastAPI**, and multi-agent orchestration.

The system accepts uploaded financial PDF documents and performs:

- Financial metric extraction
- Risk assessment
- Investment insight generation
- Structured analysis reporting

This project was developed as part of an **AI Internship Debug Assignment**, where the original codebase contained deterministic bugs and inefficient prompts that required debugging and optimization.

---

## 🧠 Key Features

### ✔ Multi-Agent AI Architecture

The system uses specialized AI agents:

| Agent | Responsibility |
|---|---|
| Financial Document Verifier | Validates uploaded documents |
| Financial Analyst | Extracts financial insights |
| Risk Assessor | Identifies realistic risks |
| Investment Insights Agent | Provides neutral insights |

---

### ✔ FastAPI Backend

- Upload financial PDFs
- Send analysis query
- Receive structured AI response

---

### ✔ CrewAI Orchestration

- Sequential / hierarchical task execution
- Agent collaboration
- Tool integration

---

### ✔ Queue Worker Model (Bonus)

- Celery + Redis support
- Concurrent request handling
- Scalable architecture

---

### ✔ Database Integration (Bonus)

- SQLite storage
- Saves:
  - filename
  - query
  - analysis result

---

## 🏗️ System Architecture

Client
↓
FastAPI API
↓
Queue Worker (Celery)
↓
CrewAI Orchestrator
↓
Specialized Agents
↓
Database Storage (SQLite)


---

## 🐛 Bugs Found & Fixes

### 1. Undefined LLM
**Issue:** LLM object was not initialized.  
**Fix:** Added CrewAI LLM configuration.

---

### 2. Incorrect Agent Parameter
**Issue:** `tool=` used instead of `tools=`.  
**Fix:** Updated to correct CrewAI syntax.

---

### 3. Missing PDF Loader
**Issue:** PDF reader not imported.  
**Fix:** Added `PyPDFLoader` for reliable PDF extraction.

---

### 4. Async Tool Misconfiguration
**Issue:** Async functions incompatible with CrewAI tools.  
**Fix:** Converted tools to synchronous functions.

---

### 5. File Path Not Passed
**Issue:** Uploaded file path ignored during analysis.  
**Fix:** Passed `file_path` into Crew kickoff context.

---

### 6. Unsafe / Inefficient Prompts
**Issue:** Prompts encouraged hallucinations and fake outputs.  
**Fix:** Rewritten prompts to enforce factual analysis.

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/financial-document-analyzer.git
cd financial-document-analyzer
```


2️⃣ Install Dependencies

pip install -r requirements.txt

▶️ Run Application

uvicorn main:app --reload

API will start at:

http://127.0.0.1:8000

📡 API Documentation

http://127.0.0.1:8000/docs

📂 API Endpoint

POST /analyze

| Field | Type   | Description        |
| ----- | ------ | ------------------ |
| file  | PDF    | Financial document |
| query | string | Analysis request   |


Example Response
```
code Js 

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

Celery

Redis

SQLite

PyPDF

###  🧪 Future Improvements

Agent memory sharing

Structured JSON outputs

Financial metric auto-tables

Streaming responses

Cloud deployment

###  👨‍💻 Assignment Goal

This project demonstrates:

Debugging skills

Prompt engineering optimization

Multi-agent AI system design

Backend API development

Scalable architecture thinking







