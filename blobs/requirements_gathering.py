def run(state):
    """
    Initialize or continue requirements gathering process.

    Args:
        state: Current recruitment workflow state

    Returns:
        Dict with state updates
    """
    if not state.messages:  # Using dot notation instead of dict notation
        # Get job requirements input using the correct JobRequirements model
        job_requirements = JobRequirements(
            title=input("What is the job title? "),
            company_description=input("Provide a description of the company: "),
            job_requirements=input("List the job requirements (comma-separated): ").split(","),
            candidate_responsibilities=input("List the candidate responsibilities (comma-separated): ").split(","),
            candidate_qualifications=input("List the candidate qualifications (comma-separated): ").split(","),
            company_benefits=input("List the company benefits (comma-separated): ").split(","),
            interview_date=datetime.strptime(
                input("What is the interview date (YYYY-MM-DD)? "),
                "%Y-%m-%d"
            ),
            preferred_country=input("What is the preferred country for the role? "),
            years_experience=int(input("What is the required years of experience? ")),
            linkedin_profiles=[
                p.strip()
                for p in input("Provide any LinkedIn profile URLs (comma-separated, optional): ").split(",")
                if p.strip()
            ],
            skills_required=input("List the required skills (comma-separated): ").split(","),
            salary_range=input("What is the salary range for the role? ")
        )

        return {
            "messages": [
                SystemMessage(content="You are an HR assistant gathering detailed job requirements."),
                HumanMessage(content="Let's begin gathering the job requirements. What is the job title?")
            ],
            "job_requirements": job_requirements,
            "phase": "requirements_gathering"
        }
    else:
        return {"phase": state.phase}  # Return current state if messages exist