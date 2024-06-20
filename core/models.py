from django.db import models
from ckeditor.fields import RichTextField

class Resume(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    career_objective = RichTextField(blank=True, null=True)
    email = models.EmailField(max_length=254, null=True, blank=True, unique=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    city = models.CharField(max_length=500, null=True, blank=True)
    website = models.URLField(max_length=500, null=True, blank=True)
    linkedin = models.URLField(max_length=500, null=True, blank=True)
    skype = models.CharField(max_length=500, null=True, blank=True)
    github = models.URLField(max_length=500, null=True, blank=True)
    stackoverflow = models.URLField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or 'Unnamed Resume'
    
    
# PROFESSIONAL EXPERIENCE
class ProfessionalExperience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='experiences')
    title = models.CharField(max_length=500, null=True, blank=True)
    description = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.title or 'Untitled Experience'
    

# EDUCATIONAL QUALIFICATION
class EducationalQualification(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='educational')
    name_of_degree = models.CharField(max_length=500, null=True, blank=True)
    college_or_school_name = models.CharField(max_length=550, null=True, blank=True)
    passing_years = models.CharField(max_length=200, null=True, blank=True)
    percentage = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name_of_degree or 'Untitled Educational'
    

# SKILL SETS
class SkillSet(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='skills')
    skills = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.skills or 'Unnamed skills'
    

# PROJECT DETAILS
class ProjectDetail(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='projects')
    project_title = models.CharField(max_length=500, null=True, blank=True)
    short_summary = RichTextField(null=True, blank=True)
    project_description = RichTextField(null=True, blank=True)
    technologies_and_tools_used = RichTextField(null=True, blank=True)
    conclusion = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.project_title or 'Unnamed Project'


# LANGUAGES
class Language(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='languages')
    language_name = models.CharField(max_length=550, null=True, blank=True)
    value = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.language_name or 'Unnamed Language'
    



# SUMMARY
class Summary(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='Summarys')
    Sort_Summary = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.Sort_Summary or 'Unnamed Summarys'


