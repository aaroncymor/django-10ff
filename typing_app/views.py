from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
import random
from .models import TypingTest

WORD_LIST = [
    "the", "be", "to", "of", "and", "a", "in", "that", "have", "I",
    "it", "for", "not", "on", "with", "he", "as", "you", "do", "at",
    "this", "but", "his", "by", "from", "they", "we", "say", "her", "she",
    "or", "an", "will", "my", "one", "all", "would", "there", "their", "what"
]

def index(request):
    # Get 40 random words for the typing test
    words = random.sample(WORD_LIST, 40)
    context = {
        'words': words,
    }
    return render(request, 'typing_app/index.html', context)

@require_http_methods(["POST"])
def save_result(request):
    try:
        wpm = int(request.POST.get('wpm', 0))
        test = TypingTest.objects.create(wpm=wpm, accuracy=100)
        return render(request, 'typing_app/result_fragment.html', {'test': test})
    except Exception as e:
        return HttpResponse(str(e), status=500)
