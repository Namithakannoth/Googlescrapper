from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.


def home(request):
    if request.method == "POST":
        mysearch = request.POST.get('data')
        completeData = requests.get("https://www.ask.com/web?q="+mysearch).text

        soup = BeautifulSoup(completeData, "html.parser")
        allboxes = soup.find_all('div', {'class': 'PartialSearchResults-item'})

        complete_details = []
        for i in allboxes:  
            title = i.find(
                class_="PartialSearchResults-item-title-link result-link").text
            greenData = i.find(class_="PartialSearchResults-item-url").text
            description = i.find(
                class_="PartialSearchResults-item-abstract").text

            urlRedirect = i.find('a').get('href')
            complete_details.append(
                (title, greenData, description, urlRedirect))

        return render(request, "home.html", {'complete_details': complete_details})

    return render(request, "home.html")
