from django.shortcuts import render
from .models import Todos, Got
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# Create your views here.

def index(request):
    return render(request,"home.html",{})
def todos(request):
    context = {"todos_list": Todos.objects.all()}
    return render(request,"todos.html",context)


def gots(request):
    context = {"gots_list": Got.objects.all()}
    return render(request, "gots.html", context)

def add(request):
    return render(request, "add.html", {})


def addrecord(request):
    x = request.POST["name"]
    todo = Todos(name=x)
    todo.save()
    return HttpResponseRedirect(reverse("index"))


def delete(request, id):
    todo = Todos.objects.get(pk=id)
    todo.delete()
    got=Got(name=todo.name)
    got.save()
    return HttpResponseRedirect(reverse("index"))

def posts(request):
    posts=pd.read_csv("C:/Users/elnur/OneDrive/Masaüstü/QSS/Python/django/todolist/todos/posts.csv")
    context={"posts":posts,"columns":["Domain","Votes","Dates","Links"]}
    return render(request, "posts.html", context)

def pandas(request):
    return render(request, "pandas.html", {})

def adddataframe(request):
    x = request.POST["name"]
    df=pd.read_csv("C:/Users/elnur/Downloads/"+x)
    context={
        "dfname":x,
        "df":df
    }
    return render(request, "df.html", context)


def encoder(request):
    x = request.POST["name"]
    y=request.POST["column"]
    model = request.POST["regressor"]
    outlier = request.POST["outlier"]
    df=pd.read_csv("C:/Users/elnur/Downloads/"+x)
    df.dropna(inplace=True)
    df2 = df.apply(LabelEncoder().fit_transform)
    
   
    if outlier=="remove":
        data1=stats.zscore(df2)
        df2=df2[(data1<3).all(axis=1)]
    else:
        pass

    if model=="LinearRegression":
        regressor=LinearRegression()
    elif model=="KNeighborsClassifier":
        regressor=KNeighborsClassifier()
    else:
        regressor=LogisticRegression()
    X=df2.drop(y, axis=1)
    Y=df2[y]
    X_train, X_test, y_train, y_test=train_test_split(X, Y, test_size=0.2, random_state=0)
    regressor.fit(X_train, y_train)
    y_pred1 = regressor.predict(X_test)
    score=regressor.score(y_test, y_pred1)
    context={
        "encodered":x,
        "df2":df2,
        "score":score
    }
    return render(request, "df.html", context)
