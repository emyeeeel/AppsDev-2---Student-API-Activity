from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
import json
import api.models as models

students = []

class HelloView(APIView):
    def get(self, request):
        TestView.createStudents()  
        return Response({'message': 'Hello, world!'})


class TestView(APIView):
    
    def createStudents():
        student = models.Student("Amiel", "2015022790", "BSCS", 3)
        students.append(student)
        student = models.Student("Miles", "2022789456", "PolSci", 4)
        students.append(student)
        student = models.Student("AJ", "2021654987", "BSCS", 3)
        students.append(student)

    def displayAllStudents(self):
        students_data = []
        for student in students:
                students_data.append({
                "name": student.name,
                "student_id": student.student_id,
                "course": student.course,
                "year": student.year
            })
        return JsonResponse(students_data, safe=False)
    
    def getStudent(request):  
        if request.method == "POST":
            data = json.loads(request.body)
            
            student_id = data[0].get("student_id")
            
            for student in students:
                if student.student_id == student_id:
                    return JsonResponse({
                        "name": student.name,
                        "student_id": student.student_id,
                        "course": student.course,
                        "year": student.year
                    })
            return JsonResponse({"message": "No student with given student ID found."})
    
    def getNames(self, request):  
        if request.method == "POST":
            data = json.loads(request.body)
            print(data["name"])
            if data["name"] == "Leeroy":
                return JsonResponse({"message": "He is the teacher"})
            else:
                return JsonResponse({"message": "He/She is a student"})
