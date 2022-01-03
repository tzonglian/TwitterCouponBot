import scrapy


class MichaelsCouponSpider(scrapy.Spider):
    name = 'michaels-coupon'
    allowed_domains = ['https://www.michaels.com/coupons']
    start_urls = ['https://www.michaels.com/coupons/']

    def parse(self, response):
        # sanity check
        print("\n")
        print("HTTP STATUS: "+str(response.status))
        print(response.css("title::text").get())
        print("\n")
        # all coupons
        # coupons = response.css('ul.js-coupon-select')
        coupons = response.css('div.mobile-coupon-info')

        for coupon in coupons:
            shortTitle = coupon.css('h4::text').get()
            description = coupon.css('p::text').get()
            validUntil = coupon.css('span::text').get()
            print('==COUPON==')
            print(shortTitle)
            print(description)
            print(validUntil)
            print('\n')
