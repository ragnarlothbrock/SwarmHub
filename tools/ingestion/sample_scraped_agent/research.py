import requests
from bs4 import BeautifulSoup
from crewai import Agent, Crew

def run(state):
    print('Scraping health metrics summaries via requests...')
    return state