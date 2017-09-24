class Publisher(object):
    def __init__(self):
        self._subscribers = set()

    """ pub.subscribe"""
    def subscribe(self, new_subscriber):
        self._subscribers.add(new_subscriber)

    def unsubscribe(self, old_subscriber):
        self._subscribers.discard(old_subscriber)

    """ pub.sendMessage"""        
    def publish(self, message):
        for subscriber in self._subscribers:
            subscriber(message)

class Foo(object):   # un subscriber
    def __init__(self, name, publisher):
        self.name = name
        self._publisher = publisher

    """ pub.subscribe"""
    def make_subscription(self, subscribe=True):
        if subscribe:
            self._publisher.subscribe(self.deal_with_incoming_message)
        else:
            self._publisher.unsubscribe(self.deal_with_incoming_message)

    """ pub.sendMessage"""
    def say_hello(self):
        self._publisher.publish('Hello world da... ' + self.name)

    def deal_with_incoming_message(self, message):
        print 'Sono', self.name, 'e ho ricevuto:', message

pub = Publisher()
andrea = Foo('Andrea', pub)
mario = Foo('Mario', pub)
andrea.make_subscription()
mario.make_subscription()
andrea.say_hello()