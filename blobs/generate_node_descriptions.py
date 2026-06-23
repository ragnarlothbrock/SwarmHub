def run(state):
    structured_llm = create_structured_llm(config, Node_description)

    config, error, error_message  = invoke_graph(graph=state["compiled_graph"],
                          input=state["valid_input"])
    
    if error:
        raise ValueError(f"Invalid graph input: {error}")
    
    configurable = {"configurable": config}

    history = list(state["compiled_graph"].get_state_history(configurable))
    history.reverse()

    node_name_in_tasks = [item.tasks[0].name for item in history if item.tasks]
    node_name_in_tasks.remove('__start__')
    
    node_tasks_in_tasks = [item.tasks[0].result for item in history if item.tasks]

    summary_graph = state["summary_graph"]

    for index, node_name in enumerate(node_name_in_tasks):
        current_description = summary_graph.nodes[node_name].get("description", None)
        functions = summary_graph.nodes[node_name].get("tools", None)

        actual_input = node_tasks_in_tasks[index]
        actual_output = node_tasks_in_tasks[index+1]

        parameters = {"graph_description":state["user_description"],
        "input":obj_to_str(actual_input),
        "output":obj_to_str(actual_output),
        "node_name":node_name,
        "type":str(summary_graph.nodes[node_name]["type"]),
        "functions":functions,
        "income_nodes":str(summary_graph.in_edges(node_name)),
        "outcome_nodes":str(summary_graph.out_edges(node_name)),
        "node_description":current_description}
                                                       
        system_message = node_description_promt.render(**parameters)
        llm_description = structured_llm.invoke([SystemMessage(system_message)])

        summary_graph.nodes[node_name]["description"] = llm_description.node_description

    
    return {"execution_configs": [config],
            "summary_graph": summary_graph}