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
            if self.__part_of_strat(character):
                buys.append(list_of_characters.index(character))
        return buys

    def __part_of_strat(self, character):
        switch = {
            NEW: shopInfo.Character.is_warrior(character),
            WARRIORS: shopInfo.Character.is_warrior(character)
        }
        return switch.get(self.__current_strategy)
