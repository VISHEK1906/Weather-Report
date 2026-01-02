# 🌦️ Weather Hive - Real-Time Weather Reporting Application

<div align="center">

![Weather Hive Banner](https://img.shields.io/badge/Weather_Hive-Live_Weather_Data-blue?style=for-the-badge)

A modern, full-stack weather reporting web application built with **Django**, **Python**, **Bootstrap**, and **JavaScript**. Weather Hive provides real-time weather information for any city worldwide with dynamic data visualization and an intuitive user interface.

[![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=flat&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![API](https://img.shields.io/badge/REST_API-OpenWeather-orange?style=flat)](https://openweathermap.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [API](#-api-integration) • [Contributing](#-contributing)

</div>

---

## 📋 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Demo](#-demo)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [API Integration](#-api-integration)
- [Project Structure](#-project-structure)
- [Screenshots](#-screenshots)
- [Deployment](#-deployment)
- [Testing](#-testing)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [Roadmap](#-roadmap)
- [License](#-license)
- [Contact](#-contact)

---

## 🎯 Overview

**Weather Hive** is a comprehensive weather reporting application developed during my internship at **Paultech Pvt. Ltd. (September 2025 – November 2025)**. The application integrates real-time weather APIs with a Django backend to deliver accurate weather information with dynamic data visualization and a responsive user interface.

### 🎪 Key Highlights
- ⚡ **Real-Time Data**: Live weather updates from OpenWeatherMap API
- 📱 **Responsive Design**: Optimized for desktop, tablet, and mobile devices
- 📊 **Data Visualization**: Dynamic charts and weather icons
- 📧 **Newsletter Subscription**: Stay updated with weather alerts
- 💌 **Contact Form**: Secure message submission with database storage
- 🎨 **Modern UI/UX**: Clean, intuitive interface built with Bootstrap 5

---

## ✨ Features

### 🌍 Comprehensive Weather Information
- **Real-time weather search** by city name or coordinates
- **Current temperature** in Celsius/Fahrenheit
- **Weather conditions** (clear sky, clouds, rain, snow, etc.)
- **Detailed metrics**:
  - 💧 Humidity percentage
  - 💨 Wind speed and direction
  - 🌅 Sunrise and sunset times
  - 👁️ Visibility distance
  - 🌡️ Feels-like temperature
  - 🔽 Atmospheric pressure
- **Multi-day forecast** (5-day weather prediction)
- **Weather alerts** and warnings
- **Historical weather data** tracking

### 🎨 User Interface & Experience
- **Responsive Bootstrap 5 design** - works on all devices
- **Dynamic weather icons** that change based on conditions
- **Smooth animations** and transitions
- **Auto-complete search** suggestions
- **Recent searches** history
- **Favorite locations** saving feature
- **Dark/Light mode toggle**
- **Loading indicators** for better UX
- **Error handling** with user-friendly messages

### 📊 Data Visualization
- **Temperature graphs** using Chart.js
- **Wind direction compass**
- **UV index indicator**
- **Interactive weather maps**
- **Precipitation probability charts**

### 📧 Communication Features
- **Newsletter subscription** with email validation
- **Contact form** with CSRF protection
- **Email notifications** for weather alerts
- **Database storage** for user submissions
- **Admin dashboard** for managing subscriptions

### 🔒 Security Features
- CSRF token protection
- SQL injection prevention
- XSS protection
- Secure API key management
- Input validation and sanitization
- Rate limiting on API requests
- Environment variable configuration

### ⚡ Performance Optimization
- API response caching (Redis support)
- Lazy loading of images
- Minified CSS and JavaScript
- Database query optimization
- Asynchronous API calls
- Fast page load times (<2 seconds)

---

## 🎬 Demo

### Live Application
🔗 **[View Live Demo](https://weather-hive-demo.herokuapp.com)** *(Update with your deployment link)*

### Quick Preview
```
🏠 Home Page → Search any city → View detailed weather report
📧 Subscribe to newsletter → Receive weather updates
💬 Contact form → Send feedback or inquiries
```

---

## 🛠️ Tech Stack

### Backend
| Technology | Version | Purpose |
|-----------|---------|---------|
| ![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white) | 4.2+ | Web Framework |
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) | 3.10+ | Programming Language |
| ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white) | 3.x | Database |

### Frontend
| Technology | Purpose |
|-----------|---------|
| ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white) | Markup |
| ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white) | Styling |
| ![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=flat&logo=bootstrap&logoColor=white) | UI Framework |
| ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black) | Interactivity |
| ![jQuery](https://img.shields.io/badge/jQuery-0769AD?style=flat&logo=jquery&logoColor=white) | DOM Manipulation |

### APIs & Libraries
- **OpenWeatherMap API** - Weather data provider
- **Chart.js** - Data visualization
- **Font Awesome** - Icons
- **Google Fonts** - Typography

### Development Tools
- **Git** - Version control
- **VS Code** - Code editor
- **Postman** - API testing
- **Chrome DevTools** - Debugging

### Optional Enhancements
- **Redis** - Caching
- **Celery** - Background tasks
- **Docker** - Containerization
- **PostgreSQL** - Production database

---

## 🚀 Installation

### Prerequisites
Ensure you have the following installed:
- ✅ Python 3.10 or higher
- ✅ pip (Python package manager)
- ✅ Git
- ✅ Virtual Environment (venv or virtualenv)
- ✅ OpenWeatherMap API Key ([Get free API key](https://openweathermap.org/api))

---

### Step 1: Clone the Repository
```bash
git clone https://github.com/VISHEK1906/weather-hive.git
cd weather-hive
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Get API Key
1. Visit [OpenWeatherMap](https://openweathermap.org/api)
2. Create a free account
3. Generate an API key
4. Copy the API key for configuration

### Step 5: Configure Environment Variables
Create a `.env` file in the root directory:

```env
# Django Settings
SECRET_KEY='django-insecure-your-secret-key-here'
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Weather API
OPENWEATHER_API_KEY='your_openweathermap_api_key_here'
WEATHER_API_BASE_URL='https://api.openweathermap.org/data/2.5'

# Email Configuration (for newsletter)
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER='your_email@gmail.com'
EMAIL_HOST_PASSWORD='your_app_password'
DEFAULT_FROM_EMAIL='Weather Hive <noreply@weatherhive.com>'

# Database (optional - default is SQLite)
# DB_ENGINE='django.db.backends.postgresql'
# DB_NAME='weather_hive_db'
# DB_USER='your_db_user'
# DB_PASSWORD='your_db_password'
# DB_HOST='localhost'
# DB_PORT='5432'

# Cache (optional - Redis)
# CACHE_BACKEND='django_redis.cache.RedisCache'
# CACHE_LOCATION='redis://127.0.0.1:6379/1'

# Security (Production)
# SECURE_SSL_REDIRECT=True
# SESSION_COOKIE_SECURE=True
# CSRF_COOKIE_SECURE=True
```

### Step 6: Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 7: Create Superuser (Optional)
```bash
python manage.py createsuperuser
# Follow prompts to create admin account
```

### Step 8: Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### Step 9: Run Development Server
```bash
python manage.py runserver
```

### Step 10: Access Application
Open your browser and navigate to:
- **Main Application**: `http://127.0.0.1:8000`
- **Admin Panel**: `http://127.0.0.1:8000/admin`

---

## ⚙️ Configuration

### settings.py Configuration

#### Database Configuration
```python
import os
from pathlib import Path
from decouple import config

# Default SQLite (Development)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# PostgreSQL (Production) - Uncomment to use
# DATABASES = {
#     'default': {
#         'ENGINE': config('DB_ENGINE', default='django.db.backends.postgresql'),
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST', default='localhost'),
#         'PORT': config('DB_PORT', default='5432'),
#     }
# }
```

#### Weather API Configuration
```python
# Weather API Settings
OPENWEATHER_API_KEY = config('OPENWEATHER_API_KEY')
WEATHER_API_BASE_URL = config('WEATHER_API_BASE_URL', 
    default='https://api.openweathermap.org/data/2.5')
WEATHER_CACHE_TIMEOUT = 600  # 10 minutes
```

#### Email Configuration
```python
EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
```

#### Cache Configuration (Optional - Redis)
```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': config('CACHE_LOCATION', default='redis://127.0.0.1:6379/1'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
```

---

## 📖 Usage

### For End Users

#### 1. Search Weather
1. Open the application homepage
2. Enter city name in the search bar
3. Click "Search" or press Enter
4. View detailed weather information

#### 2. Subscribe to Newsletter
1. Scroll to the newsletter section
2. Enter your email address
3. Click "Subscribe"
4. Check your email for confirmation

#### 3. Contact Support
1. Navigate to the Contact page
2. Fill in your details (name, email, message)
3. Click "Send Message"
4. Receive confirmation notification

#### 4. View Forecast
1. After searching a city
2. Scroll down to see 5-day forecast
3. Click on specific days for detailed info

### For Administrators

#### 1. Access Admin Panel
```
URL: http://127.0.0.1:8000/admin
Login with superuser credentials
```

#### 2. Manage Newsletter Subscribers
- View all subscribers
- Export subscriber list
- Send bulk emails
- Manage subscriptions

#### 3. View Contact Form Submissions
- Read user messages
- Mark as read/unread
- Respond to inquiries
- Delete spam

#### 4. Monitor Application
- Check API usage statistics
- View error logs
- Monitor user activity

---

## 🔌 API Integration

### OpenWeatherMap API Endpoints Used

#### 1. Current Weather Data
```python
# Endpoint
GET https://api.openweathermap.org/data/2.5/weather

# Parameters
{
    'q': 'city_name',
    'appid': 'YOUR_API_KEY',
    'units': 'metric'
}

# Response Example
{
    "coord": {"lon": -122.08, "lat": 37.39},
    "weather": [{"id": 800, "main": "Clear", "description": "clear sky"}],
    "main": {
        "temp": 282.55,
        "feels_like": 281.86,
        "temp_min": 280.37,
        "temp_max": 284.26,
        "pressure": 1023,
        "humidity": 100
    },
    "wind": {"speed": 1.5, "deg": 350},
    "sys": {"country": "US", "sunrise": 1560343627, "sunset": 1560396563},
    "name": "Mountain View"
}
```

#### 2. 5-Day Forecast
```python
# Endpoint
GET https://api.openweathermap.org/data/2.5/forecast

# Parameters
{
    'q': 'city_name',
    'appid': 'YOUR_API_KEY',
    'units': 'metric',
    'cnt': 40  # Number of timestamps
}
```

#### 3. Air Pollution Data (Optional)
```python
# Endpoint
GET https://api.openweathermap.org/data/2.5/air_pollution

# Parameters
{
    'lat': latitude,
    'lon': longitude,
    'appid': 'YOUR_API_KEY'
}
```

### Implementation Example

```python
# views.py
import requests
from django.conf import settings
from django.core.cache import cache

def get_weather_data(city):
    # Check cache first
    cache_key = f'weather_{city}'
    cached_data = cache.get(cache_key)
    
    if cached_data:
        return cached_data
    
    # API request
    url = f"{settings.WEATHER_API_BASE_URL}/weather"
    params = {
        'q': city,
        'appid': settings.OPENWEATHER_API_KEY,
        'units': 'metric'
    }
    
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        
        # Cache for 10 minutes
        cache.set(cache_key, data, settings.WEATHER_CACHE_TIMEOUT)
        return data
        
    except requests.exceptions.RequestException as e:
        # Handle errors
        return None
```

### API Rate Limits
- **Free Tier**: 60 calls/minute, 1,000,000 calls/month
- **Caching**: Implemented to reduce API calls
- **Error Handling**: Graceful fallbacks for API failures

---

## 🏗️ Project Structure

```
weather-hive/
│
├── weather_project/              # Main project directory
│   ├── __init__.py
│   ├── settings.py              # Django settings
│   ├── urls.py                  # Main URL configuration
│   ├── wsgi.py                  # WSGI configuration
│   └── asgi.py                  # ASGI configuration
│
├── weather_app/                 # Weather application
│   ├── migrations/              # Database migrations
│   ├── templates/               # HTML templates
│   │   ├── base.html           # Base template
│   │   ├── home.html           # Homepage
│   │   ├── weather_detail.html # Weather details page
│   │   ├── contact.html        # Contact page
│   │   └── about.html          # About page
│   ├── static/                  # Static files
│   │   ├── css/
│   │   │   ├── style.css       # Main stylesheet
│   │   │   └── responsive.css  # Responsive styles
│   │   ├── js/
│   │   │   ├── main.js         # Main JavaScript
│   │   │   ├── weather.js      # Weather functionality
│   │   │   └── animations.js   # UI animations
│   │   └── images/
│   │       ├── icons/          # Weather icons
│   │       └── backgrounds/    # Background images
│   ├── __init__.py
│   ├── admin.py                # Admin configuration
│   ├── apps.py                 # App configuration
│   ├── models.py               # Database models
│   ├── views.py                # View functions
│   ├── urls.py                 # App URL configuration
│   ├── forms.py                # Django forms
│   ├── utils.py                # Utility functions
│   └── tests.py                # Unit tests
│
├── staticfiles/                # Collected static files (production)
├── media/                      # User uploaded files
├── templates/                  # Global templates
│   └── 404.html               # Custom 404 page
│
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (not in git)
├── .env.example               # Example environment file
├── .gitignore                 # Git ignore rules
├── manage.py                  # Django management script
├── Procfile                   # Heroku deployment
├── runtime.txt                # Python version
├── pytest.ini                 # Pytest configuration
├── docker-compose.yml         # Docker configuration
├── Dockerfile                 # Docker image
├── LICENSE                    # MIT License
└── README.md                  # This file
```

---

## 📸 Screenshots

### 🏠 Homepage
![Homepage](screenshots/homepage.png)
*Clean and modern landing page with search functionality*

### 🌤️ Weather Details
![Weather Details](screenshots/weather-details.png)
*Comprehensive weather information with dynamic icons*

### 📊 Data Visualization
![Charts](screenshots/charts.png)
*Interactive temperature and forecast charts*

### 📱 Mobile Responsive
![Mobile View](screenshots/mobile.png)
*Fully responsive design on mobile devices*

### 📧 Newsletter Subscription
![Newsletter](screenshots/newsletter.png)
*Easy newsletter subscription form*

### 💬 Contact Form
![Contact Form](screenshots/contact.png)
*User-friendly contact form with validation*

### 🎛️ Admin Dashboard
![Admin Panel](screenshots/admin.png)
*Django admin panel for managing data*

---

## 🚢 Deployment

### Heroku Deployment

#### Step 1: Install Heroku CLI
```bash
# Download from https://devcenter.heroku.com/articles/heroku-cli
heroku --version
```

#### Step 2: Login to Heroku
```bash
heroku login
```

#### Step 3: Create Heroku App
```bash
heroku create weather-hive-app
```

#### Step 4: Add Buildpack
```bash
heroku buildpacks:set heroku/python
```

#### Step 5: Set Environment Variables
```bash
heroku config:set SECRET_KEY='your-secret-key'
heroku config:set DEBUG=False
heroku config:set OPENWEATHER_API_KEY='your-api-key'
heroku config:set EMAIL_HOST_USER='your-email'
heroku config:set EMAIL_HOST_PASSWORD='your-password'
```

#### Step 6: Create Procfile
```procfile
web: gunicorn weather_project.wsgi --log-file -
```

#### Step 7: Update requirements.txt
```bash
pip freeze > requirements.txt
# Add: gunicorn, whitenoise, dj-database-url
```

#### Step 8: Deploy
```bash
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

#### Step 9: Run Migrations
```bash
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

#### Step 10: Open App
```bash
heroku open
```

### Docker Deployment

```dockerfile
# Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "weather_project.wsgi:application", "--bind", "0.0.0.0:8000"]
```

```bash
# Build and run
docker build -t weather-hive .
docker run -p 8000:8000 weather-hive
```

---

## 🧪 Testing

### Run Unit Tests
```bash
python manage.py test
```

### Run with Coverage
```bash
pip install coverage
coverage run --source='.' manage.py test
coverage report
coverage html  # Generate HTML report
```

### Test Cases Included
- ✅ Weather API integration tests
- ✅ Form validation tests
- ✅ Database model tests
- ✅ View function tests
- ✅ URL routing tests
- ✅ Template rendering tests

---

## 🔧 Troubleshooting

### Common Issues

#### 1. API Key Not Working
```
Error: 401 Unauthorized
Solution: 
- Verify API key is correct in .env file
- Check if API key is activated (takes 10 minutes)
- Ensure no extra spaces in .env file
```

#### 2. Database Errors
```
Error: No such table
Solution:
python manage.py makemigrations
python manage.py migrate
```

#### 3. Static Files Not Loading
```
Solution:
python manage.py collectstatic --noinput
# Check STATIC_URL and STATIC_ROOT in settings.py
```

#### 4. Email Not Sending
```
Solution:
- Enable 2FA on Gmail
- Generate App Password
- Use app password instead of regular password
```

#### 5. City Not Found
```
Error: 404 City Not Found
Solution:
- Check spelling of city name
- Try adding country code (e.g., "London,UK")
- Use coordinates instead of city name
```

---

## 🤝 Contributing

Contributions make the open-source community an amazing place to learn and create. Any contributions you make are **greatly appreciated**!

### How to Contribute

1. **Fork the Project**
   ```bash
   # Click the 'Fork' button on GitHub
   ```

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/weather-hive.git
   cd weather-hive
   ```

3. **Create Feature Branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```

4. **Make Your Changes**
   - Write clean, documented code
   - Follow PEP 8 style guide
   - Add tests for new features

5. **Commit Changes**
   ```bash
   git add .
   git commit -m 'Add: Amazing new feature'
   ```

6. **Push to Branch**
   ```bash
   git push origin feature/AmazingFeature
   ```

7. **Open Pull Request**
   - Go to your fork on GitHub
   - Click 'New Pull Request'
   - Describe your changes

### Contribution Guidelines
- Follow the existing code style
- Write clear commit messages
- Add tests for new features
- Update documentation
- Be respectful and constructive

### Code of Conduct
Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing.

---

## 🗺️ Roadmap

### Planned Features

#### Phase 1 (Completed ✅)
- [x] Basic weather search functionality
- [x] Responsive UI design
- [x] API integration
- [x] Contact form
- [x] Newsletter subscription

#### Phase 2 (In Progress 🚧)
- [ ] User authentication system
- [ ] Save favorite locations
- [ ] Weather alerts notifications
- [ ] Multi-language support
- [ ] Dark mode implementation

#### Phase 3 (Future 🔮)
- [ ] Weather maps integration
- [ ] Historical weather data
- [ ] Weather comparison tool
- [ ] Mobile app (React Native)
- [ ] Voice search functionality
- [ ] Social media sharing
- [ ] Weather widgets for websites
- [ ] Premium features (extended forecast)

### Feature Requests
Have an idea? [Open an issue](https://github.com/VISHEK1906/weather-hive/issues) with the tag "enhancement"

---

## 📄 Requirements

```txt
# requirements.txt

# Django Framework
Django==4.2.7
djangorestframework==3.14.0

# Environment Variables
python-decouple==3.8

# HTTP Requests
requests==2.31.0
urllib3==2.1.0

# Database
dj-database-url==2.1.0
psycopg2-binary==2.9.9  # For PostgreSQL

# Caching
django-redis==5.4.0
redis==5.0.1

# Forms & Validation
django-crispy-forms==2.1
crispy-bootstrap5==1.0.0

# Security
django-cors-headers==4.3.0

# Production Server
gunicorn==21.2.0
whitenoise==6.6.0

# Testing
pytest==7.4.3
pytest-django==4.7.0
coverage==7.3.2

# Utilities
python-dotenv==1.0.0
Pillow==10.1.0

# Development
django-debug-toolbar==4.2.0
black==23.11.0
flake8==6.1.0
```

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Vishek Kumar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## 👤 Author

<div align="center">

### **Vishek Kumar**

Full Stack Web Developer | Python Enthusiast | Open Source Contributor

[![GitHub](https://img.shields.io/badge/GitHub-@VISHEK1906-181717?style=for-the-badge&logo=github)](https://github.com/VISHEK1906)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-vishek--kumar--vk-0077B5?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/vishek-kumar-vk)
[![Email](https://img.shields.io/badge/Email-kumarvishek1906%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:kumarvishek1906@gmail.com)
[![Phone](https://img.shields.io/badge/Phone-7250681777-25D366?style=for-the-badge&logo=whatsapp)](tel:7250681777)

📍 Jamshedpur, Jharkhand, India

</div>

---

## 🙏 Acknowledgments

Special thanks to:

- **Paultech Pvt. Ltd.** - For internship opportunity and mentorship
- **OpenWeatherMap** - For providing free weather API
- **Django Community** - For excellent documentation
- **Bootstrap Team** - For responsive framework
- **Font Awesome** - For beautiful icons
- **Stack Overflow Community** - For problem-solving support
- **GitHub** - For hosting and collaboration tools

---

## 📞 Support & Feedback

### Get Help
- 📧 **Email**: kumarvishek1906@gmail.com
- 💼 **LinkedIn**: [Connect with me](https://linkedin.com/in/vishek-kumar-vk)
- 🐛 **Bug Reports**: [Create an issue](https://github.com/VISHEK1906/weather-hive/issues)
- 💡 **Feature Requests**: [Submit idea](https://github.com/VISHEK1906/weather-hive/issues/new)

### Stay Updated
- ⭐ **Star this repository** to show support
- 👀 **Watch this repository** for updates
- 🔄 **Fork this repository** to contribute

---

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/VISHEK1906/weather-hive?style=social)
![GitHub forks](https://img.shields.io/github/forks/VISHEK1906/weather-hive?style=social)
![GitHub issues](https://img.shields.io/github/issues/VISHEK1906/weather-hive)
![GitHub pull requests](https://img.shields.io/github/issues-pr/VISHEK1906/weather-hive)
![GitHub contributors](https://img.shields.io/github/contributors/VISHEK1906/weather-hive)
![GitHub last commit](https://img.shields.io/github/last-commit/VISHEK1906/weather-hive)

---

<div align="center">

### ⭐ Star this repository if you find it helpful!

**Made with ❤️ by Vishek Kumar**

*Building the future, one line of code at a time* 🚀

</div>

---

## 📚 Additional Resources

### Documentation
- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap Documentation](https://getbootstrap.com
