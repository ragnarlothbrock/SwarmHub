def run(state):
    structured_llm = create_structured_llm(config, Input)

    parameters = {"test_case_name": state["current_test_case"].name,
                  "test_case_description": state["current_test_case"].description,
                  "graph_valid_input": obj_to_str(state["valid_input"])}

    system_message = new_input_prompt.render(**parameters)

    new_input = structured_llm.invoke([SystemMessage(content=system_message)]+[HumanMessage(content="Generate the new input.")])
    new_input.tester_id = state["current_test_case"].tester_id
    new_input.test_case_id = state["current_test_case"].id

    try:
        agent_valid_input = eval(new_input.new_input)
        agent_valid_input_type = TypeAnnotator(agent_valid_input).get_type()
        valid_input_type = TypeAnnotator(state["valid_input"]).get_type()

        if agent_valid_input_type == valid_input_type:
            new_input.actual_input = agent_valid_input

            config, error, error_message  = invoke_graph(graph=state["compiled_graph"],
                                                         input=agent_valid_input, 
                                                         description= state["current_test_case"].name,
                                                         thread_id=new_input.test_case_id,
                                                         user_id=new_input.tester_id)
            new_input.is_successful = not error
            
            return {"all_new_inputs": [new_input], 
                    "execution_configs": [config]}
        else:
            raise ValueError(f"invalid input type for {new_input.new_input}")

    except Exception as e:
        return {"all_new_inputs": []}