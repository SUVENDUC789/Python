#count Character with help of dictionary
def countCharacter(sentence):
    d={}
    for i in sentence:
        d[i]=0
    for i in sentence:
        d[i]+=1
    # print(d)
    return d

#count Word with help of dictionary
def countWord(sentence):
    sentence=sentence.split()
    d={}
    for i in sentence:
        d[i]=0
    for i in sentence:
        d[i]+=1
    # print(d)
    return d


sentence="hi how are you i am fine but i miss you to kindly grunt me leav of absenece for those days only"

print('Character count : ',countCharacter(sentence))
print('Word count : ',countWord(sentence))