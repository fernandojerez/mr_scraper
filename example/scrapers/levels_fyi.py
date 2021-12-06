from mr_scraper.api.models import ScraperConfig, ContentConfig, ContentProvider, QueryConfig, attribute_query, \
    text_query, base_url

companies = ScraperConfig(
    content=ContentConfig(
        provider=ContentProvider.PUPPETEER,
        delay=2,
        url=base_url('https://www.levels.fyi')
    ),
    queries={
        'companies': QueryConfig(
            selector=".company-outline-container",
            queries={
                'url': attribute_query(selector='a', attribute='href'),
                'name': text_query(selector='a')
            }
        )
    }
)
