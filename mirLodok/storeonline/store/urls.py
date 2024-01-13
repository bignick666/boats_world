from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'app_store'

urlpatterns = [
    path('', views.index, name='index'),
    path('allmotors', views.show_motors, name='toha_motors'),
    path('<slug:slug>', views.other_motors, name='other_motors'),
    path('<slug:slug>/<int:item_id>', views.show_item, name='show_item'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
