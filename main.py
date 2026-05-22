import os
os.environ["OPENAI_API_KEY"] = 'Enter Your API Key'

'pip install -q langchain-openai langchain-community langchain-core requests duckduckgo-search --> install in your system using terminal'

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
import requests
from langchain_community.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()             '--> DuckDuckGo is a prebuilt tool for websearch'

  'This is a custom tool that we have built for are use using tool decorator'

@tool
def get_weather_data(city: str) -> str:
  
  "This function fetches the current weather data for a given city"
  
url = f'https://api.weatherstack.com/current?access_key=4d1d8ae207a8c845a52df8a67bf3623e&query={city}'
response = requests.get(url)
return response.json()

llm = ChatOpenAI()        '--> tell your code that this llm models we are using currently i am using ChatOpenAI you can use your own model'

from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

'Step 2: Pull the ReAct prompt from LangChain Hub'

prompt = hub.pull("hwchase17/react")  '--> pulls the standard ReAct agent prompt'

'Step 3: Create the ReAct agent manually with the pulled prompt'

agent = create_react_agent(
    llm=llm,               #--> llm that we have created on line 23
    tools=[search_tool, get_weather_data],     #--> tool that we have created at line 10 and 15
    prompt=prompt      #--> prompt will be automatically fetch from line 30
)

' Step 4: Wrap it with AgentExecutor '

agent_executor = AgentExecutor(
    agent=agent,              #--> agent that we have made on line 34
    tools=[search_tool, get_weather_data],
    verbose=True             #--> help us to see what is are chatbot thinking and doing. What action he is thinking of.
)

'Step 5: Invoke'

response = agent_executor.invoke({"input": "Find the capital of INDIA, then find it's current weather condition"})
print(response)

"the list of action will be printed and final output will be printed"

response['output']    '--> to get only desire output not all the unnecessary output'





