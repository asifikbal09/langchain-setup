from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers.structured import ( StructuredOutputParser, ResponseSchema)

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile",
)

response_schemas = [
    ResponseSchema(
        name="Fact_1",
        description="The first fact about the topic",
    ),
    ResponseSchema(
        name="Fact_2",
        description="The second fact about the topic",
    ),
    ResponseSchema(
        name="Fact_3",
        description="The third fact about the topic",
    ),
    ResponseSchema(
        name="Fact_4",
        description="The fourth fact about the topic",
    ),
    ResponseSchema(
        name="Fact_5",
        description="The fifth fact about the topic",
    ),
    
]

parser = StructuredOutputParser.from_response_schemas(response_schemas)

template = PromptTemplate(
    template="""
    Give five facts about {topic}.
    {format_instructions}
    """,
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
    
)

chain = template | model | parser

result = chain.invoke({"topic": "machine learning"})

print(result)
print(f"Type of result: {type(result)}")