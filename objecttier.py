import datatier


class Post:
    def __init__(self, objectID, pid, title, desc, time, up, down, approved, industry, resolved, solution):
        self._Review_ID = objectID
        self._Title = title
        self._Description = desc
        self._Read_Time = time
        self._Upvote = up
        self._Downvote = down
        self._Approved = approved
        self._Industry = industry
        self._Resolved = resolved
        self._Solution = solution
        self._Product_ID = pid

    @property
    def Review_ID(self):
        return self._Review_ID

    @property
    def Title(self):
        return self._Title

    @property
    def Description(self):
        return self._Description

    @property
    def Read_Time(self):
        return self._Read_Time

    @property
    def Upvote(self):
        return self._Upvote

    @property
    def Downvote(self):
        return self._Downvote

    @property
    def Approved(self):
        return self._Approved

    @property
    def Industry(self):
        return self._Industry

    @property
    def Resolved(self):
        return self._Resolved

    @property
    def Solution(self):
        return self._Solution

    @property
    def Product_ID(self):
        return self._Product_ID


class Comments:
    def __init__(self, id, qid, body, uid, upvote, downvote):
        self._Comments_ID = id
        self._Question_ID = qid
        self._Body = body
        self._User_ID = uid
        self._Upvote = upvote
        self._Downvote = downvote

    @property
    def Comments_ID(self):
        return self._Comments_ID

    @property
    def Question_ID(self):
        return self._Question_ID

    @property
    def Body(self):
        return self._Body

    @property
    def User_ID(self):
        return self._User_ID

    @property
    def Upvote(self):
        return self._Upvote

    @property
    def Downvote(self):
        return self._Downvote


class Product:
    def __init__(self, id, name, link):
        self._Product_ID = id
        self._Name = name
        self._Link = link

    @property
    def Comments_ID(self):
        return self._Product_ID

    @property
    def Name(self):
        return self._Name

    @property
    def Link(self):
        return self._Link


# Returns: number of posts in the database
#           if an error occurs, the function returns -1
def num_posts(dbConn):
    try:
        sql = "SELECT DISTINCT COUNT(*) FROM Posts"
        results = datatier.select_one_row(dbConn, sql)
        return results[0]
    except Exception as err:
        return -1


# Returns: number of comments in the database
#           if an error occurs, the function returns -1
def num_comments(dbConn):
    try:
        sql = "SELECT DISTINCT COUNT(*) FROM Comments"
        results = datatier.select_one_row(dbConn, sql)
        return results[0]
    except Exception as err:
        return -1


# Returns: number of products in the database
#           if an error occurs, the function returns -1
def num_products(dbConn):
    try:
        sql = "SELECT DISTINCT COUNT(*) FROM Products"
        results = datatier.select_one_row(dbConn, sql)
        return results[0]
    except Exception as err:
        return -1


# Usecase 1: want to search by product id tag
def filter_by_PID(dbConn, product_id):
    try:
        sql = "SELECT * FROM Posts WHERE Product_ID = ? ORDER BY Num_Upvotes DESC"
        results = datatier.select_n_rows(dbConn, sql, [product_id])
        posts = []
        for row in results:
            posts.append(Post(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
        return posts
    except Exception as err:
        return -1


# Usecase 2: want to search by product name
def filter_by_Name(dbConn, name):
    try:
        # TODO: change to be more loose, if we have more words then we trim down the results
        like_name = ("""
        SELECT Review_ID, Posts.Product_ID, Title, Description, Read_Time, Num_Upvotes, Num_Downvotes, Approved, Industry, Is_Resolved, Solution
FROM Posts
JOIN Products ON Posts.Product_ID = Products.Product_ID
WHERE NAME LIKE ?
ORDER BY Review_ID ASC
                     """)
        results = datatier.select_n_rows(dbConn, like_name, [name])
        posts = []
        for row in results:
            posts.append(Post(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
        return posts
    except Exception as err:
        return -1


# usecase 3: want to search by industry
def filter_by_industry(dbConn, industry):
    try:
        like_industry = """SELECT * FROM Posts WHERE Industry LIKE ? ORDER BY Num_Upvotes DESC"""
        results = datatier.select_n_rows(dbConn, like_industry, [industry])
        posts = []
        for row in results:
            posts.append(Post(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
        return posts
    except Exception as err:
        return -1


# usecase 4: want to search by problem
def filter_by_problem(dbConn, problem):
    like_problem = """
            SELECT * FROM Posts 
            WHERE Title LIKE ? OR DESCRIPTION LIKE ? 
            ORDER BY Num_Upvotes DESC
            """
    try:
        results = datatier.select_n_rows(dbConn, like_problem, [problem, problem])
        posts = []
        for row in results:
            posts.append(Post(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
        return posts

    except Exception as err:
        return -1
