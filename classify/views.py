from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests

# custom files
from .classify_num import classify_func

# Home page


def home(request):
    return HttpResponse("Welcome to the Render Host Platform")


# -> Create your views here.
@api_view(["GET"])
def classify_number_api(request):
    number = request.GET.get("number")

    # Validate input
    if not number or not number.isdigit():
        return JsonResponse(
            {"number": "alphabet", "error": "true"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    number = int(number)
    data = classify_func(number)

    # Request fun-fact api
    try:
        response = requests.get(f"http://numbersapi.com/{number}/math?json")
        # check response status
        if response.status_code == 200:
            data["fun_fact"] = response.json().get("text", "No fact found.")

    except requests.exceptions.RequestException as e:
        return JsonResponse(
            {"error": f"Error occurred: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return JsonResponse(data, status=status.HTTP_200_OK)


# @api_view(["GET"])
# def classify_number_api(request, number=None):

#     # Validate input
#     if not number:
#         return JsonResponse(
#             {"number": "alphabet", "error": "true"},
#             status=status.HTTP_400_BAD_REQUEST,
#         )

#     number = int(number)
#     data = classify_func(number)

#     # Request fun-fact api
#     try:
#         response = requests.get(f"http://numbersapi.com/{number}/math?json")
#         # check response status
#         if response.status_code == 200:
#             data["fun_fact"] = response.json().get("text", "No fact found.")

#     except requests.exceptions.RequestException as e:
#         return JsonResponse(
#             {"error": f"Error occurred: {str(e)}"},
#             status=status.HTTP_500_INTERNAL_SERVER_ERROR,
#         )

#     return JsonResponse(data, status=status.HTTP_200_OK)
