from bs4 import BeautifulSoup
import requests
'''
url = 'https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')
titles = soup.select('div.listing_title > a[target="_blank"]')
imgs = soup.select('img[width="180"]')
cates = soup.select('div.tag_line > div')

for title,img,cate in zip(titles,imgs,cates):
    data = {
        'title':title.get_text(),
        'img':img.get('src'),
        'cate':list(cate.stripped_strings),
    }
    print(data)
'''
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Cookie':'TAUnique=%1%enc%3ANdDkxEKluHSGZC1KfQx7uQiErOwopSY%2BxyICitsVTKB9i1%2B2aew%2BBQ%3D%3D; ServerPool=B; TASSK=enc%3AAOgDpHz%2Fvjg8Kn7P2W4i2ZbrnO2E0K5hBAritIKd8%2B77MZb3OeX6cTR90Mh3IMlQ2Kg14UmWszRl9JsrOelAGwAyUDx1%2BoODPWe2raylgtfP7uvCKQzR%2Fe2HYA%2Bkc0PrAw%3D%3D; VRMCID=%1%V1*id.16631*llp.%2F-a_ttcampaign%5C.MTYpc-a_ttgroup%5C.title-m16631*e.1493658782075; _jzqy=1.1493053992.1493053992.1.jzqsr=baidu|jzqct=tripadvisor.-; _jzqckmp=1; __gads=ID=ca68b26f5c7d47a5:T=1493053987:S=ALNI_MZ_gZPREj8iu7rWcY17T-J-VBjdew; CommercePopunder=SuppressAll*1493054012090; SecureLogin2=3.4%3AAMthDXLYoJ3reLXiMMOPN5UtW68VYcY4XwwGk%2FOBTLOyRCp5MSzkjYGAgrYUzmu6PsNHj5aAkeYJ2PwP1pIbW99QSdMfZDt0gjQiiw2%2FFjljdLwIYN4EhOPt5Y0exGVm3THsDJKJkiapfPeEjaZJciy8w53irBCGb3YCly%2FV8%2BjTvE35qrbVOQsHq3XjbLQVWpCuM6tx3L3Y3OzwvdrWmZc%3D; TAAuth2=%1%3%3A46eac775c79beff574103b8f73515f52%3AAKX0sa2%2B7SPGOCRpi87EIxcI%2FEXKGAEdqNlqTMmokLGJc82A5kTc6nglEtWVsEqc%2FOEsn4RK6GEy338oSrtbQpGjTtc9nYJe7fxEPx4AKnyPXosT8dAYEpICn6UdxhQyeNEOUC9MQPxmbcwtKKtsMfdAPy6lTq3hbQnYtIIKvjSMPngASl%2Ba213mGQaRhMTlVmaWkesoF2eVAt%2BegNNFm5LnqY3rMfISgjPxHiGt2crM; _jzqx=1.1493056397.1493056397.1.jzqsr=tripadvisor%2Ecn|jzqct=/attractions-g60763-activities-new_york_city_new_york%2Ehtml.-; _smt_uid=58fe3227.33fab745; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RVL.60763_114l105127_114l1687489_114l105125_114*RS.1; CM=%1%HanaPersist%2C%2C-1%7CHanaSession%2C%2C-1%7CFtrSess%2C%2C-1%7CRCPers%2C%2C-1%7CHomeAPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CRCSess%2C%2C-1%7CFtrPers%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C2%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CPremiumMCSess%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CViatorMCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Csesssticker%2C%2C-1%7CViatorMCSess%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CSaveFtrSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; TAReturnTo=%1%%2FAttraction_Review-g60763-d105125-Reviews-The_Metropolitan_Museum_of_Art-New_York_City_New_York.html; roybatty=TNI1625!ADO%2BZkUAMiUxkknLQvB%2FiDjZS2Imxj9dChoeiWE9BxIpUa9tcoF0fPrXrJLQG3yAXBPQchcYDGiSaArsIQdKt%2Fqr%2Fc%2FZffS6Do4tQa%2F%2B1DHanrkTmq6eRR3l4PkE4c6fH7gfTwrmmao%2BPhGcDz%2Bst8ZShlcaz8Ra6KYi8CmUadUX%2C1; _ga=GA1.2.1305908954.1493053991; _gat_UA-79743238-4=1; TASession=%1%V2ID.59629021D580A9CA80C2CBC813E89F31*SQ.64*MC.13091*LR.https%3A%2F%2Ftripadvisor%5C.woqu%5C.com%2Fcenter%2Forder*LP.%2F*PR.427%7C*LS.ActionRecord*GR.48*TCPAR.35*TBR.35*EXEX.3*ABTR.15*PHTB.49*FS.4*CPU.86*HS.popularity*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.BBD13DFB8055AD7ECDA38CEBA49115A5*LF.zhCN*FA.1*DF.0*MS.-1*RMS.-1*FLO.60763*TRA.true*LD.105125*BG.60763*BT.hm5r01; TAUD=LA-1493053982011-1*RDD-1-2017_04_24*LG-2556682-2.1.F.*LD-2556683-.....; _qzja=1.1259936190.1493053998735.1493053998736.1493056397302.1493056518994.1493056545946..0.0.14.2; _qzjb=1.1493056397302.9.0.0.0; _qzjc=1; _qzjto=14.2.0; _jzqa=1.2298729034767568000.1493053992.1493053992.1493056397.2; _jzqc=1; Hm_lvt_2947ca2c006be346c7a024ce1ad9c24a=1493053992,1493056413; Hm_lpvt_2947ca2c006be346c7a024ce1ad9c24a=1493056546; _jzqb=1.9.10.1493056397.1',
}

url_saves = 'https://www.tripadvisor.cn/Saves/683779'
wb_data = requests.get(url_saves,headers=headers)
soup = BeautifulSoup(wb_data.text,'lxml')
titles = soup.select('a')
print(titles)