import os

from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

def get_chat_response(prompt, memory, openai_api_key, openai_api_base):
    model = ChatOpenAI(model="glm-3-turbo",openai_api_key= openai_api_key, openai_api_base = openai_api_base)
    chain = ConversationChain(llm = model, memory = memory)

    response = chain.invoke({"input":prompt})##这是一串字典
    return response["response"]##但是只用返回回应即可

# memory = ConversationBufferMemory(return_messages = True)
# # print(get_chat_response("牛顿提出过哪些有名的定律？",memory,os.getenv("OPENAI_API_KEY"),os.getenv("OPENAI_API_BASE")))
# # print(get_chat_response("我上一个问题是什么？",memory,os.getenv("OPENAI_API_KEY"),os.getenv("OPENAI_API_BASE")))