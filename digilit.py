import collections
import string
from nltk import word_tokenize, pos_tag, ne_chunk, FreqDist
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import time
import sys
import prettytable
COUNT = collections.Counter()


class digilit:
	
	def __init__(self,input_file):
		data = open(input_file, encoding='utf-8')
		data_input = data.readlines()
		self.data_input = data_input
		
	def starter(self):
		'''
			find index of line that the word "chapter" occurs as wellj as find name entities in the data input
			return: count values of name, list of line index with the word "chapter" 
			type: Counter, list
		>>> import digilit
		>>> lit = digilit.digilit("NLFD.txt")
		>>> count = lit.starter()
		'''
		chapter_index = []
		tokens = []
		pos_words = []
		#tag, tokenize, and find name entity by nltk.ne_chunk
		for i, line in enumerate(self.data_input):
			words = word_tokenize(line)
			pos = pos_tag(words, tagset='universal')
			tokens.append(words)
			pos_words.append(pos)
			parse = ne_chunk(pos_tag(word_tokenize(line)))
			m=0
			while m in range(0,len(parse)):
				data = parse[m]
				m+=1
				try:
					if data.label() == 'PERSON': #filter for label 'PERSON'
						COUNT[(data[0][0]).strip("_")]+=1
				except:
					pass
		self.pos_words = pos_words
		self.tokens = tokens
		self.COUNT = COUNT
		return COUNT
		
	def chapterize(self,keyword):
		'''
			input keyword that will be used in segmentize text file, create dictionary of texts for each chapter
			and ranges of each chapter
			return: dictionary of texts 
			type: dict
		'''
		chapter_index =[]
		for i, line in enumerate(self.tokens):
			if keyword in line:
				chapter_index.append(i)
			if set(['THE','END']).issubset(set(line)): #Guternberg Text usually ends with this
				chapter_index.append(i)
		dict_chapter={}
		chapter_range = [(chapter_index[n],chapter_index[n+1]) for n in range(len(chapter_index)-1) if chapter_index[n+1] -chapter_index[n] > 2]
		name = [keyword+" "+str(1+n) for n in range(len(chapter_range)-1)]
		for n in range(len(chapter_range)-1):
			dict_chapter[name[n]]= self.data_input[(chapter_range[n][0]):(chapter_range[n][1])]
		self.chapter_range = chapter_range
		self.key_list = name
		return dict_chapter
		
	def create_name_list(self):
		'''
			create dictionary of names and their count values 
			return: dictionary of name:count
			type: dict, list
		>>> freq_name = create_name_list(ch_index)
		'''
		mess_list = ["project gutenberg","project gutenberg-tm", "project gutenberg-tm's", "gutenberg", "license", "gutenberg-tm", "project gutenberg-tm", "project","such"]
		key_name = [ name for name in list(COUNT.keys()) if name.lower() not in mess_list]
		freq_name = {name:COUNT[name] for name in key_name if name != ""}
		return freq_name
		
	def sort_by_chapter(self):
		'''
			create a dictionary of tokens:count by chapter and a dictionary of POS Tagged list by chapter
			return: a dictionary of tokens by chapter
			type: dict
		>>> lit.sort_by_chapter()
		>>> ['CHAPTER 1': {'Today': 23, 'I':40...},'CHAPTER 2':.......]
		'''
		token_dict={}
		pos_dict={}
		token_list = []
		pos_list = []
		num=0
		a = [y[0] for y in self.chapter_range] #begining range values
		b = [y[1] for y in self.chapter_range] #ending range values
		while num in range(len(self.chapter_range)-1):
			n1 = a[num]
			n2 = b[num]
			token_list.append(sum(self.tokens[n1:n2],[]))
			pos_list.append(sum(self.pos_words[n1:n2],[]))
			num+=1
		#count tokens of each chapter
		z=0
		for items in token_list:
			count_num = dict(FreqDist(items))
			token_dict[self.key_list[z]] = count_num
			z+=1
		a=0
		for pos in pos_list:
			y = [c[1] for c in pos if c[1] not in string.punctuation]
			count= dict(FreqDist(y))
			pos_dict[self.key_list[a]] = count
			a+=1
		self.token_dict = token_dict
		self.pos_dict = pos_dict
		return token_dict
	
	def name_in_chapter(self,num):
		'''
			find top num common names in each chapter and list of top num names
			return: dictionary of names  in each chapter, dictionary of values, word list
			type: dict, list
		>>> lit.name_in_chapter(10)
		>>> [{'CHAPTER 1': {'Name1':5,...'Name10':7}...},[[(1,2),(2,3)],[...]...], ['Name1','Name2','Name3'..]]
		'''
		p=0
		chapter_name = {}
		chapter_value=[]
		filter = self.COUNT.most_common(num)
		top_list = [x[0] for x in filter]
		#find names in dictionary of tokens by chapters
		while p in range(0,len(self.token_dict)):
			chapter = self.key_list[p]
			try:
				result= {vocab: self.token_dict[chapter][vocab] for vocab in self.token_dict[chapter]  if vocab in top_list}	
			except KeyError:
				pass
			chapter_name[chapter]=result
			#change key vocabs into numbers
			value_list=[]
			for key in chapter_name[chapter]:
				num = top_list.index(key)
				value = chapter_name[chapter][key]
				value_list.append((num,value))
			chapter_value.append(value_list)
			p+=1
		j=0
		return chapter_name, chapter_value, top_list
	
	def plot_name_common(self, chapter_value, top_list):	
		'''
			Plot graph from the value acquired from function name_in_chapter(num)
			Return: Graph
		'''
		plt.close()
		length = len(self.key_list)
		x=0
		while x in range(0,length):
			for value in chapter_value[x]:
				ax = value[0]
				ay = value[1]
				plt.scatter(1+x,ax,ay*5, color="#114565", alpha=0.3)
			x+=1
		plt.xticks(np.arange(length+1))
		plt.yticks(np.arange(len(top_list)), top_list)
		plt.show()
		return plt
		
	def name_distribution(self,num):
		'''
			Plot graph of top 'num' frequent names
			Return: Graph
		'''
		title = "Top "+str(num)+" Names By Chapters"
		ch_t,chapter,key = self.name_in_chapter(num)
		plot = self.plot_name_common(chapter,key)
		plot.title(title)
		plot.show()
		return plot
		
	def pronoun_distribution(self):
		'''
			iterate over dictionary of tokens by chapter, then return a dictionary of pronouns found in
			each chapter with its count value
		'''
		FPP = ['I','we','me', 'us', 'my', 'mine', 'our', 'ours', 'myself', 'ourself']
		SPP = ['you','You', 'your', 'yourself','yours']
		TPP = ['He','he','She','she','They','they', 'him','her','them', 'his','hers','their','theirs']
		n=0
		pronoun_chapter={}
		while n in range(0,len(self.token_dict)):
			fp_list=[]
			sp_list=[]
			tp_list=[]
			for element in self.token_dict[self.key_list[n]].items():
				if element[0] in FPP:
					fp_list.append(element)
				elif element[0] in SPP:
					sp_list.append(element)
				elif element[0] in TPP:
					tp_list.append(element)
				else:
					pass
			pronoun_chapter[self.key_list[n]]= [fp_list,sp_list,tp_list]
			n+=1
		return pronoun_chapter
		
	def summary_pn(self,chap_dat):
		''' summarize pronouns of each type for each chapter '''
		dict_key = list(self.token_dict.keys())
		i =0
		pn =[]
		while i in range(0,len(dict_key)):
			z= np.array([k for k in chap_dat[dict_key[i]]])
			pov1= sum([p[1] for p in z[0]])
			pov2 = sum([p[1] for p in z[1]])
			pov3 = sum([p[1] for p in z[2]])
			pron = np.array([pov1,pov2,pov3])
			i+=1
			pn.append(pron)
		return pn
		
	def pronoun_stat_output(self):
		'''
			show mean, sum, and percent of each pronoun type, returning a table
		'''
		pronoun = self.pronoun_distribution()
		sum_pov = self.summary_pn(pronoun)
		data = np.array(sum_pov).T
		FP=data[0]
		SP=data[1]
		TP=data[2]
		mean= [FP.mean(),SP.mean(),TP.mean(), data.mean()]
		sum = [FP.sum(),SP.sum(),TP.sum(),data.sum()]
		percent = [sum[0:3]/data.sum()*100]
		table = prettytable.PrettyTable(['Type', '1ProN', '2ProN', '3ProN', 'All'])
		table.add_row(['Mean', mean[0],mean[1],mean[2],mean[3]])
		table.add_row(['Sum', sum[0],sum[1],sum[2],sum[3]])
		table.add_row(['Percentage', sum[0]/sum[3]*100, sum[1]/sum[3]*100,sum[2]/sum[3]*100,100])
		print(table)
		return
		
	def pos_distribution(self):
		'''
			Find the numbers of each POS tags by chapter according to type
		'''
		content_pos = ['NOUN','VERB','ADJ','ADV', 'INTJ', 'PROPN']
		function_pos =['ADP','CCONJ','DET', 'SCONj', 'PRON','PART']
		pos_by_chapter={}
		i=0
		while i in range(len(self.key_list)):
			sorted_pos = []
			sorted_fn = []
			for t in list(self.pos_dict[self.key_list[i]].keys()):
				if t in content_pos:
					k = t
					v = self.pos_dict[self.key_list[i]][t]
					content = (k,v)
					sorted_pos.append(content)
				elif t in function_pos:
					k = t
					v = self.pos_dict[self.key_list[i]][t]
					function = (k,v)
					sorted_fn.append(function)
			pos_by_chapter[self.key_list[i]] = [sorted_pos,sorted_fn]
			i+=1
		self.content_words = content_pos
		self.function_words = function_pos
		self.pos_tags = pos_by_chapter
		return pos_by_chapter
	
	def pos_stat_output(self):
		i=0
		ratio=[]
		percent = []
		table = prettytable.PrettyTable(['NO.','Content Words', 'Function Words'])
		while i in range(len(self.key_list)):
			value_a = sum([element[1] for element in self.pos_tags[self.key_list[i]][0]])
			value_b = sum([element[1] for element in self.pos_tags[self.key_list[i]][1]])
			all = value_a +value_b
			ratio.append([value_a ,value_b, value_a/all, value_b/all])
			percent.append([[value_a/all], [value_b/all]])
			table.add_row([1+i, value_a/all*100, value_b/all*100])
			i+=1
		print(table)
		return
		
	def pronoun_graph(self):
		plt.close()
		pd= np.array(self.summary_pn(self.pronoun_distribution()))
		length = len(pd)
		normalized_value = [e/e.sum() for e in pd]
		nv = np.array(normalized_value)*100
		x = np.arange(length)
		y1 = nv.T[0] #first person pronoun
		y2 = nv.T[1] #second persond pronoun
		y3 = nv.T[2] #third person pronoun
		h = nv.T[0]+nv.T[1] #height of level two bar
		barWidth = 0.85
		plt.bar(x, y1, color='#4eead6', edgecolor='white', width=barWidth)
		plt.bar(x, y2, bottom = y1, color='#aa9cea', edgecolor='white', width=barWidth)
		plt.bar(x, y3, bottom= h, color='#75bcea', edgecolor='white', width=barWidth)
		plt.show()
		
	
