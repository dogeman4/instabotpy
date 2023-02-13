import time
import random
import requests

def follow_accounts():
    # Your Instagram account credentials
    username = 'mj_pics420'
    password = 'Griffin4'

    # Login to Instagram
    session = requests.Session()
    login_data = {
        'username': username,
        'password': password
    }
    response = session.post('https://www.instagram.com/accounts/login/ajax/', data=login_data, headers={'Referer': 'https://www.instagram.com/'})
    if response.status_code != 200:
        print('Login failed')
        return

    # The hashtags to search for
    hashtags = ['#hashtag1', '#hashtag2', '#hashtag3', '#hashtag4', '#hashtag5']

    # Follow 50 accounts every 24 hours
    while True:
        for hashtag in hashtags:
            # Get the list of accounts using the hashtag
            response = session.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
            if response.status_code != 200:
                print(f'Failed to get the list of accounts using hashtag {hashtag}')
                continue
            account_ids = []
            for line in response.text.split('\n'):
                if '<a href="/accounts/activity/' in line:
                    account_id = line.split('/')[4].split('"')[0]
                    account_ids.append(account_id)
            for account_id in account_ids[:50]:
                # Follow the account
                response = session.post(f'https://www.instagram.com/web/friendships/{account_id}/follow/')
                if response.status_code != 200:
                    print(f'Failed to follow account {account_id}')
                    continue
                # Send the message
                response = session.post('https://www.instagram.com/direct_v2/web/threads/broadcast/create_message/', json={'recipient_ids': [account_id], 'text': 'follow for follow'})
                if response.status_code != 200:
                    print(f'Failed to send message to account {account_id}')
                    continue
        # Wait 24 hours

        # Unfollow the accounts
        for account_id in account_ids[:50]:
            # Wait 36 hours
            time.sleep(36 * 3600)
            # Unfollow the account
            response = session.post(f'https://www.instagram.com/web/friendships/{account_id}/unfollow/')
            if response.status_code != 200:
                print(f'Failed to unfollow account {account_id}')
                continue
while 2 == 2:
    follow_accounts()
