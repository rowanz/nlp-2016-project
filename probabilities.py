from nltk import FreqDist, grammar
from nltk.corpus import treebank

def getProdFreq(parsedTree, freqdist):
	"""
	Input: nltk.tree.Tree object, FreqDist object
	Output: nothing
	"""

	# List of productions
	prodList = parsedTree.productions()

	for prod in prodList:
		if prod in freqdist:
			freqdist[prod] += 1
		else:
			freqdist[prod] = 1
	return
	

def getFreqsFromTrees(parsedSents):
	"""
	Input: List of tree objects
	Output: FreqDist
	"""
	output = FreqDist()

	for sent in parsedSents:
		getProdProb(sent, output)
	return output