def main():
	text1= "Welcome to DigiLit! \nDigiLit is a basic tool for doing digital humanities."
	text2= "This is developed by Nimit Kumwapee for the final project in 2209261 Basic Programming for NLP. Department of Linguistics, Faculty of Arts, Chulalongkorn University"
	text3= "BTW it is my first program and I have only started to code only a semester. Sorry for any errors."
	text_list = [text1, text2,text3]
	for t in text_list:
		sys.stdout.write(t);time.sleep(0.8)
		sys.stdout.write("\n")
	data_file = input("Please input the name of the file *.txt.  " )
	lit = digilit(data_file)
	if len(lit.data_input) > 5000:
		print("Your data is big. It will takes minutes.")
	print("Processing... Please be patient!")
	count = lit.starter()
	print("Please wait a little more.")
	text = '''Here is the list of functions that you can chose:
		[a] = Count Name Entities			
		[b] = Create Dictionary of Name Entities			
		[c] = Create Dictionary of Text by Chapter			
		[d] = Create Dictionary of Tokens by Chapter			
		[e] = Create Dictionary of POS Tagged Words (Whole Text)
		[f] = Create Dictionary of Pronoun Counts by Chapter
		[g] = Create Dictionary of POS by Chapter
		[h] = Find Top Names in Each Chapter			
		[i] = Statistics of Pronoun
		[j] = Statistics of POS	
		[k] = Graph Top Names Distribution		
		[l]= Graph Pronouns Distribution
		
		[x] = Exit
		
		'''
	dict_name = lit.create_name_list()
	key = input("Before we begin, please identify the section words('CHAPTER, ACT'): " )
	dict_text = lit.chapterize(key)
	token = lit.sort_by_chapter()
	pro = lit.pronoun_distribution()
	pos = lit.pos_distribution()
	x =0
	while x in range(0,50):
		print(text)
		function = input()
		if function == "[a]":
			print(count)
		elif function == "[b]":
			print(dict_name)
		elif function == "[c]":
			print(dict_text)
		elif function == "[d]":
			print(token)
		elif function == "[e]":
			print(lit.pos_words)
		elif function == "[f]":
			print(pro)
		elif function == "[g]":
			print(pos)
		elif function == '[h]':
			num = input('Number of Names:  ')
			num_name,num_value,top_list = lit.name_in_chapter(int(num))
			print(num_name)
		elif function == '[i]':
			lit.pronoun_stat_output()
		elif function == '[j]':
			lit.pos_stat_output()
		elif function == '[k]':
			num = input("Number of Names: ")
			lit.name_distribution(int(num))
		elif function == '[l]':
			lit.pronoun_graph()
		elif function == '[x]':
			break
		else:
			print("WRONG, Input with the following format[ ] from the choices given to you.")
		x+=1

if __name__ == "__main__":
	main()	
