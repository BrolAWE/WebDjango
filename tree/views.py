from django.shortcuts import render


#

def tree(request):
    workshops = Workshop.objects.all()
    return render(request, "tree.html")
