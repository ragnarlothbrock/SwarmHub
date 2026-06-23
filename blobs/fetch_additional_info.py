def run(state):
    """Fetch more details about the selected car listing."""
    listing = state["selected_listing"]

    # Crawl the car listing page to get more details about the car for sale and the seller

    async def _crawl_car_listing():
        for interface in state["web_interfaces"]:
            if listing["id"].split("_")[0].lower() in interface.__class__.__name__.lower():
                return await interface.crawl_listing(listing["url"])
    
    info_car_for_sale = asyncio.run(_crawl_car_listing())

    # Call the LLM to summarize the information about the car for sale into a concise paragraph
    prompt = SystemMessage(
        f"Summarize all the relevant information about the selected car for sale into a paragraph: {listing['title']}\n\n"
        f"Here is the raw information about the car for sale:\n\n{info_car_for_sale}"
        f"Format the summary clearly and concisely, with line breaks between sections."
    )

    car_info_summary = GPT.invoke([prompt]).content

    show_assistant_output("\033[92mHere are more details about the car for sale:\n\033[0m", flush=True)

    show_assistant_output("\033[92m" + car_info_summary + "\n\n\033[0m", flush=True)

    state["messages"] += [prompt, AIMessage(car_info_summary)]

    # Search for common issues and reliability of the car on DuckDuckGo
    car_name = listing["title"]

    queries = [f"{car_name} common issues", f"{car_name} problem", f"{car_name} reliability"]
    context = ""
    for query in queries:
        search_results = duckduckgo_search.invoke(query)
        formatted_results = f"QUERY: {query}\n\n{search_results}\n-------------------\n"
        context += formatted_results

    prompt = SystemMessage(
        f"Provide additional information about this car: {listing['title']}, "
        f"including engine specifications, common issues with this model, and market value."
        f"Here is additioanl context to help you provide the information:\n\n{context}"
        f"Here are the user needs, give some insights about the car based on the user needs:\n\n{state['user_needs']}"
    )
    
    result = GPT.invoke([prompt])
    
    listing["additional_info"] = result.content
    
    show_assistant_output(f"\033[92mHere is additional information about the model in general, coming from Internet:\n{listing['additional_info']}\n\033[0m")
    
    user_prompt = "Would you like to view more details about another listing, or refine your search (Write END to finish this conversation) ?"
    state["messages"] += [SystemMessage(user_prompt)]
    state["messages"] += [HumanMessage(get_user_input(user_prompt))]
    print(f"\033[94m{state['messages'][-1].content}\033[0m", flush=True)
    
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