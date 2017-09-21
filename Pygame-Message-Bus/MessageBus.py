class Message:
    def __init__(self, transmitter, receiver, type, data):
        self.transmitter = transmitter  # from
        self.receiver = receiver        # to
        self.type = type                # what
        self.data = data                # how much


class Message_Queue:
    def __init__(self):
        self.messages = []
        self.members = {}

    def create_message(self, transmitter, receiver, type, data=None):
        """ Create a Message and push it to the queue. Use: msg TRANSMITTER RECEIVER TYPE DATA"""
        msg = Message(transmitter, receiver, type, data)
        self.messages.append(msg)

    def dispatch_messages(self):
        entity = None
        for msg in self.messages:
            if msg:
                for e, s in self.members.items():
                    if e == msg.receiver:
                        print("Has a Key Receiver")
                        entity = msg.receiver
                    elif s == msg.receiver:
                        print("Has a Value Receiver")
                        entity = e

                if msg.transmitter in self.members.keys():
                    print("Has a Key Transmitter")
                elif msg.transmitter in self.members.values():
                    print("Has a Value Transmitter")
                else:
                    print("NO TRANSMITTER!!!")
                    self.messages.remove(msg)
                    return None

                if entity is not None:
                    entity.on_message(msg)
                    self.messages.remove(msg)
                else:
                    print("NO RECEIVER!!!")
                    self.messages.remove(msg)

    def add_member(self, entity, string):
        self.members.update({entity:string})
