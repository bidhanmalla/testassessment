from .models import Item

def list(request):
    items = [
        Item('Item 1', 'This is item 1', 10.99, 'item1.jpg'),
        Item('Item 2', 'This is item 2', 19.99, 'item2.jpg'),
        Item('Item 3', 'This is item 3', 14.99, 'item3.jpg')
    ]
    context = {'items': items}
    return render(request, 'list.html', context)
