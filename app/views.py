from django.shortcuts import render

# Create your views here.
def jinja_tag(request):
    d={"a":200,"b":120,"c":300}
    return render(request,"jinja_tag.html",d)
