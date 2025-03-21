
import os
import warnings
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_community.llms import CTransformers

class PDFChatBot:
 
    def __init__(self):
        self.data_path = os.path.abspath("bot/src/data")
        self.db_faiss_path = os.path.join('vectordb', 'db_faiss')
        self.embeddings = HuggingFaceEmbeddings(
            model_name='sentence-transformers/all-MiniLM-L6-v2',
            model_kwargs={'device': 'cpu'}
        )
        warnings.filterwarnings('ignore', message='Number of tokens.*exceeded maximum context length.*')

        model_path = os.path.abspath("bot/models/llama-2-7b-chat.ggmlv3.q8_0.bin")

        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at: {model_path}")

        self.llm = CTransformers(
            model=model_path,
            model_type="llama",
            max_new_tokens=2000,
            temperature=0
        )

    def create_vector_db(self):
        loader = DirectoryLoader(
            self.data_path,
            glob='*.pdf',
            loader_cls=PyPDFLoader
        )

        documents = loader.load()
        print("Loading completed! \nChunking Now!")
        
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=50)
        texts = text_splitter.split_documents(documents)

        db = FAISS.from_documents(texts, self.embeddings)
        db.save_local(self.db_faiss_path)
        print("Embedding saved!")

    def search_similar_documents(self, user_query, top_k=5):
        db = FAISS.load_local(self.db_faiss_path, self.embeddings, allow_dangerous_deserialization=True)
        docs = db.similarity_search(user_query, top_k=top_k)

        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            retriever=db.as_retriever(search_kwargs={"k": top_k})
        )

        response = qa_chain.invoke({"query": user_query})
        return response["result"]