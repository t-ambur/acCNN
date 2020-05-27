import constants as c

# rarities
UNDEF_RARITY = 0
COMMON = 1
UNCOMMON = 2
RARE = 3
EPIC = 4
LEGENDARY = 5

# races, 15
UNDEF_RACE = 0
CAVE_CLAN = 1
BEAST = 2
GLACIER = 3
EGERSIS = UNDEAD = 4
DRAGON = 5
GOBLIN = 6
FEATHERED = 7
KIRA = 8
DIVINITY = 9
MARINE = 10
HUMAN = 11
DEMON = 12
SPIRIT = 13
DWARF = 14
INSECTOID = 15

# classes 12
UNDEF_CLASS = 0
WARRIOR = 1
DRUID = 2
KNIGHT = 3
SHAMAN = 4
HUNTER = 5
MAGE = 6
ASSASSIN = 7
MECH = 8
WITCHER = 9
WARLOCK = 10
PRIEST = 11
WIZARD = 12
EGG = 13


# 64 characters/folders SEE c.CHAR_CATEGORIES
class Character:
    def __init__(self, name):
        self.__name = name
        self.__cost = 0
        self.__cl = None
        self.__race1 = None
        self.__race2 = None
        self.__rarity = UNDEF_RARITY
        self.__init_values()
        self.__stars = 1

    def star_up(self):
        self.__stars += 1

    def get_stars(self):
        return self.__stars

    def get_name(self):
        return self.__name

    def get_cost(self):
        return self.__cost

    def get_class_name(self):
        return self.__cl

    def get_races(self):
        return self.__race1, self.__race2

    def get_rarity(self):
        return self.__rarity

    def __init_values(self):
        switch = {
            c.CHAR_CATEGORIES[0]: self.__abyssal_guard(),
            c.CHAR_CATEGORIES[1]: self.__abyssal_crawler(),
            c.CHAR_CATEGORIES[2]: self.__argali_knight(),
            c.CHAR_CATEGORIES[3]: self.__berserker(),
            c.CHAR_CATEGORIES[4]: self.__dark_spirit(),
            c.CHAR_CATEGORIES[5]: self.__defector(),
            c.CHAR_CATEGORIES[6]: self.__desperate_doctor(),
            c.CHAR_CATEGORIES[7]: self.__devastator(),
            c.CHAR_CATEGORIES[8]: self.__doom_arbitor(),
            c.CHAR_CATEGORIES[9]: self.__dragon_knight(),
            c.CHAR_CATEGORIES[10]: self.__dwarf_sniper(),
            c.CHAR_CATEGORIES[11]: self.__e_ranger(),
            c.CHAR_CATEGORIES[12]: self.__egg(),
            c.CHAR_CATEGORIES[13]: self.__elder(),
            c.CHAR_CATEGORIES[14]: self.__empty(),
            c.CHAR_CATEGORIES[15]: self.__evil_knight(),
            c.CHAR_CATEGORIES[16]: self.__fallen_witcher(),
            c.CHAR_CATEGORIES[17]: self.__flame_wizard(),
            c.CHAR_CATEGORIES[18]: self.__fortune_teller(),
            c.CHAR_CATEGORIES[19]: self.__frost_knight(),
            c.CHAR_CATEGORIES[20]: self.__frostblaze_dragon(),
            c.CHAR_CATEGORIES[21]: self.__god_of_thunder(),
            c.CHAR_CATEGORIES[22]: self.__god_of_war(),
            c.CHAR_CATEGORIES[23]: self.__goddess_of_light(),
            c.CHAR_CATEGORIES[24]: self.__grimtouch(),
            c.CHAR_CATEGORIES[25]: self.__heaven_bomber(),
            c.CHAR_CATEGORIES[26]: self.__helicopter(),
            c.CHAR_CATEGORIES[27]: self.__hell_knight(),
            c.CHAR_CATEGORIES[28]: self.__herald(),
            c.CHAR_CATEGORIES[29]: self.__lightblade_knight(),
            c.CHAR_CATEGORIES[30]: self.__lord_of_sand(),
            c.CHAR_CATEGORIES[31]: self.__ogre_mage(),
            c.CHAR_CATEGORIES[32]: self.__pirate(),
            c.CHAR_CATEGORIES[33]: self.__razorclaw(),
            c.CHAR_CATEGORIES[34]: self.__reaper(),
            c.CHAR_CATEGORIES[35]: self.__redaxe(),
            c.CHAR_CATEGORIES[36]: self.__ripper(),
            c.CHAR_CATEGORIES[37]: self.__rogue_guard(),
            c.CHAR_CATEGORIES[38]: self.__shadowcrawler(),
            c.CHAR_CATEGORIES[39]: self.__shining_archer(),
            c.CHAR_CATEGORIES[40]: self.__shining_assassin(),
            c.CHAR_CATEGORIES[41]: self.__shining_dragon(),
            c.CHAR_CATEGORIES[42]: self.__siren(),
            c.CHAR_CATEGORIES[43]: self.__sky_breaker(),
            c.CHAR_CATEGORIES[44]: self.__soul_breaker(),
            c.CHAR_CATEGORIES[45]: self.__storm_shaman(),
            c.CHAR_CATEGORIES[46]: self.__swordsman(),
            c.CHAR_CATEGORIES[47]: self.__taboo_witcher(),
            c.CHAR_CATEGORIES[48]: self.__the_scryer(),
            c.CHAR_CATEGORIES[49]: self.__the_source(),
            c.CHAR_CATEGORIES[50]: self.__thunder_spirit(),
            c.CHAR_CATEGORIES[51]: self.__tsunami_stalker(),
            c.CHAR_CATEGORIES[52]: self.__tusk_champion(),
            c.CHAR_CATEGORIES[53]: self.__umbra(),
            c.CHAR_CATEGORIES[54]: self.__unicorn(),
            c.CHAR_CATEGORIES[55]: self.__venom(),
            c.CHAR_CATEGORIES[56]: self.__venomancer(),
            c.CHAR_CATEGORIES[57]: self.__warpwood_sage(),
            c.CHAR_CATEGORIES[58]: self.__water_spirit(),
            c.CHAR_CATEGORIES[59]: self.__werewolf(),
            c.CHAR_CATEGORIES[60]: self.__whisper_seer(),
            c.CHAR_CATEGORIES[61]: self.__wind_ranger(),
            c.CHAR_CATEGORIES[62]: self.__winter_dragon(),
            c.CHAR_CATEGORIES[63]: self.__worm()
        }
        switch.get(self.__name)

    def __abyssal_guard(self):
        self.__cost = 2
        self.__race1 = MARINE
        self.__race2 = UNDEF_RACE
        self.__cl = WARRIOR
        self.__rarity = UNCOMMON

    def __abyssal_crawler(self):
        self.__cost = 2
        self.__race1 = MARINE
        self.__race2 = UNDEF_RACE
        self.__cl = ASSASSIN
        self.__rarity = UNCOMMON

    def __argali_knight(self):
        self.__cost = 3
        self.__race1 = HUMAN
        self.__race2 = UNDEF_RACE
        self.__cl = KNIGHT
        self.__rarity = RARE

    def __berserker(self):
        self.__cost = 4
        self.__race1 = GLACIER
        self.__race2 = UNDEF_RACE
        self.__cl = WARRIOR
        self.__rarity = EPIC

    def __defector(self):
        self.__cost = 1
        self.__race1 = GLACIER
        self.__race2 = UNDEF_RACE
        self.__cl = SHAMAN
        self.__rarity = COMMON

    def __desperate_doctor(self):
        self.__cost = 2
        self.__race1 = GLACIER
        self.__race2 = UNDEF_RACE
        self.__cl = WARLOCK
        self.__rarity = UNCOMMON

    def __devastator(self):
        self.__cost = 5
        self.__race1 = GOBLIN
        self.__race2 = UNDEF_RACE
        self.__cl = MECH
        self.__rarity = LEGENDARY

    def __doom_arbitor(self):
        self.__cost = 4
        self.__race1 = DEMON
        self.__race2 = UNDEF_RACE
        self.__cl = WARRIOR
        self.__rarity = EPIC

    def __dragon_knight(self):
        self.__cost = 4
        self.__race1 = HUMAN
        self.__race2 = DRAGON
        self.__cl = KNIGHT
        self.__rarity = EPIC

    def __dwarf_sniper(self):
        self.__cost = 3
        self.__race1 = DWARF
        self.__race2 = UNDEF_RACE
        self.__cl = HUNTER
        self.__rarity = RARE

    def __e_ranger(self):
        self.__cost = 1
        self.__race1 = UNDEAD
        self.__race2 = UNDEF_RACE
        self.__cl = HUNTER
        self.__rarity = COMMON

    def __egg(self):
        self.__cost = 5
        self.__race1 = FEATHERED
        self.__race2 = UNDEF_RACE
        self.__cl = EGG
        self.__rarity = LEGENDARY

    def __elder(self):
        self.__cost = 4
        self.__race1 = HUMAN
        self.__race2 = UNDEF_RACE
        self.__cl = MAGE
        self.__rarity = EPIC

    def __empty(self):
        self.__cost = 0
        self.__race1 = UNDEF_RACE
        self.__race2 = UNDEF_RACE
        self.__cl = UNDEF_CLASS
        self.__rarity = UNDEF_RARITY

    def __evil_knight(self):
        self.__cost = 3
        self.__race1 = UNDEAD
        self.__race2 = UNDEF_RACE
        self.__cl = KNIGHT
        self.__rarity = RARE

    def __flame_wizard(self):
        self.__cost = 3
        self.__race1 = HUMAN
        self.__race2 = UNDEF_RACE
        self.__cl = MAGE
        self.__rarity = RARE

    def __frost_knight(self):
        self.__cost = 1
        self.__race1 = GLACIER
        self.__race2 = UNDEF_RACE
        self.__cl = KNIGHT
        self.__rarity = COMMON

    def __frostblaze_dragon(self):
        self.__cost = 5
        self.__race1 = DRAGON
        self.__race2 = UNDEF_RACE
        self.__cl = WARLOCK
        self.__rarity = LEGENDARY

    def __god_of_thunder(self):
        self.__cost = 5
        self.__race1 = DIVINITY
        self.__race2 = UNDEF_RACE
        self.__cl = MAGE
        self.__rarity = LEGENDARY

    def __god_of_war(self):
        self.__cost = 1
        self.__race1 = DIVINITY
        self.__race2 = UNDEF_RACE
        self.__cl = WARRIOR
        self.__rarity = COMMON

    def __goddess_of_light(self):
        self.__cost = 2
        self.__race1 = DIVINITY
        self.__race2 = UNDEF_RACE
        self.__cl = PRIEST
        self.__rarity = UNCOMMON

    def __grimtouch(self):
        self.__cost = 4
        self.__race1 = DEMON
        self.__race2 = UNDEF_RACE
        self.__cl = WIZARD
        self.__rarity = EPIC

    def __heaven_bomber(self):
        self.__cost = 1
        self.__race1 = GOBLIN
        self.__race2 = UNDEF_RACE
        self.__cl = MECH
        self.__rarity = COMMON

    def __hell_knight(self):
        self.__cost = 2
        self.__race1 = DEMON
        self.__race2 = UNDEF_RACE
        self.__cl = KNIGHT
        self.__rarity = UNCOMMON

    def __herald(self):
        self.__cost = 2
        self.__race1 = DIVINITY
        self.__race2 = UNDEF_RACE
        self.__cl = WIZARD
        self.__rarity = UNCOMMON

    def __lightblade_knight(self):
        self.__cost = 2
        self.__race1 = FEATHERED
        self.__race2 = UNDEF_RACE
        self.__cl = KNIGHT
        self.__rarity = UNCOMMON

    def __lord_of_sand(self):
        self.__cost = 3
        self.__race1 = BEAST
        self.__race2 = INSECTOID
        self.__cl = ASSASSIN
        self.__rarity = RARE

    def __ogre_mage(self):
        self.__cost = 1
        self.__race1 = KIRA
        self.__race2 = UNDEF_RACE
        self.__cl = MAGE
        self.__rarity = COMMON

    def __pirate(self):
        self.__cost = 4
        self.__race1 = HUMAN
        self.__race2 = UNDEF_RACE
        self.__cl = WARRIOR
        self.__rarity = EPIC

    def __razorclaw(self):
        self.__cost = 4
        self.__race1 = BEAST
        self.__race2 = UNDEF_RACE
        self.__cl = DRUID
        self.__rarity = EPIC

    def __reaper(self):
        self.__cost = 4
        self.__race1 = UNDEAD
        self.__race2 = UNDEF_RACE
        self.__cl = WARLOCK
        self.__rarity = EPIC

    def __redaxe(self):
        self.__cost = 1
        self.__race1 = CAVE_CLAN
        self.__race2 = UNDEF_RACE
        self.__cl = WARRIOR
        self.__rarity = COMMON

    def __ripper(self):
        self.__cost = 2
        self.__race1 = GOBLIN
        self.__race2 = UNDEF_RACE
        self.__cl = MECH
        self.__rarity = UNCOMMON

    def __rogue_guard(self):
        self.__cost = 5
        self.__race1 = DEMON
        self.__race2 = UNDEF_RACE
        self.__cl = WARRIOR
        self.__rarity = LEGENDARY

    def __shadowcrawler(self):
        self.__cost = 3
        self.__race1 = FEATHERED
        self.__race2 = UNDEF_RACE
        self.__cl = ASSASSIN
        self.__rarity = RARE

    def __shining_archer(self):
        self.__cost = 2
        self.__race1 = FEATHERED
        self.__race2 = UNDEF_RACE
        self.__cl = HUNTER
        self.__rarity = UNCOMMON

    def __shining_assassin(self):
        self.__cost = 4
        self.__race1 = FEATHERED
        self.__race2 = UNDEF_RACE
        self.__cl = ASSASSIN
        self.__rarity = EPIC

    def __shining_dragon(self):
        self.__cost = 2
        self.__race1 = FEATHERED
        self.__race2 = DRAGON
        self.__cl = MAGE
        self.__rarity = UNCOMMON

    def __siren(self):
        self.__cost = 4
        self.__race1 = MARINE
        self.__race2 = UNDEF_RACE
        self.__cl = HUNTER
        self.__rarity = EPIC

    def __sky_breaker(self):
        self.__cost = 1
        self.__race1 = GOBLIN
        self.__race2 = UNDEF_RACE
        self.__cl = MECH
        self.__rarity = COMMON

    def __soul_breaker(self):
        self.__cost = 1
        self.__race1 = GOBLIN
        self.__race2 = UNDEF_RACE
        self.__cl = ASSASSIN
        self.__rarity = COMMON

    def __storm_shaman(self):
        self.__cost = 4
        self.__race1 = CAVE_CLAN
        self.__race2 = UNDEF_RACE
        self.__cl = SHAMAN
        self.__rarity = EPIC

    def __swordsman(self):
        self.__cost = 2
        self.__race1 = CAVE_CLAN
        self.__race2 = UNDEF_RACE
        self.__cl = WARRIOR
        self.__rarity = UNCOMMON

    def __taboo_witcher(self):
        self.__cost = 1
        self.__race1 = FEATHERED
        self.__race2 = UNDEF_RACE
        self.__cl = WITCHER
        self.__rarity = COMMON

    def __the_source(self):
        self.__cost = 2
        self.__race1 = HUMAN
        self.__race2 = UNDEF_RACE
        self.__cl = MAGE
        self.__rarity = UNCOMMON

    def __thunder_spirit(self):
        self.__cost = 3
        self.__race1 = SPIRIT
        self.__race2 = UNDEF_RACE
        self.__cl = MAGE
        self.__rarity = RARE

    def __tsunami_stalker(self):
        self.__cost = 5
        self.__race1 = MARINE
        self.__race2 = UNDEF_RACE
        self.__cl = HUNTER
        self.__rarity = LEGENDARY

    def __tusk_champion(self):
        self.__cost = 1
        self.__race1 = BEAST
        self.__race2 = UNDEF_RACE
        self.__cl = WARRIOR
        self.__rarity = COMMON

    def __umbra(self):
        self.__cost = 3
        self.__race1 = DRAGON
        self.__race2 = UNDEAD
        self.__cl = HUNTER
        self.__rarity = RARE

    def __venom(self):
        self.__cost = 3
        self.__race1 = DRAGON
        self.__race2 = UNDEF_RACE
        self.__cl = ASSASSIN
        self.__rarity = RARE

    def __venomancer(self):
        self.__cost = 4
        self.__race1 = GOBLIN
        self.__race2 = KIRA
        self.__cl = WARLOCK
        self.__rarity = EPIC

    def __warpwood_sage(self):
        self.__cost = 3
        self.__race1 = FEATHERED
        self.__race2 = UNDEF_RACE
        self.__cl = DRUID
        self.__rarity = RARE

    def __water_spirit(self):
        self.__cost = 2
        self.__race1 = SPIRIT
        self.__race2 = UNDEF_RACE
        self.__cl = ASSASSIN
        self.__rarity = UNCOMMON

    def __werewolf(self):
        self.__cost = 3
        self.__race1 = HUMAN
        self.__race2 = BEAST
        self.__cl = WARRIOR
        self.__rarity = RARE

    def __whisper_seer(self):
        self.__cost = 2
        self.__race1 = FEATHERED
        self.__race2 = UNDEF_RACE
        self.__cl = DRUID
        self.__rarity = UNCOMMON

    def __wind_ranger(self):
        self.__cost = 3
        self.__race1 = FEATHERED
        self.__race2 = UNDEF_RACE
        self.__cl = HUNTER
        self.__rarity = RARE

    def __winter_dragon(self):
        self.__cost = 1
        self.__race1 = DRAGON
        self.__race2 = UNDEF_RACE
        self.__cl = MAGE
        self.__rarity = COMMON

    def __worm(self):
        self.__cost = 3
        self.__race1 = BEAST
        self.__race2 = INSECTOID
        self.__cl = WARLOCK
        self.__rarity = RARE

    def __dark_spirit(self):
        self.__cost = 5
        self.__race1 = SPIRIT
        self.__race2 = UNDEF_RACE
        self.__cl = WARLOCK
        self.__rarity = LEGENDARY

    def __fallen_witcher(self):
        self.__cost = 3
        self.__race1 = DEMON
        self.__race2 = UNDEF_RACE
        self.__cl = WITCHER
        self.__rarity = RARE

    def __fortune_teller(self):
        self.__cost = 3
        self.__race1 = GLACIER
        self.__race2 = UNDEF_RACE
        self.__cl = PRIEST
        self.__rarity = RARE

    def __helicopter(self):
        self.__cost = 5
        self.__race1 = DWARF
        self.__race2 = UNDEF_RACE
        self.__cl = MECH
        self.__rarity = LEGENDARY

    def __the_scryer(self):
        self.__cost = 5
        self.__race1 = FEATHERED
        self.__race2 = UNDEF_RACE
        self.__cl = SHAMAN
        self.__rarity = LEGENDARY

    def __unicorn(self):
        self.__cost = 1
        self.__race1 = BEAST
        self.__race2 = UNDEF_RACE
        self.__cl = DRUID
        self.__rarity = COMMON
