from django.contrib import admin

from .models import Comentario, Foro, ModeracionEvent, Post, VotoComentario, VotoPost


admin.site.register(Foro)
admin.site.register(Post)
admin.site.register(Comentario)
admin.site.register(VotoPost)
admin.site.register(VotoComentario)
admin.site.register(ModeracionEvent)
