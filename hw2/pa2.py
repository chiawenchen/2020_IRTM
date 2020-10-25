from nltk.stem import PorterStemmer
import math

times = 1095
dict_df = {}


def cosine_Similarity(x, y):
    with open('D:\\大三上\\IRTM\\hw2\\Doc\\Doc'+str(x)+'.txt', 'r') as doc_x:
        line = doc_x.readline()
        line = doc_x.readline()
        line = doc_x.readline().split()
        x = []
        x_termName = []
        while line:
            x.append(float(line[1]))
            x_termName.append(line[0])
            line = doc_x.readline().split()
    with open('D:\\大三上\\IRTM\\hw2\\Doc\\Doc'+str(y)+'.txt', 'r') as doc_y:
        line = doc_y.readline()
        line = doc_y.readline()
        line = doc_y.readline().split()
        y = []
        y_termName = []
        while line:
            y.append(float(line[1]))
            y_termName.append(line[0])
            line = doc_y.readline().split()
    sumX = sumY = 0
    for i in x:
        sumX += i**2
    len_x = sumX**0.5

    for i in y:
        sumY += i**2
    len_y = sumY**0.5
    
    x_unitVector = []
    y_unitVector = []

    for tfidf in x:
        x_unitVector.append(tfidf/len_x)
    for tfidf in y:
        y_unitVector.append(tfidf/len_y)
    CS = 0
    for i in range(len(x)):
        for j in range(len(y)):
            if x_termName[i] == y_termName[j]:
                CS +=  x_unitVector[i] * y_unitVector[j]

    return CS
## end of cosine_Similarity


for k in range(1, times+1):
    dict_tf = {}
    ## input file

    f = open(r'D:\\大三上\\IRTM\\hw2\\IRTM\\' + str(k) + '.txt')
    words = f.read()
    f.close()

    ## Tokenization
    splitWords = words.split()
    ##Remove punctuation
    exclude = [',','.','!','?','-','/',';',':','(',')','{','}','[',']',"'",'"','`','@','_','1','2','3','4','5','6','7','8','9','0','%',' ','\n','\t']

    for c in exclude:
        for i in range(len(splitWords)):
            splitWords[i] = splitWords[i].replace(c,"")
    ##Lowercasing everything
    for i in range(len(splitWords)):
        splitWords[i] = splitWords[i].lower()

    ##Stemming using Porter’s algorithm
    for i in range(len(splitWords)):
        splitWords[i] = PorterStemmer().stem(splitWords[i])

    ##Stopword removal    
    stopWordsf = open(r'D:\\大三上\\IRTM\\hw1\\NLTK_stopWord.txt') 
    stopWords = stopWordsf.read()
    stopWordsf.close()
    stopWords = stopWords.split()
    result = [i for i in splitWords if i not in stopWords and len(i) != 0]
    documentDict_noRepeatWord = set(result)

    ##calculate term frequency
    for words in result:
        if words in dict_tf.keys():
            dict_tf[words] += 1
        else:
            dict_tf[words] = 1
    ##calculate document frequency
    for words in documentDict_noRepeatWord:
        if words in dict_df.keys():
            dict_df[words] += 1
        else:
            dict_df[words] = 1

    #Save the result as a txt file
    with open('D:\\大三上\\IRTM\\hw2\\dictionary\\DOC'+str(k)+'.txt', 'w') as fout:
        fout.write(str(len(dict_tf))+"\n")
        for words in dict_tf:
            fout.write(words + "\t" + str(dict_tf[words]) + "\n")

# print(dict.items())
dict_term = {}
i = 1
dictionaryInput = "t_index     term        df\n"
for words in dict_df.keys():
    dictionaryInput += str(i)+"\t"+words+"\t"+ str(dict_df[words])+"\n"
    dict_term[words] = i
    i += 1
# print(dictionaryInput)
fout = open('D:\\大三上\\IRTM\\hw2\\dictionary.txt','w')
fout.write(dictionaryInput)
fout.close()



for k in range(1,times+1):
    with open('D:\\大三上\\IRTM\\hw2\\dictionary\\DOC'+str(k)+'.txt', 'r') as DOC:
        with open('D:\\大三上\\IRTM\\hw2\\Doc\\Doc'+str(k)+'.txt', 'w') as Doc:
            wordsTF = DOC.readline()
            Doc.write(wordsTF)
            Doc.write("t_index    tf-idf\n")
            wordsTF = DOC.readline().split()
            while wordsTF:
                tfIdf = float(wordsTF[1]) * math.log10(times/int(dict_df[wordsTF[0]]))
                Doc.write(str(dict_term[wordsTF[0]]) +" " + str(tfIdf) + "\n")
                wordsTF = DOC.readline().split()

a = input("Please input the ID number of document1:")
b = input("Please input the ID number of document2:")


if int(a) > 1095 or int(a) < 1 or int(b) > 1095 or int(b) < 1:
    print("invalide document ID")
else:
    print("Cosine Similarity:", cosine_Similarity(a, b))


    



