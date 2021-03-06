import nltk
import re
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from string import digits

ps = PorterStemmer()
def tokenize(phrase):
	# Remove any punctuation
	#phrase = phrase.translate(None, digits)
	lst = [];
	for word in re.findall(r'\s|,|[^,\s]+', phrase):
		# Remove punctuation
		word = re.sub(r'[^\w\s]','',word)	
		# Remove numbers
		word = ''.join([i for i in word if not i.isdigit()])
		# Singlular plural plus tense stemming
		word = ps.stem(word)
		if(len(word)>2):
			lst.append(word)
	return ",".join(lst)

def testTokenize():
	text = "Tandoori Roti (d) (Wheat)"
	text2 = "breakfast, eggs, juices, Lunch, milkshakes, "
	print(tokenize(text))
	print(tokenize(text2))
	print(tokenize("potatoes"))
	print(tokenize("32gm,potatoes"))

#testTokenize()