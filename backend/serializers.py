
from rest_framework import serializers
from django.core.serializers.json import DjangoJSONEncoder

from .models import Roles

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'



class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Roles):
            return str(obj)
        return super().default(obj)