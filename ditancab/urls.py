from django.urls import path
from . import views

urlpatterns = [
    path('gejala/', views.gejala_list),
    path('gejala/<int:id>', views.detail_gejala),
    path('penyakit/', views.penyakit_list),
    path('penyakit/<int:id>', views.detail_penyakit),
    path('basis-pengetahuan/', views.basispengetahuan_list),
    path('basis-pengetahuan/<int:id>', views.detail_bp),
    path('riwayat/', views.riwayat_list),
    path('riwayat/<int:id>', views.detail_riwayat)
]