from pydantic import BaseModel


class cash_desk(BaseModel):
    name: str
    available_service: list
    queue: list
    closed: bool = False

    # насколько я поняла, номера талончиков могут повторяться
    # а в жизни не так, может ведь возникнуть путаница. 
    # поэтому для каждой услуги можно завести отдельный счетчик.
    # для тестого проекта можно этот счетчик не обнулять, но написать в комментарии или  ToDO 
    # что можно сделать функцию "завершить рабочий день" когда мы обнуляем очереди и счетчики
    def add_ticket(self):
        if len(self.queue) == 0:
            self.queue.append((self.name, 1))
        else:
            self.queue.append((self.name, self.queue[-1][1]+1))

    def service_done(self):
        self.queue.pop(0)


class ticket_resive(BaseModel):
    service: str


class service_call(BaseModel):
    name: str
