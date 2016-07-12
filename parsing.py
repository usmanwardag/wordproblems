import nltk
from nltk import sent_tokenize, word_tokenize, pos_tag, RegexpParser
import string

# Global environment dictionary, which is updated after each sentence
environment = {}

def preprocess(document):

	"""
	Splits text into sentences and identify POS tags. Additionally, 
	performs a few corrections including 'and' removal and pronoun
	correction.

	Paramaters
	----------
	document: str
		Question with multiple sentences. See examples in data.py

	Returns
	-------
	sentences: str list
		text split in sentences

	words: str list
		text split in words

	tags: tuple list
		tuples with POS tag corresponding to each word
	"""

	# Split into sentences and remove punctuation.
	sentences = [s.translate(None, string.punctuation) for s in sent_tokenize(document)]
	# Split into words.
	words = [word_tokenize(sent) for sent in sentences]
	# Identify POS tags
	tags = [pos_tag(word) for word in words]


	for tag in tags:
		for i in range(0,len(tag)-1):

			# Remove any instances of 'and' which is identified by 'CC' pos
			if tag[i][1] == 'CC':

				# If 'and' is between two nound, discard it.
				# TODO: Make logic for other types of nouns as well.
				if tag[i-1][1] == 'NNP' and tag[i+1][1] == 'NNP':
					tag.remove(tag[i])

				# Else 'and' is between two sentences, in which case split
				else:
					index = tags.index(tag)
					tags.insert(index, tag[0:i])
					tags.insert(index+1, tag[i+1:])
					tags.remove(tags[index+2])

	return sentences, words, tags

# TODO: Replace phrases by single noun.
# TODO: Replace pronouns by corresponding nounds from previous sentences.

def compare(sentence, grammar):
	"""
	Compare sentence against a grammar rule to see if any matches
	are found

	Paramaters
	----------
	sentence: str
		a single sentence for which matches are to be found

	grammar: str
		grammar rule in regexp format

	Returns
	-------
	matches: nltk.tree.Tree
		all matches with the grammar rule

	"""
	matches = []

	# Apply grammar rule
	cp = RegexpParser(grammar)
	chunk = cp.parse(sentence)
	
	# Identify label of the rule
	label = grammar.split(':')[0]

	for n in chunk:
		if isinstance(n, nltk.tree.Tree):
			if n.label() == label:
				matches.append(n)

	if matches == []:
		matches.append('None')

	return matches

def check_match(sub_tree, rule):

	"""
	Apply the matches to get meaning out of sentences.

	Parameters
	----------
	sub_tree: nltk.tree.Tree
		an nltk tree defining the matches, returned by compare()
		method

	rule: str
		grammar rule which is followed by nltk.tree.Tree

	Returns
	-------
	results: tuple list
		tuples are in format: subject, operation element, primary 
		object, and secondary object. For details on these terminologies,
		see rules.py
	"""
	matches = []
	results = []

	# Get tree in form of a list
	for st in sub_tree:
		matches.append([match for match in st])

	# Instantiate to 'None' value
	sub, op, op_ele, p_obj, s_obj = 'None', 'None', 'None', 'None', 'None' 

	for match in matches:
		
		# Update if matches are found
		for a,b in match:
			if b in rule[1]:
				sub = a

			elif b in rule[3]:
				op_ele = a

			elif b in rule[4]:
				p_obj = a

			elif b in rule[5]:
				s_obj = a

		if rule[2] == 'RETAIN':
			op = 'RETAIN'

		elif rule[3] in 'OTHER':
			# TODO: add logic for basic operations including addition,
			# subtraction, multiplication, division
			pass

		results.append([(sub), (op), (op_ele), (p_obj), (s_obj)])	

	return results

def apply_results(results):
	"""
	Apply results to modify environment.

	Paramaters
	----------
	results: tuple list
		returned by check_match() method
	"""

	for result in results:
		# Instantiate a dictionary for subject
		environment[result[0]] = {}
		# Assign 'cardinal', with key being 'primary object'
		environment[result[0]][result[3]] = result[2]
