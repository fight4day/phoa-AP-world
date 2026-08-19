from typing import NamedTuple, TYPE_CHECKING
from BaseClasses import Item
from BaseClasses import ItemClassification as IC
from Fill import fill_restrictive
from Options import OptionError
from worlds.phoa.Locations import PhoaLocationData
from . import PhoaOptions

if TYPE_CHECKING:
    from .. import PhoaWorld


class PhoaItem(Item):
    game: str = "Phoenotopia: Awakening"


class PhoaItemData(NamedTuple):
    code: int
    amount: int
    type: IC


class DungeonItemSettingGroup(NamedTuple):
    shuffle_option: str
    bundle_option: str
    dungeon_name: str
    dungeon_item: str
    dungeon_item_bundle: str


# @formatter:off
item_table: dict[str, PhoaItemData] = {
    "Heart Ruby":                       PhoaItemData(3,     30, IC.useful),
    "Energy Gem":                       PhoaItemData(4,     20, IC.useful),
    "Moonstone":                        PhoaItemData(5,     65, IC.filler),
    "Wooden Bat":                       PhoaItemData(6,     1,  IC.progression),
    "Composite Bat":                    PhoaItemData(7,     1,  IC.useful),
    "Steel Bat":                        PhoaItemData(8,     1,  IC.useful),
    "Night Star":                       PhoaItemData(9,     1,  IC.useful),
    "Sky Vest":                         PhoaItemData(11,    1,  IC.useful),
    "Jade Hauberk":                     PhoaItemData(12,    1,  IC.useful),
    "GEO Jacket":                       PhoaItemData(13,    1,  IC.useful),
    "Life Saver":                       PhoaItemData(14,    1,  IC.progression),
    "Tusk Strike":                      PhoaItemData(15,    1,  IC.useful),
    "Concentrate":                      PhoaItemData(16,    1,  IC.useful),
    "Spear Bomb":                       PhoaItemData(17,    1,  IC.progression),
    "Troll's Guard":                    PhoaItemData(18,    1,  IC.useful),
    "Temperance":                       PhoaItemData(19,    1,  IC.progression),
    "Whirlwind":                        PhoaItemData(20,    1,  IC.progression),
    "Antique Cast Iron":                PhoaItemData(25,    1,  IC.useful),
    "Lucky Earrings":                   PhoaItemData(26,    1,  IC.useful),
    "Treble Shot":                      PhoaItemData(28,    1,  IC.progression),
    "Bandit's Flute":                   PhoaItemData(29,    1,  IC.progression),
    "Slingshot":                        PhoaItemData(30,    1,  IC.progression),
    "Bombs":                            PhoaItemData(31,    1,  IC.progression),
    "Crank Lamp":                       PhoaItemData(32,    1,  IC.progression),  # Ignore light requirement option?
    "Sonic Spear":                      PhoaItemData(33,    1,  IC.progression),
    "Rocket Boots":                     PhoaItemData(34,    1,  IC.progression),
    "Spheralis":                        PhoaItemData(35,    1,  IC.progression),
    "Civilian Crossbow":                PhoaItemData(37,    1,  IC.progression),
    "Double Crossbow":                  PhoaItemData(38,    1,  IC.progression),
    "Refurbished Crank Lamp":           PhoaItemData(39,    1,  IC.progression),
    "Fishing Rod":                      PhoaItemData(40,    1,  IC.useful),
    "Serpent Rod":                      PhoaItemData(41,    1,  IC.useful),
    "Kobold Blaster":                   PhoaItemData(42,    1,  IC.progression),
    "Neutron Lamp":                     PhoaItemData(43,    1,  IC.progression),  # Ignore light requirement option?
    "Remote Bombs":                     PhoaItemData(44,    1,  IC.progression),
    "Doki Herb":                        PhoaItemData(45,    9,  IC.filler),
    "Deli Sandwich":                    PhoaItemData(46,    2,  IC.filler),
    "Pumpkin Muffin":                   PhoaItemData(47,    2,  IC.filler),
    "Cooked Toad Leg":                  PhoaItemData(49,    1,  IC.filler),
    "Berry Fruit":                      PhoaItemData(50,    3,  IC.filler),
    "Lune Fruit":                       PhoaItemData(51,    1,  IC.filler),
    "Perro Egg":                        PhoaItemData(52,    5,  IC.filler),
    "Nectear":                          PhoaItemData(53,    13, IC.filler),
    "Honey Brew":                       PhoaItemData(54,    5,  IC.filler),
    "Pooki Jerky":                      PhoaItemData(56,    5,  IC.filler),
    "Fruit Jam":                        PhoaItemData(57,    2,  IC.filler),
    "Canned Beans":                     PhoaItemData(58,    4,  IC.filler),
    "Potato Lunch":                     PhoaItemData(59,    1,  IC.filler),
    "Curry Bento":                      PhoaItemData(61,    1,  IC.filler),
    "Turtle":                           PhoaItemData(63,    1,  IC.filler),
    "Cheese":                           PhoaItemData(64,    4,  IC.filler),
    "Grape Cake":                       PhoaItemData(65,    1,  IC.filler),
    "Drake Tail":                       PhoaItemData(66,    2,  IC.filler),
    "Milk":                             PhoaItemData(67,    4,  IC.filler),
    "Chocolate":                        PhoaItemData(68,    2,  IC.filler),
    "Cooked Drake Tail":                PhoaItemData(72,    1,  IC.filler),
    "Raw Meat":                         PhoaItemData(73,    3,  IC.filler),
    "Big Raw Meat":                     PhoaItemData(74,    2,  IC.filler),
    "Sushi":                            PhoaItemData(79,    1,  IC.filler),
    "Prime Fish Fillet":                PhoaItemData(81,    1,  IC.filler),
    "Gourmet Fish Fillet":              PhoaItemData(82,    1,  IC.filler),
    "Fish Skewer":                      PhoaItemData(84,    3,  IC.filler),
    "Cooked Knife Krill":               PhoaItemData(87,    1,  IC.filler),
    "Lunar Egg":                        PhoaItemData(88,    1,  IC.filler),
    "Honey Drop":                       PhoaItemData(89,    4,  IC.filler),
    "Lunar Goblet":                     PhoaItemData(92,    1,  IC.filler),
    "Anuri Pearlstone":                 PhoaItemData(98,    10, IC.progression),  # Only progression when dungeon is in location pool
    "Raw Bird":                         PhoaItemData(93,    2,  IC.filler),
    "Golden Egg":                       PhoaItemData(95,    1,  IC.filler),
    "Lunar Frog":                       PhoaItemData(99,    1,  IC.filler),
    "Lunar Vase":                       PhoaItemData(100,   1,  IC.filler),
    "Dandelion":                        PhoaItemData(101,   5,  IC.filler),
    "Panselo Potato":                   PhoaItemData(102,   4,  IC.filler),
    "Moon Kelp":                        PhoaItemData(104,   20,  IC.filler),
    "Prickle Fruit":                    PhoaItemData(106,   7,  IC.filler),
    "Stink Root":                       PhoaItemData(107,   1,  IC.filler),
    "Ouro Guard Key":                   PhoaItemData(108,   5,  IC.progression),
    "Rubber Ducky":                     PhoaItemData(109,   2,  IC.filler),
    "Ouroboros Proof":                  PhoaItemData(111,   3,  IC.progression),
    "Mystery Meat":                     PhoaItemData(112,   44, IC.filler),
    "Blue Golem Medallion":             PhoaItemData(115,   4,  IC.progression),  # Only progression when dungeon is in location pool
    "Red Golem Medallion":              PhoaItemData(116,   4,  IC.progression),  # Only progression when dungeon is in location pool
    "Calory Slush":                     PhoaItemData(118,   2,  IC.filler),
    "Keycard C":                        PhoaItemData(119,   5,  IC.progression),  # Only progression when dungeon is in location pool
    "Keycard B":                        PhoaItemData(120,   5,  IC.progression),  # Only progression when dungeon is in location pool
    "Keycard A":                        PhoaItemData(121,   5,  IC.progression),  # Only progression when dungeon is in location pool
    "Lisa's ID Card":                   PhoaItemData(122,   1,  IC.progression),
    "Bottle of Wine":                   PhoaItemData(123,   1,  IC.progression),
    "Song of Ouroboros":                PhoaItemData(124,   1,  IC.progression),
    "GEO Song":                         PhoaItemData(125,   1,  IC.useful),
    "Royal Hymn":                       PhoaItemData(126,   1,  IC.progression),
    "Prelude of Panselo":               PhoaItemData(127,   1,  IC.useful),
    "Baroque of Battle":                PhoaItemData(129,   1,  IC.useful),
    "Lullaby of Ava":                   PhoaItemData(128,   1,  IC.useful),
    "Cosette Cannoli":                  PhoaItemData(138,   1,  IC.filler),
    "Perro":                            PhoaItemData(139,   3,  IC.filler),
    "GEO Ticket":                       PhoaItemData(140,   10, IC.filler),
    "Lunar Compass":                    PhoaItemData(144,   1,  IC.filler),
    "Antique Pin":                      PhoaItemData(141,   2,  IC.filler),
    "Ouroboros Scroll":                 PhoaItemData(143,   6,  IC.filler),
    "Lunar Drake":                      PhoaItemData(145,   1,  IC.filler),
    "Spicy Noodles":                    PhoaItemData(152,   1,  IC.filler),
    "Blue Lobster Special":             PhoaItemData(153,   1,  IC.filler),
    "Lunar Crown":                      PhoaItemData(155,   1,  IC.filler),
    "Lunar Trident":                    PhoaItemData(156,   1,  IC.filler),
    "Lunar Comb":                       PhoaItemData(157,   1,  IC.filler),
    "Lunar Medal":                      PhoaItemData(158,   1,  IC.filler),
    "Lunar Watch":                      PhoaItemData(159,   1,  IC.filler),
    "Lunar Key":                        PhoaItemData(160,   1,  IC.filler),
    "Strange Urn":                      PhoaItemData(161,   1,  IC.filler),
    "Tailoring Voucher":                PhoaItemData(164,   2,  IC.filler),
    "Moon Crystal":                     PhoaItemData(165,   1,  IC.filler),
    "Mysterious Golem Head":            PhoaItemData(166,   1,  IC.filler),
    "House Soup":                       PhoaItemData(167,   2,  IC.filler),
    "Puff Pastry":                      PhoaItemData(169,   1,  IC.filler),
    "Macaron":                          PhoaItemData(171,   2,  IC.filler),
    "Saffron Milk":                     PhoaItemData(177,   4,  IC.filler),
    "Vala Bean":                        PhoaItemData(178,   1,  IC.filler),
    "Falafel":                          PhoaItemData(179,   1,  IC.filler),
    "Desert Squash":                    PhoaItemData(180,   1,  IC.filler),
    "Cooked Squash":                    PhoaItemData(181,   1,  IC.filler),
    "Dragon's Scale":                   PhoaItemData(185,   1,  IC.filler),
    # "Elixir":                           PhoaItemData(187,   1,  IC.useful),
    "Honey Bun":                        PhoaItemData(205,   3,  IC.filler),
    "Grape Juice":                      PhoaItemData(206,   2,  IC.filler),
    "Spell of Rejuvenation":            PhoaItemData(216,   1,  IC.useful),
    "Anuri Pearlstone Necklace":        PhoaItemData(217,   1,  IC.progression),  # Only progression when dungeon is in location pool
    "Ouro Guard Keyring":               PhoaItemData(218,   1,  IC.progression),  # Only progression when dungeon is in location pool
    "Big Blue Golem Medallion":         PhoaItemData(219,   1,  IC.progression),  # Only progression when dungeon is in location pool
    "Big Red Golem Medallion":          PhoaItemData(220,   1,  IC.progression),  # Only progression when dungeon is in location pool
    "Moonstone Bundle":                 PhoaItemData(221,   7,  IC.progression),  # 10
    "Panselo Franway Teleporter":       PhoaItemData(222,   1,  IC.filler),
    "Atai Franway Teleporter":          PhoaItemData(223,   1,  IC.filler),
    "Cosette Franway Teleporter":       PhoaItemData(224,   1,  IC.filler),
    "Master Keycard C":                 PhoaItemData(225,   1,  IC.progression),  # Only progression when dungeon is in location pool
    "Master Keycard B":                 PhoaItemData(226,   1,  IC.progression),  # Only progression when dungeon is in location pool
    "Master Keycard A":                 PhoaItemData(227,   1,  IC.progression),  # Only progression when dungeon is in location pool
    "Progressive Prelude of Panselo":   PhoaItemData(292,   2,  IC.useful),
    "Progressive Bat":                  PhoaItemData(293,   2,  IC.useful),
    "Progressive Slingshot":            PhoaItemData(294,   2,  IC.progression),
    "Progressive Bombs":                PhoaItemData(295,   2,  IC.progression),
    "Progressive Crank Lamp":           PhoaItemData(296,   2,  IC.progression),  # Ignore light requirement option?
    "Progressive Spear":                PhoaItemData(297,   2,  IC.progression),
    "Progressive Crossbow":             PhoaItemData(298,   2,  IC.progression),
    "Progressive Fishing Rod":          PhoaItemData(299,   2,  IC.useful),
    "1 Rin":                            PhoaItemData(301,   4,  IC.filler),
    "5 Rin":                            PhoaItemData(305,   2,  IC.filler),
    "9 Rin":                            PhoaItemData(309,   1,  IC.filler),
    "10 Rin":                           PhoaItemData(310,   1,  IC.filler),
    "15 Rin":                           PhoaItemData(315,   3,  IC.filler),
    "20 Rin":                           PhoaItemData(320,   16,  IC.filler),
    "25 Rin":                           PhoaItemData(325,   8,  IC.filler),
    "30 Rin":                           PhoaItemData(330,   13, IC.filler),
    "35 Rin":                           PhoaItemData(335,   15, IC.filler),
    "40 Rin":                           PhoaItemData(340,   17,  IC.filler),
    "45 Rin":                           PhoaItemData(345,   2,  IC.filler),
    "50 Rin":                           PhoaItemData(350,   8,  IC.filler),
    "60 Rin":                           PhoaItemData(360,   1,  IC.filler),
    "75 Rin":                           PhoaItemData(375,   1,  IC.filler),
    "100 Rin":                          PhoaItemData(400,   1,  IC.filler),
}
# @formatter:on

