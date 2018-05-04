numOfWords=int(input());
dictionary = dict();
for i in range(0, numOfWords):
	inputString = input();
	charsList = inputString.split();
	inputList = list(map(str, charsList))
	
	dictionary[inputList[0]] = inputList[1];

sentenceToTranslate = input();
sentenceWordsList = sentenceToTranslate.split()

translatedSentence = '';
for word in sentenceWordsList:
	translatedSentence = translatedSentence + dictionary.get(word, word) + ' '

translatedSentence = translatedSentence[:-1];

print(translatedSentence)
	