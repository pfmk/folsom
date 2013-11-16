from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Organization(models.Model):
	name = models.CharField(max_length=50)
	address_street = models.CharField(max_length=50)
	address_city = models.CharField(max_length=60)
	address_state = models.CharField(max_length=30)
	address_zip = models.CharField(max_length=50)
	address_zip.verbose_name = "Zip"
	website = models.URLField()

class Person(models.Model):
	name_first = models.CharField(max_length=50)
	name_middle = models.CharField(max_length=50)
	name_last = models.CharField(max_length=50)

class Client(models.Model):
	persons = models.OneToOneField(Person)

# -------------------------------------------------------------------------------------- #
#	Demographic Information
# -------------------------------------------------------------------------------------- #

#	Define select boxes first; then questions
	
	RACE_ETHNICITY = (
		('Bl', 'Black, non-Hispanic'),
		('La', 'Latino or Hispanic'),
		('NA', 'Native American'),
		('PI', 'Pacific Islander'),
		('Wh', 'White, non-Hispanic'),
		('MR', 'Multi-Racial'),
		('Ot', 'Other'),
	)

	LANGUAGES_SPOKEN = (
		('Bn', 'Bengali'),
		('Ch', 'Chinese'),
		('En', 'English'),
		('Ru', 'Russian'),
		('Sp', 'Spanish'),
		('Ot', 'Other'),
	)

	MARITAL_STATUS = (
		('Si', 'Single'),
		('Ma', 'Married'),
		('NM', 'Not married, live with partner'),
		('Se', 'Separated'),
		('Di', 'Divorced'),
		('Wi', 'Widow/widower'),
		('Ot', 'Other'),
	)

	IMMIGRATION_STATUS = (
		('NA', 'Choose not to answer'),
		('US', 'U.S. citizen'),
		('LR', 'Legal Permanent Resident'),
		('Ot', 'Other'),
	)

	HIGHEST_EDUCATION = (
		('El', 'Elementary (grades 1-8)'),
		('Sh', 'Some high school'),
		('HS', 'High school graduate'),
		('GD', 'GED'),
		('SC', 'Some college'),
		('AD', 'Associate\'s Degree'),
		('BA', 'Bachelor\'s degree'),
		('NA', 'Never attended school'),
	)

	INTERNET_ACCESS = (
		('home', 'Yes, at home'),
		('other', 'Yes, at another location'),
		('no', 'No'),
	)

	HEALTH_INSURANCE = (
		('employer', 'Yes, from my employer'),
		('government', 'Yes, from the government'),
		('no', 'No'),
	)

	YES_NO_IDK = (
		('yes', 'Yes'),
		('no', 'No'),
		('idk', 'I don\'t know'),
	)

#	Define questions
	race_ethnicity = models.CharField(choices=RACE_ETHNICITY)
	languages_spoken = models.CharField(max_length=1, choices=LANGUAGES_SPOKEN)
	marital_status = models.CharField(max_length=1, choices=MARITAL_STATUS)
	immigration_status = models.CharField(max_length=1, choices=IMMIGRATION_STATUS)
	highest_education = models.CharField(max_length=1, choices=HIGHEST_EDUCATION)
	registered_vote = models.CharField(max_length=1, choices=YES_NO_IDK)
	internet_access = models.CharField(max_length=1, choices=YES_NO_IDK)
	health_insurance = models.CharField(max_length=1, choices=YES_NO_IDK)







class Client_NextDoor(models.Model):
	clients = models.OneToOneField(Client)

#	Define select boxes first; then questions
	WHY_CX = (
		('employment', 'Looking for employment'),
		('promotion', 'Applying for promotion'),
		('license', 'Applying for City/State license'),
		('housing', 'Looking for housing'),
		('convictions', 'Want to know conviction history'),
		('other', 'Other'),
	)

	YES_NO_IDK = (
		('yes', 'Yes'),
		('no', 'No'),
		('idk', 'I don\'t know'),
	)

#	Define questions	
	why_cx = models.CharField(max_length=1, choices=WHY_CX)
	why_cx.verbose_name = "13. Why do you want to get a copy of your criminal record?"

	arrested = models.CharField(max_length=1, choices=YES_NO_IDK)
	arrested.verbose_name = "14. Have you ever been arrested?"

	convicted = models.CharField(max_length=1, choices=YES_NO_IDK)
	convicted.verbose_name = "15. Have you ever been convicted of a crime?"

	employer_refused = models.CharField(max_length=1, choices=YES_NO_IDK)
	employer_refused.verbose_name = "16. Has an employer ever refused to hire you because of your criminal record?"
		
	employer_declined = models.CharField(max_length=1, choices=YES_NO_IDK)
	employer_declined.verbose_name = "17. Has an employer ever fired you because of your criminal record?"
	
	class Meta:
		verbose_name_plural = "Next Door Clients"

class Notes(models.Model):
	body = models.TextField()
#	pub_date = models.DateTimeField(default=datetime.datetime.now)
	author = models.ForeignKey(User)
	sticky = models.BooleanField(default=False)