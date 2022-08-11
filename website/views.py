from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def subtract(request):
    from random import randint

    num_1 = randint(0, 10)
    num_2 = randint(0, 10)
    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']
        correct_answer = int(old_num_1) - int(old_num_2)

        if not answer:
            my_answer = "Hey you forget to fill the form!"
            color = "warning"

            return render(request, 'divide.html', {
                'my_answer': my_answer,
                'num_1': num_1,
                'num_2': num_2,
                'color': color,
            })

        try:

            if int(answer) == correct_answer:
                my_answer = "Correct! " + old_num_1 + " - " + old_num_2 + " = " + answer
                color = "success"
            else:
                my_answer = "Incorrect! " + old_num_1 + " - " + old_num_2 + \
                    " != " + answer + " it is " + str(correct_answer)
                color = "danger"

            return render(request, 'subtract.html', {
                'answer': answer,
                'my_answer': my_answer,
                'num_1': num_1,
                'num_2': num_2,
                'color': color,
            })

        except:
            my_answer = "You fill the form incorrect!"
            color = "warning"

            return render(request, 'divide.html', {
                'my_answer': my_answer,
                'num_1': num_1,
                'num_2': num_2,
                'color': color,
            })

    return render(request, 'subtract.html', {
        'num_1': num_1,
        'num_2': num_2,
    })


def add(request):
    from random import randint

    num_1 = randint(0, 10)
    num_2 = randint(0, 10)
    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']
        correct_answer = int(old_num_1) + int(old_num_2)

        if not answer:
            my_answer = "Hey you forget to fill the form!"
            color = "warning"

            return render(request, 'divide.html', {
                'my_answer': my_answer,
                'num_1': num_1,
                'num_2': num_2,
                'color': color,
            })

        try:

            if int(answer) == correct_answer:
                my_answer = "Correct! " + old_num_1 + " + " + old_num_2 + " = " + answer
                color = "success"
            else:
                my_answer = "Incorrect! " + old_num_1 + " + " + old_num_2 + \
                    " != " + answer + " it is " + str(correct_answer)
                color = "danger"

            return render(request, 'add.html', {
                'answer': answer,
                'my_answer': my_answer,
                'num_1': num_1,
                'num_2': num_2,
                'color': color,
            })
        except:
            my_answer = "You fill the form incorrect!"
            color = "warning"

            return render(request, 'divide.html', {
                'my_answer': my_answer,
                'num_1': num_1,
                'num_2': num_2,
                'color': color,
            })

    return render(request, 'add.html', {
        'num_1': num_1,
        'num_2': num_2,
    })


def multiple(request):
    from random import randint

    num_1 = randint(0, 10)
    num_2 = randint(0, 10)
    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']
        correct_answer = int(old_num_1) * int(old_num_2)

        if not answer:
            my_answer = "Hey you forget to fill the form!"
            color = "warning"

            return render(request, 'divide.html', {
                'my_answer': my_answer,
                'num_1': num_1,
                'num_2': num_2,
                'color': color,
            })

        try:

            if int(answer) == correct_answer:
                my_answer = "Correct! " + old_num_1 + " x " + old_num_2 + " = " + answer
                color = "success"
            else:
                my_answer = "Incorrect! " + old_num_1 + " x " + old_num_2 + \
                    " != " + answer + " it is " + str(correct_answer)
                color = "danger"

            return render(request, 'multiple.html', {
                'answer': answer,
                'my_answer': my_answer,
                'num_1': num_1,
                'num_2': num_2,
                'color': color,
            })
        except:
            my_answer = "You fill the form incorrect!"
            color = "warning"

            return render(request, 'divide.html', {
                'my_answer': my_answer,
                'num_1': num_1,
                'num_2': num_2,
                'color': color,
            })

    return render(request, 'multiple.html', {
        'num_1': num_1,
        'num_2': num_2,
    })


def divide(request):
    from random import randint

    num_1 = randint(0, 10)
    num_2 = randint(1, 10)
    answer = request.POST.get('answer')

    if request.method == "POST":
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']
        correct_answer = int(old_num_1) / int(old_num_2)

        if not answer:
            my_answer = "Hey you forget to fill the form!"
            color = "warning"

            return render(request, 'divide.html', {
                'my_answer': my_answer,
                'num_1': num_1,
                'num_2': num_2,
                'color': color,
            })

        try:
            if float(answer) == correct_answer:
                my_answer = "Correct! " + old_num_1 + " / " + old_num_2 + " = " + answer
                color = "success"
            else:
                my_answer = "Incorrect! " + old_num_1 + " / " + old_num_2 + \
                    " != " + answer + " it is " + str(correct_answer)
                color = "danger"

            return render(request, 'divide.html', {
                'answer': answer,
                'my_answer': my_answer,
                'num_1': num_1,
                'num_2': num_2,
                'color': color,
            })

        except:
            my_answer = "You fill the form incorrect!"
            color = "warning"

            return render(request, 'divide.html', {
                'my_answer': my_answer,
                'num_1': num_1,
                'num_2': num_2,
                'color': color,
            })

    return render(request, 'divide.html', {
        'num_1': num_1,
        'num_2': num_2,
    })


"""
my_answer = "Hey you forget to fill the form!"
        color = "warning"

        return render(request, 'divide.html', {
            'my_answer': my_answer,
            'num_1': num_1,
            'num_2': num_2,
            'color': color,
        })
"""
