from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid

from crewai import Crew, Process
from agents import financial_analyst
from task import analyze_financial_document

app = FastAPI(title="Financial Document Analyzer")


def run_crew(query: str, file_path: str):
    financial_crew = Crew(
        agents=[financial_analyst],
        tasks=[analyze_financial_document],
        process=Process.sequential,
    )

    result = financial_crew.kickoff({
        "query": query,
        "file_path": file_path
    })

    return result


@app.get("/")
async def root():
    return {"message": "Financial Document Analyzer API running"}


@app.post("/analyze")
async def analyze(
    file: UploadFile = File(...),
    query: str = Form(default="Analyze this financial document")
):

    file_id = str(uuid.uuid4())
    file_path = f"data/{file_id}.pdf"

    try:
        os.makedirs("data", exist_ok=True)

        with open(file_path, "wb") as f:
            f.write(await file.read())

        if not query.strip():
            query = "Analyze this financial document"

        response = run_crew(query, file_path)

        return {
            "status": "success",
            "query": query,
            "analysis": str(response),
            "file_processed": file.filename
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
