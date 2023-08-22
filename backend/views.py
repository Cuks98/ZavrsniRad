from django.shortcuts import render
from django.http import HttpResponse

from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
from .serializers import LazyEncoder
from .models import Roles
# from .models import Role

# Create your views here.


def say_hello(request):
    return HttpResponse("hello world")

def get_roles(request):
    roles = Roles.objects.all()
    # serializer = RoleSerializer(roles, many=True)
    return HttpResponse(serialize("json", Roles.objects.all(), cls=LazyEncoder)
)