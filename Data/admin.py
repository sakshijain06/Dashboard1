from django.contrib import admin
from Data.models import  TestCase

# Register your models here.

    
class TestCaseAdmin(admin.ModelAdmin):
    list_display=('swfName','test_path','test_area','suite','test_caseid','lst_dt','lst_user')
    list_per_page=40;
    
    ordering=('-swfName',)
    list_filter=('suite','lst_user','test_area')
    search_fields=['swfName','test_path']
#    actions=[selectBuild] #enter_receipt_patial,enter_receipt_fully,add_penalty,reminder_telephone,reminder_letter]
    #fields = ('sno', 'partyName', 'incaseOf','status')
#    fieldsets=(
#        (None,{
#            'fields': ('partyName','incaseOf','address1','city'
#                       ,'IssueDate','DueDate'
#                       ,'status')
#        }),
#        ('options',{
#            'classes': ('collapse',),
#            'fields': ('option1','option2','option3','option4')
#        }),
#        ('reminder details',{
#            'classes': ('collapse',),
#            'fields': ('telephone1','telephone2','reminder1','reminder2','p1','p2')
#        }),
#    )

admin.site.register(TestCase,TestCaseAdmin)