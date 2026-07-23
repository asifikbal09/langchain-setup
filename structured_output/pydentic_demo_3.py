from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pydantic import BaseModel, Field, EmailStr
from typing import Optional 

load_dotenv()

class JobApplication(BaseModel):
    name: str = "unknown"
    experience: int = Field(None, description="The number of years of experience the applicant has in their field")
    email: EmailStr = Field(..., description="The email address of the applicant")
    expected_salary: int = Field(gt=0, description="The expected salary of the applicant")
    
    
model = ChatGroq(
    model="llama-3.3-70b-versatile",
)

structured_output = model.with_structured_output(JobApplication)

result = structured_output.invoke(
    """
    My name is John Doe and I am a software engineer with 5 years of experience in web development. I have worked with various technologies including Python, JavaScript, and React. I am looking for opportunities to work on challenging projects that allow me to grow my skills and contribute to the success of the team. I am particularly interested in roles that involve full-stack development and cloud computing. I have a strong background in building scalable web applications and have experience with AWS and Docker. I am also passionate about learning new technologies and staying up-to-date with industry trends. I am excited about the possibility of joining a dynamic team where I can make a meaningful impact and continue to grow as a professional.
    I am looking for a salary of $120,000 per year.
    """
)

print(result)