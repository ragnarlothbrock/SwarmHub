def run(state):
    """Build and refine search filters based on user needs."""

    show_assistant_output("Building filters based on user needs...")
    
    for interface in state["web_interfaces"]:
        filters_info = interface.get_filters_info()
        
        # TODO: Check if this website is useful to the user based on the filters
        # If not continue to the next interface
        
        # If the website is useful, use LLM to setup the filters based on user needs
        
        # Define system instructions with filters information
        system_message = SystemMessage(filters_info + "\n\n" + "User needs:\n" + state["user_needs"])

        # Use the LLM to process the user's needs and set the filters
        try:
            result = GPT.invoke([system_message])
            llm_response = result.content.strip()

            # Validate and set the filters for the interface
            interface.set_filters_from_llm_response(llm_response)
            show_assistant_output(f"\nSuccessfully set filters for: {interface.__class__.__name__}")
            show_assistant_output(f"Updated URL: {interface.url}")
        except ValueError as e:
            show_assistant_output(f"Failed to set filters for {interface.base_url}: {e}")
        except Exception as e:
            show_assistant_output(f"An error occurred while processing filters for {interface.base_url}: {e}")
    
    return