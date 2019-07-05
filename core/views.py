from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.shortcuts import render, redirect
from core.forms import MoodForm
from core.models import Mood


myDict = {}

@login_required
def home(request):
    return render(request, 'home.html')

# user authentication process
class Signup(View):

    def get(self, request):
        form = UserCreationForm(request.GET)
        return render(request, 'Signup.html', {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('home')
        else:
            form = UserCreationForm()
        return render(request, 'Signup.html', {'form': form})

# input from user
class Index(View):

    def get(self, request):
        form = MoodForm(request.GET)
        return render(request, 'show.html', {'form': form})

    def post(self,request):
        if request.method == "POST":
            form = MoodForm(request.POST)
            if form.is_valid():
                try:
                    obj = form.save(commit=False)
                    p = form.data
                    print(p)
                    print(obj)

##################################### MOVIE RATING BY REVIEWS #######################################################

                    positive_keywords = ["best", "great", "owsome",
                                         "fantastic", "mindblowing", "amazing",
                                         "marvellous","nice", "super", "good",
                                         "lovely", "love", "smashing", "cool",
                                         "marvellous","smashing","superb",""]

                    negative_keywords = ["bad", "wrost", "flop",
                                         "boaring","not good",
                                         "disguasting", "bakwas",
                                         "faltu", "complicated",
                                         "notbad"]
                    review = []
                    print(p['name1'],p['name2'],p['name3'],p['name4'],p['name5'])
                    a = p['name1']
                    b = p['name2']
                    c = p['name3']
                    d = p['name4']
                    e = p['name5']

                    user1 = a
                    split = user1.split()
                    review.append(split)

                    user2 = b
                    split = user2.split()
                    review.append(split)

                    user3 = c
                    split = user3.split()
                    review.append(split)

                    user4 = d
                    split = user4.split()
                    review.append(split)

                    user5 = e
                    split = user5.split()
                    review.append(split)

                    Pos_counter = 0
                    Neg_counter = 0

                    for each in review:
                        print(each)
                        for word in each:
                            if word in positive_keywords:

                                Pos_counter += 1

                            elif word in negative_keywords:

                                Neg_counter += 1
                            else:
                                pass

                    print("Positive counter is", Pos_counter)
                    print("Negative counter is", Neg_counter)

                    print(
                        "--------------------------------------------------------------------------------------------------------------")

                    if Pos_counter >= Neg_counter:
                        print("Result:")
                        total = Pos_counter
                        per = float(total) * (100 / 5)
                        print("Percentage is: ", per)
                        print("Good movie go for it")
                        print(
                            "-----------------------------------------------------------------------------------------------------------")
                        print("Rating for movie")

                        for i in range(Pos_counter):
                            print("✯ ", end="")

                        obj.star = Pos_counter
                        obj.opinion = 'Go for Movie'
                        obj.result = per
                        obj.save()

                    else:
                        total = Pos_counter
                        per = float(total) * (100 / 5)
                        print("Percentage is: ", per)
                        print("Dont go for movie")
                        print(
                            "-----------------------------------------------------------------------------------------------------------")

                        for i in range(Pos_counter):
                            print("Rating for movie")
                            print("✯ ", end="")
                            print("\n")


                        obj.result = per
                        obj.star = Pos_counter
                        obj.opinion = 'Dont go for Movie'
                        obj.save()


                    print("-------")
                    return redirect('/show')
                except:
                    pass
        else:
            form = MoodForm()
        return render(request,'index.html',{'form':form})


# show all the data on html
class Show(View):

    def get(self, request):
        form = MoodForm(request.GET)
        employees = Mood.objects.all()
        return render(request, "show.html", {'employees': employees})

    def post(self, request):
        if request.method == "POST":
            form = MoodForm(request.POST)
            if form.is_valid():
                try:
                    return redirect('show')
                except:
                    pass
        else:
            form = MoodForm()
        return render(request, 'index.html', {'form': form})

# for delete perticular record
class Delete(View):

    def get(self,request, id):
        mood = Mood.objects.get(id=id)
        mood.delete()

        return redirect("/show")

    def post(self, request):
        if request.method == "POST":
            form = MoodForm(request.POST)
            if form.is_valid():
                try:
                    return redirect('show')
                except:
                    pass
        else:
            form = MoodForm()
        return render(request, 'index.html', {'form': form})