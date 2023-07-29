# Write all of those here.# Contains main driver code for the Chainlit to work.

from langchain import PromptTemplate, Cohere, LLMChain
import chainlit as cl

from custom_llm import CodeGenAlpha

template = """ Write a code for the following problem :
{question} 

Code:
"""

@cl.langchain_factory(use_async=False)
def factory():
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=CodeGenAlpha(), verbose=True)

    return llm_chain


@cl.langchain_rename   # This will be particularly useful when we want to customize this thing for production.
def rename(orig_author):
    rename_dict = {
        'LLMChain': 'Scooby'   # Scooby is a great name for the LLM Chain !!
    }
    return rename_dict.get(orig_author, orig_author)


@cl.on_chat_start
async def main():
    await cl.Message(content="Welcome to Cranberry !! Let's start this").send()
