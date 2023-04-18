from django.shortcuts import render

def home(request):
    members = [
        {'name': 'John', 'student_number': '123456'},
        {'name': 'Jane', 'student_number': '654321'}
    ]
    context = {'members': members}
    return render(request, 'home.html', context)

def list(request):
    items = [
        {'name': 'Item 1', 'description': 'This is item 1'},
        {'name': 'Item 2', 'description': 'This is item 2'},
        {'name': 'Item 3', 'description': 'This is item 3'}
    ]
    context = {'items': items}
    return render(request, 'list.html', context)

def detail(request, item_id):
    item = {'name': 'Item ' + item_id, 'description': 'This is item ' + item_id + ' detail'}
    context = {'item': item}
    return render(request, 'detail.html', context)

def data_model(request):
    return render(request, 'data_model.html')
