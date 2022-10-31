import random
import sqlite3
import datetime


class Database:

    def __init__(self):
        self.base = sqlite3.connect('discord.db')
        self.cursor = self.base.cursor()

    def transfer(self, sender: str, recipient: str, amount: int):
        senderamount = int(self.amount(userid=sender))
        recipeientamount = int(self.amount(userid=recipient))
        if amount > senderamount:
            return "Unsuccessful"

        newsenderamount = senderamount - amount
        newrecepientamount = recipeientamount + amount
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
        daily = self.cursor.execute("SELECT daily FROM userbalance WHERE userid == ?", (userid, )).fetchall()
        if daily[0][0] == "True":
            randomnum = random.randint(10, 50)
            recipeientamount = int(self.amount(userid=str(userid)))
            newrecepientamount = recipeientamount + randomnum
            self.cursor.execute('UPDATE userbalance SET northern == ? WHERE userid == ?',
                                (int(newrecepientamount), str(userid), ))
            self.base.commit()
            self.cursor.execute('UPDATE userbalance SET daily == ? WHERE userid == ?',
                                ('False', userid, ))
            self.base.commit()
            return f"Вам было начислено {randomnum}Sev. Возвращайся за следующей наградой позже"
        return f"Вам уже было начислена ежедневная награда сегодня"


class Account(Database):

    def returnAmount(self, userid: str):
        return self.amount(userid=userid)

    def dailyCommand(self, userid: str):
        return self.daily(userid=userid)


class Currency:
    pass
