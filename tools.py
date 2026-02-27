import os
from dotenv import load_dotenv
from langchain.tools import tool
from langchain_community.document_loaders import PyPDFLoader

load_dotenv()


@tool("Read Financial Document")
def read_data_tool(path: str) -> str:
    """
    Read and return text from a PDF file.
    """

    if not os.path.exists(path):
        return "Error: File not found."

    try:
        docs = PyPDFLoader(path).load()

        if not docs:
            return "Error: PDF is empty or unreadable."

        full_report = ""

        for page in docs:
            content = page.page_content

            # Replace double line breaks
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")

            full_report += content + "\n"

        return full_report if full_report.strip() else "Error: No text extracted from PDF."

    except Exception as e:
        return f"Error reading PDF: {str(e)}"
