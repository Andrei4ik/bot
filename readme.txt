covid19 = COVID19Py.COVID19()
vk_session = vk_api.VkApi(token = TOKEN)
sessionApi= vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def sender(id,text):
    vk_session.method('messages.send',{'user_id': id, 'message' : text, 'random_id' : 0})

latest = covid19.getLatest()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:

            msg = event.text.lower()
            id = event.user_id

            if msg == 'мир':
                sender(id, latest)