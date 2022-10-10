import random

import config


class flagQuizes:

    def __init__(self):
        self.__rightAnswer = -1
        self.__allFlags = config.flags
        self.__randomArray = []
        self.__howMuchWasUsed = 0

    def flagToName(self):
        self.__randomArray = self.__shuffle(self.__allFlags)

    def returnRndArray(self):
        return self.__randomArray

    def returnRightAnswer(self):
        return self.__rightAnswer

    def __shuffle(self, array):
        self.__rightAnswer = random.randint(0, len(array))
        rndArray = [self.__rightAnswer, random.randint(0, len(array) - 1),
                    random.randint(0, len(array) - 1),
                    random.randint(0, len(array) - 1)]
        random.shuffle(rndArray)
        self.__howMuchWasUsed += 1
        return rndArray
