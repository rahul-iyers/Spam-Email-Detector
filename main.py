from collections import defaultdict
import re
import pandas as pd

# DATA PREPROCESSING

df = pd.read_csv("emails.csv")
df['text'] = df['text'].str.partition(' ')[2]

# CREATING WORD MAP COUNTS
spamWordMap = defaultdict(int)
normalWordMap = defaultdict(int)

for rowIndex, email in enumerate(df['text']):
    words = email.split()
    filtered_words = [word for word in words if re.match(r'^[a-zA-Z]+$', word)]
    filtered_words = [word.lower() for word in filtered_words]
    if df.loc[rowIndex, 'spam'] == 1:
        for word in filtered_words:
            spamWordMap[word]+=1
    else:
        for word in filtered_words:
            normalWordMap[word]+=1

sizeSpamWordMap = len(spamWordMap)
sizeNormalWordMap = len(normalWordMap)

def spamDetection(text):
    inputTextWordMap = defaultdict(int)
    words = text.split()
    filtered_words = [word for word in words if re.match(r'^[a-zA-Z]+$', word)]
    filtered_words = [word.lower() for word in filtered_words]
    # inputLength = len(filtered_words)
    for word in filtered_words:
        inputTextWordMap[word]+=1
    
    normalEmailProbability = 1
    for word in inputTextWordMap:
        # wordCount = normalWordMap[word]
        if normalWordMap[word] == 0:
            normalWordMap[word] = 1
        normalEmailProbability *= normalWordMap[word] / sizeNormalWordMap
    

    spamEmailProbability = 1
    for word in inputTextWordMap:
        # wordCount = spamWordMap[word]
        if spamWordMap[word] == 0:
            spamWordMap[word] = 1
        spamEmailProbability *= spamWordMap[word] / sizeSpamWordMap
    
    # normalMessage = "This email does not appear to be spam!"
    # spamMessage = "This email appears to be spam!"

    print("NORMAL PROB: ", normalEmailProbability)
    print("SPAM PROB: ", spamEmailProbability)

    percentage = spamEmailProbability / (spamEmailProbability + normalEmailProbability) * 100
    
    return f"There is a {round(percentage)}% chance that this is a spam email."


    