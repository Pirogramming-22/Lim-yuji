from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from .forms import ReviewForm

# Create your views here.
# 리뷰 리스트 페이지
def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/review_list.html', {'reviews': reviews})

# 리뷰 디테일 페이지
def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    return render(request, 'reviews/review_detail.html', {'review': review})

# 리뷰 작성 페이지
def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews:review_list')
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_form.html', {'form': form})

# 리뷰 수정 페이지
def review_edit(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('reviews:review_detail', pk=review.pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'reviews/review_form.html', {'form': form})

# 리뷰 삭제
def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    review.delete()
    return redirect('reviews:review_list')

# 리뷰 수정 & 작성
def review_form(request, pk=None):
    if pk:  # 수정 모드
        review = get_object_or_404(Review, pk=pk)
        form = ReviewForm(request.POST or None, instance=review)
    else:  # 작성 모드
        form = ReviewForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        review = form.save()  # form.save()가 수정/생성 모두 처리
        if pk:
            return redirect('reviews:review_detail', pk=review.pk)
        return redirect('reviews:review_list')

    return render(request, 'reviews/review_form.html', {'form': form})