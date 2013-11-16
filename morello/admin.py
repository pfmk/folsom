from django.contrib import admin
from morello.models import Organization, Person, Client, Client_NextDoor

class OrganizationAdmin(admin.ModelAdmin):
	fields = (('name', 'address_street'), 'address_state', 'address_zip', 'website')

class PersonInline(admin.TabularInline):
	model = Person

class ClientAdmin(admin.ModelAdmin):
#	fields = (('race_ethnicity', 'languages_spoken', 'marital_status'), ('immigration_status', 'highest_education'))

	fieldsets = [
		(None,
			{'fields': [	('name_first'),
							('name_middle'),
							('name_last')]
			}
		),
		('Demographic information', 
			{'fields': [	('race_ethnicity', 'languages_spoken'), 
							('marital_status', 'immigration_status'), 
							('highest_education', 'registered_vote'),
							('internet_access', 'health_insurance')], 
							'classes': ['wide']
			}
		),
		('Employment, housing, and income information', 
			{'fields': [	('employment_status', 'current_job'),
							('employment_period', 'union_job'), 
							('why_unemployed', 'unemployment_period'),
							('collecting_unemployment'), 
							('housing_situation', 'housing_adults'), 
							('housing_children', 'housing_period'),
							('household_income')], 
							'classes': ['wide']
			}
		),
	]

"""
	fieldsets = [
		(None,
			{'fields': [	('name_first', 'name_middle', 'name_last')]}
		),
		('Demographic information', 
			{'fields': [	('race_ethnicity', 'languages_spoken', 'marital_status'), 
							('immigration_status', 'highest_education'), 
							('registered_vote', 'internet_access', 'health_insurance')], 
#							'classes': ['collapse']
			}
		),
		('Employment, housing, and income information', 
			{'fields': [	('employment_status', 'current_job', 'employment_period', 'union_job'), 
							('why_unemployed', 'unemployment_period', 'collecting_unemployment'), 
							('housing_situation', 'housing_adults', 'housing_children', 'housing_period', 'household_income')], 
#							'classes': ['collapse']
			}
		),
	]
#	inlines = [PersonInline]
"""

class ClientInline(admin.StackedInline):
	model = Client
	extra = 1

class Client_NextDoorAdmin(admin.ModelAdmin):
	fields = ('client', ('why_cx', 'arrested', 'convicted'), ('employer_refused', 'employer_declined'))
#	fields = (('why_cx', 'arrested', 'convicted'), ('employer_refused', 'employer_declined'))
	
#	inlines = [ClientInline]

admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Client_NextDoor, Client_NextDoorAdmin)

#	list_display = ('description', 'frequency', 'person')
#	list_editable = ('description', 'frequency', 'person')
