from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile",
)

parser = JsonOutputParser()

template = PromptTemplate(
    template="""
    Explain {topic} in simple terms.
    {format_instructions}
    """,
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
    
)


chain = template | model | parser

result = chain.invoke({"topic": "machine learning"})

print(result)
print(f"Type of result: {type(result)}")