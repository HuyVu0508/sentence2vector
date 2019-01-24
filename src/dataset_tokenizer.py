from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize  

number_of_files = 120

# Paths
path_raw = "..\\UMBC corpus\\webbase_all_POS\\"
path_tokenized_words = "..\\UMBC corpus\\webbase_all_sentences_tokenized\\words"
path_tokenized_POSs = "..\\UMBC corpus\\webbase_all_sentences_tokenized\\POSs"

# Loop through all files, tokenizing and printing to files
for i in range(1,(number_of_files+1)):
    print(i)
    if i%10==0:
        print("File number - " + str(i))
    
    with open(path_raw + "raw ("+ str(i) + ").possf2", "rb") as f_raw:
        corpus = f_raw.read().decode('utf-8')
        sentences = sent_tokenize(corpus)
        
        word_sentences = []
        POS_sentences = []
        for j,sentence in enumerate(sentences):

            if (sentence[0:5]=="''_''"):
                continue       
            
            try:
                phrases = sentence.split(" ")
                words = []
                POSs = []
                for phrase in phrases:
                    splits = phrase.split("_")
                    words.append(splits[0].replace('\n', ' '))
                    POSs.append(splits[1])
                word_sentences.append(" ".join(words))   
                POS_sentences.append(" ".join(POSs))
            except:
                continue
            
        word_sentences = "\n".join(word_sentences)
        with open(path_tokenized_words + "/tokenized (" + str(i) +").txt", "w", encoding='UTF-8') as f_tokenized:
            f_tokenized.write(word_sentences)
        POS_sentences = "\n".join(POS_sentences)
        with open(path_tokenized_POSs + "/tokenized (" + str(i) +").txt", "w", encoding='UTF-8') as f_tokenized:
            f_tokenized.write(POS_sentences)            
        del sentences
        del word_sentences
        del POS_sentences        
    




















