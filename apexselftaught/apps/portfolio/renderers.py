from apexselftaught.apps.core.renderers import ApexJSONRenderer


class ProjectJSONRenderer(ApexJSONRenderer):
    charset = 'utf-8'
    object_label = 'project'
    pagination_object_label = 'projects'
    pagination_count_label = 'projectCount'


class LanguageSpecificsJSONRenderer(ApexJSONRenderer):
    charset = 'utf-8'
    object_label = 'language-specifics'
    pagination_object_label = 'languages-specifics'
    pagination_count_label = 'languagesSpecificCount'


class ProgrammingLanguageJSONRenderer(ApexJSONRenderer):
    charset = 'utf-8'
    object_label = 'language'
    pagination_object_label = 'languages'
    pagination_count_label = 'languageCount'


class TechnicalJSONRenderer(ApexJSONRenderer):
    charset = 'utf-8'
    object_label = 'technical'
    pagination_object_label = 'technical'
    pagination_count_label = 'technicalCount'


class FrameworkJSONRenderer(ApexJSONRenderer):
    charset = 'utf-8'
    object_label = 'framework'
    pagination_object_label = 'frameworks'
    pagination_count_label = 'frameworksCount'


class SoftSKillsProficiencyJSONRenderer(ApexJSONRenderer):
    charset = 'utf-8'
    object_label = 'soft_skill'
    pagination_object_label = 'soft_skills'
    pagination_count_label = 'softSkillsCount'


class CertificationJSONRenderer(ApexJSONRenderer):
    charset = 'utf-8'
    object_label = 'certificate'
    pagination_object_label = 'certificates'
    pagination_count_label = 'certificateCount'
