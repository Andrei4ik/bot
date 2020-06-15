import vk_api
from vk_api.longpoll import VkLongPoll,VkEventType 
from config import TOKEN
from _logic import vkbot

vk_session = vk_api.VkApi(token = TOKEN)
sessionApi= vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def printMsg(id,out):
    vk_session.method('messages.send',{'user_id': id, 'message' : out, 'random_id' : 0})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            
            bot = vkbot(event.user_id)
            printMsg(event.user_id, bot.new_message(event.text))
