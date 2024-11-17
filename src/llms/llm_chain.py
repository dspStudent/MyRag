from langchain.chains import LLMChain
import llms.groq_llm as groq_llm_client
import prompt_templates as pt
from langchain_core.prompts import ChatPromptTemplate

meta_data_prompt=ChatPromptTemplate.from_template(pt.META_DATA_PROMPT)

rag_chain_prompt=ChatPromptTemplate.from_template(pt.USER_PROMPT_TEMPLATE)

meta_data_chain=meta_data_prompt | groq_llm_client.llm

rag_chain=rag_chain_prompt | groq_llm_client.llm

