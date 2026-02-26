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
        return "File not found."

    docs = PyPDFLoader(path).load()

    full_report = ""
    for page in docs:
        content = page.page_content

 * Replace double line breaks
        while "\n\n" in content:
            content = content.replace("\n\n", "\n")

        full_report += content + "\n"

    return full_report
