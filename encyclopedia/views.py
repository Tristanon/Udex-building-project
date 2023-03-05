from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.db.models import Q
import markdown
import random
from django.urls import reverse
from .models import User, Listing, Category, Comment
from . import util

def convert_md_to_html(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)
    
def addComment(request, id):
    currentUser = request.user
    listingData = Listing.objects.get(pk=id)
    message = request.POST['newComment']
    newComment = Comment(
        author=currentUser,
        listing=listingData,
        message=message,
    )
    newComment.save()
    return HttpResponseRedirect(reverse("listing", args=(id, )))

def listing(request, id):
    listingData = Listing.objects.get(pk=id)
    allComments = Comment.objects.filter(listing=listingData)
    return render(request, "encyclopedia/listing.html",{
        "listing": listingData,
        "allComments": allComments
    })

def index(request):
    # wiki_list = util.list_entries()
    # css_file = util.get_entry("CSS")
    # coffee = util.get_entry("coffee")
    activeListings = Listing.objects.filter(isActive=True)
    allCategories = Category.objects.all()
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "listings": activeListings,
        "categories": allCategories,  
    })

def displayCategory(request):
    if request.method == "POST":
        categoryFromForm = request.POST['category']
        category = Category.objects.get(categoryName = categoryFromForm)
        activeListings = Listing.objects.filter(isActive=True, category=category)
        allCatagories = Category.objects.all()
        return render(request, "encyclopedia/index.html",{
            "listings": activeListings,
            "categories": allCatagories,
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "encyclopedia/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "encyclopedia/login.html")
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "encyclopedia/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "encyclopedia/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "encyclopedia/register.html")

def entry(request, title):
    html_content = convert_md_to_html(title)
    if html_content == None:
        return render(request, "encyclopedia/error.html",{
            "message": "This entry does not exist"
        })
    else:
        return render(request, "encyclopedia/entry.html",{
            "title": title,
            "content": html_content,
        })
def createListing(request):
    if request.method == "GET":
        allCategories = Category.objects.all()
        return render(request, "encyclopedia/create.html",{
            "categories": allCategories
        })
    else:
        # Get the data from the form
        title = request.POST["title"]
        description = request.POST["description"]
        imageUrl = request.POST["imageUrl"]
        Completed = request.POST["Completed"]
        Namefor = request.POST["Namefor"]
        Architect = request.POST["Architect"]
        Style = request.POST["Style"]
        Materials = request.POST["Materials"]
        Location = request.POST["Location"]
        Address = request.POST["Address"]
        Phone = request.POST["Phone"]
        category = request.POST["category"] 


        # Who is the user
        currentUser = request.user

        # Get all content about the particular category
        categoryData = Category.objects.get(categoryName = category)

        # Create a new listing object
        newListing = Listing(
            title=title,
            description=description,
            imageUrl=imageUrl,
            Completed=Completed,
            NameFor=Namefor,
            Architect=Architect,
            Style=Style,
            Materials=Materials,
            author=currentUser,
            Location=Location,
            Address=Address,
            Phone=Phone,
            category = categoryData,
        )

        # Insert the object in our database
        newListing.save()
        # Redirect to index page
        return HttpResponseRedirect(reverse(index))
    
def search(request):
    if request.method == "POST":
        building_search = request.POST['search']
        buildings = Listing.objects.filter(Q(description__contains = building_search)| Q(title__contains=building_search) | Q(NameFor__contains=building_search))
        return render(request, "encyclopedia/search.html",{
            "building_search": building_search,
            "buildings" : buildings
        })
    else:
        return render(request, "encyclopedia/search.html",{})
    


        # activeListings = Listing.objects.filter(isActive=True)
        # html_content = convert_md_to_html(entry_search)
        # if html_content is not None:
        #     return render(request, "encyclopedia/entry.html",{
        #     "title": entry_search,
        #     "content": html_content,
        #     })
        # else:
        #     allEntries = util.list_entries()
        #     recommendation = []
        #     for entry in allEntries:
        #         if entry in allEntries:
        #             if entry_search.lower() in entry.lower():
        #                 recommendation.append(entry)
        #     return render(request, "encyclopedia/search.html",{
        #             "recommendation": recommendation,
        #     })

def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html") 
    else:
        title = request.POST['title']
        content = request.POST['content']
        titleExist = util.get_entry(title)
        if titleExist is not None:
            return render(request, "encyclopedia/error.html", {
                "message": "Entry already exists" 
            })
        else:
            util.save_entry(title, content)
            html_content = convert_md_to_html(title)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": html_content
            })

def edit(request):
    if request.method == 'POST':
        title = request.POST['entry_title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html",{
            "title": title,
            "content": content
        })

def save_edit(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title,content)
        html_content = convert_md_to_html(title)
        return render(request, "encyclopedia/entry.html",{
            "title": title,
            "content": html_content
        })

def random_page(request):
    allEntries = util.list_entries()
    random_entry = random.choice(allEntries)
    html_content = convert_md_to_html(random_entry)
    return render(request, "encyclopedia/entry.html",{
        "title": random_entry,
        "content": html_content
    })
    
