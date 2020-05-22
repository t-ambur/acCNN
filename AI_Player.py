import controls


class Player:
    def __init__(self, ahk):
        self.controller = controls.Control(ahk)
        self.gold = 5
        self.round = 1
        self.exp = 0
        self.level = 1
        self.bag_items = 0
        self.deployed_chars = 0
        self.chars_on_bench = 0
        self.bench_full = False
        self.store = Store()

    def next_round(self):
        self.round += 1
        self.exp += 1
        self.gold += 5
        self.check_levelup()
        self.store.reset_store()

    def deploy(self, pos):
        if 1 <= pos <= 8:
            self.controller.deploy(pos)
            self.deploy_character()
            self.remove_from_bench(1)

    def choose_item(self, num_items):
        if num_items == 1:
            self.controller.grab_item(2)
        elif num_items == 3:
            self.controller.grab_item(1)

    def get_store(self):
        return self.store

    def get_level(self):
        return self.level

    def check_levelup(self):
        x = self.exp
        lvl = self.level
        if x >= 1 and lvl <= 1:
            self.level = 2
        elif x >= 2 and lvl <= 2:
            self.level = 3
        elif x >= 4 and lvl <= 3:
            self.level = 4
        elif x >= 8 and lvl <= 4:
            self.level = 5
        elif x >= 16 and lvl <= 5:
            self.level = 6
        elif x >= 32 and lvl <= 6:
            self.level = 7
        elif x >= 54 and lvl <= 7:
            self.level = 8
        elif x >= 86 and lvl <= 8:
            self.level = 9
        elif x >= 126 and lvl <= 9:
            self.level = 10

    def add_gold(self, amount):
        self.gold += amount

    def spend_gold(self, amount):
        if amount <= self.gold:
            self.gold -= amount
        else:
            self.gold = 0

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

    def add_to_bench(self):
        if self.chars_on_bench < 8:
            self.chars_on_bench += 1

    def remove_from_bench(self, num):
        if num <= self.chars_on_bench:
            self.chars_on_bench -= num
        else:
            self.chars_on_bench = 0

    def number_on_bench(self):
        return self.chars_on_bench

    def is_bench_full(self):
        return self.chars_on_bench >= 8

    def deploy_character(self):
        if self.deployed_chars < self.level:
            self.deployed_chars += 1

    def can_deploy_character(self):
        return self.deployed_chars < self.level

    def buy_pos(self, pos, cost):
        if 0 <= pos <= 4:
            if cost <= self.gold:
                if not self.is_bench_full():
                    self.store.buy_pos(pos)
                    self.add_to_bench()
                    self.spend_gold(cost)
                    return True
        return False


class Store:
    def __init__(self):
        self.positions = [True, True, True, True, True]
        self.num_bought = 0

    def reset_store(self):
        for position in self.positions:
            position = True
        self.num_bought = 0

    def buy_pos(self, pos):
        if 0 <= pos <= 4:
            self.positions[pos] = False

    def can_buy_pos(self, pos):
        if 0 <= pos <= 4:
            return self.positions[pos]
        else:
            return False

    def how_many_bought(self):
        return self.num_bought


class State:
    def __init__(self):
        self.start = "shop"
        self.current = self.start
        self.next = "board"
        self.round = 1

    def get_state(self):
        return self.current

    def next_state(self):
        self.current = self.next
        self.determine_next_state()
        return self.current

    def determine_next_state(self):
        if self.current is "shop":
            self.next = "board"
        elif self.current is "item":
            self.round += 1
            self.next = "shop"
        elif self.current is "board":
            if self.round < 4:
                self.next = "item"
            elif self.round >= 10 and self.round % 5 == 0:
                self.next = "item"
            else:
                self.round += 1
                self.next = "shop"
