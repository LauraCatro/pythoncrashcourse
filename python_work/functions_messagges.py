def send_messages(short_messages, sent_messages):
    while short_messages:
        messages = short_messages.pop()
        sent_messages.append(messages)


def show_messages(sent_messages):
    for message in sent_messages:
        print(f"{message}")


short_messages = ['Happy', 'Birthday', 'Carlitos']
sent_messages = []


send_messages(short_messages[:], sent_messages)
show_messages(short_messages)
show_messages(sent_messages)


# print(short_messages)
# print(sent_messages)
