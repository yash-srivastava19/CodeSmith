import os
from langchain import PromptTemplate, Cohere, LLMChain
import chainlit as cl
from custom_llm import CustomLLM
os.environ["COHERE_API_KEY"] = "3FZy1Q1sd9Yfs289shdPgwjAt4MEuMxUmQx3oecK"

template = """Question: {question}

Answer: Let's think step by step."""


@cl.langchain_factory(use_async=False)
def factory():
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=CustomLLM(), verbose=True)

    return llm_chain


@cl.langchain_rename   # This will be particularly useful when we want to customize this thing for production.
def rename(orig_author):
    rename_dict = {
        'LLMChain': 'Scooby'
    }
    return rename_dict.get(orig_author, orig_author)


@cl.on_chat_start
async def main():
    await cl.Message(content="Welcome to Cranberry !! Let's start this").send()
