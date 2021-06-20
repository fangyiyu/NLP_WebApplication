from transformers import AutoModelForMaskedLM, AutoTokenizer
from transformers import pipeline, set_seed



def pred(a, b):
  nlp = pipeline("fill-mask", model='distilbert-base-cased')
  sequence = f"{a} {nlp.tokenizer.mask_token} {b}"
  result0 = nlp(sequence)
  result = []
  for i in range(len(result0)):
    result.append(result0[i]['sequence'])
  return result

def summarizetext(text):
  summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
  result = summarizer(text, min_length=10, do_sample=False)
  return result

def generator(prompt, max_length):
  model = pipeline('text-generation', model='xlnet-base-cased')
  set_seed(42)
  result = model(prompt, max_length=max_length, num_return_sequences=1)
  return result

def QA(context, question):
  model_name = "deepset/roberta-base-squad2"
  nlp = pipeline(model=model_name, tokenizer=model_name, task="question-answering")
  result = nlp(question=question, context=context)
  return (result['answer'], result['score'])

def classification(text):
  model = pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment")
  result = model(text)
  return result

def translation(text):
  model = pipeline("translation_en_to_fr", model="t5-small")
  result = model(text)
  return result


    
