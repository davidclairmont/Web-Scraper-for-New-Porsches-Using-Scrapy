# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class PorschePipeline(object):
    def process_item(self, item, spider):
        ## a PorscheItem is sent to this pipeline and turned into a dictionary
        dic_data = {
            'URL': item.get('url') + ' ',
            'Name': item.get('name'),
            'Fuel Economy': item.get('fuel_economy'),
            'Price': item.get('price'),
            'Transmission': item.get('transmission'),
            'Exterior Color': item.get('exterior'),
            'Interior Color': item.get('interior'),
            'Body/Seating': item.get('body_seating'),
            'Drivetrain': item.get('drivetrain'),
            'Engine': item.get('engine'),
            'Stock #': item.get('stock_number'),
            'Location': item.get('location'),
            'VIN': item.get('vin'),
            'Contact #': item.get('phone_number')
        }
        return dic_data