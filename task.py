from crewai import Task
from agents import financial_analyst
from tools import FinancialDocumentTool

analyze_financial_document = Task(
    description="""
    Analyze the financial document located at {file_path}.

    User query: {query}

    Steps:
    1. Extract key financial metrics.
    2. Summarize company financial health.
    3. Identify risks.
    4. Provide neutral investment insights.
    """,

    expected_output="""
    Structured report:

    - Executive Summary
    - Key Financial Metrics
    - Risk Analysis
    - Market Insights
    - Final Conclusion (non-financial-advice disclaimer)
    """,

    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)
