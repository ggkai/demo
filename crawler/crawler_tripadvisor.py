from bs4 import BeautifulSoup
import requests
import time

#爬一个列表的数据，猫途鹰。通过移动端爬图片
header={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    'Cookie':'VRMCID=%1%V1*id.10570*llp.%2F*e.1516026902436; PMC=V2*MS.15*MD.20180108*LD.20180108; TAUnique=%1%enc%3AI%2BOYwSMUvOav8rxuEviDSEwk%2FEZ3mJCD0UbIpfAjerNlCcwg%2FZDeZg%3D%3D; TAPD=cn.tripadvisor.com; ServerPool=C; TASSK=enc%3AAAf7Wmwj5QtgE4atfhDIfnj%2FJYPDKgdcCjDoe7hIj7HprY2Vxkk8zGmZ9TINbvUxfXF%2FrNCqj2HaQATTB%2FiPSCtbiWCoaSszeaes2vgl%2B7xmcgc8tRM9Ryomtv5SXaCnMQ%3D%3D; PAC=ACzG28R_sjPt2CaxZ-04Sl6G94wRfa1lJDk_Di6DE0T18KuKVugauQ83SJ20FVzJ2UyE7BzJQB6T7C81IMtTLrpLafogUNRp0xi_h7QCpEodOkfo6bxmAmI0tTNBB_g5dFCEfbuKK4BKdssnq6JPfwyxnhmpntco4SM_pBoxKRi5-VJhN8WNkIteGF3tHnCiuQ%3D%3D; TART=%1%enc%3ACMxqX9jI6HySGw9JxIgJ2fG5j%2BYjoJwpuKbFXT06TWRwO07cfUPt23Va3dJ6R4UFCeyaC1LeImE%3D; __gads=ID=52d91064733399ca:T=1515422126:S=ALNI_MYAgkmxadOr4ClSxyunwVRBixAo1Q; BEPIN=%1%160d63c016b%3Bweb113b.b.tripadvisor.com%3A10023%3B; ki_t=1515422840363%3B1515422840363%3B1515422840363%3B1%3B1; ki_r=; ki_u=6d10042c-d833-3688-fd0f-f1e4; ki_s=175381%3A1.1.0.0.2; TAReturnTo=%1%%2FAttractions-g60763-Activities-c47-t163-New_York_City_New_York.html; SecureLogin2=3.4%3AAN8g%2B5HoPyzLd6QN9kNBvnc4wboVndvHh8bXP1WElJo7oDMpP6roK4XGrYRWiPaS%2B%2F4EI%2FMwYPyA4fLodx1b6%2BOapUnMVqmkJbd88%2FBTf3smHSBr%2FZQob17cSedDC1B4Lkg5Z5b2HkgwYmLluUpaH%2B0IMzWG3kMjMaCZtgzPm3AcJvF6eGgxo9MJ0tsoXwPcQ%2B7wyW2zH2qaVj%2Faq8f5Gw0%3D; TAAuth3=3%3Ab0305713413af40e43a4da826383d995%3AAHuO6HYeax0Vs5%2FTTKI%2BFJmb60vWUGdvpz06linUR1TLgCAxCzb9zhF9ADP%2BHsHWhzR%2FQ0BMYAWiKsU7cdbINdc0FIlKDqiG4q15UCkLV4gpfWk3Q1Jd79hJpO%2FqZFDPy7T2mkGBUFLycuPWcUxtgrl1QTLO2SS6t0rW9B27OErrP6mifazLtNGiGeqXniS7cCAkahNE%2Fe%2F6ZxjvFDlzYb8%3D; CM=%1%HanaPersist%2C%2C-1%7Cpu_vr2%2C%2C-1%7CPremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CRestAds%2FRPers%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7Cpu_vr1%2C%2C-1%7CFtrPers%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C2%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CRestPartSess%2C%2C-1%7Ccatchsess%2C7%2C-1%7Cbrandsess%2C%2C-1%7CRestPremRSess%2C%2C-1%7CCpmPopunder_1%2C3%2C1515511239%7CCCSess%2C%2C-1%7CCpmPopunder_2%2C3%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7C%24%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CRestAdsPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CSPMCSess%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7Cmds%2C1515422737368%2C1515509137%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CRestAds%2FRSess%2C%2C-1%7CHomeAPers%2C%2C-1%7C+r_lf_1%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7C+r_lf_2%2C%2C-1%7Ccatchpers%2C3%2C1516027541%7CLaFourchette+MC+Banners%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7CRestPartPers%2C%2C-1%7CRestPremRPers%2C%2C-1%7Cvr_npu2%2C%2C-1%7Csh%2C%2C-1%7CLastPopunderId%2C137-1859-null%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7Cvr_npu1%2C%2C-1%7CCCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cbrandpers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CSPMCPers%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CWarPopunder_Session%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CWarPopunder_Persist%2C%2C-1%7CTheForkORPers%2C%2C-1%7Cr_ta_2%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7Cr_ta_1%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CCPNC%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; roybatty=TNI1625!AKhnUVKscXTG5ACoOt6QmvNWR3gJ5TxVtrmj4KgZGQfdQ36IK6QRhtVn1QLc0S0tC%2Fq883Q3BfpcNenhVYnYq58RFoKivGii%2FXEcqLYLsQB8NVF15R3gRsyFBiARHjs5U%2BuPInhTwBqAEQ5maVtBGgFF%2B8%2B6WJ37JyjbquW3a3E6%2C1; TASession=%1%V2ID.B1A3B727DDC0052E6648680F0C3B5124*SQ.74*PR.427%7C*LS.DemandLoadAjax*GR.31*TCPAR.85*TBR.16*EXEX.76*ABTR.1*PHTB.57*FS.90*CPU.74*HS.recommended*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.86075DCE56A07D883F0665E02F2732A0*LF.zhCN*FA.1*DF.0*IR.1*OD.null*MS.-1*RMS.-1*FLO.60763*TRA.true*LD.60763; TATravelInfo=V2*AY.2018*AM.1*AD.9*DY.2018*DM.1*DD.10*A.2*MG.-1*HP.2*FL.3*RVL.305921_8l294217_8l60763_8*DSM.1515424931197*RS.1; TAUD=LA-1515422118444-1*RDD-1-2018_01_08*HD-618926-2018_01_09.2018_01_10*LD-2812734-2018.1.9.2018.1.10*LG-2812736-2.1.F.'
}
url_saves='https://cn.tripadvisor.com/Saves/70844269'
url='https://cn.tripadvisor.com/Attractions-g60763-Activities-c47-t163-New_York_City_New_York.html'
urls=['https://cn.tripadvisor.com/Attractions-g60763-Activities-c47-t163-oa{}-New_York_City_New_York.html#FILTERED_LIST'.format(str(i)) for i in range(30,150,30)]
def get_attractions(url,data=None):
    wb_data = requests.get(url)
    time.sleep(2)#每次请求延时2秒
    soup = BeautifulSoup(wb_data.text, 'lxml')
    # titles=soup.select('#ATTR_ENTRY_ > div.attraction_clarity_cell > div > div > div.listing_info > div.listing_title > a')
    titles = soup.select('div.listing_title > a[target="_blank"]')
    images = soup.select('img[width="180"]')
    for title, image in zip(titles, images):
        data = {
            'title': title.get_text(),
            'image': image.get('src')
        }
        print(data)
#图片爬取不了
def get_favs(url,data=None):
    wb_data = requests.get(url, headers=header)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    titles = soup.select(
        '#trip-item-collection-container > div > div > div.saves-location-details.ui_media > div.media-content > div > a')
    images = soup.select(
        '#trip-item-collection-container > div > div > div.saves-location-details.ui_media > div.media-left > a')
    for title, image in zip(titles, images):
        data = {
            'title': title.get_text(),
            'image': image.get('url')
        }
        print(data)

for singal_url in urls:
    get_attractions(singal_url)
