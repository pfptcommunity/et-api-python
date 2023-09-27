from .Resource import Resource, TResource


class Readable(Resource):
    def __init__(self, parent: TResource, uri: str):
        Resource.__init__(self, parent, uri)

    def read(self):
        self.session.get(self.uri)


class Creatable(Resource):
    def __init__(self, parent: TResource, uri: str):
        Resource.__init__(self, parent, uri)

    def create(self):
        self.session.post(self.uri)


class Deletable(Resource):
    def __init__(self, parent: TResource, uri: str):
        Resource.__init__(self, parent, uri)

    def delete(self):
        self.session.delete(self.uri)


class Updatable(Resource):
    def __init__(self, parent: TResource, uri: str):
        Resource.__init__(self, parent, uri)

    def update(self):
        self.session.put(self.uri)
