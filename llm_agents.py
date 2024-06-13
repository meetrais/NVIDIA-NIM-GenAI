from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
import os

def get_llm_agent_response(user_text, model, temperature):
    #NVIDIA_API_KEY = os.environ.get("NVIDIA_API_KEY")
    NGC_API_KEY = os.environ.get("NGC_API_KEY")
    NGC_BASE_URL = "https://integrate.api.nvidia.com/v1"
    #NGC_MODEL = "meta/llama3-70b-instruct"
    NGC_MODEL = model
    
    llm = ChatOpenAI(temperature=temperature,
                    base_url = NGC_BASE_URL,
                    api_key = NGC_API_KEY,
                    model= NGC_MODEL)

    tools = [TavilySearchResults(max_results=1)]
    prompt = ChatPromptTemplate.from_messages(
        [
            (
            "system",
            "You are a helpful assistant. If you dont have exact answer then use TavilySearchResults tool.",
            ),
            ("placeholder", "{chat_history}"),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
        ]
    )

    # Construct the Tools agent
    agent = create_tool_calling_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    response = agent_executor.invoke({"input": user_text})
    
    return response["output"]