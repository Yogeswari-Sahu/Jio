# from flask import Flask,render_template, url_for, request, redirect, jsonify, json, flash,current_app
import pandas as pd
import random

FILENAME='ProductData.csv'

# with app.app_context():
#     # within this block, current_app points to app.
#     print current_app.name

# df=()
# def fileavailable():
#     try:
#         file = pd.read_csv(FILENAME)
#         return True
#             # if df:
#             #     print('sucsess')
#             # else:
#                 # print('get one more')
#     except:
#         return False
        

df = pd.read_csv(FILENAME)

# except Exception as e:
#     print('heelllllooooo exc')
#     flash('File not found','error')

dfprod=[]
reorder=[]
randomlist=[]
# quant=[12,34,56,32,11]

def filterprod(brand,priceSegment):
    if(brand and priceSegment):
        df1=df[df['Price Segment']==priceSegment]
        # print(df1)
        df2=df1[df1['Brand']==brand]
        dffinal=df2['Product']
        # dffinal=dffinal.to_json(orient='values')
        dffinal=list(dffinal)
        print(dffinal)
        return dffinal
    elif(brand):
        df1=df[df['Brand']==brand]
        dffinal=df1['Product']
        # dffinal=dffinal.to_json(orient='values')
        dffinal=list(dffinal)
        print(dffinal)
        return dffinal
    elif(priceSegment):
        df1=df[df['Price Segment']==priceSegment]
        dffinal=df1['Product']
        # dffinal=dffinal.to_json(orient='values')
        dffinal=list(dffinal)
        print(dffinal)
        return dffinal

def prod():
    dffinal=df['Product']
    col=list(dffinal)
    # dffinal=dffinal.to_json(orient='values')
    # print(col)
    return col

def brand():
    dffinal=df['Brand'].unique()
    col=list(dffinal)
    # dffinal=dffinal.to_json(orient='values')
    print(col)
    return col


def ps():
    dffinal=df[['priceSegmentList','priceValueList']]
    # dffinal.set_index('priceSegmentList')['priceValueList'].to_dict()
    col=list(dffinal)
    # col=dffinal.to_dict()
    # dffinal=dffinal.to_json(orient='values')
    print(col)
    return col

def getmeasure(self_context,cross_context):
    randomlist = []
    for i in range(len(cross_context)):
        n = round(random.uniform(0.5,1.5),2)
        p=cross_context[i]['prod']
        randomlist.append({
            'prod':p,
            'meas':n
        })
    return randomlist
    
def getreorder(self_context,cross_context):
    randomlist = getmeasure(self_context,cross_context)
    reorder = []
    for i in range(len(randomlist)):
        r=randomlist[i]['meas']
        q=float(cross_context[i]['quant'])
        reo=round(q*r)
        p=cross_context[i]['prod']
        reorder.append({
            'prod':p,
            'quant':q,
            'reorder':reo
        })
    return reorder
