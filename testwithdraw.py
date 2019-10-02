from python22.withdraw import withdraw, data
from python22.myexceptions import InvalidAccountError, InsuffientAmtError

import logging
logging.basicConfig(level=logging.ERROR, filename="app.log")


def main ():
    logging.info(" main program start")

    while True:
        try :
            print("###########################")
            print("####### WITHDRAW ##########")
            print("###########################")

            accno = input("Account Number#")
            amount = int ( input ("Amount"))
            withdraw(accno, amount)

            print ("Transaction is succesful")
            print (" Current balance of {} is {}".format("accno", data[accno] ))

        except InvalidAccountError as e:
            logging.error(e)
            print ("Account number is incorrect")

        except InsuffientAmtError as e:
            logging.error(e)
            print ("Account has no suffient fund!!!")

        except Exception as e:
            logging.critical(e)
            print ()

        logging.info(" main program end")


main()