from fastapi import Depends, FastAPI, HTTPException

from models import service_call, ticket_resive, cash_desk

app = FastAPI()


def get_database():
    from fast_api_db import database
    return database


@app.get("/")
async def root():
    return {"message": "Яндекс практикум. Хакатон #3"}


@app.get("/servises/")
async def servises(database=Depends(get_database)):
    return database['servises']


@app.get("/cash_desks/")
async def cash_desks(database=Depends(get_database)):
    return [{'name': cash_desk.name,
             'available_service': cash_desk.available_service,
             'closed': cash_desk.closed}
            for cash_desk in database['cash_desks']]


@app.get("/show_queue/")
async def get_articles(database=Depends(get_database)):
    return [(cash_desk.name, *cash_desk.queue)
            for cash_desk in database['cash_desks']]


@app.post("/resive_ticket/")
async def create_ticket(ticket: ticket_resive,
                        database=Depends(get_database)):
    if ticket.service in database['servises']:
        unbusiest_deck = None
        for pos, cash_desk in enumerate(database['cash_desks']):
            if (not cash_desk.closed
                    and ticket.service in cash_desk.available_service):
                if unbusiest_deck is None:
                    unbusiest_deck = pos
                elif (len(cash_desk.queue)
                      < len(database['cash_desks'][unbusiest_deck].queue)):
                    unbusiest_deck = pos
        if unbusiest_deck is not None:
            deck = database['cash_desks'][unbusiest_deck]
            deck.add_ticket()
            return deck.queue[-1][0] + str(deck.queue[-1][1])
        raise HTTPException(status_code=403,
                            detail="no cash desks supporting this service")
    raise HTTPException(status_code=403,
                        detail="service not supported")


@app.post("/service_done/")
async def serv_done(service_call: service_call,
                    database=Depends(get_database)):
    cash_desk_found = False
    for cash_desk in database['cash_desks']:
        if cash_desk.name == service_call.name:
            cash_desk.service_done()
            cash_desk_found = True
            next_client = None
            if len(cash_desk.queue) > 0:
                next_client = cash_desk.queue[0][0] + str(cash_desk.queue[0][1])
            return {"message": f'Next client {next_client}'}
    if not cash_desk_found:
        raise HTTPException(status_code=403,
                            detail="cash desk not found")


@app.get("/show_current_client/{cash_desk_name}")
async def show_current_client(cash_desk_name, database=Depends(get_database)):
    cash_desk_found = False
    for cash_desk in database['cash_desks']:
        if cash_desk.name == cash_desk_name:
            current_client = None
            if len(cash_desk.queue) > 0:
                next_client = cash_desk.queue[0][0] + str(cash_desk.queue[0][1])
            return {"message": f'Current client {next_client}'}
    if not cash_desk_found:
        raise HTTPException(status_code=403,
                            detail="cash desk not found")


@app.post("/close_cash_desk/")
async def close_cash_desk(service_call: service_call,
                          database=Depends(get_database)):
    cash_desk_found = False
    for cash_desk in database['cash_desks']:
        if cash_desk.name == service_call.name:
            cash_desk_found = True
            current_queue = cash_desk.queue
            for client in current_queue:
                min_queue = None
                for pos, cash_desk_for_add in enumerate(database['cash_desks']):
                    if (cash_desk_for_add.name
                            != service_call.name):
                        if min_queue is None:
                            min_queue = pos
                        elif len(cash_desk_for_add.queue) < len(
                                database['cash_desks'][min_queue].queue):
                            min_queue = pos
                if min_queue is not None:
                    database['cash_desks'][min_queue].queue.append(client)
            cash_desk.queue = []
            cash_desk.closed = True
            return {"message": f'Cash desk {cash_desk.name} closed'}

    if not cash_desk_found:
        raise HTTPException(status_code=403,
                            detail="Cash desk not found")


@app.post("/cash_desk_add/")
async def cash_desk_add(cash_desk: cash_desk,
                          database=Depends(get_database)):
    database['cash_desks'].append(cash_desk)
    return cash_desk

@app.post("/service_add/")
async def service_add(service_call: service_call,
                          database=Depends(get_database)):
    database['servises'].append(service_call.name)
    return cash_desk