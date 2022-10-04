import wikipedia
from yake import KeywordExtractor

# build a function to return the summary of a wikipedia page
def get_wiki_summary(page):
    """
    Return the summary of a wikipedia page
    """
    return wikipedia.summary(page)


# build a function search wikipedia pages for a match
def search_wiki_pages(page):
    """
    Search wikipedia pages for a match
    """
    return wikipedia.search(page)


# build a function to return the wikipedia page
def get_wiki_page(page):
    """
    Return the wikipedia page
    """
    return wikipedia.page(page)


# return the top 10 keywords from the content of a page
def get_wiki_keywords(page):
    """Get the top 10 keywords from the content of a page."""
    content = get_wiki_page(page).content
    extractor = KeywordExtractor()
    keywords = extractor.extract_keywords(content)
    # return a dictionary of the top 10 keywords
    return {keyword: score for keyword, score in keywords[:10]}
