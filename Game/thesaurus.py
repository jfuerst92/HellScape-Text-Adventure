#!/usr/bin/env python

import urllib2
import json

apiKey = "6c701453bead91b0ba510fd415171f2f"


def apiRequest(word):
	response = urllib2.urlopen("http://words.bighugelabs.com/api/2/" + apiKey + "/" + word + "/json").read()
	return json.loads(response)

def getSynonymsByType(response, wordType):
	return response[wordType]["syn"]
	
def validateWord(wordArrayOfArrays, word, wordType):
	#first check if word is already in wordArray
	for arrayNum in range(len(wordArrayOfArrays)):
		for wurd in wordArrayOfArrays[arrayNum]:
			if (wurd == word):
				return True, arrayNum, wordArrayOfArrays[arrayNum]
	
	#else send api request to get synonyms for word and see if a word in wordArray is a synonym
	wordSynonyms = getSynonymsByType(apiRequest(word), wordType)
	for word1 in wordSynonyms:
		for arrayNum in range(len(wordArrayOfArrays)):
			for word2 in wordArrayOfArrays[arrayNum]:
				if (word1 == word2):
					wordArrayOfArrays[arrayNum].append(word)
					return True, arrayNum, wordArrayOfArrays[arrayNum]

	#if no match found, word is invalid
	return False, -1, []
	


