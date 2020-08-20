from django.shortcuts import render
from . import test_model
from . import ML_Model

def home(requests):
    return render(requests, 'index.html')

def result(requests):
    pclass = int(requests.GET['pclass'])
    sex    = int(requests.GET['sex'])
    age    = int(requests.GET['age'])
    sibsp  = int(requests.GET['sibsp'])
    parch  = int(requests.GET['parch'])
    fare   = int(requests.GET['fare'])
    embarked = int(requests.GET['embarked'])
    title  = int(requests.GET['title'])

    prediction = ML_Model.predict_Model(pclass, sex, age, sibsp, parch, fare, embarked, title)
    return render(requests, 'result.html',{'result':prediction})
