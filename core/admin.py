from django.contrib import admin
from .models import Resume, ProfessionalExperience, EducationalQualification, SkillSet, ProjectDetail, Language, Summary

class ProfessionalExperienceInline(admin.TabularInline):
    model = ProfessionalExperience
    extra = 1

class EducationalQualificationInline(admin.TabularInline):
    model = EducationalQualification
    extra = 1

class SkillSetInline(admin.TabularInline):
    model = SkillSet
    extra = 1

class ProjectDetailInline(admin.TabularInline):
    model = ProjectDetail
    extra = 1

class LanguageInline(admin.TabularInline):
    model = Language
    extra = 1

class SummaryInline(admin.TabularInline):
    model = Summary
    extra = 1

class ResumeAdmin(admin.ModelAdmin):
    inlines = [
        ProfessionalExperienceInline,
        EducationalQualificationInline,
        SkillSetInline,
        ProjectDetailInline,
        LanguageInline,
        SummaryInline,
    ]

admin.site.register(Resume, ResumeAdmin)
