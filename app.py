from flask import Flask,render_template, url_for, request, redirect, jsonify, json,flash
# from flask_cors import CORS
import pandas as pd
from datamodels import filterprod,prod,getmeasure,getreorder

app= Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
# filterlist=[]
# prod()
prodQuant=[]


brandlist=[{"Apple": "Apple"},
        {"One Plus" : "One Plus"},
        {"Xiami" :"Xiami"},
        {"Nexus":"Nexus"},
        {"Vivo": "Vivo"},
        {"Nokia": "Nokia"},
        {"Samsung": "Samsung"}
        ]


segment=[{'ps1':'0-10000 '},
        {'ps2': '10000-20000 '},
        {'ps3': '20000-30000 '},
        {'ps4': '30000-40000 '},
        {'ps5': '40000-50000 '},
        {'ps6': '50000-60000 '},
        {'ps7': '60000-70000 '}
      ]


submitdata =[]

@app.route('/', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('login.html', error = error ,title='Login')
    

@app.route('/index')
def index():
    return render_template('index.html',product_list=prodQuant)


@app.route('/filtervalues', methods=['GET','POST']) 
def filtervalues():
    if request.method == "POST":
        print(request.get_json())
        brand = request.get_json()['brand']
        # print(brand)
        priceSegment= request.get_json()['priceSegment']
        # print(priceSegment)
        # filterlist.append({
        #     'brand' : brand,
        #     'ps' :priceSegment
        # }) 
        # print(filterlist)
        result = filterprod(brand, priceSegment)
        print(result)
        
        return json.dumps(result)     

@app.route('/sender', methods=['GET', 'POST'])
def sender():
    
    filter_data =[{
        "brands" : brandlist,
        "segments" : segment,
        "products":  prod()
    }]
    return json.dumps(filter_data)


@app.route('/submit', methods=['POST']) 
def submit(): 
    getjson=request.get_json()
    print(getjson)
    productchoose=getjson['product']
    pricedrop=getjson['priceDrop']
    remix=getjson['remix']
    prodQuant=getjson['prodQuant']
    print(prodQuant)
    randomlist=getmeasure(productchoose,prodQuant)
    # random=getjson['randomlist']
    # print(randomlist)
    reorderlist=getreorder(productchoose,prodQuant,randomlist)
    # reorder=getjson['reorderlist']
    # print(reorderlist)
    submitdata.append({
        'ProdQuant':prodQuant,
        'Product_Chosen': productchoose,
        'Price_Drop': pricedrop,
        'Remix_type' : remix
    })
    print(submitdata)
    outputtable=[{
        "randomlist":randomlist,
        "reorderlist": reorderlist
    }]
    flash('Submitted successfully','success')
    return json.dumps(outputtable)
 
if __name__ == "__main__":
    app.run(debug=True)


