import nsq

def message_handler(message):
    if message['type'] == 'customer_signup':
        email_address = message['email_address']
        email_message = send_email(email_address):
        pub(email_message)
    return True

if __name__ == "__main__":
    reader = nsq.Reader('customer_events',
                        'music_co_events',
                        message_handler=message_handler)
    nsq.run()
