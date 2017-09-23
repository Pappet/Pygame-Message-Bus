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
                        entity = msg.receiver
                    elif s == msg.receiver:
                        entity = e

                if msg.transmitter  not in self.members.keys() and msg.transmitter not in self.members.values():
                    self.send_msg_to_console(msg, "No TRANSMITTER")
                    self.messages.remove(msg)
                    return None

                if entity is not None:
                    entity.on_message(msg)
                    self.send_msg_to_console(msg)
                    self.messages.remove(msg)
                else:
                    self.send_msg_to_console(msg, "No RECEIVER")
                    self.messages.remove(msg)

    def add_member(self, entity, string):
        self.members.update({entity:string})

    def send_msg_to_console(self ,msg, string = None):
            if msg.transmitter is not "Console" and msg.receiver is not "Console":
                # print("its an output msg")
                if "Console" in self.members.values():
                    # print("print msg to Console")
                    if string is not None:
                        string = "ERROR: " + string
                        self.create_message("Console", "Console", "error", string)
                    else:
                        self.create_message("Console", "Console", "output", msg)

