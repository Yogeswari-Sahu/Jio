# from flask import Flask,render_template, url_for, request, redirect, jsonify, json
import pandas as pd
import random


df = pd.read_csv('ProductData.csv')
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
    return 'line36'

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
    
# def getreorder(self_context,cross_context):
#     for i in range(len(getmeasure(self_context,cross_context))):
#         r=randomlist[i]['meas']
#         # print(r)
#         q=cross_context[i]['quant']
#         # print(q)
#         reo=round(q*r)
#         p=cross_context[i]['prod']
#         reorder.append({
#             'prod':p,
#             'quant':q
#             'reorder':reo
#         })
#     print(reorder)
#     return reorder
    
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
