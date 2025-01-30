from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import os
import subprocess
import sys

# Configure Django settings
DEBUG = True
SECRET_KEY = 'insecure-development-key'
ROOT_URLCONF = __name__
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
]
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
        ],
    },
}]

# HTML template with inline styles
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Damn Vulnerable Django Server</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 30px auto;
            padding: 20px;
            max-width: 800px;
        }
        .warning {
            background-color: #ffebee;
            border: 1px solid #f44336;
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 4px;
        }
        .output {
            background-color: #f5f5f5;
            padding: 15px;
            border-radius: 4px;
            white-space: pre-wrap;
            margin-top: 20px;
        }
        input[type="text"] {
            width: 100%;
            padding: 8px;
            margin: 10px 0;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <div class="warning">
        <h2>⚠️ Warning: Vulnerable Application</h2>
        <p>This is a deliberately vulnerable application for educational purposes only.
           DO NOT deploy in production or expose to the internet.</p>
    </div>

    <h1>Command Execution Interface</h1>
    <form method="POST">
        <input type="text" name="command" placeholder="Enter system command...">
        <button type="submit">Execute</button>
    </form>

    <div class="output">
        {{ output }}
    </div>
</body>
</html>
'''

@csrf_exempt  # WARNING: This disables CSRF protection - Only for demonstration!
def execute_command(request):
    output = ""
    if request.method == "POST":
        command = request.POST.get('command', '')
        try:
            # WARNING: This is intentionally vulnerable!
            # Never execute unsanitized user input in a real application
            process = subprocess.Popen(
                command,
                shell=True,  # This makes it vulnerable to command injection
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True
            )
            stdout, stderr = process.communicate()
            output = stdout if stdout else stderr
        except Exception as e:
            output = str(e)
    
    return HttpResponse(HTML_TEMPLATE.replace('{{ output }}', output))

# URL Configuration
urlpatterns = [
    path('', execute_command),
]

# Configure Django settings
settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ROOT_URLCONF=ROOT_URLCONF,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    MIDDLEWARE=MIDDLEWARE,
    TEMPLATES=TEMPLATES
)

# Run the application
if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)