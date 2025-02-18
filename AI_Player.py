import controls
import shopInfo
import predict
import constants as c
import strategy

# TODO
# Also, code to deploy is not working


class Player:
    def __init__(self, ahk, c_model):
        self.controller = controls.Control(ahk)
        self.gold = 1
        self.round = 1
        self.char_model = c_model
        self.exp = 0
        self.level = 1
        self.check_levelup()
        self.bag_items = 0
        self.deployed_chars = 0
        self.chars_on_bench = 0
        self.bench_full = False
        self.board_list = []
        self.bench_list = []
        self.store = Store(c_model)
        self.init_lists()
        self.strategy = strategy.Strategy()
        self.strategy.set_strategy(strategy.WARRIORS)

    def init_lists(self):
        for i in range(8):
            self.bench_list.append(None)

    def add_to_bench(self, character, pos):
        if self.chars_on_bench < 8:
            if self.two_on_bench(character):
                self.chars_on_bench -= 1
                self.handle_star_up_bench_2(character)
                return True
            elif self.two_on_board(character):
                return True
            elif self.one_bench_one_board(character):
                self.chars_on_bench -= 1
                self.handle_star_up_bench_1(character)
                return True
            self.bench_list[pos] = character
            self.chars_on_bench += 1
            return True
        elif self.two_on_bench(character):
            self.chars_on_bench -= 1
            self.handle_star_up_bench_2(character)
        elif self.one_bench_one_board(character):
            self.chars_on_bench -= 1
            self.handle_star_up_bench_1(character)
            return True
        return False

    def two_on_bench(self, character):
        found_once = False
        for char in self.bench_list:
            if char is None:
                continue
            if char.get_name() == character.get_name() and char.get_stars() == character.get_stars():
                if not found_once:
                    found_once = True
                else:
                    return True
        return False

    def two_on_board(self, character):
        found_once = False
        for char in self.board_list:
            if char is None:
                continue
            if char.get_name() == character.get_name() and char.get_stars() == character.get_stars():
                if not found_once:
                    found_once = True
                else:
                    return True
        return False

    def two_stars(self, character):
        if self.two_on_bench(character):
            return True
        # check for one on bench and one on board
        if self.one_bench_one_board(character):
            return True
        # check for two on board
        if self.two_on_board(character):
            return True
        return False

    def one_bench_one_board(self, character):
        if character is None:
            return False
        for char in self.board_list:
            if char is None:
                continue
            if char.get_name() == character.get_name() and char.get_stars() == character.get_stars():
                for ben_char in self.bench_list:
                    if ben_char is None:
                        continue
                    if ben_char.get_name() == character.get_name() and ben_char.get_stars() == character.get_stars():
                        return True
        return False

    def handle_star_up_bench_1(self, character):
        if character is None:
            return False
        for char in self.bench_list:
            if char is None:
                continue
            if char.get_name() == character.get_name() and char.get_stars() == character.get_stars():
                i = self.bench_list.index(char)
                self.bench_list[i] = None

    def handle_star_up_bench_2(self, character):
        found_once = False
        if character is None:
            return False
        for char in self.bench_list:
            if char is None:
                continue
            if char.get_name() == character.get_name() and char.get_stars() == character.get_stars():
                if not found_once:
                    found_once = True
                else:
                    i = self.bench_list.index(char)
                    self.bench_list[i] = None

    def find_empty_bench_slot(self):
        for slot in self.bench_list:
            if slot is None:
                return self.bench_list.index(slot)
        return -1

    def find_char_on_bench(self):
        best = None
        worst = None
        stars = 1
        for slot in self.bench_list:
            if slot is not None:
                for piece in self.board_list:
                    if piece is None:
                        continue
                    if piece.get_name() == slot.get_name():
                        worst = self.bench_list.index(slot)
                    else:
                        if best is None:
                            best = self.bench_list.index(slot)
                            stars = slot.get_stars()
                        else:
                            if slot.get_stars() > stars:
                                best = self.bench_list.index(slot)
                                stars = slot.get_stars()
        if best is None:
            return worst
        return best

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
            return True
        elif pos == -1:
            p = self.find_char_on_bench()
            if p is None:
                return False
            if self.deployed_chars < self.get_level():
                self.controller.deploy(p)
                self.remove_from_bench(p)
                return True
        return False

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

    def start_game(self):
        self.controller.start()

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
                character = self.store.buy_pos(pos)
                if not self.is_bench_full() or self.two_stars(character):
                    slot_to_place = self.find_empty_bench_slot()
                    if slot_to_place <= -1:
                        print("couldn't find slot", flush=True)
                        return False

                    spent = self.spend_gold(cost)
                    if not spent:
                        print("couldnt spend", flush=True)
                        return False

                    self.add_to_bench(character, slot_to_place)
                    self.controller.buy(pos)
                    return True
        print("POS OR GOLD OR BENCHFULL", flush=True)
        return False

    def buy_if_needed(self):
        positions_to_buy = []
        positions_to_buy = self.strategy.determine_buys(self.store.characters)
        if len(positions_to_buy) <= 0:
            if self.deployed_chars < self.level:
                print("Plan B. buying first: No available pieces for strat", flush=True)
                positions_to_buy.append(0)
            else:
                return False
        for pos in positions_to_buy:
            ok = self.buy_pos(pos, self.store.get_cost_of_pos(pos))
            if not ok:
                print("COULD NOT BUY POS:", str(pos), flush=True)
        return True

    def leave_store(self):
        self.controller.toggle_store()


class Store:
    def __init__(self, model):
        self.positions = [True, True, True, True, True]
        self.characters = []
        self.num_bought = 0
        self.model_char = model
        self.report_string = ""

    def load_characters(self, l):
        self.characters.clear()
        for name in l:
            char = shopInfo.Character(name)
            print(int(char.get_class_name()))
            self.characters.append(char)

    def get_characters(self):
        return self.characters

    def get_cost_of_pos(self, pos):
        return self.characters[pos].get_cost()

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

    def read_in_shop(self):
        pos1_i = predict.predict(r'store\pos1.png', self.model_char, "character")
        pos2_i = predict.predict(r'store\pos2.png', self.model_char, "character")
        pos3_i = predict.predict(r'store\pos3.png', self.model_char, "character")
        pos4_i = predict.predict(r'store\pos4.png', self.model_char, "character")
        pos5_i = predict.predict(r'store\pos5.png', self.model_char, "character")
        pos1 = c.CHAR_CATEGORIES[pos1_i]
        pos2 = c.CHAR_CATEGORIES[pos2_i]
        pos3 = c.CHAR_CATEGORIES[pos3_i]
        pos4 = c.CHAR_CATEGORIES[pos4_i]
        pos5 = c.CHAR_CATEGORIES[pos5_i]
        self.report_string = ">>> 1=" + pos1 + " 2=" + pos2 + "\n>>>3=" + pos3 + " 4=" + pos4 + "\n>>>5=" + pos5
        print(self.report_string, flush=True)
        self.load_characters([pos1, pos2, pos3, pos4, pos5])

    def get_report(self):
        return self.report_string


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
