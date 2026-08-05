from .models import Wishlist
from .destinations_data import DESTINATIONS
from django.http import Http404
from .models import ContactMessage, Itinerary
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .forms import EditProfileForm
@login_required(login_url="login")
def home(request):
    return render(request,'main/home.html')
def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "main/login.html")
def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        messages.success(
    request,
    "Thank you for contacting Silver Escapes! We'll get back to you soon."
)
        return redirect("contact")
    return render(request, "main/contact.html")
def about(request):
    return render(request, "main/about.html")
def register_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect("register")
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        return redirect(f"{reverse('login')}?registered=true")
    return render(request, "main/register.html")
def logout_page(request):
    logout(request)
    return redirect("home")
def faq(request):
    return render(request, "main/faq.html")
@login_required(login_url="login")
def dashboard(request):

    itineraries = Itinerary.objects.filter(
        user=request.user
    ).order_by("-created_at")[:3]

    trips = []

    for trip in itineraries:

        days = (trip.end_date - trip.start_date).days + 1

        trips.append({

            "destination": trip.destination,

            "days": days

        })

    wishlist_items = Wishlist.objects.filter(user=request.user)

    wishlist = []

    for item in wishlist_items:

        destination = DESTINATIONS.get(item.destination)

        if destination:

            wishlist.append({

                "name": destination["name"],

                "slug": item.destination

            })

    return render(request, "main/dashboard.html", {

        "trips": trips,

        "wishlist": wishlist,

    })
def destinations(request):
    return render(request, "main/destinations.html")

@login_required(login_url="login")
def itinerary(request):

    if request.method == "POST":

        destination = request.POST["destination"]
        start_date = request.POST["start_date"]
        end_date = request.POST["end_date"]
        travelers = request.POST["travelers"]
        budget = request.POST["budget"]
        notes = request.POST["notes"]

        Itinerary.objects.create(
            user=request.user,
            destination=destination,
            start_date=start_date,
            end_date=end_date,
            travelers=travelers,
            budget=budget,
            notes=notes
        )

        messages.success(request, "Itinerary created!")

        return redirect("itinerary")

    itineraries = Itinerary.objects.filter(
        user=request.user
    ).order_by("-created_at")
    selected_destination = request.GET.get("destination", "")

    return render(request, "main/itinerary.html", {
        "itineraries": itineraries,
        "selected_destination": selected_destination,
    })
@login_required(login_url="login")
def delete_itinerary(request, id):

    trip = Itinerary.objects.get(id=id, user=request.user)

    trip.delete()

    messages.success(request, "Itinerary deleted.")

    return redirect("itinerary")
@login_required(login_url="login")
def edit_itinerary(request, id):

    trip = Itinerary.objects.get(id=id, user=request.user)

    if request.method == "POST":

        trip.destination = request.POST["destination"]
        trip.start_date = request.POST["start_date"]
        trip.end_date = request.POST["end_date"]
        trip.travelers = request.POST["travelers"]
        trip.budget = request.POST["budget"]
        trip.notes = request.POST["notes"]

        trip.save()

        messages.success(request, "Itinerary updated!")

        return redirect("itinerary")

    return render(request,
                  "main/edit_itinerary.html",
                  {"trip": trip})
def destination_detail(request, slug):

    destination = DESTINATIONS.get(slug)

    if destination is None:
        raise Http404("Destination not found.")
    

    saved = False

    if request.user.is_authenticated:

        saved = Wishlist.objects.filter(
        user=request.user,
        destination=slug
    ).exists()

    return render(request, "main/destination_detail.html", {

    "destination": destination,

    "slug": slug,

    "saved": saved

})

@login_required(login_url="login")
def toggle_wishlist(request, slug):

    item = Wishlist.objects.filter(
        user=request.user,
        destination=slug
    )

    if item.exists():

        item.delete()

    else:

        Wishlist.objects.create(
            user=request.user,
            destination=slug
        )

    return redirect("destination_detail", slug=slug)
@login_required(login_url="login")
def edit_profile(request):

    profile = request.user.profile

    if request.method == "POST":

        form = EditProfileForm(
            request.POST,
            request.FILES,
            instance=request.user
        )

        if form.is_valid():

            form.save()

            profile.phone_number = form.cleaned_data["phone_number"]

            if form.cleaned_data["profile_picture"]:
                profile.profile_picture = form.cleaned_data["profile_picture"]

            profile.save()

            return redirect("dashboard")

    else:

        form = EditProfileForm(instance=request.user)
        form.fields["phone_number"].initial = profile.phone_number

    return render(
        request,
        "main/edit_profile.html",
        {
            "form": form
        }
    )
@login_required
def remove_profile_picture(request):

    profile = request.user.profile

    if profile.profile_picture:
        profile.profile_picture.delete(save=False)

    profile.profile_picture = ""
    profile.save()

    return redirect("edit_profile")
def hotels(request, slug):

    destination = DESTINATIONS.get(slug)

    if destination is None:
        raise Http404("Destination not found.")

    return render(
        request,
        "main/hotels.html",
        {
            "destination": destination,
            "hotels":destination["hotels"],
            "slug": slug,
        },
    )