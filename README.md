## Day 2 — URL Shortener (v1)

A small Django app built as Day 2 of the 50-Day Django + Data Science roadmap. This is a minimal, in-memory URL shortener used to practice URL routing, form handling, and redirects in Django.

## What it includes
- Simple form to submit a long URL
- In-memory short code generation (no database)
- Redirect endpoint that maps short code → long URL
- Basic validation and shareable short links built from the request

## Tech used
- Django 5.x
- Python 3.12+

## How to run (local)
1. Create and activate your virtual environment if not already active:

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

2. Run the development server:

```powershell
python manage.py runserver
```

3. Open `http://127.0.0.1:8000/` in your browser, paste a long URL into the form and submit. The app will return a short link like `http://127.0.0.1:8000/r/abc123/` which redirects to the original URL.

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
