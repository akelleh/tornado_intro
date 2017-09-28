import nsq


def message_handler(message):
    if message['type'] == 'customer_signup':
        customer_id = message['customer_id']
        loyalty_message = start_loyalty_account(customer_id):
        pub(loyalty_message)
    return True

if __name__ == "__main__":
    reader = nsq.Reader('customer_events',
                        'music_co_events',
                        message_handler=message_handler)
    nsq.run()
