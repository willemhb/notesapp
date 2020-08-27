"""notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListNotes.as_view(), name="list_notes"),
    path("<int:pk>/", views.NotesDetail.as_view(), name="notes_detail"),
    path("create/", views.CreateNote.as_view(), name="notes_create"),
    path("search/", views.search_notes, name='search_notes'), 
    path("<int:pk>/edit/", views.UpdateNote.as_view(), name="notes_update"),
    path("<int:pk>/delete/", views.DeleteNote.as_view(), name="notes_delete"),
]
