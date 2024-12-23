import wikipediaapi

def get_wikipedia_description(word):
    user_agent = "MyWikipediaApp/1.0 (rishijain.211cv142@nitk.edu.in)" 
    
    wiki_wiki = wikipediaapi.Wikipedia(
        language='en', 
        extract_format=wikipediaapi.ExtractFormat.WIKI,
        user_agent=user_agent  
    )
    
    page = wiki_wiki.page(word)
    if page.exists():
        return page.summary
    else:
        return None