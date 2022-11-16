# :suspect: Third hackathon Yandex workshops. Problem-solving on FastAPI. (3 difficulty level)
## TASK B: Tickets in "Somebank" :money_with_wings:There are several cash desks. They may provide several types of services. The client can order a ticket at the cash desk for one kind of service. The type of service is fixed in the voucher number. It would help if you wrote an API that:

- shows information about cash registers
- shows information about services
- issues a ticket in line at the cashier
- shows queues
- "Service rendered." Those. Removes a client from the queue (in the correct order) and returns information about the next client.
- shows which customer is currently being serviced at the checkout
Difficulty levels for this task

### Level 1:
Initially, we rigidly set in the code the number of cash desks, types of services, and which cash desks can provide which services. For example, there are two cash desks in our branch. Through both, you can deposit/withdraw money; one deals with mortgages and the other deals with the issuance of cards.

### Level 2:
Add the method "Cashier closed" with the queue distribution for the remaining ones.

### Level 3:
Make methods for creating new cash registers and new services.

## :shipit: In the plans
- Make it possible to work with the database
- Make the code look good
- Write a tests :grinning:
