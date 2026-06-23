def run(state):
    structured_llm = create_structured_llm(config, Testers)
    
    parameters = {"graph_description":state["user_description"],
                    "human_analyst_feedback":"Include: functional tester, anti injection and jailbreak LLM engeener, vulnerabilities bounty hunter", 
                    "max_analysts":3}

    system_message = testers_instructions.render(**parameters)
    created_testers = structured_llm.invoke([SystemMessage(system_message)])

    nodes = [node_data for node_name, node_data in state["summary_graph"].nodes(data=True) if node_data.get("description", None)]
    testers = created_testers.testers
    
    return {"testers": {tester.id: tester for tester in created_testers.testers},
            "node_and_tester": generate_pairs(nodes, testers),
            "test_cases": []}