# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sqlite3
import objecttier

from textblob import TextBlob


stop_words = {
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
    "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
    "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
    "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
    "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
    "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
    "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
    "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
    "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
    "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"
}
def printNice(results):
    for result in results:
        print(f"""----------------------------------------------------------------------
| Upvotes: {result.Upvote}      | Title: {result.Title}       
| Downvotes: {result.Downvote}  | Solution: {result.Solution}
|
| Read Time: {result.Read_Time} seconds
| TSR Approved: {result.Approved}
---
| Description: {result.Description}
| Product: {result.Product_ID}
| Industry: {result.Industry}
 """)
    print("----------------------------------------------------------------------")


# have a few options on how many items you want to search for
dbconn = sqlite3.connect('Forum.db')


# usecase 1: want to search by product id tag
def returnStats(dbconn):
    posts = objecttier.num_posts(dbconn)
    comments = objecttier.num_comments(dbconn)
    products = objecttier.num_products(dbconn)
    print(f"""General Statistics:
   Number of Posts: {posts:,}
   Number of Comments: {comments:,}
   Number of Products: {products:,}""")


def searchbyID(dbconn):
    product_id = input("What is the product id you are looking for? ")
    results = objecttier.filter_by_PID(dbconn, product_id)
    printNice(results)


# usecase 2: want to search by product name
def searchbyName(dbconn):
    answer = TextBlob(input("What is the name of the product you are looking for? "))
    name = answer.correct()
    results = objecttier.filter_by_Name(dbconn, name)
    printNice(results)


# usecase 3: want to search by industry
def searchbyIndustry(dbconn):
    answer = TextBlob(input("What industry are you looking for? "))
    industry = answer.correct()
    results = objecttier.filter_by_industry(dbconn, industry)
    printNice(results)


def removeDup (results):
    ids = set()
    newResults = list()
    for result in results:
        if result.Review_ID not in ids:
            newResults.append(result)
            ids.add(result.Review_ID)
        else:
            continue
    return newResults


# usecase 4: want to search by problem
def searchbyProblem(dbconn):
    answer = TextBlob(input("What is your problem? "))
    problem = answer.correct()
    all_data = problem.split()
    all_results = []
    for item in all_data:
        reformated = f"%{item}%"
        results = objecttier.filter_by_problem(dbconn, reformated)
        all_results += results
    newResults = removeDup(all_results)
    printNice(newResults)

# Press the green button in the gutter to run the script.
print("** Welcome to the Search Forum Database Application **\n")
print()
returnStats(dbconn)

choice = input("Please enter a command (1-4, x to exit): ")

while choice != "x":
    if choice == "1":
        # usecase 1: want to search by product id tag
        searchbyID(dbconn)
    elif choice == "2":
        # usecase 2: want to search by product name
        searchbyName(dbconn)
    elif choice == "3":
        # usecase 3: want to search by industry
        searchbyIndustry(dbconn)
    elif choice == "4":
        # usecase 4: want to search by problem
        searchbyProblem(dbconn)
    else:
        print("**Error, unknown command, try again...\n")

    choice = input("Please enter a command (1-4, x to exit): ")

#
# done
#
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
