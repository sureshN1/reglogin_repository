from django.contrib import admin
from testapp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['fname','lname','sid','dob','email','phone']
admin.site.register(Student,StudentAdmin)
