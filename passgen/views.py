from django.shortcuts import render
import secrets

def home(request):
    password = ''
    error = None
    
    if 'generate' in request.GET:
        # Start with lowercase letters (always included)
        char = list("abcdefghijklmnopqrstuvwxyz")
        
        # Add optional character types
        if request.GET.get('uppercase'):
            char.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        if request.GET.get('numbers'):
            char.extend(list("0123456789"))
        if request.GET.get('symbols'):
            char.extend(list("!@#$%^&*()_+"))
        
        # Exclude similar characters if selected
        if request.GET.get('exclude_similar'):
            similar_chars = "il1Lo0O"
            char = [c for c in char if c not in similar_chars]
        
        try:
            length = int(request.GET.get('length', 8))
            if length < 6:
                length = 8
            password = ''.join(secrets.choice(char) for _ in range(length))
        except ValueError:
            length = 8
            password = ''.join(secrets.choice(char) for _ in range(length))
    
    return render(request, 'index.html', {
        'password': password,
        'error': error
    })