# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sqlite3

import objecttier

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
    for row in results:
        print(f"""----------
Title: {row.Title}
Description: {row.Description}
Solution: {row.Solution}
TSR Approved: {row.Approved}
Industry: {row.Industry}
----------
""")

# usecase 2: want to search by product name
def searchbyName(dbconn):
    name = input("What is the name of the product you are looking for? ")
    results = objecttier.filter_by_Name(dbconn, name)
    for row in results:
        print(f"""----------
Title: {row.Title}
Description: {row.Description}
Solution: {row.Solution}
TSR Approved: {row.Approved}
Industry: {row.Industry}
----------
""")

# usecase 3: want to search by industry
def searchbyIndustry(dbconn):
    industry = input("What industry are you looking for? ")
    results = objecttier.filter_by_industry(dbconn, industry)
    for row in results:
        print(f"""----------
Title: {row.Title}
Description: {row.Description}
Solution: {row.Solution}
TSR Approved: {row.Approved}
Industry: {row.Industry}
----------
""")

# usecase 4: want to search by problem
def searchbyProblem(dbconn):
    problem = input("What is your problem? ")
    results = objecttier.filter_by_problem(dbconn, problem)
    for row in results:
        print(f"""----------
Title: {row.Title}
Description: {row.Description}
Solution: {row.Solution}
TSR Approved: {row.Approved}
Industry: {row.Industry}
----------
""")

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
