from django.shortcuts import redirect, render
from dotenv import load_dotenv
import os
import requests
from datetime import datetime
from .models import Contact
from django.utils import timezone
from django.contrib import messages
from .models import Subscription
from .models import Camera
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

load_dotenv()  # Load .env file at runtime (works in dev; see notes below)
API_KEY = os.getenv("WEATHER_API_KEY")

# ---------- Helpers ----------


def ensure_icon_url(icon_value: str) -> str:
    """WeatherAPI icons sometimes start with //...; make them absolute."""
    if not icon_value:
        return ""
    if icon_value.startswith("//"):
        return "https:" + icon_value
    return icon_value


def weekday_from_iso_date(iso_date: str) -> str:
    """iso_date like '2025-11-10' -> 'Mon'."""
    try:
        return datetime.strptime(iso_date, "%Y-%m-%d").strftime("%a")
    except Exception:
        return ""


def get_client_ip(request):
    """Extract user's IP address (works behind proxies/CDN if header is set)."""
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        # take the first IP in the comma-separated list
        ip = x_forwarded_for.split(",")[0].strip()
    else:
        ip = request.META.get("REMOTE_ADDR")
    # Local dev or missing IP -> use a public fallback to avoid geolocate failure
    if ip in ("127.0.0.1", "::1", None, ""):
        return "1.1.1.1"
    return ip


def get_city_from_ip(ip):
    """Get city name from IP address using ipapi.co."""
    try:
        resp = requests.get(f"https://ipapi.co/{ip}/json/", timeout=5)
        data = resp.json()
        return data.get("city") or "Delhi"  # fallback
    except requests.exceptions.RequestException:
        return "Delhi"

# ---------- Weather calls ----------


def current_weather(city):
    """Fetch current weather from WeatherAPI."""
    if not API_KEY:
        return None, "Missing WEATHER_API_KEY. Check your .env and settings."
    base_url = "https://api.weatherapi.com/v1/current.json"
    params = {"key": API_KEY, "q": city, "aqi": "no"}

    try:
        r = requests.get(base_url, params=params, timeout=10)
        data = r.json()
        if "error" in data:
            return None, data["error"].get("message", "API error")

        current = data["current"]
        location = data["location"]
        weather_data = {
            "city": location["name"],
            "country": location["country"],
            "temperature": current["temp_c"],
            "condition": current["condition"]["text"],
            "icon": ensure_icon_url(current["condition"]["icon"]),
            "humidity": current["humidity"],
            "wind_kph": current["wind_kph"],
            "feelslike_c": current["feelslike_c"],
            "last_updated": current.get("last_updated"),  # 'YYYY-MM-DD HH:MM'
        }
        return weather_data, None

    except requests.exceptions.RequestException:
        return None, "Network error. Please try again later."


def forecast_weather(city, days=7):
    """Fetch forecast from WeatherAPI."""
    if not API_KEY:
        return None, "Missing WEATHER_API_KEY. Check your .env and settings."
    base_url = "https://api.weatherapi.com/v1/forecast.json"
    params = {"key": API_KEY, "q": city,
              "days": days, "aqi": "no", "alerts": "no"}

    try:
        r = requests.get(base_url, params=params, timeout=10)
        data = r.json()
        if "error" in data:
            return None, data["error"].get("message", "API error")

        out = []
        for day in data["forecast"]["forecastday"]:
            out.append({
                "date": day["date"],  # 'YYYY-MM-DD'
                "day_name": weekday_from_iso_date(day["date"]),  # 'Mon', etc
                "max_temp": day["day"]["maxtemp_c"],
                "min_temp": day["day"]["mintemp_c"],
                "condition": day["day"]["condition"]["text"],
                "icon": ensure_icon_url(day["day"]["condition"]["icon"]),
            })
        return out, None

    except requests.exceptions.RequestException:
        return None, "Network error. Please try again later."

# ---------- Views ----------


def base(request):
    return render(request, "base.html")


def index(request):
    """
    Shows:
      - date/day, city, country
      - current temperature, feels like, wind, humidity, condition + icon
      - forecast date/day, min/max temps, condition + icons
    """
    weather_data = None
    forecast_data = None
    error_message = None

    if request.method == "POST":
        city = (request.POST.get("city") or "").strip()
        if city:
            weather_data, err1 = current_weather(city)
            forecast_data, err2 = forecast_weather(city, days=3)
        else:
            err1 = "Please enter a city."
            err2 = None
    else:
        user_ip = get_client_ip(request)
        user_city = get_city_from_ip(user_ip)
        weather_data, err1 = current_weather(user_city)
        forecast_data, err2 = forecast_weather(user_city, days=3)

    # Prefer to show a meaningful error if either call failed
    error_message = err1 or err2

    return render(request, "index.html", {
        "weather": weather_data,
        "forecast": forecast_data,
        "error": error_message,
    })


def news(request):
    return render(request, "news.html")


def livecameras(request):
    """
    List view for live cameras with optional filters:
      - country (GET param 'country')
      - only high quality (GET param 'quality' = 'yes' or 'no')
      - per-page count (GET param 'per_page', integer)
      - page (GET param 'page')
    """
    qs = Camera.objects.all()

    country = request.GET.get('country', '').strip()
    quality = request.GET.get('quality', '').strip().lower()
    per_page = request.GET.get('per_page') or 8

    if country:
        qs = qs.filter(country__iexact=country)

    if quality == 'yes':
        qs = qs.filter(is_high_quality=True)
    elif quality == 'no':
        qs = qs.filter(is_high_quality=False)

    countries = Camera.objects.order_by().values_list('country', flat=True).distinct()
    countries = [c for c in countries if c]

    per_page_options = [4, 8, 12, 16, 20]

    try:
        per_page = int(per_page)
    except:
        per_page = 8

    paginator = Paginator(qs, per_page)
    page = request.GET.get('page')
    cameras_page = paginator.get_page(page)

    return render(request, "live-cameras.html", {
        "cameras_page": cameras_page,
        "countries": countries,
        "selected_country": country,
        "selected_quality": quality,
        "per_page": per_page,
        "per_page_options": per_page_options,
        "paginator": paginator,
    })

def photos(request):
    return render(request, "photos.html")


def contact(request):
    """
    Handles Contact Us form submission and renders the contact page.
    """
    if request.method == "POST":
        name = request.POST.get("username")
        email = request.POST.get("email")
        company = request.POST.get("companyname")
        website = request.POST.get("website")
        message = request.POST.get("message")

        if name and email and message:
            Contact.objects.create(
                name=name,
                email=email,
                company_name=company,
                website=website,
                message=message,
                created_at=timezone.now()
            )
            messages.success(
                request, "Thank you for contacting us. We'll get back to you soon!")
            return redirect("contact")
        else:
            messages.error(request, "Please fill out all required fields.")

    return render(request, "contact.html")

def subscribe(request):
    """
    Handles subscription form submission from the footer.
    """
    if request.method == "POST":
        email = request.POST.get("email", "").strip()

        if not email:
            messages.error(request, "Please enter your email address.")
            return redirect(request.META.get("HTTP_REFERER", "/"))

        # Check for duplicate
        if Subscription.objects.filter(email=email).exists():
            messages.info(request, "You're already subscribed! Thank you.")
            return redirect(request.META.get("HTTP_REFERER", "/"))

        # Save new subscription
        Subscription.objects.create(email=email, subscribed_at=timezone.now())
        messages.success(request, "Thank you for subscribing!")
        return redirect(request.META.get("HTTP_REFERER", "/"))

    # Redirect to home if GET request (no form)
    return redirect("/")
