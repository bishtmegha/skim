def strip_all(s):
	s = s.strip()
	s = s.strip('\n\"\',-&\t')
	s = s.lower()
#	print s
	return s
	
print "Reading the dataset...",
#f = open('dataset.txt', 'r')
sentences = []
with open('data.txt', 'r') as f:
	for line in f:
		sentences.append(line)
print ""
f.close()
print "Training the n-grams model..."
initial_words = []
bi_grams = {}
count = {}
count[None] = 0
for sentence in sentences:
	word = sentence.split(' ')[0]
	word = strip_all(word)
	if not word in bi_grams:
		bi_grams[None] = {word:1.0}
	else:
		bi_grams[None][word] +=1.0
	if not word in count:
		count[word]=1
	else:
		count[word]+=1

for sentence in sentences:
	words = sentence.split(' ')
	for i in xrange(1,len(words)):
		words[i] = strip_all(words[i])
		if not words[i-1] in count:
			count[words[i-1]]=1
		else:
			count[words[i-1]]+=1
		if not words[i-1] in bi_grams.keys():
			bi_grams[words[i-1]] = {}
			bi_grams[words[i-1]][words[i]] = 1.0
		else:
			if not words[i] in bi_grams[words[i-1]].keys():
				bi_grams[words[i-1]][words[i]]=1.0
			else:
				bi_grams[words[i-1]][words[i]]+=1.0

for key in bi_grams:
	for sub_key in bi_grams[key]:
		if not key == None:
			bi_grams[key][sub_key] /= count[key]

#print bi_grams

print ""
print "Enter a word: ",
ip_word = raw_input().split(' ')[0]

pre = sorted(bi_grams[ip_word],key=bi_grams[ip_word].get)
print pre[-1],pre[-2],pre[-3]

#for keys in bi_grams[ip_word]:
#	print keys,bi_grams[ip_word][keys]
