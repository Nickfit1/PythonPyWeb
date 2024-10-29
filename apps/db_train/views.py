from django.shortcuts import render
from django.views import View
from .models import Author, AuthorProfile, Entry, Tag
from django.db.models import Q, Max, Min, Avg, Count
# from .models import ...


class TrainView(View):
    def get(self, request):
        max_self_esteem = Author.objects.aggregate(max_self_esteem=Max('self_esteem'))
        self.answer1 = Author.objects.filter(self_esteem=max_self_esteem['max_self_esteem'])

        max_entry_author = Entry.objects.aggregate(max_entry=Max('author'))
        self.answer2 = Author.objects.get(entries=max_entry_author['max_entry'])

        self.answer3 = Entry.objects.filter(tags__name__in=['Кино', 'Музыка'])

        self.answer4 = Author.objects.filter(gender__in='ж').count()

        self.answer5 = None  # TODO Какой процент авторов согласился с правилами при регистрации?

        self.answer6 = Author.objects.filter(authorprofile__stage__gte=1).filter(authorprofile__stage__lte=5)

        max_age = Author.objects.aggregate(max_age=Max('age'))
        self.answer7 = max_age['max_age']

        self.answer8 = None

        self.answer9 = Author.objects.filter(age__lte=25)

        self.answer10 = None  # TODO Сколько статей написано каждым автором?

        context = {f'answer{index}': self.__dict__[f'answer{index}'] for index in range(1, 11)}

        return render(request, 'train_db/training_db.html', context=context)

