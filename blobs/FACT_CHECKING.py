def run(state):
    chunks = get_or_create_chunks(state)
    article_text = state["article_text"]
    fact_checking_results = fact_check_article(article_text, chunks)
    return {"fact_check_result": fact_checking_results}