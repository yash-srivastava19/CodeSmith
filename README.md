# CodeSmith

**NEW** Check out the dpeloyed version [here](https://yash-srivastava19-codesmith.hf.space)

<img src="https://github.com/yash-srivastava19/CodeSmith/assets/85068689/642a45fb-12a3-47ee-8cb0-7b31dd58b83e" width="350" />

Attention - all programmers. There is a new product in town. Are you currently learning python programming, or preparing for programming competitions but don't have anyone to shoot ideas to? Worry not - I've developed CodeSmith - A ChatGPT inspired Chatbot which can double as a programming assistant. CodeSmith knows a lot about math, statistics, machine learning in Python, and can be a great asset to do programming with. Although the apllication is free and open source, it can handle some requests(not production level). Some advantages : 

- No calling of OpenAI API. Although OpenAI models are quite accurate for code generation, I know it's expensive, and most of us don't have access to it.
- No shady business. Your data is safe and secure, and your chats are safe in cloud.

**NOTE :** The code generated by CodeSmith might not be 100% accurate, and it might work worse for languages other than Python(as with other language models), so be careful of copying generating code. 

![Screenshot 2023-07-29 135700](https://github.com/yash-srivastava19/CodeSmith/assets/85068689/33ee9c04-751a-40bd-81c3-00fd6a48d39b)


![Screenshot 2023-07-29 135823](https://github.com/yash-srivastava19/CodeSmith/assets/85068689/0a48ef12-7c89-4ac8-9fe3-39da9cf69bf9)

## About CodeSmith - Technical
CodeSmith is an application made using Langchain, Chainlit and Cohere. A similar model of the application is deployed on Huggingface spaces, and can be embedded in any website or application.

The model used by CodeSmith is a Cohere Command model, which is fine tuned using the `data.txt` file in the repository. The file contains code examples from two sources, namely : 

- [CodeAlpaca-20K](https://huggingface.co/datasets/sahil2801/CodeAlpaca-20k) : Python examples from the training set were handpicked to be used for finetuning.
- [Project Euler Solution](https://github.com/nayuki/Project-Euler-solutions/tree/master/python) : A personal favourite website, the problems from project euler python folder in the repo were handpicked to be used for finetuning. 

The model was then sent for finetuning, and was accesable using an API. This custom model(`called code-gen-alpha`), was then wrapped in a Langchain custom LLM class, and used by the `LLMChain`(together with `PromptTemplate`) to be used by the Chainlit factory.

## Possible Expansion : 
I wanted to used Llama2, together with a the full version of CodeAlpaca-20K and ProjectEuler dataset for finetuning, and add support for RAG(or sources, possible bugs), but with low budget and computing power, it is very difficult. I tried using huggingface models as well(falcon-7b-instruct, and other chat versions of small models), but their speed was not good enough to be used in an application - so I went with Cohere.

The aim is to build upon this project, with more data and more computing power. Till anything significant comes up, I've decided that all of the data will be in Python prgramming language, but I'll let my future self decide on that. 

Also, if anyone is interested in providing some computing power, or helping in expanding the project, welp. 

## Credits
Lots of documentation, Coffee, Google Bard(for coming up with the name CodeSmith, amongst other valuable feedback). 
