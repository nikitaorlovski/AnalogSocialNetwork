from django.http import HttpResponse
from django.shortcuts import render
def about(request):
    return HttpResponse("О сайте")


def contact(request):
    return HttpResponse("Контакты")

def test(request, pk):
    return HttpResponse(f"ID = {pk}")