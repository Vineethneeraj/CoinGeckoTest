import json

from flask import Flask,request,render_template,jsonify
from pycoingecko import CoinGeckoAPI

cg=CoinGeckoAPI(demo_api_key="CG-WYG91YRHY5Dcy3sjYaaNvEts")
app = Flask(__name__)

#To get all coins list in market
@app.route("/")
def index():
    page_result = cg.get_coins_markets(vs_currency='inr',page=1,per_page=10)
    return jsonify(page_result)
@app.route("/<int:limit>/page/<int:page_number>",methods=['GET','POST'])
def index_page(limit,page_number):
    page_result=''
    #limiting values per_page and pagination
    if request.method == "GET":
        page_result = cg.get_coins_markets(vs_currency='inr',page=page_number,per_page=limit)
    return jsonify(page_result)

#To search different currency
@app.route("/search=<name>",methods=['POST','GET'])
def search(name):
    if request.method=='GET':
       search_term=cg.get_price(ids=name,vs_currencies="inr")
       return search_term
#To get all coins according to their categories
@app.route("/categories",methods=['POST','GET'])
def page1_categories():
    categories_result=cg.get_coins_categories(vs_currency='inr', page=1, per_page=10)
    return jsonify(categories_result)
@app.route("/categories/<limit>/page/<page_number>",methods=['GET','POST'])
def pages_categories(limit,page_number):
    if request.method=='GET':
        categories_result=''
        if int(limit)>10 and int(page_number)>1:
            categories_result=cg.get_coins_categories(vs_currency='inr',page=int(page_number),per_page=int(limit))
        else:
            categories_result = cg.get_coins_categories(vs_currency='inr', page=1, per_page=10)
        return jsonify(categories_result)


