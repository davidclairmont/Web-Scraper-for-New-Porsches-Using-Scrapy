import scrapy
from porsche.items import PorscheItem

class NewPorscheSpider(scrapy.Spider):
    ## name of the spider
    name = 'new_porsche_spidey'
    ## domains spider is allowed to access
    allowed_domains = ['parkplace.com']
    ## starting places for the spider
    start_urls = ['https://www.parkplace.com/new-porsche.htm']

    def parse(self, response):
        ## gets the url for the next page
        next_page_url = response.xpath('//a[@rel="next"]/@data-href').extract()
        ## gets the urls for each car on the page
        all_cars_urls = response.xpath('//a[@class="url"]/@href').extract()

        ## calls parsePorsche for each car on the page
        for url in all_cars_urls:
            car_url = 'https://www.parkplace.com/' + url
            yield scrapy.Request(car_url, callback=self.parsePorsche)

        ## checks if there is a next page
        if len(next_page_url) > 0:
            next_page_url = 'https://www.parkplace.com/new-porsche.htm' + next_page_url[0]
            yield scrapy.Request(next_page_url, callback=self.parse)


    def parsePorsche(self, response):
        ## gets the url of the current car page
        url = response.request.url
        names = response.xpath('//span[@class="font-weight-bold"]/text()').extract()
        name = "".join(names)
        ## does checks for the description fields, some contain only 3 fields, some 5, some 6, and most contain 7
        CHECK = response.xpath('//dd[@class="col-xs-7 p-0"]/span/text()').extract()
        if len(CHECK) == 3:
            exterior = CHECK[0]
            interior = CHECK[1]
            engine = CHECK[2]
            fuel_economy = 'N/A'
            drivetrain = 'N/A'
            body_seating = 'N/A'
            transmission = 'N/A'

        elif len(CHECK) == 5:
            exterior = CHECK[0]
            interior = CHECK[1]
            body_seating = CHECK[2]
            transmission = CHECK[3]
            engine = CHECK[4]
            fuel_economy = 'N/A'
            drivetrain = 'N/A'

        elif len(CHECK) == 6:
            fuel_economy = CHECK[0]
            exterior = CHECK[1]
            interior = CHECK[2]
            body_seating = CHECK[3]
            transmission = CHECK[4]
            engine = CHECK[5]
            drivetrain = 'N/A'
        else:
            fuel_economy = CHECK[0]
            exterior = CHECK[1]
            interior = CHECK[2]
            body_seating = CHECK[3]
            transmission = CHECK[4]
            drivetrain = CHECK[5]
            engine = CHECK[6]

        ## extract info that is always on a car page
        price = response.xpath('//span[@class="price-value"]/text()')[0].extract()
        phone_number = response.xpath('//span[@data-phone-ref="GROUP_SALES"]/text()')[0].extract()
        location = response.xpath('//div[@class="d-sm-inline mr-5"]/strong/text()')[0].extract()
        stock_number = response.xpath('//ul[@class="additional-details list-inline my-0 font-weight-normal ddc-font-size-small text-muted"]/li/text()')[4].extract()
        vin = response.xpath('//ul[@class="additional-details list-inline my-0 font-weight-normal ddc-font-size-small text-muted"]/li/text()')[1].extract()
        
        ## creates the Porsche item for the car and adds relevant data
        item = PorscheItem()
        item['url'] = url
        item['name'] = name
        item['fuel_economy'] = fuel_economy
        item['transmission'] = transmission
        item['exterior'] = exterior
        item['interior'] = interior
        item['body_seating'] = body_seating
        item['drivetrain'] = drivetrain
        item['engine'] = engine
        item['price'] = price
        item['phone_number'] = phone_number
        item['location'] = location
        item['stock_number'] = stock_number
        item['vin'] = vin
            
        yield item
