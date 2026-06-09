from django.shortcuts import render, redirect, get_object_or_404
from .models import FeeRecord
from .forms import FeeRecordForm
from django.db.models import Q

def home(request):
    query = request.GET.get('search', '')
    if query:
        records = FeeRecord.objects.filter(
            Q(student_name__icontains=query) | Q(roll_no__icontains=query)
        )
    else:
        records = FeeRecord.objects.all()
    return render(request, 'fees/home.html', {'records': records, 'query': query})

def add_record(request):
    if request.method == 'POST':
        form = FeeRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FeeRecordForm()
    return render(request, 'fees/add.html', {'form': form})

def edit_record(request, pk):
    record = get_object_or_404(FeeRecord, pk=pk)
    if request.method == 'POST':
        form = FeeRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FeeRecordForm(instance=record)
    return render(request, 'fees/edit.html', {'form': form, 'record': record})

def toggle_status(request, pk):
    record = get_object_or_404(FeeRecord, pk=pk)
    record.status = 'Unpaid' if record.status == 'Paid' else 'Paid'
    record.save()
    return redirect('home')

def delete_record(request, pk):
    record = get_object_or_404(FeeRecord, pk=pk)
    if request.method == 'POST':
        record.delete()
    return redirect('home')