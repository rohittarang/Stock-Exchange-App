from django.shortcuts import render
import requests
import json

# Create your views here.

def Index(request):
    api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_df9e96a139ec4c78b06b6288f9c07286")
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error, Data not loading"
    
    return render(request,'index.html',{'api':api})