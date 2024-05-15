from django.http import HttpResponse
def index(request):
    return HttpResponse("<h2>Главная</h2>")

def about(request):
    return HttpResponse("О сайте")


def contact(request):
    return HttpResponse("Контакты")
