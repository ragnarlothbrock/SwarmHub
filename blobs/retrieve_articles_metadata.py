def run(state):
    """Using the NewsAPI params, perform api call."""
    # parameters generated for the News API
    newsapi_params = state["newsapi_params"]

    # decrement the number of searches remaining
    state['num_searches_remaining'] -= 1

    try:
        # create a NewsApiClient object
        newsapi = NewsApiClient(api_key=os.getenv('NEWSAPI_KEY'))
        
        # retreive the metadata of the new articles
        articles = newsapi.get_everything(**newsapi_params)

        # append this search term to the past searches to avoid duplicates
        state['past_searches'].append(newsapi_params)

        # load urls that have already been returned and scraped
        scraped_urls = state["scraped_urls"]

        # filter out articles that have already been scraped
        new_articles = []
        for article in articles['articles']:
            if article['url'] not in scraped_urls and len(state['potential_articles']) + len(new_articles) < 10:
                new_articles.append(article)

        # reassign new articles to the state
        state["articles_metadata"] = new_articles

    # handle exceptions
    except Exception as e:
        print(f"Error: {e}")

    return state