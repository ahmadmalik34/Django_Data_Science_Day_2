from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
import secrets

URL_MAP = {}

def create(request):
    """Show form (GET) and create short URL (POST)."""
    context = {}
    if request.method == 'POST':
        long_url = request.POST.get('long_url', '').strip()
        if not long_url:
            context['error'] = 'Please enter a URL.'
            return render(request, 'shortner/home.html', context)

        if not long_url.startswith(('http://', 'https://')):
            long_url = 'https://' + long_url

        # generate unique code (avoid collisions)
        code = secrets.token_urlsafe(4)
        while code in URL_MAP:
            code = secrets.token_urlsafe(4)

        URL_MAP[code] = long_url
        short_url = request.build_absolute_uri(f'/r/{code}/')
        context.update({'short_url': short_url, 'long_url': long_url})

    return render(request, 'shortner/home.html', context)

def redirect_url(request, code):
    long_url = URL_MAP.get(code)
    if not long_url:
        return HttpResponseNotFound("Short URL not found.")
    return redirect(long_url)