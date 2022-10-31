import sqlite3


class DatabaseParsing:

    def __init__(self):
        self.base = sqlite3.connect('discord.db')
        self.cur = self.base.cursor()


