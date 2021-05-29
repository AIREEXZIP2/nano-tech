from textblob import TextBlob
y=input("type your sentence: ")
edu=TextBlob(y)
x=edu.sentiment.polarity
# negative = x<0 and Neutral = 0 and positive x>0 && x<=1
if x<0:
	print("negative")
elif x==0:
	print("Neutral")
elif x>0 and x<=1:
    print("positive")	