upgrade_groups = [
    ("upgradable_bats", "Progressive Bat", ["Wooden Bat", "Composite Bat"]),
    ("upgradable_tools", "Progressive Slingshot", ["Slingshot", "Treble Shot"]),
    ("upgradable_tools", "Progressive Bombs", ["Bombs", "Remote Bombs"]),
    ("upgradable_tools", "Progressive Crank Lamp", ["Crank Lamp", "Neutron Lamp"]),
    ("upgradable_tools", "Progressive Crossbow", ["Civilian Crossbow", "Double Crossbow"]),
    ("upgradable_tools", "Progressive Fishing Rod", ["Fishing Rod", "Serpent Rod"]),
    ("upgradable_spear", "Progressive Spear", ["Sonic Spear", "Spear Bomb"]),
    ("upgradable_prelude", "Progressive Prelude of Panselo", ["Prelude of Panselo", "Spell of Rejuvenation"]),
]

dungeon_item_setting_groups = [
    DungeonItemSettingGroup("anuri_pearlstone_shuffle", "bundle_anuri_pearlstones", "Anuri Temple",
                            "Anuri Pearlstone", "Anuri Pearlstone Necklace"),
    DungeonItemSettingGroup("ouro_guard_key_shuffle", "bundle_ouro_guard_keys", "Ouroboros Hideout",
                            "Ouro Guard Key", "Ouro Guard Keyring"),
    DungeonItemSettingGroup("golem_medallion_shuffle", "bundle_golem_medallions", "Thomas's Lab",
                            "Blue Golem Medallion", "Big Blue Golem Medallion"),
    DungeonItemSettingGroup("golem_medallion_shuffle", "bundle_golem_medallions", "Thomas's Lab",
                            "Red Golem Medallion", "Big Red Golem Medallion"),
    DungeonItemSettingGroup("keycard_shuffle", "bundle_keycards", "Castle Dungeon", "Keycard C", "Master Keycard C"),
    DungeonItemSettingGroup("keycard_shuffle", "bundle_keycards", "Castle Dungeon", "Keycard B", "Master Keycard B"),
    DungeonItemSettingGroup("keycard_shuffle", "bundle_keycards", "Castle Dungeon", "Keycard A", "Master Keycard A"),
]

