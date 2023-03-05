from django.urls import path

from . import views

urlpatterns = [
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("new/", views.new_page, name="new_page"),
    path("edit/", views.edit, name="edit"),
    path("save_edit/", views.save_edit, name="save_edit"),
    path("random_page/", views.random_page, name="random_page" ),
    path("create", views.createListing, name="create"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("displayCategory", views.displayCategory, name="displayCategory"),
    path("addComment/<int:id>", views.addComment, name="addComment")
]
