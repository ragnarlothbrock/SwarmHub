def run(state):
  if "best_product" in state and state['best_product']:
    user_query = state["query"]
    best_product_name = state["best_product"]["product_name"]
    justification = state["best_product"]["justification"]
    youtube_link = state["youtube_link"]
    recipient_email=state['email']
    parser = JsonOutputParser(pydantic_object=EmailRecommendation)
    prompt = PromptTemplate(
    template=email_template_prompt,
    input_variables=["product_name", "justification_line", "user_query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
    )
    chain = prompt | llm | parser
    response = chain.invoke({"product_name": best_product_name, "justification_line": justification, "user_query": user_query})
    html_content = email_html_template.format(product_name=best_product_name, justification=response["justification_line"], youtube_link=youtube_link,heading=response['heading'])
    send_email(recipient_email,subject=response['subject'],body=html_content)