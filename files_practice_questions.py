

1. Using the file school_prompt2.txt, find the number of characters in the file and assign that value to the variable num_char.
num_char=0
with open("school_prompt2.txt",'r') as f:
    content=f.read()
    for char in content:
        num_char+=1

2.Find the number of lines in the file, travel_plans2.txt, and assign it to the variable num_lines.
num_lines=0
with open("travel_plans2.txt",'r') as f:
    for line in f:
        num_lines+=1

3.Create a string called first_forty that is comprised of the first 40 characters of emotion_words2.txt.
first_forty=''
with open("emotion_words2.txt",'r') as f:
    content=f.read()
    first_forty=content[:40]

4.Write code to find out how many lines are in the file emotion_words.txt as shown above. Save this value to the variable num_lines. Do not use the len method.
num_lines=0
with open("emotion_words.txt",'r') as f:
    for line in f.readlines():
        num_lines+=1


            


