from django.shortcuts import render, reverse
from django.http import Http404, HttpResponseRedirect
from django.db.models import Q
from.forms import CreateNewItem

from.models import Item


def home(request):
    """
    View for home page
    :param request
    :return: Renders home page from home.html view
    """
    items = Item.objects.all()

    # If search was used, query items and return only the once that contain searched word in either title or category
    if request.method == "POST":
        searched = request.POST['searched']
        items = Item.objects.filter(Q(title__contains=searched) | Q(category__contains=searched))
        results_no = items.count()
        context = {'items': items, 'searched': searched, 'results_no':  results_no}
        return render(request, 'home.html', context)

    # If search was not used, render home page with all items as default
    else:
        context = {'items': items}
        return render(request, 'home.html', context)


def item_detail(request, item_id):
    """
    View for item detail page
    :param request
    :param item_id: id of the requested item
    :return: Renders item detail page from item_detail.html view
    """

    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        raise Http404('Item Not Found')

    # If search was used, query items and return only the once that contain searched word in either title or category.
    # User will be redirected to home page
    if request.method == "POST":
        searched = request.POST['searched']
        items = Item.objects.filter(Q(title__contains=searched) | Q(category__contains=searched))
        results_no = items.count()
        context = {'items': items, 'searched': searched, 'results_no':  results_no}
        return render(request, 'home.html', context)

    # Render item detail page
    else:
        context = {'item': item}
        return render(request, 'item_detail.html', context)


def item_create(request):
    """
    View for item create page
    :param request
    :return: Renders item create page from item_create.html view
    """

    # When user clicks on submit button, POST request is generated. Form with all input should be saved in database.
    # If successful, user will be redirected to the item detail page of the item, that was just created
    if request.method == 'POST':
        form = CreateNewItem(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            return HttpResponseRedirect(reverse('item_detail', kwargs={'item_id': instance.id}))

    # Render item create page
    else:
        form = CreateNewItem()
    context = {'form': form}
    return render(request, 'item_create.html', context)
