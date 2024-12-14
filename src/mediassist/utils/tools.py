from crewai_tools import SerperDevTool, WebsiteSearchTool
from .environment import get_serper_api_key


def get_tools(language):
    search_tool = SerperDevTool(api_key=get_serper_api_key())
    web_rag_tool = WebsiteSearchTool(api_key=get_serper_api_key())

    if language == "en":
        return [search_tool, web_rag_tool]
    elif language == "ar":
        return [search_tool, web_rag_tool]
