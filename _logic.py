import vk_api
import requests
import COVID19Py
from vk_api.longpoll import VkLongPoll,VkEventType 
from config import TOKEN
import bs4 as bs4



class vkbot:
    def __init__(self, user_id):
    
        print("Создан объект бота!")
        self.ID = user_id
        self.NAME = self.defnameFromVKid(user_id)
        
        self.COMMANDS = ["ПРИВЕТ", "МИР", "ВРЕМЯ"]

    def defnameFromVKid(self, user_id):
        msg = requests.get("https://vk.com/id"+str(user_id))
        bs = bs4.BeautifulSoup(msg.text, "html.parser")
    
        user_name = self.defclean(bs.findAll("title")[0])
    
        return user_name.split()[0]

    def deftime(self):
        msg = requests.get("https://my-calend.ru/date-and-time-today")
        b = bs4.BeautifulSoup(msg.text, "html.parser")
        return self.defclean(str(b.select(".page")[0].findAll("h2")[1])).split()[1]

    def defCorona(self):
        covid19 = COVID19Py.COVID19()
        location = covid19.getLatest()
        result = f"данные по всему миру\nЗаболевшие: {location['confirmed']}\nумерло :{location['deaths']}"

        return result

    @staticmethod
    def defclean(string_line):
        """
        Очистка строки stringLine от тэгов и их содержимых
        :param string_line: Очищаемая строка
        :return: очищенная строка
        """
        result = ""
        not_skip = True
        for i in list(string_line):
            if not_skip:
                if i == "<":
                    not_skip = False
                else:
                    result += i
            else:
                if i == ">":
                    not_skip = True
    
        return result
    def new_message(self, message):

        # Привет
        if message.upper() == self.COMMANDS[0]:
            return f"Привет, {self.NAME}!"
    
        # мир
        elif message.upper() == self.COMMANDS[1]:
            return self.defCorona()
    
        # Время
        elif message.upper() == self.COMMANDS[2]:
            return self.deftime()
    
        else:
            return "Не понимаю о чем вы..."