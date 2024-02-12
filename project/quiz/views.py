from django.shortcuts import render, redirect
from .models import Users, Quiz
from .forms import Users_Forms
from django.http import HttpResponse
from django.template import loader


def site_register(request):
    if request.method == "POST":
        form = Users_Forms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = Users_Forms()

    context = {
        "forms": form
    }
    return render(request, "site_register.html", context)

def site_login(request):
    data = Users.objects.all()
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]

        for i in data:
            if firstname == i.firstname and lastname == i.lastname and email == i.email:
                return redirect("quiz_page")

        else:
            return render(request, 'site_login.html', {'error_message': 'Invalid login'})

    return render(request, "site_login.html")

def home_page(request):
    temp = loader.get_template("welcome.html")
    return HttpResponse(temp.render())


def quiz_page(request):
    if request.method == 'POST':
        questions = Quiz.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0

        for q in questions:
            total += 1
            if q.togri_jav == request.POST.get('question_' + str(q.id)):
                score += 10
                correct += 1
            else:
                wrong += 1

        if total != 0:
            percent = score / (total * 10) * 100
        else:
            percent = 0

        context = {
            'score': score,
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total,
            "questions": questions
        }
        return render(request, 'congrat.html', context)
    else:
        questions = Quiz.objects.all()
        context = {
            'questions': questions
        }
        return render(request, 'quiz_page.html', context)


# def quiz_page(request):
#     if request.method == 'POST':
#         questions = Quiz.objects.all()
#         score = 0
#         wrong = 0
#         correct = 0
#         total = 0
#         for i in questions:
#             total += 1
#             if i.togri_jav == request.POST.get(f"question_{i.id}"):
#                 score += 10
#                 correct += 1
#             else:
#                 wrong += 1
#         if total != 0:
#             percent = score / (total * 10) * 100
#         else:
#             percent = 0
#
#         context = {
#             'score': score,
#             'correct': correct,
#             'wrong': wrong,
#             'percent': percent,
#             'total': total,
#             "questions": questions
#         }
#         return render(request, 'congrat.html', context)
#     else:
#         questions = Quiz.objects.all()
#         user_id = request.session.get('user_id')  # Assuming user ID is stored in session
#         if user_id:
#             user_data = Users.objects.filter(id=user_id).first()
#             if user_data:
#                 first_name = user_data.firstname
#                 last_name = user_data.lastname
#                 # If there are other fields like age, phone number, address, etc., you can fetch them similarly
#             else:
#                 first_name = ""
#                 last_name = ""
#         else:
#             first_name = ""
#             last_name = ""
#
#         context = {
#             'questions': questions,
#             "firstname": first_name,
#             "lastname": last_name
#         }
#         return render(request, 'quiz_page.html', context)


