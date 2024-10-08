from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import pandas as pd
# Create your views here.

API_URL='https://disease.sh/v3/covid-19/countries'
@api_view(['GET'])
def getCovidData(request):
    if request.method=='GET':
        response=requests.get(API_URL)
        data=response.json()
        df = pd.DataFrame(data)
        selected_columns=['country','cases','deaths','recovered']
        df=df[selected_columns]
        top_countries = df.sort_values(by='cases', ascending=False).head(5)
        top_countries.to_csv("covid_data.csv",index=False)
        return Response({
            "message": "Data saved to'covid_data.csv'",
        })


