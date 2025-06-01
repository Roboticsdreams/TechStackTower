from django.http import HttpResponse
from django.shortcuts import render
import pathlib

this_dir = pathlib.Path(__file__).parent.resolve(0).parent

def index(request):
    return HttpResponse("<h1>Index page.</h1>")

def home_view(request, *args, **kwargs):
    print(this_dir)
    html_file = this_dir / 'templates/dummy_home.html'
    html_content = html_file.read_text()
    return HttpResponse(html_content)

def inline_view(request, *args, **kwargs):
    my_title = "Inline Title"
    my_content = "Inline Content"
    dynamic_context = {
        "my_title": my_title,
        "my_content": my_content
    }
    html_content = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{my_title}</title>
</head>
<body>
    <h1>{my_content}</h1>
</body>
</html>
""".format(**dynamic_context)
    return HttpResponse(html_content)

def template_view(request):
    context = {
        "my_title": "Template Title",
        "my_content": "Template Content"
    }

    return render(request, "template.html", context)

def inheritance_view(request):
    context = {
        "my_title": "Inheritance Title",
        "my_content": "Inheritance Content"
    }

    return render(request, "home.html", context)