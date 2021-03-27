from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from case.models import Case

# Register your models here.


class CaseAdmin(GuardedModelAdmin):
    '''Define how to register model Case in console.'''


REGISTER_ITEMS = [
    (Case, CaseAdmin),
]

for model_class, admin_class in REGISTER_ITEMS:
    admin.site.register(model_class, admin_class)
