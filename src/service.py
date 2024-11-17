import vector_db.qdrant_vectorDB as vdb
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
import llms.llm_chain as lc
import constants as const

def get_meta_data(content):
    return lc.meta_data_chain.invoke({"input_text":content}).content

def get_rag_input(prompt, retrival_data):
    return 

text_split=RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=20,
    length_function=len,
    is_separator_regex=False,
)


def make_chunks(text):
    meta_data= get_meta_data(text)
    chunks=[]
    for chunk in text_split.split_text(text):
        chunks.append(Document(
            page_content=chunk,
            metadata={
                "name":"Devi Sri Ranga Prasad Gudimetla",
                "index":meta_data
            }
        ))
    return chunks

def add_content(text):
    vdb.add_content(make_chunks(text=text))

def add_content_user(text):
    data=make_chunks(text=text)
    print(data)
    vdb.add_content_user(data)


def get_rag_input(prompt,retrival_data):
    return lc.rag_chain.invoke({"context":retrival_data, "user_prompt":prompt}).content


def get_output(text):
    retrival_data=vdb.retrieve_content(content=text, k=const.k)
    return get_rag_input(prompt=text, retrival_data=retrival_data)

def get_output_user(text):
    retrival_data=vdb.retrieve_content_user(content=text, k=const.k)
    return get_rag_input(prompt=text, retrival_data=retrival_data)