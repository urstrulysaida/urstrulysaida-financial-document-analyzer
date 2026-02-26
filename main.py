import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, LLM
from tools import FinancialDocumentTool

# ----- LLM -----
llm = LLM(
    model="gpt-4o-mini",
    temperature=0.2
)

# ----- Agents -----

financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="""
    Analyze financial documents accurately using provided data.
    Never invent facts.
    Base analysis only on document content.
    """,
    verbose=True,
    memory=True,
    backstory="""
    You are an experienced financial analyst focused on factual,
    evidence-based analysis and clear explanations.
    """,
    tools=[FinancialDocumentTool.read_data_tool],
    llm=llm,
    allow_delegation=False
)

verifier = Agent(
    role="Financial Document Verifier",
    goal="""
    Verify whether the uploaded file is a valid financial document.
    Reject unrelated files.
    """,
    verbose=True,
    memory=True,
    llm=llm,
    allow_delegation=False
)

risk_assessor = Agent(
    role="Risk Assessment Specialist",
    goal="""
    Identify realistic financial risks based on document data.
    Avoid exaggeration or speculation.
    """,
    verbose=True,
    memory=True,
    llm=llm,
    allow_delegation=False
)
