from python22.myexceptions import InvalidAccountError, InsuffientAmtError

import logging
logging.basicConfig(level=logging.DEBUG, filename="app.log")

data = {"1111": 10000, "2222": 20000}

def withdraw (accno, amt ):

    logging.info("Called withdraw function")

    logging.debug("accno is" + str ( accno))
    logging.debug("amt is " + str (amt))

    if (accno not in data) :
        raise InvalidAccountError()

    if (data[accno] < amt):
        raise InsuffientAmtError()

    data [accno] = data[accno]- amt
    logging.debug("transaction is successful")