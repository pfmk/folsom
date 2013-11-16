from django.db import models
from django.contrib.auth.models import User

from django import forms
from django.contrib.localflavor.us.forms import USStateField

# Create your models here.

class Organization(models.Model):
	name = models.CharField(max_length=50)
	address_street = models.CharField("Street address", max_length=50)
	address_city = models.CharField(max_length=60)
	address_state = models.CharField("State", max_length=60)
#	address_state = USStateField()
	address_zip = models.CharField("Zip", max_length=50)
	website = models.URLField()

class Person(models.Model):
	name_first = models.CharField("First name", max_length=50)
	name_middle = models.CharField("Middle name", max_length=50, blank=True)
	name_last = models.CharField("Last name", max_length=50)

class Client(Person):
#	Options used for multiple questions
	YES = 1
	NO = 2
	IDK = 3
	YES_NO = (
		(YES, 'Yes'),
		(NO, 'No'),
	)

	YES_NO_IDK = (
		(YES, 'Yes'),
		(NO, 'No'),
		(IDK, 'I don\'t know'),
	)

# -------------------------------------------------------------------------------------- #
#	Demographic Information
#	Choices defined this way because http://www.b-list.org/weblog/2007/nov/02/handle-choices-right-way/
# -------------------------------------------------------------------------------------- #

# Race/Ethnicity
	BLACK = 1
	LATINO = 2
	NATIVE_AMERICAN = 3
	PACIFIC_ISLANDER = 4
	WHITE = 5
	MULTI_RACIAL = 6
	OTHER = 7
	RACE_ETHNICITY = (
		(BLACK, 'Black, non-Hispanic'),
		(LATINO, 'Latino or Hispanic'),
		(NATIVE_AMERICAN, 'Native American'),
		(PACIFIC_ISLANDER, 'Pacific Islander'),
		(WHITE, 'White, non-Hispanic'),
		(MULTI_RACIAL, 'Multi-Racial'),
		(OTHER, 'Other'),
	)
	race_ethnicity = models.SmallIntegerField("Race/Ethnicity", choices=RACE_ETHNICITY, blank=True)


# Languages spoken
	BENGALI = 1
	CHINESE = 2
	ENGLISH = 3
	RUSSIAN = 4
	SPANISH = 5
	OTHER = 6
	LANGUAGES_SPOKEN = (
		(BENGALI, 'Bengali'),
		(CHINESE, 'Chinese'),
		(ENGLISH, 'English'),
		(RUSSIAN, 'Russian'),
		(SPANISH, 'Spanish'),
		(OTHER, 'Other'),
	)
	languages_spoken = models.SmallIntegerField(choices=LANGUAGES_SPOKEN, default=ENGLISH, blank=True)


# Marital status
	SINGLE = 1
	MARRIED = 2
	PARTNERED = 3
	SEPARATED = 4
	DIVORCED = 5
	WIDOW = 6
	OTHER = 7
	MARITAL_STATUS = (
		(SINGLE, 'Single'),
		(MARRIED, 'Married'),
		(PARTNERED, 'Not married, live with partner'),
		(SEPARATED, 'Separated'),
		(DIVORCED, 'Divorced'),
		(WIDOW, 'Widow/widower'),
		(OTHER, 'Other'),
	)
	marital_status = models.SmallIntegerField(choices=MARITAL_STATUS, blank=True)


# Immigration status
	NO_ANSWER = 1
	US_CITIZEN = 2
	LEGAL_RESIDENT = 3
	OTHER = 4
	IMMIGRATION_STATUS = (
		(NO_ANSWER, 'Choose not to answer'),
		(US_CITIZEN, 'U.S. citizen'),
		(LEGAL_RESIDENT, 'Legal Permanent Resident'),
		(OTHER, 'Other'),
	)
	immigration_status = models.SmallIntegerField(choices=IMMIGRATION_STATUS, default=US_CITIZEN, blank=True)


