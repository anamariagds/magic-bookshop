from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=60)
    autor = models.CharField(max_length=60)
    resumo = models.TextField()
    categoria = models.CharField(max_length=10)
    img = models.ImageField(upload_to='capa_livro', null=True, blank=True)
    pdf = models.FileField(upload_to='arquivo_pdf', null=True, blank=True)


    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name= 'Livro' 
        