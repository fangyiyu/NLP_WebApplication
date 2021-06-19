from transformers import AutoModelForMaskedLM, AutoTokenizer
import torch
from transformers import pipeline, set_seed



def pred(a, b):
  tokenizer = AutoTokenizer.from_pretrained("distilbert-base-cased")
  model = AutoModelForMaskedLM.from_pretrained("distilbert-base-cased")
  sequence = f"{a} {tokenizer.mask_token} {b}"

  input = tokenizer.encode(sequence, return_tensors="pt")
  mask_token_index = torch.where(input == tokenizer.mask_token_id)[1]

  token_logits = model(input).logits
  mask_token_logits = token_logits[0, mask_token_index, :]

  top_5_tokens = torch.topk(mask_token_logits, 5, dim=1).indices[0].tolist()
  
  result = []
  for token in top_5_tokens:
    result.append(tokenizer.decode([token]))
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
  model = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr")
  result = model(text)
  return result


    
