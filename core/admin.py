from django.contrib import admin

from core.models import Category, Portfolio_Category, Post, Team, Testimonial,Famil,Event

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Testimonial)
admin.site.register(Portfolio_Category)
admin.site.register(Team)
admin.site.register(Famil)
admin.site.register(Event)
