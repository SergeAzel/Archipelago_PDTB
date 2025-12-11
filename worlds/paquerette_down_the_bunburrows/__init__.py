from BaseClasses import ItemClassification, CollectionState, Region
from BaseClasses import Tutorial, Item
from worlds.AutoWorld import World, WebWorld

from .RawItems import raw_list_of_tools
from .Items import item_name_to_id, item_id_to_name, fluffle
from .Locations import location_name_to_id, location_id_to_name, \
        generateRegionLocations, PaqueretteLocation

from .RawLocations import pinkLocations, sunkenLocations, hayLocations, \
        spookyLocations, forgottenLocations, templeLocations, \
        falseHellLocations, sleepHellLocations, crumblingHellLocations, \
        hellTempleLocations

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

    def create_item(self, item: str) -> PaqueretteItem:
        return PaqueretteItem(item, ItemClassification.progression,
                              self.item_name_to_id[item], self.player)

    def create_filler(self, item: str) -> PaqueretteItem:
        return PaqueretteItem(item, ItemClassification.filler,
                              self.item_name_to_id[item], self.player)

    def create_items(self):
        self.itempool = []

        for item_name in raw_list_of_tools:
            self.itempool.append(self.create_item(item_name))

        print("Itempool size: " + str(len(self.itempool)))

        while len(self.itempool) < len(location_id_to_name):
            self.itempool.append(self.create_filler(fluffle))

        print("Final Itempool size: " + str(len(self.itempool)))

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
                                  generateRegionLocations(self.player,
                                                          pinkLocations))
        menu.connect(pink)

        sunken = self.create_region("Sunken", "The Sunken Bunburrow",
                                    generateRegionLocations(self.player,
                                                            sunkenLocations))
        pink.connect(sunken, rule=self.is_sunken_unlocked)

        hay = self.create_region("Hay", "The Hay Bunburrow",
                                 generateRegionLocations(self.player,
                                                         hayLocations))
        sunken.connect(hay, rule=self.is_hay_unlocked)

        spooky = self.create_region("Spooky", "The Spooky Bunburrow",
                                    generateRegionLocations(self.player,
                                                            spookyLocations))
        hay.connect(spooky)  # Always accessible from C-3

        forgotten = self.create_region("Forgotten", "The Forgotten Bunburrow",
                                       generateRegionLocations(self.player,
                                                               forgottenLocations))
        hay.connect(forgotten)  # Nearly always accessible

        temple = self.create_region("Temple" "The Temple of Bun",
                                    generateRegionLocations(self.player,
                                                            templeLocations))
        hay.connect(temple, rule=self.is_temple_unlocked)

        falseHell = self.create_region("FalseHell", "The False Hells",
                                       generateRegionLocations(self.player,
                                                               falseHellLocations))
        hay.connect(falseHell, rule=self.is_temple_unlocked)

        sleepHell = self.create_region("SleepHell", "The Nightmare Hells",
                                       generateRegionLocations(self.player,
                                                               sleepHellLocations))
        forgotten.connect(sleepHell, rule=self.is_sleep_hell_unlocked)

        crumbledHell = self.create_region("CrumbledHell", "The Crumbling Hells",
                                          generateRegionLocations(self.player,
                                                                  crumblingHellLocations))
        sleepHell.connect(crumbledHell, rule=self.is_crumbled_hell_unlocked)

        hellTemple = self.create_region("HellTemple", "The Temple of Hell",
                                        generateRegionLocations(self.player,
                                                                hellTempleLocations))
        crumbledHell.connect(hellTemple, rule=self.is_hell_temple_unlocked)

    def is_sunken_unlocked(self, state: CollectionState) -> bool:
        return len(state.locations_checked) >= 10

    def is_hay_unlocked(self, state: CollectionState) -> bool:
        return len(state.locations_checked) >= 18

    def is_temple_unlocked(self, state: CollectionState) -> bool:
        return state.has("C-13", self.player, 1)

    def is_sleep_hell_unlocked(self, state: CollectionState) -> bool:
        return state.has("E-11", self.player, 1) and \
                state.has("E-10", self.player, 1) and \
                state.has("E-9", self.player, 1) and \
                state.has("E-8", self.player, 1) and \
                state.has("E-7", self.player, 1) and \
                state.has("E-6", self.player, 1) and \
                state.has("E-5", self.player, 1) and \
                state.has("E-4", self.player, 1) and \
                state.has("E-3", self.player, 1)

    def is_crumbled_hell_unlocked(self, state: CollectionState) -> bool:
        return state.has("E-20", self.player, 1) and \
                state.has("C-20", self.player, 1)

    def is_hell_temple_unlocked(self, state: CollectionState) -> bool:
        return state.has("C-22", self.player, 1)
