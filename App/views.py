from django.shortcuts import render,get_object_or_404
from .models import Song
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    songs =Song.objects.all()
    paginator =Paginator(Song.objects.all().order_by('id'),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'index.html',{
        'page_obj':page_obj,
        'all_songs':songs,
    })

def song_detail(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    return render(request, 'song_detail.html', {'song': song})