from django.contrib import admin
from . import models

admin.site.register(models.Penyakit)
admin.site.register(models.Gejala)
admin.site.register(models.BasisPengetahuan)
admin.site.register(models.UserModel)
admin.site.register(models.Riwayat)
