
class Article:
    id = 0
    title = ""
    description = ""

    def toDict(self):
        return dict(id=self.id, title=self.title, description=self.description)