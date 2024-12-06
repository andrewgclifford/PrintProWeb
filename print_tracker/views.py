from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("""
        <h1>Welcome to PrintProWeb</h1>
        <p>Available endpoints:</p>
        <ul>
            <li><a href="/admin/">Admin Interface</a></li>
            <li><a href="/api/">API</a></li>
        </ul>
    """)