item_inclusion_priority: list[str] = \
    ["Progressive Bat", "Composite Bat", "Steel Bat", "Night Star", "Progressive Fishing Rod", "Serpent Rod",
     "Fishing Rod", "Progressive Prelude of Panselo", "Prelude of Panselo", "Spell of Rejuvenation",
     "Baroque of Battle", "Lullaby of Ava", "GEO Song", "Sky Vest", "Jade Hauberk", "GEO Jacket", "Concentrate",
     "Troll's Guard", "Tusk Strike", "Lucky Earrings", "Antique Cast Iron", "Energy Gem", "Heart Ruby",
     "Dragon's Scale", "100 Rin", "75 Rin", "60 Rin", "50 Rin", "45 Rin", "40 Rin", "35 Rin", "30 Rin", "25 Rin",
     "20 Rin", "15 Rin", "Golden Egg", "Calory Slush", "Honey Brew", "Grape Juice", "Spicy Noodles", "Curry Bento",
     "Blue Lobster Special", "Honey Drop", "Rubber Ducky", "Stink Root", "House Soup", "Fish Skewer", "Grape Cake",
     "Deli Sandwich", "Pumpkin Muffin", "Potato Lunch", "Puff Pastry", "Honey Bun", "Cooked Toad Leg", "Saffron Milk",
     "Milk", "Cheese", "Canned Beans", "Pooki Jerky", "Cosette Cannoli", "Panselo Potato", "Cooked Drake Tail",
     "Mystery Meat", "Macaron", "Chocolate", "Falafel", "Desert Squash", "Cooked Squash", "Cooked Knife Krill",
     "Sushi", "Big Raw Meat", "Raw Meat", "Raw Bird", "Drake Tail", "Gourmet Fish Fillet", "Prime Fish Fillet",
     "Fruit Jam", "Vala Bean", "Berry Fruit", "Perro Egg", "Nectear", "Prickle Fruit", "Moon Kelp", "Doki Herb",
     "Lune Fruit", "Dandelion", "10 Rin", "9 Rin", "5 Rin", "1 Rin", "Strange Urn", "Lunar Frog", "Lunar Vase",
     "Lunar Drake", "Lunar Compass", "Lunar Medal", "Lunar Trident", "Lunar Goblet", "Lunar Egg", "Lunar Key",
     "Lunar Comb", "Lunar Watch", "Lunar Crown", "Moonstone", "Moonstone Bundle", "Ouroboros Scroll", "GEO Ticket",
     "Antique Pin", "Turtle", "Perro", "Tailoring Voucher", "Moon Crystal", "Mysterious Golem Head"]


