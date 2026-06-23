def run(state):
    chunks = get_or_create_chunks(state)
    article_text = state["article_text"]
    grammar_and_bias_review_results = (
        grammary_and_bias_analysis_article(article_text, chunks)
    )
    return {"grammar_and_bias_review_result": grammar_and_bias_review_results}