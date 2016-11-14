#!/usr/bin/env python

#from thesaurus import apiRequest
#from thesaurus import getSynonymsByType
from thesaurus import validateWord


#userInput = raw_input("Enter an initial verb:")
verbs = [['look'], ['touch'], ['go'], ['fly']]
for verb in verbs:
	print(verb[0])
#verbs.append(userInput)
userInput = raw_input("Next verb: ")
while userInput != "exit":
	isASyn, index, temp = validateWord(verbs, userInput, "verb")
	if isASyn:
		print("Your word is a synonym")
		verbs[index] = temp
	else:
		print("Not a synonym")
	for verbArray in verbs:
		for verb in verbArray:
			print verb
		print('-----------')
	userInput = raw_input("Next verb: ")
	
'''
verbSynonyms = getSynonymsByType(apiRequest("fly"), "verb")

i = 0
for verb in verbSynonyms:
	print(str(i) + ": " + verb)
	i += 1
'''