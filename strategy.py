import shopInfo

NEW = 0
WARRIORS = 1


class Strategy:
    def __init__(self):
        self.__current_strategy = NEW

    def get_current_strategy_number(self):
        return self.__current_strategy

    def determine_buys(self, list_of_characters):
        buys = []
        for character in list_of_characters:
            # print(character.get_name())
            if self.__part_of_strat(character):
                buys.append(list_of_characters.index(character))
        return buys

    def set_strategy(self, st):
        self.__current_strategy = st

    def __part_of_strat(self, character):
        s = self.__current_strategy
        if s == NEW:
            return shopInfo.Character.is_warrior(character),
        elif s == WARRIORS:
            return shopInfo.Character.is_warrior(character)
        else:
            print("ELSE IN STRAT", flush=True)
            return False
