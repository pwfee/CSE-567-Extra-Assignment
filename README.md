### CSE-567-Extra-Assignment

Constituent to dependency structure

Author: Wenfeng Pan, Nannan Zhai

https://www.overleaf.com/read/yqstjcmznfxs

#### 1. Corpus preparation and Constituent parsing

First, we have to decide the data split scheme.

Refer to [Improved Inference for Unlexicalized Parsing
](http://www.coli.uni-saarland.de/~yzhang/rapt-ws1112/papers/petrov_2007.pdf), we choose this scheme.

|  | TrainSet | DevSet | TestSet |
| --- | --- | --- | --- |
| ArticleID | 1-270, 400-1151 | 301-325 | 271-300 |

Then we use Python to extract the <S> </S> from the SGML files `ctb5.1/bracketed/chtb_*.fid.utf8`

#### GrammarTrainer
```
$ java -cp berkeleyParser.jar edu.berkeley.nlp.PCFGLA.GrammarTrainer -path revise/train.txt -out chinese.gr --treebank SINGLEFILE
```

#### Test Model

```
$ java -jar berkeleyParser.jar -gr chinese.gr -inputFile revise/test.txt -outputFile revise/parsed.txt
```

#### Eval Model

```
$ evalb -p COLLINS.prm revise/train.txt revise/parsed.txt
```

#### 2. Corpus converting to Dependency structure

We use Stanford Parser to convert the treebank to universal dependency.

https://nlp.stanford.edu/software/lex-parser.html

```
java -cp "*" -Xmx1g edu.stanford.nlp.trees.international.pennchinese.UniversalChineseGrammaticalStructure -checkConnected -basic -keepPunct -conllx -treeFile treebank.txt
``` 

After using `parse.py`, it automatically separate the data and call the Stanford Parser to convert the treebank.

```
$ python parse.py

[Start]
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



#### 3. Dependency parsing

```
$ ./udpipe --train model/ctb_ud.model data/train.conllu
```

```
$ ./udpipe --accuracy  --parse model/ctb_ud.model data/test.conllu

Parsing from gold tokenization with gold tags - forms: 109239, 
UAS: 79.78%, LAS: 76.73%
```



