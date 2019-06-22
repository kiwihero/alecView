
#import libraries 

import nltk
import numpy as np
import random
import string
from sklearn.features_extraction.text import TfidVectorizer 
from sklearn.metrics.pairwaise import cosine_similarity 

#read the corpus file
f = open('InterveiwBot.txt','r',errors=ignore') as fin
    raw = f.read()
	raw = raw.lower
	nltk.download('pukt')
	nltk.download('wordnet')
	
	
	#convert to sentences
	sent_tokens = nltk.sent_tokenize(raw) 
	
	# convert to list of words
	word_tokens = nltk.word_tokenize(raw)
	
	
lemmer = nltk.stem.WordNetLemmatizer()

def LemToken(tokens):
    return[lemmer.lemmatize(token) for token in tokens]
	remove_punct_dict = dict((punct),None) for puct
	in string.punctuation)
	def LemNormalize(text)
	  return
	  
   LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
   
   GREET_INPUT =("hello")
   
   GREET_RESPONSE =["hello","How are you?"]
   
   
   #to get response from what you want bot to say
   
   def greet(sentence):
   
   for word in sentence.split():
    if word.lower() in GREET_INPUT:
	  return random.choice(GREET_RESPONSE)
	  
	  def response(user_response):
	      bot_response = ' '
		  sent_tokens.append(user_response)
		  
	TfidVec = TfidVectorizer(tokenizer = LemNormalize, stop_words = 'english')
	tfidf =TfidVec.fit_transform(sent_tokens)
	vals = cosine_similarity(tfidf[-1],tfidf)
	idx = vals.flatten()
	flat.sort()
	req_tfidf = flat[-2]
	
	   if(req_tfidf == 0):
	     bot_response + " I do not Understand"
		 return bot_ response
   
   
   else:
   
   bot_response = bot_response + sent_tokens[idx]
   return bot_response
   
   # line for the chatbot
   
   flag = True
   print("ALEC: My name is Alec.")
   
   while(flag == true):
        user_response = user_response.lower()
		if user_response != 'Good bye'):
		if(user_response == 'Thank you' or == 'thanks fo your time'):
		      flag = False
	         print("ALEC: "You are welcome..")
			 
		else: 
            print("ALEC: " , end " ")
            print(response(user_response))
            sent_tokens.remove(user_response)
			flag = Flase
			print(ALEC:Good Bye.")
			
			
