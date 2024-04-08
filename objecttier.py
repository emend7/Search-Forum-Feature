
import datatier
class Post:

    def __init__(self, id, title, desc, time, up, down, approved, industry, resolved):
        self._Review_ID = id
        self._Title = title
        self._Description = desc
        self._Read_Time = time
        self._Upvote = up
        self._Downvote = down
        self._Approved = approved
        self._Industry = industry
        self._Resolved = resolved

    @property
    def Review_ID(self):
        return self._Review_ID

    @property
    def Title(self):
        return self._Title

    @property
    def Description(self):
        return self._Description



class Comments:
    def __init__(self, id):
        self._Comments_ID = id

    @property
    def Comments_ID(self):
        return self._Comments_ID

class Product:
    def __init__(self, id):
        self._Product_ID = id

    @property
    def Comments_ID(self):
        return self._Product_ID