# Write a program that searches through a series of product reviews for keywords such as "good", "bad", "excellent", "poor", and "average". If a keyword is found, the program should highlight the keyword in the review in uppercase so they stand out.

python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "This was a poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]

keywords = ["good", "bad", "excellent", "poor", "average"]

for review in python_reviews: # loop through the reviews
    for keyword in keywords: # loop through the keywords
        if keyword in review: # check if the keyword is in the review
            review = review.replace(keyword, keyword.upper()) # replace the keyword with the uppercase keyword
    print(review) # print the review

print('='*50)
#--------------------------------------------------------------------

# Define a function that tallies the number of positive and negative words in each review. The function should return the number of positive and negative words in each review.

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]


def count_pos_neg_words():
    positive_count = 0
    negative_count = 0
    for word in python_reviews:      # loop through the reviews
        for words in positive_words: # loop through the positive words
            if words in word:        # check if the positive word is in the review
                positive_count += 1  # increment the positive count
        for words in negative_words: # loop through the negative words
            if words in word:        # check if the negative word is in the review
                negative_count += 1  # increment the negative count

    print(f'The number of positive words are {positive_count} and the number of negative words are {negative_count}') # print the positive and negative counts

count_pos_neg_words()

print('='*50)

#--------------------------------------------------------------------------------

# Implement a function that takes the first 30 characters of a review and appends "..." to create a summary. Ensure that the summary does not cut off any words.

def review_summary():

    for review in python_reviews:               # loop through the reviews
        summary = review[:30]                   # get the first 30 characters of the review
        space = summary.find(" ", 20)           # find the last space in the first 30 characters. Start searching from the 20th character (trial and error)     (to avoid cutting off words) reference: https://www.w3schools.com/python/ref_string_find.asp. It could have also been displayed as summary.find(" ", 20, 30) but it is not necessary as the summary is already sliced to 30 characters.
        summary_split = summary[:space] + "..." # slice the summary to the last space and add "..."
            
        print(summary_split)                    # print the summary

review_summary()        

print('='*50)

