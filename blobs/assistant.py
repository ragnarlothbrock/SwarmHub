def run(state):
   return {"messages": [llm_with_tools.invoke([sys_msg] + state["messages"])]}