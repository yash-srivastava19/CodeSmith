from langchain import PromptTemplate, LLMChain
import chainlit as cl
from custom_llm import CustomLLM
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
)

template = """ Write a code for the following problem :
{question} 

Code:
"""


@cl.on_chat_start
def factory():
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    prompt = ChatPromptTemplate.from_messages([system_message_prompt])
    llm = CustomLLM()

    llm_chain = LLMChain(prompt=prompt, llm=llm, verbose=True,)

    cl.user_session.set("llm_chain", llm_chain)



@cl.on_message
async def main(message):
    llm_chain = cl.user_session.get("llm_chain")

    res = await llm_chain.acall(message, callbacks=[cl.AsyncLangchainCallbackHandler()])

    await cl.Message(content=res["text"]).send()



@cl.author_rename   # This will be particularly useful when we want to customize this thing for production.
def rename(orig_author):
    rename_dict = {
        'LLMChain': 'Scooby'
    }
    return rename_dict.get(orig_author, orig_author)
