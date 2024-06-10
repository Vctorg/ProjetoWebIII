from django.contrib import admin
from django.utils.html import format_html
from .models import Post

admin.site.site_header = ("Administração da ONG")
admin.site.site_title = ("Administração da ONG")
admin.site.index_title = ("Bem-vindo ao painel de administração da ONG")

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'previa_imagem', 'previa_texto', 'data')

    def previa_imagem(self, obj):
        return format_html('<img src="{0}" width="100"/>'.format(obj.imagem.url))

# Register your models here.
admin.site.register(Post, PostAdmin)
