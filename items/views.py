from django.shortcuts import render, reverse
from django.http import Http404, HttpResponseRedirect
from django.db.models import Q
from.forms import CreateNewItem

from.models import Item


def home(request):
    items = Item.objects.all()
    if request.method == "POST":
        searched = request.POST['searched']
        items = Item.objects.filter(Q(title__contains=searched) | Q(category__contains=searched))
        results_no = items.count()
        context = {'items': items, 'searched': searched, 'results_no':  results_no}
        return render(request, 'home.html', context)
    else:
        context = {'items': items}
        return render(request, 'home.html', context)


def item_detail(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        raise Http404('Item Not Found')

    if request.method == "POST":
        searched = request.POST['searched']
        items = Item.objects.filter(Q(title__contains=searched) | Q(category__contains=searched))
        results_no = items.count()
        context = {'items': items, 'searched': searched, 'results_no':  results_no}
        return render(request, 'home.html', context)
    else:
        context = {'item': item}
        return render(request, 'item_detail.html', context)


def item_create(request):
    if request.method == 'POST':
        form = CreateNewItem(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            return HttpResponseRedirect(reverse('item_detail', kwargs={'item_id': instance.id}))
    else:
        form = CreateNewItem()
    context = {'form': form}
    return render(request, 'item_create.html', context)