# Highest education completed?
	ELEMENTARY = 1
	SOME_HIGH_SCHOOL = 2
	HIGH_SCHOOL = 3
	GED = 4
	SOME_COLLEGE = 5
	ASSOCIATES = 6
	BACHELORS = 7
	POST_GRAD = 8
	NONE = 9
	HIGHEST_EDUCATION = (
		(ELEMENTARY, 'Elementary (grades 1-8)'),
		(SOME_HIGH_SCHOOL, 'Some high school'),
		(HIGH_SCHOOL, 'High school graduate'),
		(GED, 'GED'),
		(SOME_COLLEGE, 'Some college'),
		(ASSOCIATES, 'Associate\'s Degree'),
		(BACHELORS, 'Bachelor\'s degree'),
		(POST_GRAD, 'Post-graduate'),
		(NONE, 'Never attended school'),
	)
	highest_education = models.SmallIntegerField("Highest education completed?", choices=HIGHEST_EDUCATION, blank=True)


# Are you registered to vote?
	registered_vote = models.SmallIntegerField("Are you registered to vote?", choices=YES_NO_IDK, blank=True)


# Do you have internet access?
	HOME = 1
	OTHER = 2
	NO = 3
	INTERNET_ACCESS = (
		(HOME, 'Yes, at home'),
		(OTHER, 'Yes, at another location'),
		(NO, 'No'),
	)
	internet_access = models.SmallIntegerField("Do you have internet access?", choices=INTERNET_ACCESS, blank=True)


# Do you have health insurance?
	EMPLOYER = 1
	GOVERNMENT = 2
	NO = 3
	HEALTH_INSURANCE = (
		(EMPLOYER, 'Yes, from my employer'),
		(GOVERNMENT, 'Yes, from the government'),
		(NO, 'No'),
	)
	health_insurance = models.SmallIntegerField("Do you have health insurance?", choices=HEALTH_INSURANCE, blank=True)

# -------------------------------------------------------------------------------------- #
#	Employment information
# -------------------------------------------------------------------------------------- #

# Employment status
	FULL_TIME = 1
	PART_TIME = 2
	SELF_EMPLOYED = 3
	TEMP_EMPLOYED = 4
	UNEMPLOYED = 5
	EMPLOYMENT_STATUS = (
		(FULL_TIME, 'Employed full-time'),
		(PART_TIME, 'Employed part-time'),
		(SELF_EMPLOYED, 'Self-employed'),
		(TEMP_EMPLOYED, 'Temporarily employed'),
		(UNEMPLOYED, 'Unemployed'),
	)
	employment_status = models.SmallIntegerField(choices=EMPLOYMENT_STATUS)


# If employed, what is your current job?
	current_job = models.CharField("If employed, what is your current job?", max_length=20, blank=True)

# How long at current job?
	employment_period = models.DecimalField("How long at current job?", decimal_places=2, max_digits=3, blank=True)
#	employment_period.help_text = "Enter in years. Can use decimals to indicate months: 1.5 years."
	employment_period.label_suffix = ""

# Are you in a union?
	union_job = models.SmallIntegerField("Are you in a union?", choices=YES_NO, blank=True)

# If not employed, why?
	DISABLED = 1
	FAMILY = 2
	STUDENT = 3
	TRAINING = 4
	RETIRED = 5
	NO_WORK = 6
	OTHER = 7
	WHY_UNEMPLOYED = (
		(DISABLED, 'Disabled'),
		(FAMILY, 'Family obligations'),
		(STUDENT, 'Full-time student'),
		(TRAINING, 'Participating in training program'),
		(RETIRED, 'Retired'),
		(NO_WORK, 'Unable to find work'),
		(OTHER, 'Other'),
	)
	why_unemployed = models.SmallIntegerField("If not employed, why?", choices=WHY_UNEMPLOYED, default=UNEMPLOYED, blank=True)

