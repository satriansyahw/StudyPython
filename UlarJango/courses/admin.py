from django.contrib import admin 
from .models import Course,Step 
# admin.site.register(Course)
# admin.site.register(Step)



class StepInline(admin.StackedInline):
    model=Step
    
class CourseAdmin(admin.ModelAdmin):
    inlines=[StepInline,]
    
admin.site.register(Course, CourseAdmin)
admin.site.register(Step)