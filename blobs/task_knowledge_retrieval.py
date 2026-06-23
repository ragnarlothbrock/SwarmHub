def run(state):
    """use Tavily to look up information on the task."""

    search_foundation = "What are the steps for the following task? {task}"
    search_query = search_foundation.format(task=approach["task"])
    
    searches = tavily_client.search(search_query, max_results=10)

    details = ""

    for result in searches['results']:
        if details == "":
            details = result['content']
        else:
            details = f"{details} {result['content']}"

    approach["details"] = details

    return approach