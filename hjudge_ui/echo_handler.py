

class EchoHandler(object):
    def __init__(self):
        pass

    def handle(self, request):
        request["status"]="Processed by echo handler"
        print request
        return request
