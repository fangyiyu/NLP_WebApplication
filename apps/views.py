from django.shortcuts import render, redirect
from . import predict


# Create your views here.

def index(request):
    return render(request, 'apps/index.html')
    
def summarize(request):
    if request.method == "POST":
        text = request.POST.get("abstract")
        conclude = predict.summarizetext(text)[0]['summary_text']
        return render(request, 'apps/summarize.html', {
            "conclude": conclude,
            "abstract": text,
        })
    return render(request,'apps/summarize.html')

def textgenerator(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        length = int(request.POST.get("length"))
        result = predict.generator(prompt, length)[0]['generated_text']
        return render(request, 'apps/generation.html', {
            "result": result,
            "text": prompt,
        })
    return render(request, 'apps/generation.html')

def qa(request):
    if request.method == "POST":
        question = request.POST.get("question")
        context = request.POST.get("context")
        result = predict.QA(context, question)
        return render(request, 'apps/questions.html',{
            "answer": result[0],
            "score": result[1],
            "question": question,
            "context": context,
        })
    return render(request, 'apps/questions.html')

def sentimental(request):
    if request.method == "POST":
        review = request.POST.get("review")
        result = predict.classification(review)
        mapping = {"LABEL_0":"Joy", 'LABEL_1': "Optimism", 'LABEL_2': "Anger", 'LABEL3': 'Sadness'}
        emotion = mapping[result[0]['label']]
        score = result[0]['score']
        return render(request, 'apps/sentimental.html',{
            "emotion": emotion,
            "score": round(result[0]['score'],3),
            "review": review,
        }) 
    return render(request, 'apps/sentimental.html')


def translate(request):
    if request.method == "POST":
        text = request.POST.get("text")
        result = predict.translation(text)
        return render(request, 'apps/translate.html',{
            "result": result[0]['translation_text'],
            "text": text,
        })
    return render(request, 'apps/translate.html')


