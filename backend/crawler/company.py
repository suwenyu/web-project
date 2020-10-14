import sys, os, json
import django
from tqdm import tqdm
from django.db import IntegrityError

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from stock.models import Company
# # Your script code
import requests
from bs4 import BeautifulSoup

url = "https://www.cnyes.com/twstock/stock_astock.aspx"
# res = requests.get(url)
# soup = BeautifulSoup(res.text, "html.parser")

# if res.status_code != 200:
#     raise Exception("Can not reach the website")

class CompanyCrawler:
    def __init__(self, url):
        self.url = url
        self.res = requests.get(url)
        self.soup = BeautifulSoup(self.res.text, 'html.parser')
        self.cate_url = []
        self.base_url = "https://www.cnyes.com/twstock/"

    def get_cate(self, id):
        table = self.soup.find(id=id)
        cate_list = table.find("ul", class_="kdlist")
        for item in cate_list.find_all("li"):
            link = item.find("a").get("href")
            cate = item.text
            self.cate_url.append(link)

    def get_comp(self):
        for value in self.cate_url:
            response = requests.get(self.base_url + value)
            content = BeautifulSoup(response.text, 'html.parser')
            table = content.find("table")
            for item in tqdm(table.find_all("tr")):
                if item.find("td"):
                    try:
                        ticker = item.find_all("td")[1].text
                        name = item.find_all("td")[2].text
                        self.get_detail(ticker)
                    except IndexError:
                        print(value)

    def get_detail(self, ticker):
        url = "https://marketinfo.api.cnyes.com/mi/api/v1/TWS:{}:STOCK/info"
        res = requests.get(url.format(ticker))
        comp_data = json.loads(res.text)

        data = {
            "name_ch": comp_data["data"]["companyName"],
            "name_en": comp_data["data"]["companyEnglishName"],
            "address": comp_data["data"]["companyAddress"],
            "category": comp_data["data"]["industryType"],
            "description": comp_data["data"]["description"],
            "ticker": comp_data["data"]["symbolId"],
            "stocktype": comp_data["data"]["stockType"],
            "website": comp_data["data"]["url"],
        }
        try:
            Company.objects.create(**data)
        except IntegrityError:
            print(data)
            return


    def run(self):
        self.get_cate("kinditem_0")
        self.get_cate("kinditem_1")
        self.get_comp()

crawler = CompanyCrawler(url)
crawler.run()