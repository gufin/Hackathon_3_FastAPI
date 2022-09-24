from pydantic import BaseModel


class cash_desk(BaseModel):
    name: str
    available_service: list
    queue: list
    closed: bool

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
