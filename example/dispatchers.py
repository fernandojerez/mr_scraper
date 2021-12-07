from mr_scraper.api import dispatch, ScraperMessage


def levels_fyi():
    """Scraper using Puppeter"""
    message = ScraperMessage(
        scraper="example.scrapers.levels_fyi",
        type='companies',
        payload={'url': '/company/'}
    )
    return dispatch(message)
