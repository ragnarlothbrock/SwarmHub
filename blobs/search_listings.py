def run(state):
    """Search for cars on LaCentrale and mobile.de based on filters."""
    """Display the first listings for the user to view."""
    """Synchronous wrapper for search_listings."""

    state["messages"] += [SystemMessage("Searching for listings based on user needs, this may take time...")]
    show_assistant_output(state["messages"][-1].content)

    async def _search_listings():
        return await fetch_listings_from_sources(state["web_interfaces"])
    
    listings = asyncio.run(_search_listings())
    state["listings"] = listings
    
    show_assistant_output(f"Successfully fetched {len(listings)} listings from the sources.")
    
    AI_message = ""
    
    # Display the first few listings for the user to view
    AI_message += "Here are recent listings that match your requirements:\n"
    for i, listing in enumerate(state["listings"][:5], 1):
        AI_message += f"{i}.\n"
        for key, value in listing.items():
            formatted_key = key.replace("_", " ").capitalize()
            if formatted_key == "Image" and value:
                AI_message += f"   {formatted_key}: ![Example Image]({value})\n"
            else:
                AI_message += f"   {formatted_key}: {value}\n"
        AI_message += "\n"  # Add an extra line for readability
    
    user_prompt = "Would you like to view more details about a specific listing, or refine your search (Write END to finish this conversation) ?"
    AI_message += user_prompt
        
    state["messages"].append(AIMessage(AI_message))
    show_assistant_output(f"\033[92m{state['messages'][-1].content}\033[0m")
    state["messages"].append(HumanMessage(get_user_input(user_prompt)))
    print(f"\033[94m{state['messages'][-1].content}\033[0m")
       
    response = json.loads(CLASSIFIER_GPT.invoke(state["messages"]).content)

    if response["action"] == "select_listing":
        state["next_node"] = "fetch_additional_info"
        selected_listing_id = response["listing_id"]
        for i, listing in enumerate(state["listings"][:5], 1):
            if selected_listing_id in listing["id"]:
                state["selected_listing"] = listing
                break
    elif response["action"] == "refine_search":
        state["next_node"] = "ask_user_needs"
    else:
        state["next_node"] = END
        
    return state