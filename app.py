import csv
import operator

positiveMap = {}
negativeMap = {}
frequencyMap = {}

with open("Tweets.csv", "rb") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:

        # Exclude the header line
        try:
            float(row[2])
        except:
            continue

        sentiment = row[1]
        confidence = float(row[2])
        tweet = row[10]

        # print "Sentiment: " + str(sentiment)
        # print "Confidence: " + str(confidence)
        # print "Tweet: " + str(tweet)

        for word in tweet.split():
            if word[0] == "@":
                continue
            word = ''.join(e.lower() for e in word if e.isalnum())

            if word in frequencyMap:
                frequencyMap[word] += 1
            else:
                frequencyMap[word] = 1

            if sentiment == "positive":
                if word in positiveMap:
                    positiveMap[word] += confidence
                else:
                    positiveMap[word] = confidence
            
            if sentiment == "negative":
                if word in negativeMap:
                    negativeMap[word] += confidence
                else:
                    negativeMap[word] = confidence        


frequencyMap = sorted(frequencyMap.items(), key=operator.itemgetter(1), reverse=True)
positiveMap = sorted(positiveMap.items(), key=operator.itemgetter(1), reverse=True)
negativeMap = sorted(negativeMap.items(), key=operator.itemgetter(1), reverse=True)

limit = 50

count = 0

for k, v in positiveMap:
    if count == limit:
        break
    print k + " " + str(v)
    count += 1

print "\n\n"

count = 0

for k, v in negativeMap:
    if count == limit:
        break

    print k + " " + str(v)
    count += 1


print "\n\n"

count = 0

for k, v in frequencyMap:
    if count == limit:
        break

    print k + " " + str(v)
    count += 1

