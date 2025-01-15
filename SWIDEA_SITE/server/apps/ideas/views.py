from django.shortcuts import render, get_object_or_404, redirect
from .forms import IdeaForm
from django.db.models import Count, Exists, OuterRef
from django.http import JsonResponse
from .models import Idea, IdeaStar
import json



def idea_list(request):
    sort = request.GET.get('sort', 'latest')  # 기본 정렬은 최신순
    ideas = Idea.objects.annotate(
        star_count=Count('ideastar')
    ) 
    if sort == 'likes':  # 찜하기순
        ideas = Idea.objects.annotate(likes_count=Count('ideastar')).order_by('-likes_count')
    elif sort == 'name':  # 이름순
        ideas = Idea.objects.order_by('title')
    elif sort == 'oldest':  # 등록순 (오래된 순)
        ideas = Idea.objects.order_by('created_at')
    else:  # 최신순
        ideas = Idea.objects.order_by('-created_at')

    return render(request, 'ideas/list.html', {'ideas': ideas})

def update_interest(request, pk):
    if request.method == 'POST':
        idea = get_object_or_404(Idea, pk=pk)
        data = json.loads(request.body)
        action = data.get('action')

        if action == 'increase':
            idea.interest += 1
        elif action == 'decrease' and idea.interest > 0:
            idea.interest -= 1

        idea.save()
        return JsonResponse({'new_interest': idea.interest})

    return JsonResponse({'error': 'Invalid request'}, status=400)

def toggle_star(request, pk):
    if request.method == 'POST':
        idea = get_object_or_404(Idea, pk=pk)
        star, created = IdeaStar.objects.get_or_create(idea=idea)
        star.is_starred = not star.is_starred
        star.save()
        return JsonResponse({"is_starred": star.is_starred})
    return JsonResponse({"error": "Invalid request method."}, status=400)

def idea_detail(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    return render(request, 'ideas/detail.html', {'idea': idea})

def idea_create(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ideas:list')
    else:
        form = IdeaForm()
    return render(request, 'ideas/form.html', {'form': form})

def idea_update(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('ideas:detail', pk=pk)
    else:
        form = IdeaForm(instance=idea)
    return render(request, 'ideas/form.html', {'form': form})

def idea_delete(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == 'POST':
        idea.delete()
        return redirect('ideas:list')
    return render(request, 'ideas/idea_confirm_delete.html', {'idea': idea})