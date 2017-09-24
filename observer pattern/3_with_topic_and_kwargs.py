from collections import defaultdict

from singoletto import Singleton


class Publisher(object):

    __metaclass__ = Singleton

    def __init__(self):
        self._tactics = defaultdict(set)

    def subscribe(self, reaction, topic):
        self._tactics[topic].add(reaction)

    def sendMessage(self, topic, **kwargs):
        for method in self._tactics[topic]:
            method(**kwargs)


class Warship(object):
    def __init__(self, name):
        self._name = name
        self._pub = Publisher()

        self._pub.subscribe(reaction=self.vira, topic="arriva_un_siluro")
        self._pub.subscribe(reaction=self.spara_cannonata, topic="scende_il_missile")

    def manda_torpedine(self):
        print '{}: lancio la torpedine'.format(self._name)
        self._pub.sendMessage(topic="arriva_un_siluro", strambata=30)

    def lancia_missile(self):
        print '{}: lancio il missile'.format(self._name)
        self._pub.sendMessage(topic="scende_il_missile", alzo=45, chili=200)

    def vira(self, strambata):
        print '{}: viro di {} gradi'.format(self._name, strambata)

    def spara_cannonata(self, alzo, chili):
        print '{}: sparo la cannonata con alzo {} e chili {}'.format(self._name, alzo, chili)

if __name__ == "__main__":
    # 1 .
    bismarck = Warship(name="Bismarck")
    valiant = Warship(name="Valiant")
    # 2.
    bismarck.manda_torpedine()
    valiant.lancia_missile()

