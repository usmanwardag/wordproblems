from parsing import *

import rules as ru
import data

def solve(text):

	"""
	Answers a word problem.

	Paramater
	---------
	text: str
		Question with multiple sentences. See examples in data.py

	Returns
	-------
	Currently not specified
	"""

	rules = ru.rules()
	_,_,tags = preprocess(text)

	# Debug
	for tag in tags:
	 	print tag
	print '------------'

	# Extract grammar regexp portion from grammar rules
	grammar = [rule[0] for rule in rules]

	for tag in tags:		
		index = -1
		
		for g in grammar:
		
			matches = compare(tag, g)
			index += 1
			
			# If a match is found, exit
			if matches[0] is not 'None':
				break

		# If match is not found, ignore sentence
		if matches[0] is 'None':
			continue

		results = check_match(matches, rules[index])
		apply_results(results)
		print environment

	# TODO: Understand question and extract information from environment.

if __name__ == "__main__":
	text = data.level0()
	solve(text)

