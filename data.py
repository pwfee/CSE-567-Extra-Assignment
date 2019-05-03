#!/usr/bin/python
import os

ABS_PATH = os.path.abspath('.') 
NLP_TOOLS_PATH = "~/Dev/cl_extra/stanford-parser-full-2018-10-17"
JAVA_COMMAND = "java -cp \"*\" -Xmx1g edu.stanford.nlp.trees.international.pennchinese.UniversalChineseGrammaticalStructure -checkConnected -basic -keepPunct -conllx -treeFile "

TREE_BANKS_PATH = ABS_PATH + "/ctb5.1/bracketed"
TREE_BANKS_EXT = ['.utf8']

TRAIN_RATE = 80
TEST_RATE = 20

OUTPUT_TRAIN = ABS_PATH + "/data/train.conllu"
OUTPUT_TEST = ABS_PATH + "/data/test.conllu"

def filterFiles(folder, exts, train_rate, test_rate):
	_list = list()
	train_file_list = list()
	test_file_list = list()
		
	for fname in os.listdir(folder):
		if fname.endswith(tuple(exts)):
			_list.append(fname)
	
	total_file_num = len(_list)
	train_file_num = int(total_file_num * (TRAIN_RATE * 1.0 / (TRAIN_RATE + TEST_RATE)))
	test_file_num = int(total_file_num - train_file_num)
	
	return _list[:train_file_num], _list[train_file_num:]
	
def main():
	train_file_list, test_file_list = filterFiles(TREE_BANKS_PATH, TREE_BANKS_EXT, TRAIN_RATE, TEST_RATE)	
	print "[Start]TRAIN_RATE: %s%% TEST_RATE: %s%%" % (TRAIN_RATE, TEST_RATE)
	
	for idx, fname in enumerate(train_file_list):
		print "[Convert][Train Dataset]Filename:%s (%s/%s)" % (fname, idx + 1, len(train_file_list))
		pp = os.popen("cd " + NLP_TOOLS_PATH + " && " + JAVA_COMMAND + TREE_BANKS_PATH + "/" + fname) 
		info = pp.readlines()
		f = open(OUTPUT_TRAIN,'a')
		for line in info:  
			f.write(line)    
		f.close()

	for idx, fname in enumerate(test_file_list):
		print "[Convert][Test Dataset]Filename:%s (%s/%s)" % (fname, idx + 1, len(test_file_list))
		pp = os.popen("cd " + NLP_TOOLS_PATH + " && " + JAVA_COMMAND + TREE_BANKS_PATH + "/" + fname) 
		info = pp.readlines()
		f = open(OUTPUT_TEST,'a')
		for line in info:  
			f.write(line)    
		f.close()
		
	print "[End]Data successfully separate"
		
if __name__ == '__main__':
	main()