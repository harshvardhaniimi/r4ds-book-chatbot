import csv
from datetime import datetime
import os
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

# read API key from text file
def read_api_key(file):
    with open(file, "r") as f:
        return f.read().strip()
    
os.environ["OPENAI_API_KEY"] = read_api_key("api_key.txt")

class ImprovedChatBot:
    def __init__(self, llm, retriever):
        self.llm = llm
        self.retriever = retriever
        self.chat_history = []
        
    def query(self, question):
        try:
            response = self.llm({"question": question, "chat_history": self.chat_history})
            answer = response["answer"]
            self.chat_history.append((question, answer))
        except Exception as e:
            answer = "Error: " + str(e)
        return answer

# Initialize components
print("Initializing components... Please wait.")
loader = DirectoryLoader("documents/", glob="*.*")
txt_docs = loader.load_and_split()
embeddings = OpenAIEmbeddings()
txt_docsearch = Chroma.from_documents(txt_docs, embeddings, persist_directory="txt_docsearch")
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.2)
qa = ConversationalRetrievalChain.from_llm(llm, retriever=txt_docsearch.as_retriever())

# Print that it's ready
print("Chatbot is ready to chat! To halt the conversation, press Ctrl + C.")

# Initialize the ImprovedChatBot
chatbot = ImprovedChatBot(qa, txt_docsearch.as_retriever())

# Create folder for communications if not exists
if not os.path.exists("communications"):
    os.mkdir("communications")
    
def main():
    chat_rows = []
    try:
        while True:
            question = input("You: ")
            answer = chatbot.query(question)
            print(f"LLM: {answer}")

            # Append to chat history
            chat_rows.append(["You", question])
            chat_rows.append(["LLM", answer])
    except KeyboardInterrupt:
        # Press Cmd + C or Ctrl + C to terminate the conversation
        print("Conversation terminated by the user.")
        
        # Save the conversation
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        with open(f"communications/{timestamp}.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Speaker", "Content"])
            writer.writerows(chat_rows)

if __name__ == "__main__":
    main()
