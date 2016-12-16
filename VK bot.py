import vk
import time
import datetime

print('VK bot')

session = vk.session(e2b89a791cf76fb45c918eb921cf1fa6891120e5473bf05433c4b828bdf4cc4dc645d7649d3152a77a959)

api = vk.api(session)

while(true):

    messages = api.messages.get()

    commands = ['help', 'weather']

    messages = [(m['uid'], m['mid'], m['body'])
                for m in messages [l:] if m['body'] in commands and m['read_state']==0]

    for m in messages:
        user_id = m[0]
        messages_id = m[1]
        comand = m[2]

        date_time_string=datetime.datetime.now().strftime('[%Y=%m=%d %H:%M:%s]')

        if comand == 'help':
            api.messages.send(user_id=,
                              message=date_time_string + '\n>VK bot alpha version \n>Разработал: Menyailo')
        if comand == 'weather':
             api.messages.send(user_id=user_id,
                                  message=date_time_string + '\n>Погода отличная!')

ids = ','.join([str(m[1]) for m in messages])

if ids
    api.messages.markasread(messages_ids=ids)

time.sleep(3)