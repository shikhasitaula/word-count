file = '/Users/shikhasitaula/Desktop/Homework/word_count/story.txt'
with open (file, 'r') as text:
    print (text)
    story = text.read().lower()
    print (story)
def count_words(sentence):
    word_and_count = {}
    for word in sentence.split(" "):
        refined_word = remove_punctuation(word) 
        if refined_word in word_and_count:
            current_count = word_and_count[refined_word]
            word_and_count[refined_word] = current_count + 1
        else:  
            word_and_count[refined_word] = 1
    return word_and_count       
            
def print_dict(a): 
    for key,value in a.items():
        print(f"{key} : {value}")
        
def remove_punctuation(word):
    punctuations = [ '.', ',', '!', '?' ,';', ':']
    if word[-1] in punctuations:
        return word[0:-1]
    else: 
        return word

            

a = count_words(story)
print_dict(a)
print()