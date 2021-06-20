from django.shortcuts import render, redirect
from . import predict


# Create your views here.

def index(request):
    return render(request, 'apps/index.html')
    
def mask1(request):
    return render(request, 'apps/cloze.html')

def mask2(request):
    if request.method == "POST":
        ABOVE = request.POST.get('ContextAbove')
        BELOW = request.POST.get('ContextBelow')
        result = predict.pred(ABOVE, BELOW)

        return render(request, 'apps/clozeresult.html', {
            "Predict0": result[0],
            "Predict1": result[1],
            "Predict2": result[2],
            "Predict3": result[3],
            "Predict4": result[4],
            "above":ABOVE,
            "below":BELOW,
        })

def summarize1(request):
    return render(request,'apps/summarize.html')

def summarize2(request):
    if request.method == "POST":
        text = request.POST.get("abstract")
        conclude = predict.summarizetext(text)[0]['summary_text']
        return render(request, 'apps/summarizationresult.html', {
            "conclude": conclude,
            "abstract": text,
        })

def textgenerator1(request):
    return render(request, 'apps/generation.html')

def textgenerator2(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        length = int(request.POST.get("length"))
        result = predict.generator(prompt, length)[0]['generated_text']
        return render(request, 'apps/generationresult.html', {
            "result": result,
            "text": prompt,
        })

def qa1(request):
    return render(request, 'apps/questions.html')


def qa2(request):
    if request.method == "POST":
        question = request.POST.get("question")
        context = request.POST.get("context")
        result = predict.QA(context, question)
        return render(request, 'apps/answers.html',{
            "answer": result[0],
            "score": result[1],
            "question": question,
            "context": context,
        })

def sentimental1(request):
    return render(request, 'apps/sentimental.html')

def sentimental2(request):
    if request.method == "POST":
        review = request.POST.get("review")
        result = predict.classification(review)
        mapping = {"LABEL_0":"Joy", 'LABEL_1': "Optimism", 'LABEL_2': "Anger", 'LABEL3': 'Sadness'}
        emotion = mapping[result[0]['label']]
        score = result[0]['score']
        return render(request, 'apps/analysis.html',{
            "emotion": emotion,
            "score": round(result[0]['score'],3),
            "review": review,
        }) 

def translate1(request):
    return render(request, 'apps/translate.html')

def translate2(request):
    if request.method == "POST":
        text = request.POST.get("text")
        result = predict.translation(text)
        return render(request, 'apps/translated.html',{
            "result": result[0]['translation_text'],
            "text": text,
        })




