import scrapy

class NewsSpider(scrapy.Spider):
  name = "news"
  
  start_urls = [
    'https://arstechnica.com/'
  ]
  
  def parse(self, response):
    for post in response.xpath('.//*[@id="main"]/section[1]/ul/li'):
      yield {
        'title': post.xpath('header/h2/a/text()').get(),
        'excerpt': post.css('header p.excerpt::text').get(),
        'date': post.css('header p.byline time::text').get()
      }