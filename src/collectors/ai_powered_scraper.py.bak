import scrapy

class AIPoweredSpider(scrapy.Spider):
    name = "ai_powered_spider"

    def __init__(self, start_urls=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = start_urls if start_urls else ["https://example.com"]

    def parse(self, response):
        """
        Parse the response to extract relevant data.
        """
        # Example: Extract all links from the page
        links = response.css("a::attr(href)").getall()
        self.log(f"Found links: {links}")

        # Additional processing can be added here

        # Follow links recursively
        for link in links:
            yield response.follow(link, callback=self.parse)

# Usage Example:
# scrapy runspider ai_powered_spider.py -a start_urls='["https://example.com"]'