def get_item_pool(world: "PhoaWorld", locations: dict[str, PhoaLocationData]) -> tuple[list[str], list[str]]:
    local_item_table = dict(item_table)

    # Determine item classifications based on settings
    local_item_table = filter_items(local_item_table, world)

    # Remove events from locations
    locations: dict[str, PhoaLocationData] = \
        {key: location for key, location in locations.items() if location.vanillaItem}
    location_count = len(locations)

    # Initialize item pools based on classifications
    progression_items: list[str] = []
    useful_items: list[str] = []

    for item_name, item_data in local_item_table.items():
        if item_data.type == IC.progression or item_name in world.progression_item_classifications_overrides:
            progression_items.extend([item_name] * item_data.amount)
        elif item_data.type == IC.useful:
            useful_items.extend([item_name] * item_data.amount)

    # Remove progression and useful items from the items_from_locations
    replacement_map = build_replacement_map(world.options)
    items_from_locations: list[str] = [
        replacement_map.get(location.vanillaItem, location.vanillaItem)
        for location in locations.values()
    ]

    items_from_locations = [item for item in items_from_locations if item not in set(progression_items)]
    items_from_locations = [item for item in items_from_locations if item not in set(useful_items)]

    # Filter out the Wooden Bat or a Progressive Bat, from either the progression or useful items,
    # and add it to precollected items if starting with one
    precollected_items: list[str] = []
    if world.options.start_with_wooden_bat:
        for items in (progression_items, useful_items):
            for item in items:
                if item in ["Wooden Bat", "Progressive Bat"]:
                    items.remove(item)
                    precollected_items.append("Wooden Bat")
                    break

    # Check whether enough locations are available to place all progressive items
    if len(progression_items) > location_count:
        raise OptionError(
            f"Not enough progress locations({str(location_count)}) "
            f"to place all progressive items({str(len(progression_items))})"
        )

    # Sort useful and filler items by importance
    def sort_by_priority(items, priority_list: list[str]) -> list[str]:
        priority_map = {item: i for i, item in enumerate(priority_list)}
        default_priority = len(priority_list)
        return sorted(items, key=lambda x: priority_map.get(x, default_priority))

    useful_items = sort_by_priority(useful_items, item_inclusion_priority)
    items_from_locations = sort_by_priority(items_from_locations, item_inclusion_priority)

    # Construct the item pool
    item_pool = progression_items.copy()

    remaining_slots = location_count - len(item_pool)

    item_pool.extend(useful_items[:remaining_slots])
    remaining_slots = location_count - len(item_pool)

    item_pool.extend(items_from_locations[:remaining_slots])
    remaining_slots = location_count - len(item_pool)

    item_pool.extend(world.get_filler_item_name() for _ in range(remaining_slots))

    return item_pool, precollected_items


