from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^signup/$',views.signup,name='signup'),
	url(r'^song/all/$',views.songs_all,name='songs'),
	url(r'^favorite/$',views.favorite,name='favorite'),
	url(r'^song/favorite/$',views.favorite_songs,name='favorite-songs'),
	url(r'^song/(?P<pk>[0-9]+)/favorite/$',views.song_fav,name='song-favorite'),
	url(r'^album/(?P<pk>[0-9]+)/favorite/$',views.album_fav,name='album-favorite'),
	url(r'^album/add/$',views.CreateAlbum.as_view(),name='add-album'),
	url(r'^album/(?P<id>\d+)/$',views.albumdetail,name='album-detail'),
	url(r'^album/add/(?P<pk>\d+)/$',views.UpdateAlbum.as_view(),name='update-album'),
	url(r'^album/add/(?P<pk>\d+)/delete/$',views.DeleteAlbum.as_view(),name='delete-album'),	
	url(r'^song/createsong/$',views.CreateSong.as_view(),name='create-song'),
	url(r'^album/(?P<album_id>\d+)/createsong/$',views.create_album_song,name='create-album-song'),
	url(r'^deletesong/(?P<pk>[0-9]+)/$',views.DeleteSong.as_view(),name='delete-song'),
	url(r'^song/(?P<pk>[0-9]+)/$',views.SongDetail.as_view(),name='song-detail'),
	url(r'^$',views.index,name='index'),
]