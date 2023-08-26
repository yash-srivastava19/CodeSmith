## Initial Motivation

Programming is an easy skill to acquire, but being a good programmer is very difficult. Being a person who is very much interested in the AI/NLP field, and with all the recent advances in them, it got me thinking, how did I learn programming, and whether it was a correct way to approach ? So in order to test my hypotheses, I created [CodeSmith](https://github.com/yash-srivastava19/CodeSmith) - A ChatGPT-ish inspired chatbot that doubles as a programming assistant.

CodeSmith knows a lot about math, statistics, machine learning in Python, and can be a great asset to do programming with. The project is fully open source, and with the feedback from the community, I can improve upon the initial version. So, let's look into the technical aspects of CodeSmith.

Tools Used : Chainlit, Langchain, Huggingface Spaces
Skills Learned : Deployment, Dataset creation.

## Dataset Creation

Choosing the right form of data could be the difference between a headache or a clear mind - and enough emphasis should be given it to have a better performing model. I have worked a lot with Cohere's models, and knew that how to choose the data for few shot prompting. A detailed guide is available on Cohere's website, with a step-by-step instruction on how to fine tune the command model as well.

Personally, I learnt a lot about programming by solving mathematical problems. Whether it was solving basic linear algebra problems, or testing weird ideas I had in my mind. I owe a huge part of my learning to [ProjectEuler](https://projecteuler.net)(and I'm sure I'm not the only one :) ), and wanted to give back to it. CodeSmith is tribute to ProjectEuler and the awesome programming I concepts I learned from it. 

## Deployment 

Deployment is a really important part if you want to make your projects standout. I deployed CodeSmith on Huggingface Spaces, using a [Dockerized version of Chainlit](https://huggingface.co/spaces/yash-srivastava19/CodeSmith/tree/main). This was a really good alternative over using GCP, Flow.io, which requires credit card for setup. I would suggest everyone who are developing in this space to build deployed version of your product,  as it will make you stand out from the crowd.

## Technical Details

CodeSmith is an application made using Langchain, Chainlit and Cohere. A similar model of the application is deployed on Huggingface spaces, and can be embedded in any website or application.

The model used by CodeSmith is a Cohere Command model, which is fine tuned using the `data.txt` file in the github repository of the . The file contains code examples from two sources, namely :

- [CodeAlpaca-20K](https://huggingface.co/datasets/sahil2801/CodeAlpaca-20k) : Python examples from the training set were handpicked to be used for finetuning.
- [Project Euler Solution](https://github.com/nayuki/Project-Euler-solutions/tree/master/python) : A personal favourite website, the problems from project euler python folder in the repo were handpicked to be used for finetuning.

The model was then sent for finetuning, and was accesable using an API. This custom model(`called code-gen-alpha`), was then wrapped in a Langchain custom LLM class, and used by the `LLMChain`(together with `PromptTemplate`) to be used by the Chainlit factory.

## Expansion 

I wanted to used Llama2(or some code version of Llama2), together with a the full version of CodeAlpaca-20K and ProjectEuler dataset for finetuning, and add support for RAG(or sources, possible bugs), but with low budget and computing power, it is very difficult. I tried using Huggingface models as well(falcon-7b-instruct, and other chat versions of small models), but their speed was not good enough to be used in an application - so I went with Cohere.

The aim is to build upon this project, with more data and more computing power. Till anything significant comes up, I've decided that all of the data will be in Python programming language, but I'll let my future self decide on that.

Also, if anyone is interested in providing some computing power, or helping in expanding the project, [any help would be really appreciated](https://github.com/yash-srivastava19/CodeSmith).
