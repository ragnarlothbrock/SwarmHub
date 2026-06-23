def run(state):
  topic = state['topic']
  messages = [SystemMessage(content="You task is to generate 5 relevant words about the following topic: " + topic)]
  message = model_keywords.invoke(messages)
  return {'keywords': message.keys}