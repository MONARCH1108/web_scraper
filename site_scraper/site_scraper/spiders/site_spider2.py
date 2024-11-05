import scrapy


class SiteSpider3Spider(scrapy.Spider):
    name = "site_spider2"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Friedrich_Nietzsche"]

    def parse(self, response):
        figures = response.xpath('//*[@id="mw-content-text"]/div[1]/figure') 
        for fig in figures:
            link = fig.xpath('./a/@href').get()
            caption = fig.xpath('./figcaption//text()').get()
            yield {
                'link': link,
                'caption': caption
            }
        paragraph = response.xpath('//*[@id="mw-content-text"]/div[1]/p/text()').getall()
        yield {
            'paragraph': " ".join(paragraph)
        }
