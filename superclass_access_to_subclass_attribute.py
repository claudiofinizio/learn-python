class Quorum(object):
    def __init__(self):
        print 'My label is', self.__class__.model_name

class Meeting(Quorum):
    model_name = "meeting"

class Votation(Quorum):
    model_name = "votation"



if __name__ == '__main__':
    m = Meeting()
    v = Votation()