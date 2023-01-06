from django.shortcuts import render
from django.core.paginator import Paginator
from linkpage.models import *


# Create your views here.

def home(request):
    linkset = Rentry.objects.select_related('creator').order_by('creator__-views')
    query = request.GET.get('q')

    if query:
        linkset = linkset.filter(creator__name__icontains = query)
    
    paginator = Paginator(linkset, 15)
    page = request.GET.get('page')
    links = paginator.get_page(page)
    context = {
        "link" : links
    }
    return render(request, "homepage.html", context)

