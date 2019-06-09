from django.contrib.auth import authenticate, login
from .forms import SignupForm, SongForm
from django.contrib.auth import logout
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Album, Song
from django.db.models import Q
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import generic
from django.conf import settings

AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def index(request):
    albums = Album.objects.all()
    songs = Song.objects.all()
    fav = ''
    indx = 'active'
    query = request.GET.get('q')
    if query:
    	albums = albums.filter(Q(title__icontains=query)|Q(artist__icontains=query)).distinct()
    	songs = songs.filter(Q(title__icontains=query)).distinct()
    	return render(request,'music/index.html',{'albums':albums,'fav':fav,'indx':indx,'songs':songs})
    return render(request, 'music/index.html', {'albums': albums,'fav':fav,'indx':indx})

class CreateAlbum(CreateView):
	model = Album
	fields = ['title','artist','genre','logo']

#class AlbumDetail(generic.DetailView):
#	model = Album
#	fields = '__all__'

def albumdetail(request,id):
	album=get_object_or_404(Album,pk=id)
	return render(request,'music/album_detail.html',{'album':album})

class UpdateAlbum(UpdateView):
	model = Album
	fields = ['title','artist','genre','logo']

class DeleteAlbum(DeleteView):
	model = Album
	success_url = reverse_lazy('index')

class CreateSong(CreateView):
	model = Song
	fields = ['title','album','audio']

class DeleteSong(DeleteView):
	model = Song
	success_url = reverse_lazy('index')

class SongDetail(generic.DetailView):
	model = Song
	fields = '__all__'

def create_album_song(request,album_id):
	album = get_object_or_404(Album,pk=album_id)
	form = SongForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		song = form.save(commit=False)
		song.audio = request.FILES['audio']
		song.album = album
		song.save()
		return redirect('album-detail',id=album_id)
	return render(request,'music/song_form.html',{'form':form})

def signup(request):
	form = SignupForm(request.POST or None)
	if form.is_valid():
		form.save()
		username = form.cleaned_data.get('username')
		raw_password = form.cleaned_data.get('password1')
		email = form.cleaned_data.get('email')
		user = authenticate(username=username,password=raw_password,email=email)
		login(request, user)
		return redirect('index')
	return render(request,'music/signup.html',{'form':form})

def song_fav(request,pk):
	song = get_object_or_404(Song,pk=pk)
	user = request.user
	if not user in song.user.all():
		song.user.add(user)
		song.save()
	else:
		song.user.remove(user)
		song.save()
	return redirect('favorite-songs')

def album_fav(request,pk):
	album = get_object_or_404(Album,pk=pk)
	user = request.user
	if not user in album.user.all():
		album.user.add(user)
		album.save()
	else:
		album.user.remove(user)
		album.save()
	return redirect('favorite')

def favorite(request):
	user = request.user
	albums = user.album_set.all()
	fav = 'active'
	indx = ''
	return render(request,'music/index.html',{'albums':albums,'fav':fav,'indx':indx})

def favorite_songs(request):
	user = request.user
	songs = user.song_set.all()
	addr = 'favorite'
	return render(request,'music/song_view.html',{'songs':songs,'addr':addr})

def songs_all(request):
	songs = Song.objects.all()
	addr = 'song'
	return render(request,'music/song_view.html',{'songs':songs,'addr':addr})
