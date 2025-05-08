from langchain_community.llms import VLLMOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# This it the language model we'll use. We'll talk about what we're doing below in the next section
llm = VLLMOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_base=os.getenv("OPENAI_API_BASE"),
    model="openai/hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4",
    temperature=0,
    max_tokens=400,
)
