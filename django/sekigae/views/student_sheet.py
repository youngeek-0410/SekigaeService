from sekigae.models import StudentSheet, Student
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
import json


def student_sheet_dict(sheet_id):
    students_dict = list(Student.objects.filter(student_sheet=sheet_id).values())
    sheet = StudentSheet.objects.filter(pk=sheet_id)
    sheet_dict = list(sheet.values())[0]
    return {"sheet": sheet_dict, "students": students_dict}


class StudentSheetsView(LoginRequiredMixin, View):
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        sheets = StudentSheet.objects.filter(owner_id=request.user.pk)
        sheets_dict = list(sheets.values())
        return JsonResponse({"sheets": sheets_dict})

    def post(self, request, *args, **kwargs):
        user = request.user
        json_data = json.loads(request.body)
        name = json_data['sheet']['name']
        students = json_data['students']
        sheet = StudentSheet(name=name, owner_id=user.pk)
        sheet.save()
        for student in students:
            s = Student(name=student['name'], number=student['number'], student_sheet=sheet)
            if not Student.objects.filter(number=s.number, student_sheet=sheet).exists():
                s.save()
        return JsonResponse(student_sheet_dict(sheet.pk))


class StudentSheetDetailView(LoginRequiredMixin, View):
    http_method_names = ['get', 'delete', 'patch']

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        sheet = StudentSheet.objects.filter(pk=pk).first()
        if sheet is None:
            return JsonResponse({"error": "Could not query the student sheet"}, status=404)
        if sheet.owner.pk != request.user.pk:
            return JsonResponse({"error": "You do not have access rights."}, status=403)
        return JsonResponse(student_sheet_dict(sheet.pk))

    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        sheet = StudentSheet.objects.filter(pk=pk).first()
        if sheet is None:
            return JsonResponse({"error": "Could not query the student sheet"}, status=404)
        if sheet.owner.pk != request.user.pk:
            return JsonResponse({"error": "You do not have access rights."}, status=403)
        sheet.delete()
        return JsonResponse({"message": "Successfullu deleted"})

    def patch(self, request, *args, **kwargs):
        pk = kwargs['pk']
        sheet = StudentSheet.objects.filter(pk=pk).first()
        if sheet is None:
            return JsonResponse({"error": "Could not query the student sheet"}, status=404)
        if sheet.owner.pk != request.user.pk:
            return JsonResponse({"error": "You do not have access rights."}, status=403)

        json_data = json.loads(request.body)
        sheet_name = json_data['sheet']['name']
        students = json_data['students']
        sheet.name = sheet_name
        sheet.save()
        Student.objects.filter(student_sheet=sheet).delete()
        for student in students:
            s = Student(name=student['name'], number=student['number'], student_sheet=sheet)
            if not Student.objects.filter(number=s.number, student_sheet=sheet).exists():
                s.save()
        return JsonResponse(student_sheet_dict(sheet.pk))


def student_sheets_test(request):
    return render(request, 'sekigae/student_sheet/student_sheets_test.html')


def student_sheets_detail_test(requesst):
    return render(requesst, 'sekigae/student_sheet/student_sheets_detail_test.html')
