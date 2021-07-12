from transformers import pipeline, set_seed

def generator(prompt, max_length):
  model = pipeline('text-generation', model='xlnet-base-cased')
  set_seed(42)
  result = model(prompt, max_length=max_length, num_return_sequences=1)
  return result

def pred(a, b):
  nlp = pipeline("fill-mask", model='distilbert-base-cased')
  sequence = f"{a} {nlp.tokenizer.mask_token} {b}"
  result0 = nlp(sequence)
  result = []
  for i in range(len(result0)):
    result.append(result0[i]['sequence'])
  return result

def summarizetext(text):
  # sshleifer/distilbart-cnn-12-6 for Pytorch
  summarizer = pipeline("summarization", model="google/pegasus-xsum")
  result = summarizer(text, min_length=10, do_sample=False)
  return result

def QA(context, question):
  # deepset/roberta-base-squad2 for Pytorch
  model_name = "distilbert-base-uncased-distilled-squad"
  nlp = pipeline(model=model_name, tokenizer=model_name, task="question-answering")
  result = nlp(question=question, context=context)
  return (result['answer'], result['score'])

def classification(text):
  # nlptown/bert-base-multilingual-uncased-sentiment for pytorch, ranking from 1 to 5 stars
  model = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-emotion")
  result = model(text)
  return result

def translation(text):
  model = pipeline("translation_en_to_fr", model="t5-small")
  result = model(text)
  return result


    