def filter_items(items, world: "PhoaWorld") -> dict[str, PhoaItemData]:
    for option, upgradable, bases in upgrade_groups:
        if getattr(world.options, option):
            for base in bases:
                items.pop(base, None)
            continue
        items.pop(upgradable, None)

    for dungeon_item_setting_group in dungeon_item_setting_groups:
        if getattr(world.options, dungeon_item_setting_group.bundle_option):
            items.pop(dungeon_item_setting_group.dungeon_item, None)
            continue
        items.pop(dungeon_item_setting_group.dungeon_item_bundle, None)

    items.pop("Moonstone" if world.options.bundle_moonstones else "Moonstone Bundle", None)

    removal_map = [
        (not world.options.enable_heart_ruby_locations
         and not world.options.keep_excluded_status_upgrades_in_item_pool,
         ["Heart Ruby"]),
        (not world.options.enable_energy_gem_locations
         and not world.options.keep_excluded_status_upgrades_in_item_pool,
         ["Energy Gem"]),
        (not world.options.enable_moonstone_locations
         and not world.options.keep_excluded_status_upgrades_in_item_pool,
         ["Moonstone"]),
    ]

    for condition, names in removal_map:
        if condition:
            for name in names:
                if name in world.progression_item_classifications_overrides:
                    raise OptionError(
                        "KeepExcludedStatusUpgradesInItemPool Error: "
                        "Items excluded from the item pool are progression items for enabled locations. "
                        "Consider disabling these locations or keeping status upgrades in the item pool."
                    )
                items.pop(name, None)

    return items


