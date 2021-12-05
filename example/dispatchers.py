from mr_scraper.api import ScraperMessage, dispatch


def levels_fyi():
    """Scraper using Puppeter"""
    message = ScraperMessage(
        scraper="example.scrapers.levels_fyi",
        type='companies',
        payload={'url': '/company/'}
    )
    return dispatch(message)
