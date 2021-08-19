from sekigae.models import StudentSheet
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers


def student_sheets(request):
    owner = request.user
    if request.method == 'GET':
        sheets = StudentSheet.objects.filter(owner_id=owner.pk)
        sheets_json = serializers.serialize('json', sheets)
        return HttpResponse(sheets_json)
    elif request.method == 'POST':
        sheet = StudentSheet(name=request.POST['name'], owner_id=owner.pk)
        sheet.save()
        return HttpResponse(sheet)


def student_sheets_detail(request, pk):
    owner = request.user
    sheet = StudentSheet.objects.get(pk=pk, owner_id=owner.pk)
    if request.method == 'GET':
        sheet_json = serializers.serialize('json', [sheet])
        return HttpResponse(sheet_json)
    elif request.method == 'POST':
        if request.POST['_METHOD'] == 'PATCH':
            sheet.name = request.POST['name']
            sheet.save()
            sheet_json = serializers.serialize('json', [sheet])
            return HttpResponse(sheet_json)
        elif request.POST['_METHOD'] == 'DELETE':
            sheet.delete()
            sheet_json = serializers.serialize('json', [sheet])
            return HttpResponse(sheet_json)


def student_sheets_test(request):
    return render(request, 'sekigae/student_sheet/student_sheets_test.html')


def student_sheets_detail_test(requesst):
    return render(requesst, 'sekigae/student_sheet/student_sheets_detail_test.html')
