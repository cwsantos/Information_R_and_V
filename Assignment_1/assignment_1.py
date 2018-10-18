from PorterStemmer import PorterStemmer

def tokenize(input):
    for i in range(len(input)):
        token = input[i]
        if token[-1] == ',' or token[-1] == '.' or token[-1] == ';':
            token = token[:-1]
        token = token.lower()
        input[i] = token

def finalize(tInput, swInput):
    p = PorterStemmer()
    output = open("output.txt", 'w')
    for i in range(len(tInput)):
        token = tInput[i]
        if token == "a" or token == "an" or token == "the":
            output.write("%s\t- article\n" % token)
        elif any(token in x for x in swInput):
            output.write("%s\t- stop word\n" % token)
        else:
            stemword = p.stem(token, 0, len(token)-1)
            output.write("%s\t- %s\n" % (token, stemword))
    output.close()
#----------------------------------------------------------
tokens = open("input.txt", 'r').read()
stopwords = open("stop_word.txt", 'r').read()

stopwords = stopwords.split("\n")
tokens = tokens.split(" ")

tokenize(tokens)
finalize(tokens, stopwords)