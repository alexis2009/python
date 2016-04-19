import optparse
import sys
from twisted.python import log
from twisted.web.static import File
from twisted.web.server import Site
from twisted.internet import reactor

from autobahn.twisted.websocket import WebSocketServerFactory, \
    WebSocketServerProtocol
from autobahn.twisted.resource import WebSocketResource


class ChatServerProtocol(WebSocketServerProtocol):

    def onOpen(self):
        self.sendMessage("Enter you name")
        self.logged = False

    def connectionLost(self, reason):
        self.factory.unregister(self)
        self.factory.systemMessage(self, "{} left us...".format(self.name))

    def onMessage(self, payload, isBinary):
        if self.logged:
            self.factory.communicate(self, payload, isBinary)
        else:
            if payload in [c.name for c in self.factory.clients]:
                self.sendMessage("Name already exist. Enter again")
            else:
                self.name = payload
                self.logged = True

                self.sendMessage("Welcome, {}!!!".format(self.name))

                self.factory.systemMessage(
                    self,
                    "{} joined us...".format(self.name)
                )

                users_list = ', '.join([_.name for _ in self.factory.clients])
                if users_list:
                    self.sendMessage("Online users: {}".format(users_list))

                self.factory.register(self)


class ChatFactory(WebSocketServerFactory):

    def __init__(self, *args, **kwargs):
        super(ChatFactory, self).__init__(*args, **kwargs)
        self.clients = []

    def register(self, client):
        self.clients.append(client)

    def unregister(self, client):
        self.clients.remove(client)

    def communicate(self, client, payload, isBinary):
        for c in self.clients:
            c.sendMessage("<{}> {}".format(client.name, payload))

    def systemMessage(self, client, message):
        for c in self.clients:
            c.sendMessage("{}".format(message))


def parse_args():
    parser = optparse.OptionParser()

    parser.add_option('--port', type='int')
    parser.add_option('--iface', default='localhost')

    options, _ = parser.parse_args()

    return options


def main():
    log.startLogging(sys.stdout)

    root = File("web")

    factory = ChatFactory(u"ws://127.0.0.1:8080")
    factory.protocol = ChatServerProtocol
    resource = WebSocketResource(factory)
    root.putChild(u"ws", resource)

    site = Site(root)
    reactor.listenTCP(8080, site)
    reactor.run()


if __name__ == '__main__':
    main()
