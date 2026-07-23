from pydantic import BaseModel, Field, EmailStr
from typing import Optional 

class JobApplication(BaseModel):
    name: str = "unknown"
    email: EmailStr = Field(..., description="The email address of the applicant")
    phone: Optional[str] = Field(None, description="The phone number of the applicant")
    resume: str = Field(..., description="A brief summary of the applicant's experience and background")
    cover_letter: Optional[str] = Field(None, description="An optional cover letter from the applicant")
    
new_applicant_data = {
    "name": "Jane Smith",
    "email": "jane.smith@example.com",
    "phone": "123-456-7890",
    "resume": "I am a software engineer with 3 years of experience in web development. I have worked with various technologies including Python, JavaScript, and React. I am looking for opportunities to work on challenging projects that allow me to grow my skills and contribute to the success of the team.",
    "cover_letter": "I am particularly interested in roles that involve full-stack development and cloud computing. I have a strong background in building scalable web applications and have experience with AWS and Docker. I am also passionate about learning new technologies and staying up-to-date with industry trends. I believe in writing clean and maintainable code and following best practices in software development. I am excited about the possibility of joining a dynamic team where I can make a meaningful impact and continue to grow as a professional."
}

applicant = JobApplication(**new_applicant_data)

print(f"Applicant: {applicant}")

application_data = applicant.model_dump()  # Convert the Pydantic model to a dictionary

application_json = applicant.model_dump_json()  # Convert the Pydantic model to a JSON string

print(f"Application Data (dict): {application_data}")
print(f"Application Data (JSON): {application_json}")