def build_replacement_map(options: PhoaOptions) -> dict[str, str]:
    mapping = {}

    for option, upgradable, bases in upgrade_groups:
        if getattr(options, option):
            for base in bases:
                mapping[base] = upgradable

    for dungeon_item_setting_group in dungeon_item_setting_groups:
        if getattr(options, dungeon_item_setting_group.bundle_option):
            mapping[dungeon_item_setting_group.dungeon_item] = dungeon_item_setting_group.dungeon_item_bundle

    return mapping


def filter_dungeon_items(world: "PhoaWorld", location_data: dict[str, PhoaLocationData],
                         dungeon_item_info: DungeonItemSettingGroup,
                         item_pool_strings: list[str]):
    dungeon_item_name = \
        dungeon_item_info.dungeon_item_bundle \
            if getattr(world.options, dungeon_item_info.bundle_option) \
            else dungeon_item_info.dungeon_item

    dungeon_locations = []
    for location_name in location_data.keys():
        if location_name.startswith(dungeon_item_info.dungeon_name):
            dungeon_locations.append(location_name)

    world.own_dungeon_locations[dungeon_item_info.dungeon_name] = dungeon_locations

    # For vanilla placements
    if (getattr(world.options, dungeon_item_info.shuffle_option) ==
            getattr(world.options, dungeon_item_info.shuffle_option).option_vanilla):
        while dungeon_item_name in item_pool_strings:
            item_pool_strings.remove(dungeon_item_name)

        for location_name in dungeon_locations:
            if location_data[location_name].vanillaItem == dungeon_item_info.dungeon_item:
                location_to_place = world.multiworld.get_location(location_name, world.player)
                location_to_place.place_locked_item(world.create_item(dungeon_item_name))
                if getattr(world.options, dungeon_item_info.bundle_option).value:
                    break

    # Within own dungeon
    elif (getattr(world.options, dungeon_item_info.shuffle_option) ==
          getattr(world.options, dungeon_item_info.shuffle_option).option_own_dungeon):
        world.own_dungeon_keys.setdefault(dungeon_item_info.dungeon_name, [])
        while dungeon_item_name in item_pool_strings:
            item_pool_strings.remove(dungeon_item_name)
            world.own_dungeon_keys[dungeon_item_info.dungeon_name].append(world.create_item(dungeon_item_name))


def fill_dungeon_items_in_own_dungeon(world: "PhoaWorld", dungeon_item_info: DungeonItemSettingGroup) -> None:
    if (getattr(world.options, dungeon_item_info.shuffle_option) !=
            getattr(world.options, dungeon_item_info.shuffle_option).option_own_dungeon):
        return

    dungeon_items = world.own_dungeon_keys[dungeon_item_info.dungeon_name]

    locations = []
    for location_name in world.own_dungeon_locations[dungeon_item_info.dungeon_name]:
        location = world.multiworld.get_location(location_name, world.player)
        if location.item is None:
            locations.append(location)

    if len(dungeon_items) > len(locations):
        raise Exception(
            f"'{dungeon_item_info.dungeon_name}' has {len(dungeon_items)} dungeon items to place,"
            f"but only {len(locations)} available locations."
        )

    # This state pretends to have all items minus the dungeon items
    state = world.multiworld.get_all_state()
    for dungeon_item in dungeon_items:
        state.remove(dungeon_item)

    world.multiworld.random.shuffle(locations)
    fill_restrictive(world.multiworld, state, locations, dungeon_items)
