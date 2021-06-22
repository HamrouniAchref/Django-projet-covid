from django.contrib import admin

# Register your models here.
from .models import Vaccin
from .models import Pays
from .models import EffetSecondaire
from .models import Maladie
admin.site.register(Pays)
admin.site.register(Vaccin)
admin.site.register(EffetSecondaire)
admin.site.register(Maladie)


