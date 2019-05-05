#!/usr/bin/python
import os

ABS_PATH = os.path.abspath('.') 
NLP_TOOLS_PATH = "~/Dev/cl_extra/stanford-parser-full-2018-10-17"
JAVA_COMMAND = "java -cp \"*\" -Xmx1g edu.stanford.nlp.trees.international.pennchinese.UniversalChineseGrammaticalStructure -checkConnected -basic -keepPunct -conllx -treeFile "

TREE_BANKS_PATH = ABS_PATH + "/ctb5.1/bracketed"

TRAIN_ID_1 = [1, 270]
TRAIN_ID_2 = [400, 454]
TRAIN_ID_3 = [500, 554]
TRAIN_ID_4 = [590, 1151]
DEV_ID = [301, 325]
TEST_ID = [271, 300]

OUTPUT_TRAIN = ABS_PATH + "/data/train.conllu"
OUTPUT_DEV = ABS_PATH + "/data/dev.conllu"
OUTPUT_TEST = ABS_PATH + "/data/test.conllu"

def generateID():
	train_file_list = list()
	dev_file_list = list()
	test_file_list = list()
	
	for file in range(TRAIN_ID_1[0], TRAIN_ID_1[1] + 1):
		train_file_list.append(str(file).zfill(3))
		
	for file in range(TRAIN_ID_2[0], TRAIN_ID_2[1] + 1):
		train_file_list.append(str(file))

	for file in range(TRAIN_ID_3[0], TRAIN_ID_3[1] + 1):
		train_file_list.append(str(file))
		
	for file in range(DEV_ID[0], DEV_ID[1] + 1):
		dev_file_list.append(str(file))
	
	for file in range(TEST_ID[0], TEST_ID[1] + 1):
		test_file_list.append(str(file))
	
	return train_file_list, dev_file_list, test_file_list
	
def main():
	print "[Start]"
	
	train_set, dev_set, test_set = generateID()
	
	for idx, fname in enumerate(train_set):
		fname = "chtb_%s.fid.utf8" % fname
		print "[Convert][Train Dataset]Filename:%s (%s/%s)" % (fname, idx + 1, len(train_set))
		pp = os.popen("cd " + NLP_TOOLS_PATH + " && " + JAVA_COMMAND + TREE_BANKS_PATH + "/" + fname) 
		info = pp.readlines()
		f = open(OUTPUT_TRAIN,'a')
		for line in info:  
			f.write(line)    
		f.close()

	for idx, fname in enumerate(train_set):
		fname = "chtb_%s.fid.utf8" % fname
		print "[Convert][Train Dataset]Filename:%s (%s/%s)" % (fname, idx + 1, len(train_set))
		pp = os.popen("cd " + NLP_TOOLS_PATH + " && " + JAVA_COMMAND + TREE_BANKS_PATH + "/" + fname) 
		info = pp.readlines()
		f = open(OUTPUT_TRAIN,'a')
		for line in info:  
			f.write(line)    
		f.close()

	for idx, fname in enumerate(dev_set):
		fname = "chtb_%s.fid.utf8" % fname
		print "[Convert][Dev Dataset]Filename:%s (%s/%s)" % (fname, idx + 1, len(dev_set))
		pp = os.popen("cd " + NLP_TOOLS_PATH + " && " + JAVA_COMMAND + TREE_BANKS_PATH + "/" + fname) 
		info = pp.readlines()
		f = open(OUTPUT_TRAIN,'a')
		for line in info:  
			f.write(line)    
		f.close()

	for idx, fname in enumerate(test_set):
		fname = "chtb_%s.fid.utf8" % fname
		print "[Convert][Test Dataset]Filename:%s (%s/%s)" % (fname, idx + 1, len(test_set))
		pp = os.popen("cd " + NLP_TOOLS_PATH + " && " + JAVA_COMMAND + TREE_BANKS_PATH + "/" + fname) 
		info = pp.readlines()
		f = open(OUTPUT_TRAIN,'a')
		for line in info:  
			f.write(line)    
		f.close()
		
	print "[End]Data successfully separate"
		
if __name__ == '__main__':
	main()