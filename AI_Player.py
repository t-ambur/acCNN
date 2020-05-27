import controls
import shopInfo


class Player:
    def __init__(self, ahk, rnd=1):
        self.controller = controls.Control(ahk)
        self.gold = 1
        self.round = rnd
        self.exp = (rnd-1)
        self.level = 1
        self.check_levelup()
        self.bag_items = 0
        self.deployed_chars = 0
        self.chars_on_bench = 0
        self.bench_full = False
        self.board_list = []
        self.bench_list = []
        self.store = Store()
        self.init_lists()

    def init_lists(self):
        for i in range(8):
            self.bench_list.append(None)

    def add_to_bench(self, character, pos):
        if self.chars_on_bench < 8:
            self.bench_list[pos] = character
            self.chars_on_bench += 1
            return True
        return False

    def find_empty_bench_slot(self):
        for slot in self.bench_list:
            if slot is None:
                return self.bench_list.index(slot)
        return -1

    def remove_from_bench(self, pos):
        if self.bench_list[pos] is not None:
            self.bench_list[pos] = None
            self.chars_on_bench -= 1
            return True
        return False

    def add_to_board(self, character):
        if self.deployed_chars < self.level:
            self.board_list.append(character)
            self.deployed_chars += 1
            return True
        return False

    def next_round(self):
        self.round += 1
        self.exp += 1
        if self.round == 2:
            self.gold += 2
        elif self.round == 3:
            self.gold += 3
        elif self.round == 4:
            self.gold += 4
        else:
            self.gold += 5
        self.check_levelup()
        self.store.reset_store()

    def deploy(self, pos):
        if 1 <= pos <= 8:
            self.controller.deploy(pos)
            self.remove_from_bench(pos)

    def choose_item(self, num_items, option):
        if num_items == 1:
            self.controller.grab_item(2)
            self.add_items(1)
        elif num_items == 3:
            self.controller.grab_item(option)
            self.add_items(1)

    def get_store(self):
        return self.store

    def get_level(self):
        return self.level

    def get_chance(self):
        chances = []
        if self.level == 1:
            chances = [100, 0, 0, 0, 0]
        elif self.level == 2:
            chances = [70, 30, 0, 0, 0]
        elif self.level == 3:
            chances = [60, 35, 5, 0, 0]
        elif self.level == 4:
            chances = [50, 35, 15, 0, 0]
        elif self.level == 5:
            chances = [40, 35, 23, 2, 0]
        elif self.level == 6:
            chances = [33, 30, 30, 7, 0]
        elif self.level == 7:
            chances = [30, 30, 30, 10, 0]
        elif self.level == 8:
            chances = [24, 30, 30, 15, 1]
        elif self.level == 9:
            chances = [22, 30, 25, 20, 3]
        else:
            chances = [19, 25, 25, 25, 6]
        return chances

    def check_levelup(self):
        x = self.exp
        lvl = self.level
        if x >= 1 and lvl <= 1:
            self.level = 2
        if x >= 2 and lvl <= 2:
            self.level = 3
        if x >= 4 and lvl <= 3:
            self.level = 4
        if x >= 8 and lvl <= 4:
            self.level = 5
        if x >= 16 and lvl <= 5:
            self.level = 6
        if x >= 32 and lvl <= 6:
            self.level = 7
        if x >= 54 and lvl <= 7:
            self.level = 8
        if x >= 86 and lvl <= 8:
            self.level = 9
        if x >= 126 and lvl <= 9:
            self.level = 10

    def add_gold(self, amount):
        self.gold += amount

    def spend_gold(self, amount):
        if amount <= self.gold:
            self.gold -= amount
            return True
        return False

    def get_gold(self):
        return self.gold

    def get_items(self):
        return self.bag_items

    def add_items(self, num):
        self.bag_items += num

    def remove_items(self, num):
        if num <= self.bag_items:
            self.bag_items -= num
        else:
            self.bag_items = 0

    def number_on_bench(self):
        return self.chars_on_bench

    def is_bench_full(self):
        return self.chars_on_bench >= 8

    def can_deploy_character(self):
        return self.deployed_chars < self.level

    def buy_pos(self, pos, cost):
        if 0 <= pos <= 4:
            if cost <= self.gold:
                if not self.is_bench_full():
                    character = self.store.buy_pos(pos)

                    slot_to_place = self.find_empty_bench_slot()
                    if slot_to_place <= -1:
                        return False

                    self.add_to_bench(character, slot_to_place)

                    spent = self.spend_gold(cost)
                    if not spent:
                        return False

                    self.controller.buy(pos)
                    return True
        return False

    def leave_store(self):
        self.controller.toggle_store()


class Store:
    def __init__(self):
        self.positions = [True, True, True, True, True]
        self.characters = []
        self.num_bought = 0

    def load_characters(self, l):
        self.characters.clear()
        for name in l:
            self.characters.append(shopInfo.Character(name))

    def get_characters(self):
        return self.characters

    def reset_store(self):
        for position in self.positions:
            position = True
        self.num_bought = 0

    def buy_pos(self, pos):
        if 0 <= pos <= 4:
            self.positions[pos] = False
            return self.characters[pos]
        return None

    def can_buy_pos(self, pos):
        if 0 <= pos <= 4:
            return self.positions[pos]
        else:
            return False

    def how_many_bought(self):
        return self.num_bought


class State:
    def __init__(self, rnd=1):
        self.start = "shop"
        self.current = self.start
        self.next = "board"
        self.round = rnd

    def get_state(self):
        return self.current

    def next_state(self):
        self.determine_next_state()
        self.current = self.next
        return self.current

    def get_round(self):
        return self.round

    def determine_next_state(self):
        if self.current is "shop":
            self.next = "board"
        elif self.current is "item":
            self.round += 1
            self.next = "shop"
        elif self.current is "board":
            if self.round < 4:
                self.next = "item"
            elif self.round >= 9 and (self.round+1) % 5 == 0:
                self.next = "item"
            else:
                self.round += 1
                self.next = "shop"
