from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apexselftaught.apps.portfolio.views import (ProjectViewSet, ProgrammingLanguageSpecificsViewSet,
                                                 ProgrammingLanguageViewSet, TechnicalEngineeringProficiencyViewSet,
                                                 FrameworkViewSet, SoftSkillsProficiencyViewSet, CertificationViewSet)

router = DefaultRouter(trailing_slash=False)
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'language-specifics', ProgrammingLanguageSpecificsViewSet, basename='language-specifics')
router.register(r'languages', ProgrammingLanguageViewSet, basename='languages')
router.register(r'technical-skills', TechnicalEngineeringProficiencyViewSet, basename='technical-skills')
router.register(r'frameworks', FrameworkViewSet, basename='frameworks')
router.register(r'soft-skills', SoftSkillsProficiencyViewSet, basename='soft-skills')
router.register(r'certificates', CertificationViewSet, basename='certificates')

urlpatterns = [
    path('', include(router.urls))
]
