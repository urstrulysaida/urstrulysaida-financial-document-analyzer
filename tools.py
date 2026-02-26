import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from crewai_tools import SerperDevTool

# Web search tool (optional)
search_tool = SerperDevTool()


class FinancialDocumentTool:

    @staticmethod
    def read_data_tool(path="data/sample.pdf"):
        """
        Read and return text from PDF.
        """
        if not os.path.exists(path):
            return "File not found."

        docs = PyPDFLoader(path).load()

        full_report = ""
        for page in docs:
            content = page.page_content

            while "\n\n" in content:
                content = content.replace("\n\n", "\n")

            full_report += content + "\n"

        return full_report
