class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []  
        self.messages = []      

    def call(self, other_phone):
        record = f"{self.phone_number} called {other_phone.phone_number}"
        print(record)
        self.call_history.append(record)

    def show_call_history(self):
        print(f"Call history for {self.phone_number}:")
        for record in self.call_history:
            print(record)

    def send_message(self, other_phone, content):
        message = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }
        self.messages.append(message)       # Save in sender's messages
        other_phone.messages.append(message)  # Save in recipient's messages
        print(f"Message sent from {self.phone_number} to {other_phone.phone_number}: {content}")

    def show_outgoing_messages(self):
        print(f"Outgoing messages from {self.phone_number}:")
        for msg in self.messages:
            if msg["from"] == self.phone_number:
                print(f"To {msg['to']}: {msg['content']}")

    def show_incoming_messages(self):
        print(f"Incoming messages for {self.phone_number}:")
        for msg in self.messages:
            if msg["to"] == self.phone_number:
                print(f"From {msg['from']}: {msg['content']}")

    def show_messages_from(self, other_phone):
        print(f"Messages from {other_phone.phone_number} to {self.phone_number}:")
        for msg in self.messages:
            if msg["from"] == other_phone.phone_number and msg["to"] == self.phone_number:
                print(msg['content'])



phone1 = Phone("123-456")
phone2 = Phone("987-654")

phone1.call(phone2)
phone2.call(phone1)

phone1.show_call_history()
phone2.show_call_history()

phone1.send_message(phone2, "Hello! How are you?")
phone2.send_message(phone1, "I am fine, thanks!")

phone1.show_outgoing_messages()
phone1.show_incoming_messages()
phone1.show_messages_from(phone2)
