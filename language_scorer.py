def lang_scorer(fname1, fname2):
    with open(fname1, 'r') as fhandle: # Opens the first file as read only
        words= fname1.read() # Reads the opened file

    words = words.split("\n")

    with open(fname2, 'r') as fhandle:
        text = fname2.read()

    text = text.upper()

    punc = "!,.;:'\"?-`"

    for p in punc:
        text = text.replace(p, " ")

    split_text = text.split()

for t in split_text:

    score1 = []

    for w in words:
        if (split_text.count(w)) > 0:
        score1.append((w, split_text.count(w)))
        score2 = 0

    for words,score in score1:
        print(words,score)
        score2 += score
        print(score2)

        final_score = sum(score for words, score in score1) / len(split_text)
        print(final_score)
            score1.append(final_score)
        print(score1)