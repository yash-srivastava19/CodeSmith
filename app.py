# This will be the classic gradio application with threading done. All I need to do is to wrap a custom LLM around it, and then use it however I want.

import os
from typing import Optional, Tuple

import gradio as gr
from langchain.chains import ConversationChain
from langchain.llms import Cohere   # Instead of this, I'll use my custom LLM wrapper.
from threading import Lock


def load_chain():
    """Logic for loading the chain you want to use should go here."""
    
    llm = Cohere(temperature=0)
    chain = ConversationChain(llm=llm)
    
    return chain


def set_cohere_api_key(api_key: str):
    """Set the api key and return chain.
    If no api_key, then None is returned.
    """
    if api_key:
        os.environ["COHERE_API_KEY"] = api_key
        chain = load_chain()
        os.environ["COHERE_API_KEY"] = ""
        
        return chain

class ChatWrapper:

    def __init__(self):
        self.lock = Lock()   # Threading makes our thing a lot easier. UI and logic should run on different threads.
    def __call__(self, api_key: str, inp: str, history: Optional[Tuple[str, str]], chain: Optional[ConversationChain]):
        """Execute the chat functionality."""
        
        self.lock.acquire()
        
        try:
            history = history or []
            # If chain is None, that is because no API key was provided.
            if chain is None:
                history.append((inp, "Please paste your Cohere key to use"))
                return history, history
            
            # Set Cohere key
            import cohere
            cohere.Client(api_key)   # See, this could a bottleneck.
            
            # Run chain and append input.
            output = chain.run(input=inp)
            history.append((inp, output))
            
        except Exception as e:
            raise e
        finally:
            self.lock.release()
        
        return history, history

chat = ChatWrapper()

block = gr.Blocks(gr.themes.Monochrome())


with block:
    with gr.Row():
        gr.Markdown("<h3><center>LangChain Demo</center></h3>")

        cohere_api_key_textbox = gr.Textbox(
            placeholder="Paste your Cohere API key ",
            show_label=False,
            lines=1,
            type="password",
        )

    chatbot = gr.Chatbot()

    with gr.Row():
        message = gr.Textbox(
            label="What's your question?",
            placeholder="What's the answer to life, the universe, and everything?",
            lines=1,
        )
        submit = gr.Button(value="Send", variant="secondary").style(full_width=False)

    gr.Examples(
        examples=[
            "Hi! How's it going?",
            "What should I do tonight?",
            "Whats 2 + 2?",
        ],
        inputs=message,
    )

    state = gr.State()
    agent_state = gr.State()

    submit.click(chat, inputs=[cohere_api_key_textbox, message, state, agent_state], outputs=[chatbot, state])
    message.submit(chat, inputs=[cohere_api_key_textbox, message, state, agent_state], outputs=[chatbot, state])

    cohere_api_key_textbox.change(
        set_cohere_api_key,
        inputs=[cohere_api_key_textbox],
        outputs=[agent_state],
    )

block.launch(debug=True)
