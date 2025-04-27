from langchain_community.llms import VLLMOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# This it the language model we'll use. We'll talk about what we're doing below in the next section
llm = VLLMOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_base=os.getenv("OPENAI_API_BASE"),
    model="openai/my-vlllm3",
    temperature=0,
)
