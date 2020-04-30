# from apexselftaught.utils.BaseModel import BaseModel, models
# from apexselftaught.apps.authentication.models import User


# # Create your models here.

# class Project(BaseModel):
#     name = models.CharField(max_length=300, null=False, blank=False)
#     link = models.URLField(null=True)
#     description = models.TextField(null=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name


# class ProgrammingLanguage(BaseModel):
#     name = models.CharField(max_length=300, null=False, blank=False)

#     def __str__(self):
#         return self.name


# class ProgrammingLanguageSpecifics(BaseModel):
#     language = models.OneToOneField(ProgrammingLanguage, related_name='language',
#                                     on_delete=models.CASCADE)
#     proficiency = models.IntegerField(null=True, blank=False)
#     is_primary = models.BooleanField(default=False)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)


# class TechnicalEngineeringProficiency(BaseModel):
#     algorithms_proficiency = models.IntegerField(null=True, blank=False)
#     backend_testing_proficiency = models.IntegerField(null=True, blank=False)
#     frontend_testing_proficiency = models.IntegerField(null=True, blank=False)
#     design_patterns_proficiency = models.IntegerField(null=True, blank=False)
#     data_structure_proficiency = models.IntegerField(null=True, blank=False)
#     object_oriented_programming_proficiency = models.IntegerField(null=True, blank=False)
#     ui_ux_proficiency = models.IntegerField(null=True, blank=False)
#     git_proficiency = models.IntegerField(null=True, blank=False)
#     databases_proficiency = models.IntegerField(null=True, blank=False)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)


# class Framework(BaseModel):
#     name = models.CharField(max_length=300, null=False, blank=False)
#     language = models.ForeignKey(ProgrammingLanguage, on_delete=models.CASCADE)
#     proficiency = models.IntegerField(null=True, blank=False)
#     is_primary = models.BooleanField(default=False)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name


# class SoftSKillsProficiency(BaseModel):
#     team_work = models.IntegerField(null=True)
#     logic_reason = models.IntegerField(null=True)
#     communication_proficiency = models.IntegerField(null=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)


# class Certification(BaseModel):
#     title = models.CharField(max_length=300, null=False)
#     institution = models.CharField(max_length=300, null=False)
#     date_issued = models.DateField(null=False)
#     expiration_date = models.DateField(null=False)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title
