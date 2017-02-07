# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http.request import QueryDict
from django.http import request
import traceback
from django.http.response import JsonResponse
from WebUI.models import OrderModel
import json
#import pdb

global allResult
allResult = []

# Create your views here.
def mainInputForm(req):
#    pdb.set_trace()
    try:
        return render(req, 'mainInputForm.html', req.GET.dict())
    except:
        return render(req, 'mainInputForm.html')

def singleOrderForm(req):
    return render(req, 'singleOrderForm.html')    

def showResult(req):
    return render(req, 'showResult.html', { 'allResult': allResult} )

def submitOrder(req):
    print("SubmitOrder come in");
    returnDict = {} 

    if req.method == "POST":
        try:
            jsonStr = ""
            for key in req.POST:
                jsonStr = key
#                print jsonStr
                break
                
            jsonObj = json.loads(jsonStr)
            curOrderModel = OrderModel()
            for curData in jsonObj:
                if curData["id"] == "MAWBNO":
                    curOrderModel.MainID = curData["val"]
                if curData["id"] == "airCompany":
                    curOrderModel.AirComp = curData["val"]
                if curData["id"] == "mainOrderInputDate":
                    curOrderModel.MainOrderInputDate = curData["val"]
                if curData["id"] == "MAWBNO":
                    curOrderModel.MAWBNO = curData["val"] 
                if curData["id"] == "OrderComp":
                    curOrderModel.OrderComp = curData["val"] 
                if curData["id"] == "OrderSubmitor":
                    curOrderModel.OrderSubmitor = curData["val"]  
                if curData["id"] == "ShipperNameAndAddr":
                    curOrderModel.ShipperNameAndAddr = curData["val"]
                    
            if "" != curOrderModel.MainID:
                    allResult.append(curOrderModel) 
    
                                                   
            returnDict["errorCode"] = "0"           
        except:
            returnDict["errorCode"] = "2"
            print traceback.format_exc()
            returnDict["errorMsg"] = traceback.format_exc()
    else:
        returnDict["errorMsg"] = "request method is not post"
        returnDict["errorCode"] = "1"
    
    return JsonResponse(returnDict)
    













