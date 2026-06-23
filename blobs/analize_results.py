def run(state):
    structured_llm = create_structured_llm(config, FinalOutput)

    current_result_config = state["execution_configs"].pop(0)

    if not current_result_config["description"]:
        return {"listResults": []}
    
    for test_case in state["test_cases"]:
        if test_case.id == current_result_config["thread_id"]:
            current_test_case = test_case
            break  

    tester = state["testers"][current_result_config["user_id"]] 

    configurable = {"configurable": current_result_config}

    parameters = {"test_case_name" : current_test_case.name,
                  "role_description":tester.description,
                  "test_case_description":current_test_case.description,
                  "acceptance_criteria":current_test_case.acceptance_criteria,
                  "output":obj_to_str(state["compiled_graph"].get_state(configurable).values)}

    system_message = assertion_prompt.render(**parameters)
    final_output = structured_llm.invoke([SystemMessage(content=system_message)]+[HumanMessage(content="Generate the final output.")])
    final_output.tester_id = tester.id
    final_output.test_case_id = current_test_case.id

    return {"listResults": [final_output]}