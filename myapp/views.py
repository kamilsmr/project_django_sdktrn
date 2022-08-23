
from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect

data = {
    "telefon":"telefon kategorisindeki ürünler",
    "bilgisayar":"telefon kategorisindeki ürünler",
    "elektronik":"telefon kategorisindeki ürünler"


}

def index(request):
    return HttpResponse("index")

def details(request):
    return HttpResponse("details")



# dinamik kategori


def getProductsByCategoryId(request, category_id):
    category_list = list(data.keys())
    if category_id > len(category_list):
        return HttpResponseNotFound("yanlış kategori seçimi")
    redirect_text = category_list[category_id-1]
    return redirect("/" + redirect_text)

# HttpResponseRedirect ve redirect aynı görevi yapar fakat 
# HttpResponseRedirect importunu from django.http.response import HttpResponse, HttpResponseRedirect
# redirect importunu from django.shortcuts import render, redirect
def getProductsByCategory(request, category):
    try:
        category_text = data[category]
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("yanlış kategori seçimi")
