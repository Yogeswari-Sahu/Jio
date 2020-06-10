from flask import Flask,render_template, url_for, request, redirect, jsonify, json,flash
import pandas as pd
from datamodels import filterprod,prod,getmeasure,getreorder

app= Flask(__name__)

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
# filterlist=[]

prodQuant= []
# prod()

brandlist=[{"Apple": "Apple"},
        {"One Plus" : "One Plus"},
        {"Xiami" :"Xiami"},
        {"Iphone" : "Iphone"},
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
        if request.form['email']!= 'ysahujan042526@gmail.com' or request.form['pass']!= 'mani':
            error = 'Invalid username or password. Please try again!'
        else:
            flash('You were successfully logged in','success')
            return redirect(url_for('index'))
    return render_template('login.html', error = error ,title='Login')
    
    # if request.method == 'POST':
    #     return redirect(url_for('index'))
    # return render_template('login.html', title='Login')

@app.route('/index')
def index():
    return render_template('index.html',product_list=prodQuant)

@app.route('/add', methods=['POST']) 
def add(): 
    prod = request.form['productAdd']
    quant=request.form['Quantity']

    prodQuant.append({
        'prod':prod,
        'quant':quant 
    })
    
    return redirect(url_for('index')) 

@app.route('/filter', methods=['GET','POST']) 
def filter(): 
    if request.method == "POST":
        brand = request.form['brand']
        print(brand)
        priceSegment= request.form['price-segment']
        print(priceSegment)
        # filterlist.append({
        #     'brand' : brand,
        #     'ps' :priceSegment
        # }) 
        # print(filterlist) 
        result = filterprod(brand, priceSegment)
        print(result)
        datafinal=[]
        datafinal.append ({
           "result": result
        })
        datafinal=list(datafinal)
        print(datafinal)
        flash("Filtered", "success")
        return json.dumps(datafinal)
   # return redirect(url_for('index')) 

# @app.route('/product', methods=['GET', 'POST'])
# def product():
#     return json.dumps(datafinal)

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
    
    productchoose=request.form['products']
    pricedrop=request.form['price-drop']
    remix=request.form['remix type']
        
    randomlist=getmeasure(productchoose,prodQuant)
    reorderlist=getreorder(productchoose,prodQuant)
    submitdata.append({
        'ProdQuant':prodQuant,
        'Product_Chosen': productchoose,
        'Price_Drop': pricedrop,
        'Remix_type' : remix
    })
    print(submitdata)
    flash('Submitted successfully','success')
    return render_template('index.html',measure_list=randomlist,reorder_list=reorderlist)


if __name__ == "__main__":
    app.run(debug=True)



'''

///////sample  route (the way it should be done) ---- not to uncomment this 
    @app.route("/loadpslist", methods=['POST', 'GET'])
    def loadps():
        #mobile_brand= 'None' #default value
        msg = {}
        request_dict = dict()
        if request.method == "POST":
            request_dict = request.json
        elif request.method == "GET":
            request_dict = request.args
        #print("LoadPS is called")
        msg = [{
                "name": "All",
                "abbreviation": "-1"
            },
            {
                "name": "PS0",
                "abbreviation": "0"
            },
            {
                "name": "PS1",
                "abbreviation": "1"
            },
            {
                "name": "PS2",
                "abbreviation": "2"
            },
            {
                "name": "PS3",
                "abbreviation": "3"
            },
            {
                "name": "PS4",
                "abbreviation": "4"
            },
            {
                "name": "PS5",
                "abbreviation": "5"
            },
            {
                "name": "PS6",
                "abbreviation": "6"
            },
            {
                "name": "PS7",
                "abbreviation": "7"
            }]
        return json.dumps(msg)
'''