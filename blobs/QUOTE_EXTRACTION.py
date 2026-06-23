def run(state):
    chunks = get_or_create_chunks(state)
    article_text = state["article_text"]
    quote_extraction_results = quote_extraction_article(article_text, chunks)
    return {"quote_extraction_result": quote_extraction_results}