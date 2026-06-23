def run(state):
    """Node to retrieve clauses based on contract type and filter for relevancy"""
    contract_type = state['contract_info'].contract_type

    try:
        # First get ALL General Clauses (no limit)
        general_clauses = clause_retriever.get_clauses_by_contract_type(
            contract_type="General Clauses",
            k=10  # Using a high number to effectively get all clauses
        )

        # Then get specific contract clauses
        specific_clauses = clause_retriever.get_clauses_by_contract_type(
            contract_type=contract_type,
            k=10  # Get more clauses initially since we'll filter them
        )

        # Filter specific clauses for relevancy using LLM
        system_prompt = f"""You are a legal clause relevancy analyzer.
        For each clause, determine if it is relevant for a {contract_type}.
        Respond with either "RELEVANT" or "NOT RELEVANT".
        Base your decision on how essential and appropriate the clause is for this type of contract."""

        filtered_specific_clauses = []
        for clause in specific_clauses:
            messages = [
                SystemMessage(content=system_prompt),
                HumanMessage(content=f"Clause Title: {clause['clause_title']}\n\nClause Text: {clause['clause_text']}")
            ]

            response = llm.invoke(messages).content.strip().upper()
            if response == "RELEVANT":
                filtered_specific_clauses.append(clause)

        # Format clauses for inclusion in the state
        formatted_clauses = []

        # Add ALL General Clauses first
        for clause in general_clauses:
            formatted_clause = f"""### {clause['clause_title']}

            {clause['clause_text']}
            """
            formatted_clauses.append(formatted_clause)

        # Then add filtered specific contract clauses
        for clause in filtered_specific_clauses:
            formatted_clause = f"""### {clause['clause_title']}

            {clause['clause_text']}
            """
            formatted_clauses.append(formatted_clause)

        return {"clauses": formatted_clauses,
                 "current_step": 0}  # Return to clauses instead of sections

    except Exception as e:
        error_message = f"Error retrieving clauses: {str(e)}"
        return {"clauses": [error_message]}