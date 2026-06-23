def run(state):
  # 1. find any interesting topic from retriever

  retriever = vectorstore.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"k": 1, "score_threshold": 0.5},
  )

  if not IS_LOCAL_ENVIRONMENT:
    # Use Pinecone
    results = retriever.invoke(state['random_anchor'], filter={"source": "wealthofnations"})
  else:
    # Use Local Chroma
    results = retriever.invoke(state['random_anchor'])


  # referenced_document = list(results)[0].page_content
  referenced_document = "test"

  # 2. generate interesting question from the topic
  host = state['host']

  narrator_msg = f"""
  Present an interesting and insightful question from the topic from the following interesting fact(s):
  {referenced_document}

  Remember that you are the host, do not break the character.
  """
  response = llm.invoke([
    SystemMessage(content=host.sys_msg),
    SystemMessage(content="Your job is to ask a quesetion about the topic to the users for dicsussion."),
    HumanMessage(content=narrator_msg, name="narrator")
  ])
  response.name = host.name
  response.content = f"{host.name}: {response.content}"
  response.pretty_print()
  return {
    'message': [response],
    'curr_discussion': [response],
    "setEndDiscussion": False
  }