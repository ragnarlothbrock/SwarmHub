def run(state):
  topic = state['topic']
  keywords = state['keywords']
  messages = [SystemMessage(content="You task is to generate 5 subtopics to make a podcast about the following topic: " + topic +"and the following keywords:" + " ".join(keywords))]
  message = model_structure.invoke(messages)
  return { "subtopics": message.subtopics[0].subtopics}