def run(state):
  """
  Downloads source material from the Gutenberg project
  """
  import requests
  response = requests.get(WEB_DEFAULT_BOOK)

  source_file_path = Path(f"{LOCAL_ARCHIVE_PATH}{LOCAL_DEFAULT_BOOK}")
  with open(source_file_path, "w") as source_file:
    source_file.write(response.text)

  return state