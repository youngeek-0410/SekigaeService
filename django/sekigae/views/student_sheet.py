from sekigae.models import StudentSheet
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
import json


class StudentSheetsView(LoginRequiredMixin, View):
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        sheets = StudentSheet.objects.filter(owner_id=request.user.pk)
        sheets_json = serializers.serialize('json', sheets)
        return HttpResponse(sheets_json)

    def post(self, request, *args, **kwargs):
        user = request.user
        json_data = json.loads(request.body)
        name = json_data['name']
        sheet = StudentSheet(name=name, owner_id=user.pk)
        sheet.save()
        sheet_json = serializers.serialize('json', [sheet])
        return HttpResponse(sheet)


class StudentSheetDetailView(LoginRequiredMixin, View):
    http_method_names = ['get', 'delete', 'patch']

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        sheet = StudentSheet.objects.filter(pk=pk).first()
        if sheet is None:
            return JsonResponse({"error": "Could not query the student sheet"}, status=404)
        if sheet.owner.pk != request.user.pk:
            return JsonResponse({"error": "You do not have access rights."}, status=403)
        sheet_json = serializers.serialize('json', [sheet])
        return HttpResponse(sheet_json)

    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        sheet = StudentSheet.objects.filter(pk=pk).first()
        if sheet is None:
            return JsonResponse({"error": "Could not query the student sheet"}, status=404)
        if sheet.owner.pk != request.user.pk:
            return JsonResponse({"error": "You do not have access rights."}, status=403)
        sheet.delete()
        sheet_json = serializers.serialize('json', [sheet])
        return HttpResponse(sheet_json)

    def patch(self, request, *args, **kwargs):
        pk = kwargs['pk']
        sheet = StudentSheet.objects.filter(pk=pk).first()
        if sheet is None:
            return JsonResponse({"error": "Could not query the student sheet"}, status=404)
        if sheet.owner.pk != request.user.pk:
            return JsonResponse({"error": "You do not have access rights."}, status=403)
        json_data = json.loads(request.body)
        sheet.name = json_data['name']
        sheet.save()
        sheet_json = serializers.serialize('json', [sheet])
        return HttpResponse(sheet_json)


def student_sheets_test(request):
    return render(request, 'sekigae/student_sheet/student_sheets_test.html')


def student_sheets_detail_test(requesst):
    return render(requesst, 'sekigae/student_sheet/student_sheets_detail_test.html')
