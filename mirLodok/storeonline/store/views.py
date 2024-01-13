from django.shortcuts import render, get_object_or_404
from .models import Group, OutboardMotor
from .forms import ContactForm


def index(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send()
            return render(request, 'base.html')
    title = 'Главная Мир лодок'
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'store/index2.html', context)


def show_motors(request):
    motors = OutboardMotor.objects.all()
    groups = Group.objects.all()
    title = 'Все моторы'
    return render(request, 'store/list2.html', {'motors': motors, 'groups': groups, 'title': title})


def other_motors(request, slug):
    groups = Group.objects.all()
    group = get_object_or_404(Group, slug=slug)
    motors = group.motor.all()
    title = group.title
    context = {
        'groups': groups,
        'group': group,
        'motors': motors,
        'title': title
    }
    return render(request, 'store/list2.html', context)


def show_item(request, slug, item_id):
    item = get_object_or_404(OutboardMotor, pk=item_id)
    group = get_object_or_404(Group, slug=slug)
    title = str(item)
    context = {
        'item': item,
        'group': group,
        'title': title,
    }
    return render(request, 'store/cart2.html', context)
