def run(state):
    chunks = get_or_create_chunks(state)
    article_text = state["article_text"]
    tone_analysis_results = tone_analysis_article(article_text, chunks)
    return {"tone_analysis_result": tone_analysis_results}