from django.contrib import admin

from .models import Course, Student_courses, Student, Section, Section_themes

class CourseAdmin(admin.ModelAdmin):
    search_fields = ['name', 'price', 'duration']
    list_display = ['name', 'price', 'duration']

class SectionAdmin(admin.ModelAdmin):
    search_fields = ['name',]
    list_display = ['name','themes']

class Section_themesAdmin(admin.ModelAdmin):
    search_fields = ['section', 'course']
    list_display = ['section', 'course']

class StudentAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'username','telegram_id','is_admin']
    list_display = ['first_name', 'last_name', 'username', 'telegram_id', 'is_admin']

class StudentCourseAdmin(admin.ModelAdmin):
    search_fields = ['student', 'course', 'date']
    list_display = ['student', 'course', 'date']

admin.site.register(Course, CourseAdmin)
admin.site.register(Student_courses, StudentCourseAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Section_themes, Section_themesAdmin)
admin.site.register(Student, StudentAdmin)

