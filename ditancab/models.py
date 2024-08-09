from django.db import models

class Gejala(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

class Penyakit(models.Model):
    nama        = models.CharField(max_length=255)
    definisi    = models.TextField()
    solusi      = models.TextField()
    gambar      = models.ImageField(upload_to='penyakit/', null=True)

    def __str__(self):
        return self.nama
    
class Riwayat(models.Model):
    nama    = models.CharField(max_length=255)
    tgl     = models.DateTimeField()
    result  = models.TextField()

    def __str__(self):
        return self.nama
    
class BasisPengetahuan(models.Model):
    kode_gejala = models.ForeignKey(Gejala, on_delete=models.CASCADE)
    kode_penyakit = models.ForeignKey(Penyakit, on_delete=models.CASCADE)
    bobot = models.FloatField()

class UserModel(models.Model):
    username    = models.CharField(max_length=200)
    email       = models.EmailField()
    password1   = models.CharField(max_length=255)
    password2   = models.CharField(max_length=255)

    def __str__(self):
        return self.username