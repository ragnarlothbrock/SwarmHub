def run(state):
  """
  Performs NER against source material
  """
  embbed_paragraphs(vectorstore)

  entities_file_path = Path(f"{LOCAL_ARCHIVE_PATH}entities_{LOCAL_DEFAULT_BOOK}")

  found_entities = extract_entities(f"{LOCAL_ARCHIVE_PATH}{LOCAL_DEFAULT_BOOK}")
  json_entities = json.dumps(found_entities)

  with open(entities_file_path, "w") as output:
      output.write(json_entities)

  return state