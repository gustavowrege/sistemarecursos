# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import EtapaRecurso, Recurso, Candidato


admin.site.register(EtapaRecurso)
admin.site.register(Recurso)



class CandidatoResource(resources.ModelResource):

    class Meta:
        model = Candidato

class CandidatoAdmin(ImportExportModelAdmin):
    resource_class = CandidatoResource

admin.site.register(Candidato, CandidatoAdmin)
