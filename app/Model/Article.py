class Article:
    def __init__(self, title, content, summary):
        self.title = title
        self.content = content
        self.summary = summary
    def __str__(self):
        strRes = self.title + '\n'
        strRes += self.summary + '\n'
        strRes += self.content
        return strRes