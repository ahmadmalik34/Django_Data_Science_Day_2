# 🔗 URL Shortener (v1)

<div align="center">

**Create Short Links Without a Database**

[![Django](https://img.shields.io/badge/Django-5.0%2B-darkgreen?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)](https://www.python.org/)

[Features](#-features) • [Installation](#-installation) • [Usage](#-quick-start)

</div>

---

## 🎯 Overview

Master Django URL routing, form handling, and redirects by building a functional URL shortener.

**No database. No complexity. Pure Django magic.**

```
Long URL:  https://example.com/this-is-a-really-long-url?param=value
           ↓
         (Shorten)
           ↓
Short URL: http://127.0.0.1:8000/r/abc123/
           ↓
         (Click)
           ↓
Redirected to original URL
```

---

## ✨ Features

| Feature | Details |
|---------|---------|
| 🔗 **URL Shortening** | Generate short codes for long URLs |
| 🎯 **Redirects** | Short link redirects to original URL |
| ✅ **Validation** | Input validation and error handling |
| 📋 **In-Memory Storage** | Uses Python dictionary (no database) |
| 🔄 **Form Handling** | Django forms for user input |
| 📱 **Responsive UI** | Clean, simple interface |

---

## 📦 Tech Stack

- **Framework:** Django 5.0+
- **Language:** Python 3.8+
- **Storage:** In-memory Python dictionary
- **Frontend:** HTML5 + CSS3

---

## 🚀 Quick Start

### Installation

```bash
# Create virtual environment
python -m venv venv

# Activate it
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

### Run Locally

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

### How to Use

1. Navigate to the home page
2. Paste a long URL into the form
3. Click "Shorten"
4. Get a short link like `http://127.0.0.1:8000/r/abc123/`
5. Share or click the short link to redirect

---

## 🔧 How It Works

### URL Routing

```python
path('r/<str:short_code>/', views.redirect_short_url, name='redirect')
```

Maps short codes to view functions.

### In-Memory Storage

Uses a global Python dictionary to store mappings:

```python
url_mapping = {
    'abc123': 'https://example.com/long-url',
    'xyz789': 'https://another-site.com'
}
```

### Redirect Logic

```python
def redirect_short_url(request, short_code):
    url = url_mapping.get(short_code)
    if url:
        return redirect(url)
    return HttpResponse("Short code not found")
```

---

## 📚 What You'll Learn

✅ Django URL routing with `path()` and path parameters  
✅ Function-based views  
✅ Django forms and form handling  
✅ The `redirect()` function  
✅ HTTP status codes (302 redirects)  
✅ String generation and validation  
✅ Template rendering with context  

---

## ⚠️ Limitations

⚠️ **In-Memory Only** — Data lost on server restart  
⚠️ **Single Instance** — Doesn't work with multiple processes  
⚠️ **No Persistence** — Not suitable for production  

*This is intentional for learning purposes. Day 3+ introduces databases.*

---

## 🔄 Next Steps

- **Day 3:** Add a database to persist short links
- **Day 4:** Create an admin panel
- **Day 5:** Add user authentication

---

<div align="center">

**Day 2 of 50 — Django × Data Science Challenge**

Learning URL routing and redirects.

</div>

## Important notes
- This version stores URL mappings in a process-level Python `dict` (in-memory). Mappings are lost when the server restarts or the process reloads.
- Short codes are generated using Python's `secrets.token_urlsafe()` for unpredictability. Collisions are unlikely for small runs but possible; the app should check and regenerate on collision for production.
- For production-ready shorteners, persist mappings in a database and add validation, rate-limiting, and abuse protections.

## Next steps (suggested)
- Add a `ShortURL` model and migrate to persistent storage
- Add a simple analytics counter saved to the DB
- Add tests for create & redirect flows

---

Built during Day 2 of the 50-Day Django + Data Science roadmap.
