
# coding: utf-8

# In[ ]:


from nltk.stem import PorterStemmer
## input file
f = open(r'D:/大三上/IRTM/hw1/input.txt')
words = f.read()
f.close()

## Tokenization
splitWords = words.split()
# print("=====Tokenization:", end = "\n")
# for words in splitWords: 
#     print(words)

##Remove punctuation
exclude = [',','.','!','?','-','/',';',':','(',')','{','}','[',']',"'",'"']

for c in exclude:
    for i in range(len(splitWords)):
        splitWords[i] = splitWords[i].replace(c,"")
# print("=====Remove punctuation:", end = "\n")
# for words in splitWords: 
#     print(words)

##Lowercasing everything
for i in range(len(splitWords)):
    splitWords[i] = splitWords[i].lower()
# print("=====Lowercasing everything:", end = "\n")
# for words in splitWords: 
#     print(words)

##Stemming using Porter’s algorithm
for i in range(len(splitWords)):
    splitWords[i] = PorterStemmer().stem(splitWords[i])
    
# print("=====Stemming using Porter’s algorithm:", end = "\n")
# for words in splitWords: 
#     print(words)

##Stopword removal    
stopWordsf = open(r'D:\大三上\IRTM\hw1\NLTK_stopWord.txt') 
stopWords = stopWordsf.read()
stopWordsf.close()
stopWords = stopWords.split()
result = [i for i in splitWords if i not in stopwords]

# print("=====Stopword removal&result:", end = "\n")
# for words in result: 
#     print(words)

##Save the result as a txt file
fout = open('D:/大三上/IRTM/hw1/result.txt','w')
fout.write('\n'.join(result))
fout.close()
    

