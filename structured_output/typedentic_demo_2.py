from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Literal, Optional

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile",
)

# Define the schema

class ResumeAnalysis(TypedDict):
    candidate_name: Annotated[str, "The full name of the candidate"]
    key_skills: Annotated[list[str], "Extract a list of key skills the candidate possesses"]
    summary: Annotated[str, "Provide a brief summary of the candidate's experience and background"]
    experience_level: Annotated[Literal["entry_level", "mid_level", "senior_level"], "Determine the experience level of the candidate based on their background and skills"]
    strengths: Annotated[Optional[list[str]], "Identify the candidate's strengths based on their experience and skills"]
    weaknesses: Annotated[Optional[list[str]], "Identify the candidate's weaknesses or areas for improvement based on their experience and skills"]
    
    
# create structured output using the schema

structured_output = model.with_structured_output(ResumeAnalysis)

# invoke the model with structured output

result = structured_output.invoke(
    """
    My name is John Doe and I am a software engineer with 5 years of experience in web development. I have worked with various technologies including Python, JavaScript, and React. I am looking for opportunities to work on challenging projects that allow me to grow my skills and contribute to the success of the team.
    I am particularly interested in roles that involve full-stack development and cloud computing. I have a strong background in building scalable web applications and have experience with AWS and Docker. I am also passionate about learning new technologies and staying up-to-date with industry trends.
    
    also, I have experience in leading small teams and mentoring junior developers. I believe in writing clean and maintainable code and following best practices in software development. I am excited about the possibility of joining a dynamic team where I can make a meaningful impact and continue to grow as a professional.
    
    """
    
)

print(result)