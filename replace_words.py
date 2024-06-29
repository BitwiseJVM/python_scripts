# Question : Given a dictionary consisting of many roots as well 
# as a sentence, write a function “replace words” to stem all the words in the sentence with the root forming it.
# Note:  If a word has many roots that can form it, 
# replace it with the root with the shortest length. Here is an example input and output for this problem

# example 1 : 
# roots = ["cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"

# ANS = "the cat was a rat by the bat"

# example 2: 
# roots = ["cat", "batter", "Bat","rat"]
# sentence = "the cattle was rattled by the battery"

# ANS = "the cat was a rat by the bat"


def replace_words(dictionary,sentence):
#first split the sentence in words then check if root exists , choose the shortest root, join the splitted sentence
    wordlist=sentence.split()
    final_list=[]
    for word in wordlist:
        temp=word
        temp_length=len(word)
        for root in dictionary:       
            if word.startswith(root) and len(root)<temp_length:
                temp=root
        final_list.append(temp)

    final_sentence=' '.join(final_list)

    return final_sentence

sentence=input("enter the sentence: ")
roots={'cat','bat','rat'}

print(replace_words(roots,sentence))
