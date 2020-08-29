


# 1.The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number of 
# characters in the file and save to the variable num.
num=0
with open("travel_plans.txt",'r') as fileobj:
    content=fileobj.read()
    num=len(content)

# 2.We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number of 
# words in the file and assign this value to the variable num_words.
with open("emotion_words.txt",'r') as fileobj:
    content=fileobj.read()
    num_words=len(content.split())


# 3.Assign to the variable num_lines the number of lines in the file school_prompt.txt.
with open("school_prompt.txt",'r') as fileobj:
    num_lines=len(fileobj.readlines())

# 4.Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
with open("school_prompt.txt",'r') as fileobj:
    beginning_chars=fileobj.read()[:30]


# 5.Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.
three=[]
with open("school_prompt.txt",'r') as fileobj:
    content=fileobj.readlines()
    for line in content:
        words=line.split()
        three.append(words[2])


# 6.Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.
emotions=[]
with open("emotion_words.txt",'r') as fileobj:
    content=fileobj.readlines()
    for line in content:
        words=line.split()
        emotions.append(words[0])

# 7.Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.
with open("travel_plans.txt",'r') as fileobj:
    first_chars=fileobj.read()[0:33]


# 8.Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words
p_words=[]
with open("school_prompt.txt",'r') as f:
    lines=f.readlines()
    for sentence in lines:
        words=sentence.split()
        for word in words:
            if 'p' in word:
                p_words.append(word)
       
    #    or
p_words=[]
with open("school_prompt.txt",'r') as f:
    content=f.read()
    words=content.split()
    for word in words:
        if 'p' in word:
            p_words.append(word)