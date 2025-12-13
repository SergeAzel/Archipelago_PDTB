from BaseClasses import ItemClassification, CollectionState, Region
from BaseClasses import Tutorial, Item, Location
from worlds.AutoWorld import World, WebWorld

from .RawItems import raw_list_of_tools
from .Items import item_name_to_id, item_id_to_name, fluffle
from .Locations import location_name_to_id, location_id_to_name, \
        generateRegionLocations, PaqueretteLocation, list_of_bunnies

from .RawLocations import pinkLocations, \
        sunkenLocations, hayLocations, spookyLocations, \
        forgottenUpperLocations, forgottenMiddleLocations, \
        forgottenLowerLocations, templeLocations, \
        falseHellLocations, sleepHellLocations, crumblingHellLocations, \
        hellTempleLocations, pillarsLocations

from .Consts import PaqueretteGame

from .Options import options_presets, PaqueretteOptions


class PaqueretteItem(Item):
    game: str = PaqueretteGame


class PaqueretteDownTheBunburrowsWeb(WebWorld):
    theme = "grassFlowers"
    options_presets = options_presets


class PaqueretteDownTheBunburrowsWorld(World):
    game: str = PaqueretteGame

    options_dataclass = PaqueretteOptions
    options: PaqueretteOptions

    web = PaqueretteDownTheBunburrowsWeb()
    required_client_version = (0, 1, 0)
    topology_present: bool = True

    item_name_to_id = item_name_to_id
    item_id_to_name = item_id_to_name

    location_id_to_name = location_id_to_name
    location_name_to_id = location_name_to_id


    def create_items(self):
        self.itempool = []

        for item_name in raw_list_of_tools:
            self.itempool.append(PaqueretteItem(item_name, ItemClassification.progression,
                              self.item_name_to_id[item_name], self.player))

        while len(self.itempool) < len(location_id_to_name):
            self.itempool.append(PaqueretteItem(fluffle, ItemClassification.filler,
                              self.item_name_to_id[fluffle], self.player))

        self.multiworld.itempool += self.itempool

    def create_region(self, name, hint="", locations=[]):
        region = Region(name, self.player, self.multiworld, hint=hint)

        for location in locations:
            location.parent_region = region
            region.locations += [location]

        self.multiworld.regions += [region]

        return region

    def create_regions(self) -> None:
        menu = self.create_region("Menu")
        pink = self.create_region("Pink", "The Pink Bunburrow",
                                  generateRegionLocations(self.player, pinkLocations))
        sunken = self.create_region("Sunken", "The Sunken Bunburrow",
                                    generateRegionLocations(self.player, sunkenLocations))
        hay = self.create_region("Hay", "The Hay Bunburrow",
                                 generateRegionLocations(self.player, hayLocations))
        spooky = self.create_region("Spooky", "The Spooky Bunburrow",
                                    generateRegionLocations(self.player, spookyLocations))

        forgottenUpper = self.create_region("ForgottenUpper", "The Forgotten Bunburrow",
                generateRegionLocations(self.player, forgottenUpperLocations))
        forgottenMiddle = self.create_region("ForgottenMiddle", "The Forgotten Bunburrow",
                generateRegionLocations(self.player, forgottenMiddleLocations))
        forgottenLower = self.create_region("ForgottenLower", "The Forgotten Bunburrow",
                generateRegionLocations(self.player, forgottenLowerLocations))

        temple = self.create_region("Temple", "The Temple of Bun",
                                    generateRegionLocations(self.player, templeLocations))

        falseHell = self.create_region("FalseHell", "The False Hells",
                                       generateRegionLocations(self.player, falseHellLocations))
        sleepHell = self.create_region("SleepHell", "The Nightmare Hells",
                                       generateRegionLocations(self.player, sleepHellLocations))
        crumbledHell = self.create_region("CrumbledHell", "The Crumbling Hells",
                                          generateRegionLocations(self.player, crumblingHellLocations))
        hellTemple = self.create_region("HellTemple", "The Temple of Hell",
                                        generateRegionLocations(self.player, hellTempleLocations))
        pillars = self.create_region("Pillars", "The Pillars Room",
                                     generateRegionLocations(self.player, pillarsLocations))

        menu.connect(pink)
        pink.connect(sunken)
        sunken.connect(hay, rule=lambda state: len(self.get_bunnies(state)) >= 18)
        hay.connect(spooky)  # Always accessible from C-3
        hay.connect(forgottenUpper, rule=lambda state: len(self.get_bunnies(state)) >= 45)
        forgottenUpper.connect(forgottenMiddle, rule=self.is_forgotten_middle_unlocked_by_upper)
        hay.connect(forgottenMiddle, rule=self.is_forgotten_middle_unlocked_by_center)
        forgottenMiddle.connect(forgottenLower, rule=self.is_forgotten_lower_unlocked_by_middle)
        hay.connect(forgottenLower, rule=self.is_forgotten_lower_unlocked_by_center)
        hay.connect(temple, rule=self.is_temple_unlocked)
        hay.connect(falseHell, rule=self.is_temple_unlocked)
        forgottenLower.connect(sleepHell, rule=self.is_sleep_hell_unlocked)
        sleepHell.connect(crumbledHell, rule=self.is_crumbled_hell_unlocked)
        crumbledHell.connect(hellTemple, rule=self.is_hell_temple_unlocked)
        hellTemple.connect(pillars, rule=self.is_pillars_unlocked)

    def get_bunnies(self, state: CollectionState) -> list:
        return [bunny for bunny in list_of_bunnies
                    if state.can_reach(bunny[0], "Location", self.player)]

    def set_rules(self) -> None:
        self.multiworld.completion_condition[self.player] = self.can_win

    def can_win(self, state: CollectionState) -> bool:
        canWeWin = state.can_reach("C-27-1", "Location", self.player)
        return canWeWin

    # region-specific rules below
    def is_forgotten_middle_unlocked_by_center(self, state: CollectionState) -> bool:
        # Access check by C-5 or C-3 (via E-3)
        doWeHaveThem = state.has("C-5", self.player, 1) or \
                state.has("E-3", self.player, 1)

        if doWeHaveThem:
            return True
        return False

    def is_forgotten_middle_unlocked_by_upper(self, state: CollectionState) -> bool:
        # Access restricted by burrow unlock and E-2, E-3
        doWeHaveThem = state.has("E-2", self.player, 1) and \
                state.has("E-3", self.player, 1)

        if doWeHaveThem:
            return True
        return False

    def is_forgotten_lower_unlocked_by_middle(self, state: CollectionState) -> bool:
        # Access restricted by E-5, E-6, E-7, E-8, and E-9
        doWeHaveThem = state.has("E-5", self.player, 1) and \
                state.has("E-6", self.player, 1) and \
                state.has("E-7", self.player, 1) and \
                state.has("E-8", self.player, 1) and \
                state.has("E-9", self.player, 1)

        if doWeHaveThem:
            return True
        return False

    def is_forgotten_lower_unlocked_by_center(self, state: CollectionState) -> bool:
        # Access only restricted by C-10
        doWeHaveThem = state.has("C-10", self.player, 1)

        if doWeHaveThem:
            return True
        return False

    def is_temple_unlocked(self, state: CollectionState) -> bool:
        doWeHaveThem = state.has("C-13", self.player, 1)

        if doWeHaveThem:
            return True
        return False

    def is_sleep_hell_unlocked(self, state: CollectionState) -> bool:
        doWeHaveThem = state.has("E-11", self.player, 1) and \
                state.has("E-10", self.player, 1)

        if doWeHaveThem:
            return True
        return False

    def is_crumbled_hell_unlocked(self, state: CollectionState) -> bool:
        doWeHaveThem = state.has("E-20", self.player, 1) and \
                state.has("C-20", self.player, 1)

        if doWeHaveThem:
            return True
        return False

    def is_hell_temple_unlocked(self, state: CollectionState) -> bool:
        doWeHaveThem = state.has("C-22", self.player, 1)

        if doWeHaveThem:
            return True
        return False

    def is_pillars_unlocked(self, state: CollectionState) -> bool:
        doWeHaveThem = state.has("N-26", self.player, 1) and \
               state.has("C-26", self.player, 1) and \
               state.has("C-25", self.player, 1) and \
               state.has("N-25", self.player, 1) and \
               state.has("S-25", self.player, 1) and \
               state.has("S-26", self.player, 1) and \
               state.has("E-23", self.player, 1) and \
               state.has("E-24", self.player, 1) and \
               state.has("E-25", self.player, 1) and \
               state.has("E-26", self.player, 1) and \
               state.has("E-27", self.player, 1)

        if doWeHaveThem:
            return True
        return False
