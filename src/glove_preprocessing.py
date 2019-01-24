import numpy as np



def loadGloveModel(gloveFile,vocabulary_size, embedding_size):
    print("Loading Glove Model")
    f = open(gloveFile,'rb')
    dictionary = []
    embeddings = np.zeros([vocabulary_size, embedding_size])

    # Attach <unk> word on last line of Glove file
    last_line = f.readlines()[-1]
    splitLine = last_line.split()
    word = splitLine[0]
    dictionary.append(word)    
    word_embedding = np.array([float(val) for val in splitLine[1:]])
    embeddings[0,:] = word_embedding
    
    # Attach all words from 0 -> vocabulary_size-2 (total of vocabulary_size-1 words)
    f.seek(0, 0)
    for i, line in enumerate(f):
        if i==(vocabulary_size-1):
            break        
        splitLine = line.split()
        word = splitLine[0]
        dictionary.append(word)
        word_embedding = np.array([float(val) for val in splitLine[1:]])
        embeddings[i+1,:] = word_embedding

    print("Done.",len(dictionary)," words loaded!")
    return dictionary, embeddings

# Read data
embedding_dim = 300
vocabulary_size = 50000
gloveFile = "D:/Stony Brook University/Subjects/Fall 2018/NLP/Final project NLP/S2V-master/src/dictionaries/glove.6B/glove.6B."+str(embedding_dim)+"d.txt"
dictionary, embeddings = loadGloveModel(gloveFile, vocabulary_size, embedding_dim)

# Write down to dictinary and npy files
gloveProcessedPath = "D:/Stony Brook University/Subjects/Fall 2018/NLP/Final project NLP/S2V-master/src/dictionaries/Glove"
# Write dictionary .txt
with open(gloveProcessedPath + "/glove.6B." + str(embedding_dim) + "d.txt", "w", encoding='UTF-8') as f_dictionary:
    for i in range(len(dictionary)):
        f_dictionary.write(dictionary[i].decode("utf-8") + "\n")
    f_dictionary.close()
    
# Write embedding array .npy    
np.save(gloveProcessedPath + "/glove.6B." + str(embedding_dim) + "d.npy", embeddings)    
    












