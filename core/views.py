from django.shortcuts import render
from .forms import NgramForm
from django.http import HttpResponse
import io

def generate_ngrams(text, n):
    return [text[i:i+n] for i in range(len(text)-n+1)]

def ngram_view(request):
    if request.method == 'POST':
        form = NgramForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            n = form.cleaned_data['n']
            ngrams = generate_ngrams(text, n)
            # Запис n-грам у файл
            buffer = io.StringIO()
            for gram in ngrams:
                buffer.write(gram + '\n')
            buffer.seek(0)
            response = HttpResponse(buffer, content_type='text/plain')
            response['Content-Disposition'] = 'attachment; filename=ngrams.txt'
            return response
    else:
        form = NgramForm()

    return render(request, 'ngram_form.html', {'form': form})
