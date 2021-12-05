from mr_scraper.api.models import ScraperConfig, ContentConfig, ContentProvider, QueryConfig, attribute_query, \
    text_query, base_url

companies = ScraperConfig(
    content=ContentConfig(
        provider=ContentProvider.PUPPETEER,
        delay=2,
        url=base_url('https://www.levels.fyi')
    ),
    queries={
        'Company': QueryConfig(
            selector=".company-outline-container",
            queries={
                'Url': attribute_query(selector='a', attribute='href'),
                'Name': text_query(selector='a')
            }
        )
    }
)
