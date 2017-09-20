class Message:
    def __init__(self, transmitter, receiver, type, data):
        self.transmitter = transmitter  # from
        self.receiver = receiver        # to
        self.type = type        # what
        self.data = data        # how much


class Message_Queue:
    def __init__(self):
        self.messages = []

    def create_message(self, transmitter, receiver, type, data):
        """ Create a Message and push it to the queue. Use: msg ..."""
        # print("Creating Message\n"
        #       "from:" + str(transmitter) +
        #       "\nto:" + str(receiver) +
        #       "\nwhat:" + str(type) +
        #       "\ndata:" + str(data))
        msg = Message(transmitter, receiver, type, data)
        self.messages.append(msg)

    def dispatch_messages(self):
        for msg in self.messages:
            if msg:
                #print("Got a message. Try to find a receiver!")
                entity = msg.receiver
                if entity:
                    #print("Found entity and sending message")
                    entity.on_message(msg)
                    self.messages.remove(msg)
