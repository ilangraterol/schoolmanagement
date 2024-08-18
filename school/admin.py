from django.contrib import admin
from .models import Attendance,StudentExtra,TeacherExtra,Notice, Institucion
# Register your models here. (by sumit.luv)
class StudentExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(StudentExtra, StudentExtraAdmin)

class TeacherExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(TeacherExtra, TeacherExtraAdmin)

class AttendanceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Attendance, AttendanceAdmin)

class NoticeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Notice, NoticeAdmin)

class InstitucionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'phone', 'documento', 'fecha_creacion', 'admin')
    search_fields = ('nombre', 'documento')
    list_filter = ('fecha_creacion',)

admin.site.register(Institucion, InstitucionAdmin)