from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field, EmailStr

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile",
)

class ModelEvaluation(BaseModel):
    model_name: str = Field(..., description="The name of the model being evaluated"),
    accuracy: float = Field(ge=0, le=1, description="The accuracy of the model on the evaluation dataset, represented as a float between 0 and 1"),
    dataset : str = Field(description="The name of the dataset used for evaluation"),

parser = PydanticOutputParser(
    pydantic_object=ModelEvaluation 
)

template = PromptTemplate(
    template="""
    generate the name, accuracy and dataset of a fictional machine learning model trained for {task}.
    {format_instructions}
    """,
    input_variables=["task"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
    
)

chain = template | model | parser

result = chain.invoke({"task": "image classification"})

print(result)
print(f"Type of result: {type(result)}")