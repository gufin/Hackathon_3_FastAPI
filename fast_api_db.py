from models import cash_desk

services = ['mortgage', 'cash', 'credit']
service1, service2, service3 = services[0], services[1], services[2]
cash_desk1 = cash_desk(name='A',
                       available_service=[service1, service2],
                       queue=[('A', 1),('A', 2),('A', 3)],
                       closed=False)
cash_desk2 = cash_desk(name='B',
                       available_service=[service2],
                       queue=[('B', 1),('B', 2),('B', 3),('B', 4),('B', 5)],
                       closed=False)
cash_desk3 = cash_desk(name='C',
                       available_service=[service3],
                       queue=[],
                       closed=False)
cash_desks = [cash_desk1, cash_desk2, cash_desk3]
database = {
            'servises': services,
            'cash_desks': cash_desks,
}