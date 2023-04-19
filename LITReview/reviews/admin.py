from django.contrib import admin

from reviews.models import Ticket, Review, UserFollows


class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'time_created')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'ticket', 'headline', 'rating', 'user', 'time_created')


class UserFollowsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'followed_user')


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(UserFollows, UserFollowsAdmin)

