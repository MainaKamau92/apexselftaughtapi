from rest_framework.exceptions import ValidationError
from apexselftaught.apps.core.permissions import IsOwnerOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, viewsets
from rest_framework.response import Response
from apexselftaught.apps.core.database import get_model_object, get_query_set
from apexselftaught.apps.portfolio.models import Project, ProgrammingLanguageSpecifics, ProgrammingLanguage, \
    TechnicalEngineeringProficiency, Framework, SoftSKillsProficiency, Certification
from apexselftaught.apps.portfolio.serializers import ProjectSerializer, ProgrammingLanguageSpecificsSerializer, \
    ProgrammingLanguageSerializer, TechnicalEngineeringProficiencySerializer, FrameworkSerializer, \
    SoftSKillsProficiencySerializer, CertificationSerializer
from apexselftaught.apps.portfolio.renderers import ProjectJSONRenderer, LanguageSpecificsJSONRenderer, \
    ProgrammingLanguageJSONRenderer, TechnicalJSONRenderer, FrameworkJSONRenderer, SoftSKillsProficiencyJSONRenderer, \
    CertificationJSONRenderer


class ProjectViewSet(viewsets.ViewSet, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOnly,)
    renderer_classes = (ProjectJSONRenderer,)
    serializer_class = ProjectSerializer

    def create(self, request):
        project = request.data.get('project', {})
        serializer_context = {
            'user': request.user
        }
        serializer = self.serializer_class(data=project, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        project = request.data.get('project', {})
        project_instance = get_model_object(Project, 'id', pk)
        self.check_object_permissions(request, project_instance)
        serializer_context = {
            'user': request.user
        }
        serializer = self.serializer_class(data=project, context=serializer_context,
                                           instance=project_instance, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        queryset = get_query_set(Project)
        page = self.paginate_queryset(queryset)
        serializer = self.serializer_class(page, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk):
        project = get_model_object(Project, 'id', pk)
        serializer = self.serializer_class(project)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        project = get_model_object(Project, 'id', pk)
        self.check_object_permissions(request, project)
        project.delete()
        return Response(dict(message=f'Project with id {pk}, deleted.'), status=status.HTTP_200_OK)


class ProgrammingLanguageSpecificsViewSet(viewsets.ViewSet, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOnly,)
    renderer_classes = (LanguageSpecificsJSONRenderer,)
    serializer_class = ProgrammingLanguageSpecificsSerializer

    def create(self, request):
        language_details = request.data.get('language', {})
        language_id = language_details.get('language')
        if language_id is None:
            raise ValidationError('language field is required.')
        language = get_model_object(ProgrammingLanguage, 'id', language_id)
        serializer_context = {
            'user': request.user,
            'language': language
        }
        serializer = self.serializer_class(data=language_details, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        language_details = request.data.get('language', {})
        language_id = language_details.get('language')
        language = get_model_object(ProgrammingLanguage, 'id', language_id) if language_id is not None else None
        language_instance = get_model_object(ProgrammingLanguageSpecifics, 'id', pk)
        self.check_object_permissions(request, language_instance)
        serializer_context = {
            'user': request.user,
            'language' if language is not None else None: language
        }
        serializer = self.serializer_class(data=language_details, context=serializer_context,
                                           instance=language_instance, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        queryset = get_query_set(ProgrammingLanguageSpecifics)
        page = self.paginate_queryset(queryset)
        serializer = self.serializer_class(page, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk):
        language = get_model_object(ProgrammingLanguageSpecifics, 'id', pk)
        serializer = self.serializer_class(language)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        language = get_model_object(ProgrammingLanguageSpecifics, 'id', pk)
        self.check_object_permissions(request, language)
        language.delete()
        return Response(dict(message=f'Programming Language specifics of id {pk} deleted.'), status=status.HTTP_200_OK)


class ProgrammingLanguageViewSet(viewsets.ViewSet, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOnly,)
    renderer_classes = (ProgrammingLanguageJSONRenderer,)
    serializer_class = ProgrammingLanguageSerializer

    def list(self, request):
        queryset = get_query_set(ProgrammingLanguage)
        page = self.paginate_queryset(queryset)
        serializer = self.serializer_class(page, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk):
        language = get_model_object(ProgrammingLanguage, 'id', pk)
        serializer = self.serializer_class(language)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TechnicalEngineeringProficiencyViewSet(viewsets.ViewSet, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOnly,)
    renderer_classes = (TechnicalJSONRenderer,)
    serializer_class = TechnicalEngineeringProficiencySerializer

    def create(self, request):
        technical_details = request.data.get('technical', {})
        serializer_context = {
            'user': request.user
        }
        serializer = self.serializer_class(data=technical_details, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        technical_details = request.data.get('technical', {})
        technical_instance = get_model_object(TechnicalEngineeringProficiency, 'id', pk)
        self.check_object_permissions(request, technical_instance)
        serializer_context = {
            'user': request.user
        }
        serializer = self.serializer_class(data=technical_details, instance=technical_instance,
                                           context=serializer_context, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        queryset = get_query_set(TechnicalEngineeringProficiency)
        page = self.paginate_queryset(queryset)
        serializer = self.serializer_class(page, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk):
        technical_instance = get_model_object(TechnicalEngineeringProficiency, 'id', pk)
        serializer = self.serializer_class(technical_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        technical_instance = get_model_object(TechnicalEngineeringProficiency, 'id', pk)
        self.check_object_permissions(request, technical_instance)
        technical_instance.delete()
        return Response(dict(message='Successfully deleted technical proficiency record.'), status=status.HTTP_200_OK)


class FrameworkViewSet(viewsets.ViewSet, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOnly,)
    renderer_classes = (FrameworkJSONRenderer,)
    serializer_class = FrameworkSerializer

    def create(self, request):
        framework = request.data.get('framework', {})
        language_id = framework.get('language')
        if language_id is None:
            raise ValidationError('language field is required.')
        serializer_context = {
            'user': request.user,
            'language': get_model_object(ProgrammingLanguage, 'id', language_id)
        }
        serializer = self.serializer_class(data=framework, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        framework = request.data.get('framework', {})
        language_id = framework.get('language')
        language = get_model_object(ProgrammingLanguage, 'id', language_id) if language_id is not None else None
        framework_instance = get_model_object(Framework, 'id', pk)
        self.check_object_permissions(request, framework_instance)
        serializer_context = {
            'user': request.user,
            'language' if language is not None else None: language
        }
        serializer = self.serializer_class(data=framework, context=serializer_context, instance=framework_instance,
                                           partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        queryset = get_query_set(Framework)
        page = self.paginate_queryset(queryset)
        serializer = self.serializer_class(page, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk):
        framework = get_model_object(Framework, 'id', pk)
        serializer = self.serializer_class(framework)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        framework = get_model_object(Framework, 'id', pk)
        self.check_object_permissions(request, framework)
        framework.delete()
        return Response(dict(message='Framework successfully deleted.'), status=status.HTTP_200_OK)


class SoftSkillsProficiencyViewSet(viewsets.ViewSet, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOnly,)
    renderer_classes = (SoftSKillsProficiencyJSONRenderer,)
    serializer_class = SoftSKillsProficiencySerializer

    def create(self, request):
        soft_skill = request.data.get('soft_skill', {})
        serializer_context = {
            'user': request.user
        }
        serializer = self.serializer_class(data=soft_skill, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        soft_skill = request.data.get('soft_skill', {})
        soft_skill_instance = get_model_object(SoftSKillsProficiency, 'id', pk)
        self.check_object_permissions(request, soft_skill_instance)
        serializer_context = {
            'user': request.user
        }
        serializer = self.serializer_class(data=soft_skill, context=serializer_context, instance=soft_skill_instance,
                                           partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        queryset = get_query_set(SoftSKillsProficiency)
        page = self.paginate_queryset(queryset)
        serializer = self.serializer_class(page, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk):
        soft_skill_instance = get_model_object(SoftSKillsProficiency, 'id', pk)
        serializer = self.serializer_class(soft_skill_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        soft_skill_instance = get_model_object(SoftSKillsProficiency, 'id', pk)
        self.check_object_permissions(request, soft_skill_instance)
        soft_skill_instance.delete()
        return Response(dict(message='Successfully deleted soft skill'), status=status.HTTP_200_OK)


class CertificationViewSet(viewsets.ViewSet, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOnly,)
    renderer_classes = (CertificationJSONRenderer,)
    serializer_class = CertificationSerializer

    def create(self, request):
        certificate = request.data.get('certificate', {})
        serializer_context = {
            'user': request.user
        }
        serializer = self.serializer_class(data=certificate, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        certificate = request.data.get('certificate', {})
        certificate_instance = get_model_object(Certification, 'id', pk)
        self.check_object_permissions(request, certificate_instance)
        serializer_context = {
            'user': request.user
        }
        serializer = self.serializer_class(data=certificate, context=serializer_context, instance=certificate_instance,
                                           partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        queryset = get_query_set(Certification)
        page = self.paginate_queryset(queryset)
        serializer = self.serializer_class(page, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk):
        certificate = get_model_object(Certification, 'id', pk)
        serializer = self.serializer_class(certificate)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        certificate = get_model_object(Certification, 'id', pk)
        self.check_object_permissions(request, certificate)
        certificate.delete()
        return Response(dict(message='Certification deleted successfully'), status=status.HTTP_200_OK)
