# R4DS Book Chatbot 🤖💬

This is a super-simple-but-effective chatbot based on the concept of information retrieval. You can have a full-fledged chat interface with it in your terminal.

## How it Works 🤔

This chatbot loads up files from a `documents` folder. You can toss in text files, doc files, PDFs, PPTs, and pretty much [anything textual](https://python.langchain.com/docs/integrations/document_loaders/unstructured_file.html). (You might need to install extra dependencies.) It then converts the contents into embeddings and stores them in a `txt_docsearch` folder for quick and easy use.

See [🔐 Private ChatGPT](https://hvsc1708.substack.com/p/private-chatgpt) for how this chatbot works. Also see [🦣 Fine-tuning Large Language Models](https://hvsc1708.substack.com/p/fine-tuning-large-language-models) to understand how LLM fine-tuning works.

### Training Data 📚

We're currently using the "R For Data Science 2E" book as the training material. But the beauty of it is, you can plug in any text material you'd like!

## Prerequisites 🛠️

- **OpenAI API Key**: You're going to need one. Grab yours [here](https://platform.openai.com/account/).
  
## Getting Started 🚀

1. **Fork this Repository**: Head over to [this GitHub repo](https://github.com/harshvardhaniimi/r4ds-book-chatbot) and fork it.
2. **Clone Your Fork**: `git clone https://github.com/your-username/r4ds-book-chatbot.git`
3. **Install Dependencies**: Run `pip install -r requirements.txt`
4. **Documents**: Put in your custom documents in the `documents` folder, unless you want to use R4DS as your training material.
5. **OpenAI API Key**: Create a file named `api_key.txt` and paste your API key in it. Don't worry, it's in the `.gitignore` file, so it won't be uploaded to GitHub.
6. **Run the Bot**: Navigate to the folder and run `python chatbot.py`

## Features 🌟

- **Conversational Memory**: This chatbot remembers what you talked about! 
- **CSV Archives**: All conversations are saved in a CSV file in `communications` directory, with a timestamp for easy retrieval.

So go ahead, give it a spin and let the chat begin! 🎉

![Alt text](ss1.png)
