from django.shortcuts import render


#
from tree.models import Workshop


def tree(request):
    workshops = Workshop.objects.all()
    return render(request, "tree.html", {"workshops": workshops})
