def run(state):
    """LangGraph node that will extract tasks from given project description"""
    description = state["project_description"]
    team = state["team"]
    prompt = f"""You are an experienced project description analyzer, who needs to create a project plan.
        Create the project plan using the following steps:
        - Analyze the project description '{description}' and create a list of actionable and realistic tasks with estimated time (in days) to complete each task. If the task takes longer than 5 days, break it down into independent smaller tasks.
        - Assess dependency between tasks. For each task, identify the blocking tasks. Provide for each task the list of dependent tasks.
        - Schedule tasks based on the dependencies.
        - Allocate tasks to team members {team} based on their skills and availability, such that there is no overlapping task assigned for a team member. Ensure that no team member has 2 tasks assigned for the same time period.
    """
    structure_llm = llm.with_structured_output(ProjectPlan)
    project_plan: ProjectPlan = structure_llm.invoke(prompt)
    print(project_plan)
    return {"tasks": project_plan.tasks, "dependencies": project_plan.dependencies, "schedule": project_plan.schedule, "task_allocations": project_plan.task_allocations}