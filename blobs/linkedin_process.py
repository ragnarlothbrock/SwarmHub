def run(state):
     # Implementation to handle the LinkedIn candidate search and outreach process
    """Handle LinkedIn candidate search/outreach process"""
    candidates = []
    tool_node = ToolNode([search_linkedin_candidates, get_linkedin_profile, send_linkedin_message])

    job_details = f"""
    Role: {state.job_requirements.title}
    Company: {state.job_requirements.company_description}
    Location: {state.job_requirements.preferred_country}
    Description: {state.job_description}
    """

    if state.job_requirements.linkedin_profiles:
        # Process provided profiles
        for profile_url in state.job_requirements.linkedin_profiles:
            profile = tool_node.invoke({
                "name": "get_linkedin_profile",
                "args": {"profile_url": profile_url}
            })

            if "error" not in profile:
                message_result = tool_node.invoke({
                    "name": "send_linkedin_message",
                    "args": {
                        "profile_url": profile_url,
                        "job_details": job_details
                    }
                })

                if "error" not in message_result:
                    candidates.append(
                        CandidateProfile(
                            **profile,
                            linkedin_url=profile_url,
                            status="contacted",
                            message_sent=message_result["message"]
                        )
                    )
    else:
        # Search for candidates using Serper API
        search_results = tool_node.invoke({
            "name": "search_linkedin_candidates",
            "args": {
                "job_title": state.job_requirements.title,
                "location": state.job_requirements.preferred_country,
                "skills": state.job_requirements.skills_required
            }
        })

        for result in search_results:
            if "error" not in result:
                profile = tool_node.invoke({
                    "name": "get_linkedin_profile",
                    "args": {"profile_url": result["linkedin_url"]}
                })

                if "error" not in profile:
                    message_result = tool_node.invoke({
                        "name": "send_linkedin_message",
                        "args": {
                            "profile_url": result["linkedin_url"],
                            "job_details": job_details
                        }
                    })

                    if "error" not in message_result:
                        candidates.append(
                            CandidateProfile(
                                **profile,
                                linkedin_url=result["linkedin_url"],
                                status="contacted",
                                source="search",
                                message_sent=message_result["message"]
                            )
                        )

    return {
        "candidates": candidates,
        "linkedin_process_complete": True,
        "phase": "analyze_cv"
    }