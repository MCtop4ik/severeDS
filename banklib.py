import random
import sqlite3
import datetime


class Database:

    def __init__(self):
        self.base = sqlite3.connect('discord.db')
        self.cursor = self.base.cursor()

    def transfer(self, sender: str, recipient: str, amount: int):
        senderamount = self.amount(userid=sender)
        recipeientamount = self.amount(userid=recipient)
        if amount > senderamount[0][0]:
            return

        newsenderamount = senderamount[0][0] - amount
        newrecepientamount = recipeientamount[0][0] + amount
        self.cursor.execute('UPDATE userbalance SET northern == ? WHERE userid == ?', (newsenderamount, sender))
        self.cursor.execute('UPDATE userbalance SET northern == ? WHERE userid == ?', (newrecepientamount, recipient))
        self.base.commit()

        return "Success"

    def amount(self, userid: str):
        amount = self.cursor.execute("SELECT northern FROM userbalance WHERE userid == ?", (userid, )).fetchall()
        return amount[0][0]

    def register(self, userid: str):
        defaultmoneyamount = 0
        cvv = userid[3] + userid[4] + userid[5]
        secretCVV = 190
        self.cursor.execute("INSERT INTO userbalance(userid, northern, cvv, date, daily) VALUES (?, ?, ?, ?, ?)",
                            (str(userid),
                             defaultmoneyamount, int(cvv) ^ secretCVV,
                             datetime.datetime.today().strftime('%Y-%m-%d'), True))
        self.base.commit()

    def daily(self, userid: str):
        print('here')
        daily = self.cursor.execute("SELECT daily FROM userbalance WHERE userid == ?", (userid, )).fetchall()
        print(daily[0][0])
        if daily[0][0]:
            print('here')
            randomnum = random.randint(10, 50)
            recipeientamount = self.amount(userid=userid)
            newrecepientamount = recipeientamount[0][0] + randomnum
            self.cursor.execute('UPDATE userbalance SET northern == ? WHERE userid == ?',
                                (newrecepientamount, userid, ))
            self.base.commit()
            print('there')
            self.cursor.execute('UPDATE userbalance SET daily == ? WHERE userid == ?',
                                (False, userid, ))
            print('now')
            self.base.commit()


class Account(Database):

    def returnAmount(self, userid: str):
        return self.amount(userid=userid)

    def dailyCommand(self, userid: str):
        print('234323')
        self.daily(userid=userid)
        return "Worked"


class Currency:
    pass
