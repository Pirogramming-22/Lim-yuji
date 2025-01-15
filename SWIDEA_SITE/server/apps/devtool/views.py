from django.shortcuts import render, get_object_or_404, redirect
from .models import DevTool
from .forms import DevToolForm
from apps.ideas.models import Idea

def devtool_list(request):
    devtools = DevTool.objects.all()
    return render(request, 'devtool/list.html', {'devtools': devtools})

def devtool_detail(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    ideas = Idea.objects.filter(devtool=devtool)
    return render(request, 'devtool/detail.html', {
        'devtool': devtool,
        'ideas': ideas,
    })

def devtool_create(request):
    if request.method == 'POST':
        form = DevToolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('devtool:list')
    else:
        form = DevToolForm()
    return render(request, 'devtool/form.html', {'form': form})

def devtool_update(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    if request.method == 'POST':
        form = DevToolForm(request.POST, instance=devtool)
        if form.is_valid():
            form.save()
            return redirect('devtool:detail', pk=pk)
    else:
        form = DevToolForm(instance=devtool)
    return render(request, 'devtool/form.html', {'form': form})

def devtool_delete(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    if request.method == 'POST':
        devtool.delete()
        return redirect('devtool:list')
    return render(request, 'devtool/form.html', {'devtool': devtool})