# How long unemployed?
	unemployment_period = models.DecimalField("How long unemployed?", decimal_places=2, max_digits=3, blank=True)
#	unemployment_period.help_text = "Enter in years. Can use decimals to indicate months: 1.5 years."
	unemployment_period.label_suffix = ""


# Are you collecting unemployment insurance?
	collecting_unemployment = models.SmallIntegerField("Are you collecting unemployment insurance?", choices=YES_NO, blank=True)

# -------------------------------------------------------------------------------------- #
#	Housing information
# -------------------------------------------------------------------------------------- #

# Housing situation
	DOUBLED = 1
	HOMELESS = 2
	FAMILY = 3
	RENT = 4
	RENT_PHA = 5
	RENT_S8 = 6
	TRANSITIONAL = 7
	OTHER = 8
	HOUSING_SITUATION = (
		(DOUBLED, 'Doubled up'),
		(HOMELESS, 'Homeless'),
		(FAMILY, 'Living with family'),
		(RENT, 'Rent - no subsidy'),
		(RENT_PHA, 'Rent - public housing'),
		(RENT_S8, 'Rent - section 8'),
		(TRANSITIONAL, 'Transitional housing'),
		(OTHER, 'Other'),
	)
	housing_situation = models.SmallIntegerField(choices=HOUSING_SITUATION, blank=True)

# Number of adults in household?
	housing_adults = models.DecimalField("How many adults in household?", decimal_places=2, max_digits=3, blank=True)
#	housing_adults.help_text = "Enter in years. Can use decimals to indicate months: 1.5 years."
	housing_adults.label_suffix = ""

# Number of children in household?
	housing_children = models.DecimalField("How many children (under 18) in household?", decimal_places=2, max_digits=3, blank=True)
#	housing_children.help_text = "Enter in years. Can use decimals to indicate months: 1.5 years."
	housing_children.label_suffix = ""

# How many years lived at current residence?
	housing_period = models.DecimalField("How many years lived at current residence?", decimal_places=2, max_digits=3, blank=True)
#	housing_period.help_text = "Enter in years. Can use decimals to indicate months: 1.5 years."
	housing_period.label_suffix = ""

# Household income
	NONE = 1
	_10_LESS = 2
	_10_20 = 3
	_20_30 = 4
	_30_40 = 5
	_40_50 = 6
	_50_MORE = 7
	NA = 8
	HOUSEHOLD_INCOME = (
		(NONE, 'No income'),
		(_10_LESS, '$10,000 or less'),
		(_10_20, '$10,001-$20,000'),
		(_20_30, '$20,001-$30,000'),
		(_30_40, '$30,001-$40,000'),
		(_40_50, '$40,001-$50,000'),
		(_50_MORE, '$50,001 or more '),
		(NA, 'Don\'t know'),
	)
	household_income = models.SmallIntegerField(choices=HOUSEHOLD_INCOME)


class Client_NextDoor(models.Model):
#	clients = models.OneToOneField(Client)
	client = models.ForeignKey(Client)

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
	why_cx = models.CharField("13. Why do you want to get a copy of your criminal record?", max_length=1, choices=WHY_CX)

	arrested = models.CharField("14. Have you ever been arrested?", max_length=1, choices=YES_NO_IDK)

	convicted = models.CharField("15. Have you ever been convicted of a crime?", max_length=1, choices=YES_NO_IDK)

	employer_refused = models.CharField("16. Has an employer ever refused to hire you because of your criminal record?", max_length=1, choices=YES_NO_IDK)

	employer_declined = models.CharField("17. Has an employer ever fired you because of your criminal record?", max_length=1, choices=YES_NO_IDK)
	
	class Meta:
		verbose_name_plural = "Next Door Clients"



#class Notes(models.Model):
#	body = models.TextField()
#	pub_date = models.DateTimeField(default=datetime.datetime.now)
#	author = models.ForeignKey(User)
#	sticky = models.BooleanField(default=False)
	
