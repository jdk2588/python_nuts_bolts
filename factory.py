class Factory(object):
    def __new__(self, obj_type):
        if obj_type == "video":
            cls = Video

        elif obj_type == "audio":
            cls = Audio

        else:
            raise NotImplemented

        return cls()

class Video(object):
    def __init__(self):
        self.obj = "video"

class Audio(object):
    def __init__(self):
        self.obj = "audio"

    __someprivate = 20
    someprivate = 30

    @property
    def attr(self):
        return self.someprivate

    @attr.setter
    def attr(self, x):
        self.someprivate += x

obj = Factory("audio")
obj.attr = 20
print obj.attr
print obj.someprivate
