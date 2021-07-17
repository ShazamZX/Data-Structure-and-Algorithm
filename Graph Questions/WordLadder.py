#transform word from begin word to end word using a custom dictionary

def seq(start,end,words):
    if end not in words:
        return 0
    queue = []
    w_len = 3 #assuming every word has 3 characters if we want to make it dynamic update it in the loop everytime
    words = set(words)
    queue.append((start,1))
    while queue:
        word,step = queue.pop(0)
        if word == end:
            return step
        for i in range(w_len):
            for j in range(97,123): #a-z check all combinations
                new_word = word[:i] + chr(j) + word[i+1:]
                if new_word in words:
                    words.remove(new_word)
                    queue.append((new_word,step+1))
                    
    return 0



#driver code
        
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

print(seq(beginWord,endWord,wordList))