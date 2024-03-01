from django.contrib import admin

from users.models import *


admin.site.register(FrontendUsersModel)
admin.site.register(BackendUsersModel)
admin.site.register(TelegramUsersModel)
admin.site.register(SmmUsersModel)
admin.site.register(GraphicDesignerUsersModel)
admin.site.register(MobilografUsersModel)