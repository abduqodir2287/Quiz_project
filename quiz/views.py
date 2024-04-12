from django.shortcuts import render, redirect
from .models import Users, Quiz, Quiz_Rus
from .forms import Users_Forms
from django.http import HttpResponse
from django.template import loader


def site_register(request):
    if request.method == "POST":
        form = Users_Forms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tilni_tanlash")
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
                return redirect("tilni_tanlash")

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

def quiz_page_rus(request):
    if request.method == 'POST':
        questions = Quiz_Rus.objects.all()
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
        return render(request, 'congrat_rus.html', context)
    else:
        questions = Quiz_Rus.objects.all()
        context = {
            'questions': questions
        }
        return render(request, 'quiz_page_rus.html', context)

def tilni_tanlash(request):
    try:
        temp = loader.get_template("tilni_tanlash.html")
        return HttpResponse(temp.render())
    except:
        temp = loader.get_template("welcome.html")
        return HttpResponse(temp.render())

def first_page(request):
    try:
        temp = loader.get_template("first_page.html")
        return HttpResponse(temp.render())
    except:
        temp = loader.get_template("welcome.html")
        return HttpResponse(temp.render())

