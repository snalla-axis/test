import scrapy 
import json 
import pprint 
import requests
import string 
from scrapy.http import Request
import urllib
import pymongo
from ..items import CtripItem
from ..date import date

#from ctrip.items import CtripItem 
url = 'http://english.ctrip.com/Hotels/list/HotelJsonResult?'       
#u_list = []
#final_li = []
#final_li1=[]
#connection = pymongo.MongoClient('localhost',27017)
#db = connection.HD
#db2=connection.CT 
#record =db.hotels
#record.create_index("hotel_id",unique=True) 
#d=date()
#print d #[('2017-02-21','2017-02-22')]#,('2017-02-22','2017-02-23'),('2017-02-23','2017-02-24'),('2017-02-24','2017-02-25'),('2017-02-25','2017-02-26'),('2017-02-26','2017-02-27'),('2017-03-21','2017-03-22'),('2017-03-22','2017-03-23'),('2017-03-23','2017-03-24'),('2017-03-24','2017-03-25'),('2017-03-25','2017-03-26'),('2017-03-26','2017-03-27')]
#d =[('2017-02-17','2017-02-18'),('2017-02-19','2017-02-20'),('2017-02-21','2017-02-22'),('2017-03-17','2017-03-18'),('2017-03-19','2017-03-20'),('2017-03-21','2017-03-22')]
#fo = open('delhi3.csv','a')
class CtripSpider(scrapy.Spider):
    name = "ctrip"
    def __init__(self, loc_id='', *args, **kwargs):
        super(CtripSpider, self).__init__(*args, **kwargs)
        self.db =pymongo.MongoClient('localhost',27017) 
        self.loc_id = loc_id
        self.city_name =self.db.CT.locations.find_one({'_id':int(self.loc_id)},{'city':1})#'country': 0,'_id': 0,'state':0,'country_code':0,'type':0})
    def start_requests(self):
        #print self.loc_id
        #print self.city_name['city']
        #self.city
         #self.city_name
        #url = 'http://english.ctrip.com/Hotels/list/HotelJsonResult?'
        #for chk_in, chk_out in get_dates:#, [('12-02-2017', '13-02-2017')]
        for chk_in,chk_out in date():
            request = scrapy.FormRequest(
                url=url,
                formdata={'city':self.loc_id,'pageno':'0','checkin':str(chk_in),'checkout':str(chk_out)},#,'isScrolling':'true'},
                method='POST',
                callback=self.parse_data)
            request.meta['chkin'] = str(chk_in)
            request.meta['chkout']= str(chk_out)
            request.meta['city']=self.loc_id
            request.meta['city_name']=self.city_name['city']
            yield request
        #yield Request(url,self.parse_data,method="POST",body=urllib.urlencode(payload))
    def parse_data(self, response):
        data1=json.loads(response.body)
        #for r in data1['HotelResultModel']:
         #   fo.write(str(r['hotelId'])+"\n")
            #print  (r['hotelName'])
        c = ((data1['ResultCount'])/10)
        if c == 0:
            c = (data1['ResultCount'])
        print c 
        #print response.meta['city_name']
        #print response.meta['city']
        # #print response.meta['chkin']
        #print response.meta['chkout']
        pageno=range(0,2)
        for j in pageno:
            yield scrapy.FormRequest(
                url=url,
                formdata={'city':response.meta['city'],'pageno':str(j),'checkin':response.meta['chkin'],'checkout':response.meta['chkout']},#'isScrolling':'true'},
                dont_filter=True,
                method='POST',callback=self.data_second, meta={'city':response.meta['city'],'city_name':response.meta['city_name']}
                )
    def data_second(self,response):
        #print 'zzz'
        sdata=json.loads(response.body)
        for r in sdata['HotelResultModel']:
            item = CtripItem()
            item['hotel_id']=r['hotelId']
            item['hotel_name']=r['hotelName']
            item['loc_id']=response.meta['city']
            item['city']=response.meta['city_name']
            yield item


        #print sdata'''
        '''keyMap={'hotelId':'hotel_id','hotelUrl':'hotelUrl','isHideAmount':'isHideAmount','hotelSmallPic':'hotelSmallPic','city':'city','hotelBigPic':'hotelBigPic','currency':'currency','hotelName':'hotel_name','hotelZoneName':'hotelZoneName','loc_id':'loc_id','hotelAmount':'hotelAmount','hasPromotion':'hasPromotion','hasCoupon':'hasCoupon','hotelPreAmount':'hotelPreAmount','hotelReviewsCount':'hotelReviewsCount','hotelStarLicence':'hotelStarLicence','hotelStarCount':'hotelStarCount','lat':'lat','lng':'lng','isBookable':'isBookable','hotelRating':'hotelRating','saleTxt':'saleTxt','isMemberPromotePrice':'isMemberPromotePrice','hasAverageRate':'hasAverageRate','averageRate':'averageRate','hotelFacility':'hotelFacility','reviewUrl':'reviewUrl','evaluateStr':'evaluateStr','hotelFacilityName':'hotelFacilityName','taReviewsCount':'taReviewsCount','taReviewsIcon':'taReviewsIcon','taReviewUrl':'taReviewUrl','LandMarkDistance':'LandMarkDistance','hasPromotionCode':'hasPromotionCode','HasDiffPrice':'HasDiffPrice','MaxDiffPriceLabel':'MaxDiffPriceLabel','SalesType':'SalesType','RoomId':'RoomId','startPrice':'startPrice','couponType':'couponType','couponAmount':'couponAmount','couponTxt':'couponTxt'}#'cityname':'city','provincename':'state'}        
        for r in sdata['HotelResultModel']:
            r.update({'loc_id':response.meta['city'],'city':response.meta['city_name']})
            final_li.append({keyMap[k]: v for k, v in r.items()})
        final_li1=[{k:d[k] for k in ('hotel_id','hotel_name','loc_id','city')} for d in final_li]
        #print final_li
        try:            
            record.insert_many(final_li1, ordered=False)
        except pymongo.errors.BulkWriteError, e:
            pass'''
            #print 'location is already avilable collection ,   ' + str(e)
        #record.createIndex({'hotel_id':1},{unique:True,autoIndexId: False})
        #print final_li[0]['hotel_id']
        #print repr(final_li[0]['hotel_name']).encode('utf-8')
        #print final_li[0]['loc_id']
        #print final_li[0]['city']'''