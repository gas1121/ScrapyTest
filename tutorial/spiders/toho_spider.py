import scrapy


class QuotesSpider(scrapy.Spider):
    name = "toho"
    start_urls = ['https://hlo.tohotheater.jp/net/schedule/076/TNPI2000J01.do']
    #start_urls = ['https://hlo.tohotheater.jp/net/ticket/076/TNPI2040J03.do?site_cd=076&jyoei_date=20170209&gekijyo_cd=0761&screen_cd=10&sakuhin_cd=014183&pf_no=5&fnc=1&pageid=2000J01&enter_kbn=']

    # success url
    # https://hlo.tohotheater.jp/net/ticket/076/TNPI2040J03.do?site_cd=076&jyoei_date=20170209&gekijyo_cd=0761&screen_cd=10&sakuhin_cd=014183&pf_no=5&fnc=1&pageid=2000J01&enter_kbn=

    # checkout to target data

    # generate schedule list

    # request data

    def parse(self, response):
        #empty_seat_count = len(response.css('[alt~="空席(選択可)"]'))
        #booked_seat_count = len(response.css('[alt~="購入済(選択不可)"]'))
        #total_seat_count = empty_seat_count + booked_seat_count

        #yield {
        #    'result': str(booked_seat_count)+'/'+str(total_seat_count)
        #}
        yield {
            'result': len(response.css('div.schedule-item'))
        }