from BaseClasses import Tutorial, Item
from BaseClasses import ItemClassification as IC
from worlds.AutoWorld import WebWorld, World
from .Options import PhoaOptions, phoa_option_groups
from .Locations import PhoaLocation, get_location_data, PhoaLocationData
from .Items import PhoaItem, item_table, PhoaItemData, get_item_pool, dungeon_item_setting_groups, \
    DungeonItemSettingGroup, filter_dungeon_items, fill_dungeon_items_in_own_dungeon, item_inclusion_priority
from .Regions import create_regions_and_locations


class PhoaWebWorld(WebWorld):
    tutorials = [Tutorial(
        tutorial_name="Start Guide",
        description="A guide to start playing Phoenotopia: Awakening in Archipelago",
        language="English",
        file_name="setup_en.md",
        link="guide/en",
        authors=["Lenamphy"]
    )]
    option_groups = phoa_option_groups


class PhoaWorld(World):
    game = "Phoenotopia: Awakening"
    web = PhoaWebWorld()
    options: PhoaOptions
    options_dataclass = PhoaOptions
    location_name_to_id = {name: data.address for name, data in get_location_data(-1, None).items()}
    item_name_to_id = {name: data.code for name, data in item_table.items()}

    own_dungeon_locations: dict[str, list[str]]
    own_dungeon_keys: dict[str, list[PhoaItem]]

    progression_item_classifications_overrides: list[str]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.own_dungeon_keys = {}
        self.own_dungeon_locations = {}
        self.progression_item_classifications_overrides = []

    def generate_early(self) -> None:
        self._determine_item_classifications_overrides()

    def create_item(self, name: str) -> PhoaItem:
        item_classification = IC.progression \
            if name in self.progression_item_classifications_overrides \
            else item_table[name].type
        return PhoaItem(name, item_classification, item_table[name].code, self.player)

    def create_items(self):
        self.create_and_assign_event_items()

        location_data = get_location_data(self.player, self.options)
        item_pool_strings, precollected_items = get_item_pool(self, location_data)

        for item in precollected_items:
            precollected_item = self.create_item(item)
            if precollected_item.classification != IC.progression:
                raise Exception(f"Precollected item that is not progression: '{item}'")
            self.multiworld.push_precollected(precollected_item)

        for dungeon_item_setting_group in dungeon_item_setting_groups:
            filter_dungeon_items(self, location_data, dungeon_item_setting_group, item_pool_strings)

        item_pool: list[PhoaItem] = []

        for item_name in item_pool_strings:
            item_pool.append(self.create_item(item_name))

        self.multiworld.itempool += item_pool

    def create_regions(self):
        create_regions_and_locations(self.multiworld, self.player, self.options)

    def set_rules(self):
        self.multiworld.completion_condition[self.player] = lambda state: state.has(
            "Defeat Katash", self.player
        )

    def get_filler_item_name(self) -> str:
        return '20 Rin'

    def create_and_assign_event_items(self):
        for location in self.multiworld.get_locations(self.player):
            if location.address is None:
                location.place_locked_item(
                    Item(location.name, IC.progression, None, self.player))

    def fill_slot_data(self):
        return self.options.get_slot_data_dict()

    def _determine_item_classifications_overrides(self) -> None:
        options = self.options

        if not options.start_with_wooden_bat:
            self.progression_item_classifications_overrides.append("Progressive Bat")
        if options.enable_fishing_spots:
            self.progression_item_classifications_overrides.append("Fishing Rod")
            self.progression_item_classifications_overrides.append("Serpent Rod")
            self.progression_item_classifications_overrides.append("Progressive Fishing Rod")
        if (options.enable_rin_locations > 1
                or options.enable_minigames
                or options.enable_heart_ruby_locations
                or options.enable_moonstone_locations
                or options.enable_fishing_spots
                or options.enable_ancient_vault):
            self.progression_item_classifications_overrides.append("Energy Gem")
        if options.enable_sidequests:
            self.progression_item_classifications_overrides.append("Antique Pin")
            self.progression_item_classifications_overrides.append("GEO Song")
            self.progression_item_classifications_overrides.append("Prelude of Panselo")
            self.progression_item_classifications_overrides.append("Progressive Prelude of Panselo")
            self.progression_item_classifications_overrides.append("Baroque of Battle")
            self.progression_item_classifications_overrides.append("Lullaby of Ava")
            self.progression_item_classifications_overrides.append("Stack of Letters")
        if options.enable_geo_shop:
            self.progression_item_classifications_overrides.append("GEO Ticket")
        if options.enable_geo_challenge_rewards:
            self.progression_item_classifications_overrides.append("GEO Song")
        if options.enable_ouroboros_scroll_rewards:
            self.progression_item_classifications_overrides.append("Ouroboros Scroll")
        if options.enable_lunar_artifact_quest:
            self.progression_item_classifications_overrides.append("Lunar Frog")
            self.progression_item_classifications_overrides.append("Lunar Vase")
            self.progression_item_classifications_overrides.append("Lunar Drake")
            self.progression_item_classifications_overrides.append("Lunar Compass")
            self.progression_item_classifications_overrides.append("Lunar Trident")
            self.progression_item_classifications_overrides.append("Lunar Crown")
            self.progression_item_classifications_overrides.append("Lunar Comb")
            self.progression_item_classifications_overrides.append("Lunar Watch")
            self.progression_item_classifications_overrides.append("Lunar Goblet")
            self.progression_item_classifications_overrides.append("Lunar Medal")
            self.progression_item_classifications_overrides.append("Lunar Egg")
            self.progression_item_classifications_overrides.append("Lunar Key")
        if options.franway_unlock_mode == 3:
            self.progression_item_classifications_overrides.append("Panselo Franway Teleporter")
            self.progression_item_classifications_overrides.append("Atai Franway Teleporter")
            self.progression_item_classifications_overrides.append("Cosette Franway Teleporter")
        if options.franway_unlock_mode in (1, 2) or options.enable_moonstone_shops:
            self.progression_item_classifications_overrides.append("Moonstone")
            self.progression_item_classifications_overrides.append("Moonstone Bundle")

    def pre_fill(self) -> None:
        for dungeon_item_setting_group in dungeon_item_setting_groups:
            fill_dungeon_items_in_own_dungeon(self, dungeon_item_setting_group)
