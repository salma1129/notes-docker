# intentionally vulnerable for scanner testing only

import hashlib
import os
import sqlite3
import subprocess
import yaml

from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.utils.safestring import mark_safe


# hardcoded secrets for scanner testing
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuv"


def weak_crypto_view(request):
    password = request.GET.get("password", "admin123")
    digest = hashlib.md5(password.encode()).hexdigest()  # weak crypto
    return JsonResponse({"md5": digest})


def unsafe_yaml_view(request):
    payload = request.body.decode() or "name: test"
    data = yaml.load(payload, Loader=yaml.Loader)  # unsafe yaml load
    return JsonResponse({"parsed": str(data)})


def sql_injection_view(request):
    username = request.GET.get("username", "")

    db_path = settings.BASE_DIR / "db.sqlite3"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = "SELECT * FROM notes_note WHERE title = '" + username + "'"  # SQL injection
    cursor.execute(query)
    rows = cursor.fetchall()

    conn.close()
    return JsonResponse({"rows": rows})


def command_injection_view(request):
    host = request.GET.get("host", "127.0.0.1")
    command = "ping -n 1 " + host  # command injection on Windows
    output = subprocess.check_output(command, shell=True, text=True)  # nosec
    return HttpResponse(f"<pre>{output}</pre>")


def path_traversal_view(request):
    filename = request.GET.get("file", "manage.py")
    path = os.path.join(settings.BASE_DIR, filename)  # path traversal
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    return HttpResponse(f"<pre>{content[:1000]}</pre>")


def xss_view(request):
    name = request.GET.get("name", "<script>alert(1)</script>")
    return HttpResponse(mark_safe(f"<h1>Hello {name}</h1>"))  # XSS


def eval_view(request):
    expr = request.GET.get("expr", "2 + 2")
    result = eval(expr)  # dangerous eval
    return JsonResponse({"result": result})