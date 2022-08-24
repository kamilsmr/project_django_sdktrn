
from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect

data = {
    "telefon":["samsung s20", "samsung s21"],
    "bilgisayar":["laptop1", "laptop2"],
    "elektronik":"telefon kategorisindeki ürünler"


}

def index(request):
    categories = list(data.keys())
    return render(request, 'myapp/index.html', {
            "categories": categories
           
        })
    





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
        products = data[category]
        return render(request, 'myapp/products.html', {
            "category":category,
            "products":products
            
        })
    except:
        return HttpResponseNotFound("yanlış kategori seçimi")
