### CSE-567-Extra-Assignment

Constituent to dependency structure

#### 1. Corpus preparation and Constituent parsing

First, we use `data.py` to separate the treebank data based on Chinese Penn Treebank. 

We can specify the rate of training and testing dataset in the Python script. 

As default, we use 8:2 as train_rate/test_rate.

```
$ python data.py

[Start]TRAIN_RATE: 80% TEST_RATE: 20%
[Convert][Train Dataset]Filename:chtb_073.fid.utf8 (1/712)
[Convert][Train Dataset]Filename:chtb_215.fid.utf8 (2/712)
[Convert][Train Dataset]Filename:chtb_214.fid.utf8 (3/712)
[Convert][Train Dataset]Filename:chtb_072.fid.utf8 (4/712)
[Convert][Train Dataset]Filename:chtb_741.fid.utf8 (5/712)
[Convert][Train Dataset]Filename:chtb_527.fid.utf8 (6/712)
[Convert][Train Dataset]Filename:chtb_526.fid.utf8 (7/712)
...

[Convert][Test Dataset]Filename:chtb_665.fid.utf8 (175/178)
[Convert][Test Dataset]Filename:chtb_403.fid.utf8 (176/178)
[Convert][Test Dataset]Filename:chtb_1100.fid.utf8 (177/178)
[Convert][Test Dataset]Filename:chtb_1101.fid.utf8 (178/178)
[End]Data successfully separate
```

#### 2. Corpus converting to Dependency structure

We use Stanford Parser to convert the treebank to universal dependency.

https://nlp.stanford.edu/software/lex-parser.html

```
java -cp "*" -Xmx1g edu.stanford.nlp.trees.international.pennchinese.UniversalChineseGrammaticalStructure -checkConnected -basic -keepPunct -conllx -treeFile treebank.txt
``` 

After using `data.py`, it automatically separate the data and call the Stanford Parser to convert the treebank.


#### 3. Dependency parsing

```
$ ./udpipe --train model/ctb_ud.model data/train.conllu
```

```
$ ./udpipe --accuracy  --parse model/ctb_ud.model data/test.conllu

Parsing from gold tokenization with gold tags - forms: 109239, 
UAS: 79.78%, LAS: 76.73%
```

