from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    t = datetime.now()
    return render(request, "index.html", {"t": t})