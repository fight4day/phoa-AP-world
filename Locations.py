from enum import Flag, auto
from typing import Dict, NamedTuple, Optional, Callable

from BaseClasses import Location, CollectionState
from worlds.phoa import PhoaOptions
from worlds.phoa.LogicExtensions import PhoaLogic


class PhoaFlag(Flag):
    DEFAULT = auto()
    MAINQUEST = auto()
    HEARTRUBY = auto()
    ENERGYGEM = auto()
    MOONSTONE = auto()
    DUNGEONITEM = auto()
    LUNARARTIFACT = auto()
    FISHINGSPOT = auto()
    NPCGIFTS = auto()
    PLANTO = auto()
    MISC = auto()
    SHOPSANITY = auto()
    SMALLANIMALS = auto()
    RINCHESTS = auto()
    RINCONTAINERS = auto()
    GEOCHALLENGE = auto()
    BREAKABLE = auto()
    SIDEQUEST = auto()
    FREESTANDING = auto()
    MINIGAMES = auto()
    TRAPCHEST = auto()
    OUROBOROS = auto()
    MOONSTONE_SHOP = auto()
    PERRO = auto()
    VAULT = auto()


class PhoaLocation(Location):
    game: str = "Phoenotopia: Awakening"


class PhoaLocationData(NamedTuple):
    region: str
    address: Optional[int]
    rule: Optional[Callable[[CollectionState], bool]] = None
    flags: PhoaFlag | list[PhoaFlag] = PhoaFlag.DEFAULT
    vanillaItem: str = ""


def get_location_data(player: Optional[int], options: Optional[PhoaOptions]) -> Dict[str, PhoaLocationData]:
    logic = PhoaLogic(player)

    locations: Dict[str, PhoaLocationData] = {
        "Panselo Village - Watchtower (West) - Chest": PhoaLocationData(
            region="panselo_village",
            address=7676061,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="35 Rin",
        ),
        "Panselo Village - Watchtower (West) - Hidden in box": PhoaLocationData(
            region="panselo_village",
            address=7676031,
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Cheese",
        ),
        "Panselo Village - Watchtower (West) - Lizard": PhoaLocationData(
            region="panselo_village",
            address=7676041,
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Panselo Village - Free Gift from Panselo Shop Keeper Tao": PhoaLocationData(
            region="panselo_village",
            address=7676070,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Fruit Jam",
        ),
        "Panselo Village - Panselo Shop Item 1": PhoaLocationData(
            region="panselo_village",
            address=7676072,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Perro Egg",
        ),
        "Panselo Village - Panselo Shop Item 2": PhoaLocationData(
            region="panselo_village",
            address=7676073,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Milk",
        ),
        "Panselo Village - Panselo Shop Item 3": PhoaLocationData(
            region="panselo_village",
            address=7676074,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Panselo Potato",
        ),
        "Panselo Village - Panselo Shop Box 1 after abduction": PhoaLocationData(
            region="panselo_village",
            address=7676084,
            rule=lambda state: state.has("Slargummy boss defeated", player),
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Panselo Potato",
        ),
        "Panselo Village - Panselo Shop Box 2 after abduction": PhoaLocationData(
            region="panselo_village",
            address=7676085,
            rule=lambda state: state.has("Slargummy boss defeated", player),
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Perro Egg",
        ),
        "Panselo Village - Panselo Shop Box 3 after abduction": PhoaLocationData(
            region="panselo_village",
            address=7676086,
            rule=lambda state: state.has("Slargummy boss defeated", player),
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Fruit Jam",
        ),
        "Panselo Village - Panselo Shop Box 4 after abduction": PhoaLocationData(
            region="panselo_village",
            address=7676087,
            rule=lambda state: state.has("Slargummy boss defeated", player),
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Milk",
        ),
        "Panselo Village - Panselo Shop Box 5 after abduction": PhoaLocationData(
            region="panselo_village",
            address=7676088,
            rule=lambda state: state.has("Slargummy boss defeated", player),
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Panselo Potato",
        ),
        "Panselo Village - Dojo high up punchbag": PhoaLocationData(
            region="panselo_village",
            address=7676082,
            rule=lambda state: logic.can_deal_damage(state, exclude_lamp=True),
            flags=PhoaFlag.RINCONTAINERS,
            vanillaItem="20 Rin",
        ),
        "Panselo Village - Play Prelude of Panselo": PhoaLocationData(
            region="panselo_village",
            address=7676089,
            rule=lambda state: logic.has_music_instrument(state),
            flags=PhoaFlag.SIDEQUEST,  # Main
            vanillaItem="Prelude of Panselo",
        ),
        "Panselo Village - Inside coop": PhoaLocationData(
            region="panselo_village",
            address=7676030,
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Perro Egg",
        ),
        "Panselo Village - Orphanage roof": PhoaLocationData(
            region="panselo_village",
            address=7676028,
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Dandelion",
        ),
        "Panselo Village - On table in girl's room": PhoaLocationData(
            region="panselo_village",
            address=7676032,
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Berry Fruit",
        ),
        "Panselo Village - Pot in boys Room": PhoaLocationData(
            region="panselo_village",
            address=7676058,
            flags=PhoaFlag.RINCONTAINERS,
            vanillaItem="5 Rin",
        ),
        "Panselo Village - Box at right side of orphanage hall": PhoaLocationData(
            region="panselo_village",
            address=7676059,
            flags=PhoaFlag.RINCONTAINERS,
            vanillaItem="9 Rin",
        ),
        "Panselo Village - Orphanage attic chest": PhoaLocationData(
            region="panselo_village",
            address=7676060,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="35 Rin",
        ),
        "Panselo Village - Nana's Pumpkin Muffin": PhoaLocationData(
            region="panselo_village",
            address=7676068,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Pumpkin Muffin",
        ),
        "Panselo Village - Yesterday's lunch from Kitt": PhoaLocationData(
            region="panselo_village",
            address=7676077,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Cooked Toad Leg",
        ),
        "Panselo Village - Kitt's money for the milk": PhoaLocationData(
            region="panselo_village",
            address=7676078,
            flags=PhoaFlag.SIDEQUEST,  # Obscure
            vanillaItem="20 Rin",
        ),
        "Panselo Village - Amanda's gift lunch": PhoaLocationData(
            region="panselo_village",
            address=7676090,
            rule=lambda state: state.has("Slargummy boss defeated", player),
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Potato Lunch",
        ),
        "Panselo Village - Warehouse Chest": PhoaLocationData(
            region="panselo_village",
            address=7676062,
            rule=lambda state: logic.can_break_big_object_with_tools(state),
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="25 Rin",
        ),
        "Panselo Village - Warehouse Free standing item": PhoaLocationData(
            region="panselo_village",
            address=7676080,
            flags=PhoaFlag.MAINQUEST,
            vanillaItem="Wooden Bat",
        ),
        "Panselo Village - Jon's Potato": PhoaLocationData(
            region="panselo_village",
            address=7676069,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Panselo Potato",
        ),
        "Panselo Village - On roof next to Stan": PhoaLocationData(
            region="panselo_village",
            address=7676029,
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Dandelion",
        ),
        "Panselo Village - Rutea's room": PhoaLocationData(
            region="panselo_village_rutea's_lab",
            address=7676001,
            flags=PhoaFlag.HEARTRUBY,
            vanillaItem="Heart Ruby",
        ),
        "Panselo Village - Watchtower (East) item up top": PhoaLocationData(
            region="panselo_village",
            address=7676000,
            rule=lambda state: logic.can_break_big_object_with_tools(state, exclude_spear=True),
            flags=PhoaFlag.HEARTRUBY,
            vanillaItem="Heart Ruby",
        ),
        "Panselo Village - Watchtower (East) trap chest": PhoaLocationData(
            region="panselo_village",
            address=7676187,
            flags=PhoaFlag.TRAPCHEST,
            vanillaItem="1 Rin",
        ),
        "Panselo Region - End of secret fishing spot": PhoaLocationData(
            region="panselo_region",
            address=7676002,
            flags=PhoaFlag.ENERGYGEM,
            vanillaItem="Energy Gem",
        ),
        "Panselo Region - Franway roof": PhoaLocationData(
            region="panselo_region",
            address=7676034,
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Dandelion",
        ),
        "Panselo Region - GEO house roof": PhoaLocationData(
            region="panselo_region",
            address=7676033,
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Dandelion",
        ),
        "Panselo Region - GEO house reward": PhoaLocationData(
            region="panselo_region",
            address=7676083,
            flags=PhoaFlag.GEOCHALLENGE,
            rule=lambda state: logic.has_music_instrument(state)
                               and state.has("GEO Song", player),
            vanillaItem="GEO Ticket",
        ),
        "Panselo Region - Overworld encounter near Sunflower Road": PhoaLocationData(
            region="panselo_region",
            address=7676005,
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Panselo Region - Underneath boulder north of Panselo": PhoaLocationData(
            region="panselo_region",
            address=7676004,
            rule=lambda state: logic.has_bombs(state) or logic.can_use_spear_bomb(state),
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Panselo Region - Northeastern treetops right stone pot": PhoaLocationData(
            region="panselo_region",
            address=7676003,
            rule=lambda state: logic.can_hit_switch_from_a_distance(state)
                               or state.has("Rocket Boots", player),
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Panselo Region - Northeastern treetops left stone pot": PhoaLocationData(
            region="panselo_region",
            address=7676081,
            rule=lambda state: logic.can_hit_switch_from_a_distance(state)
                               or state.has("Rocket Boots", player),
            flags=PhoaFlag.RINCONTAINERS,
            vanillaItem="30 Rin",
        ),
        "Doki Forest - Cave guarded by Gummies - First item": PhoaLocationData(
            region="panselo_region",
            address=7676035,
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Doki Herb",
        ),
        "Doki Forest - Cave guarded by Gummies - Second item": PhoaLocationData(
            region="panselo_region",
            address=7676036,
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Doki Herb",
        ),
        "Doki Forest - Cave guarded by Gummies - Third item": PhoaLocationData(
            region="panselo_region",
            address=7676037,
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Doki Herb",
        ),
        "Doki Forest - Cave guarded by Gummies - Lizard": PhoaLocationData(
            region="panselo_region",
            address=7676042,
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Doki Forest - Lizard at climbable roots": PhoaLocationData(
            region="panselo_region",
            address=7676043,
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Doki Forest - Cave blocked by destructable blocks": PhoaLocationData(
            region="panselo_region",
            address=7676006,
            rule=lambda state: logic.has_explosives(state),
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Doki Forest - Chest through crawl space": PhoaLocationData(
            region="panselo_region",
            address=7676063,
            rule=lambda state: logic.can_deal_damage(state, exclude_rocket_boots=True, exclude_lamp=True),
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="35 Rin",
        ),
        "Doki Forest - Lizard in alcove": PhoaLocationData(
            region="panselo_region",
            address=7676044,
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Doki Forest - Campfire cave - First Lizard": PhoaLocationData(
            region="panselo_region",
            address=7676045,
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Doki Forest - Campfire cave - Second Lizard": PhoaLocationData(
            region="panselo_region",
            address=7676046,
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Doki Forest - Campfire cave - Pot high up above statue": PhoaLocationData(
            region="panselo_region",
            address=7676092,
            rule=lambda state: logic.has_sonic_spear(state),
            flags=PhoaFlag.RINCONTAINERS,
            vanillaItem="50 Rin",
        ),
        "Doki Forest - Shelby's gift for lighting the campfire": PhoaLocationData(
            region="panselo_region",
            address=7676076,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Doki Herb",
        ),
        "Doki Forest - Fish underneath Anuri Temple": PhoaLocationData(
            region="panselo_region",
            address=7676007,
            rule=lambda state: logic.has_fishing_rod(state),
            flags=PhoaFlag.FISHINGSPOT,
            vanillaItem="Dragon's Scale",
        ),
        "Doki Forest - High up the mountain left of Anuri Temple entrance": PhoaLocationData(
            region="panselo_region",
            address=7676093,
            rule=lambda state: logic.has_sonic_spear(state)
                               and state.has("Energy Gem", player, 9),  # TODO: 10 without spear trick
            flags=PhoaFlag.RINCONTAINERS,
            vanillaItem="50 Rin",
        ),
        "Doki Forest - Gift from Seth": PhoaLocationData(
            region="panselo_region",
            address=7676071,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Mystery Meat",
        ),
        "Doki Forest - Gift from Alex": PhoaLocationData(
            region="panselo_region",
            address=7676008,
            flags=PhoaFlag.MAINQUEST,
            vanillaItem="Slingshot",
        ),
        "Doki Forest - On Top of Anuri Temple": PhoaLocationData(
            region="panselo_region",
            address=7676079,
            rule=lambda state: logic.has_sonic_spear(state),
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Anuri Temple - Lizard at top of climbable vines at entrance": PhoaLocationData(
            region="anuri_temple(main_entrance)",
            address=7676047,
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Anuri Temple - Skeleton above first gate": PhoaLocationData(
            region="anuri_temple(main_entrance)",
            address=7676009,
            rule=lambda state: logic.can_deal_damage(state),
            flags=PhoaFlag.DUNGEONITEM,
            vanillaItem="Anuri Pearlstone",
        ),
        "Anuri Temple - Lizard behind Bombable Blocks": PhoaLocationData(
            region="anuri_temple(top_floor)",
            address=7676048,
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Anuri Temple - Time the gates through Scaber funnel": PhoaLocationData(
            region="anuri_temple(scaber_switch_maze)",
            address=7676024,
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Anuri Temple - Lizard left of Anuri throne": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676050,
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Anuri Temple - Lizard right of Anuri throne": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676049,
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Anuri Temple - Fight toads in treasure room": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676016,
            rule=lambda state: logic.can_break_big_object_with_tools(state),
            flags=PhoaFlag.LUNARARTIFACT,
            vanillaItem="Lunar Vase",
        ),
        "Anuri Temple - Lizard at the end of treasure room": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676051,
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Anuri Temple - Scabers maze": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676010,
            flags=PhoaFlag.DUNGEONITEM,
            vanillaItem="Anuri Pearlstone",
        ),
        "Anuri Temple - High up pot in Scabers maze": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676066,
            rule=lambda state: logic.has_sonic_spear(state),
            flags=PhoaFlag.RINCONTAINERS,
            vanillaItem="15 Rin",
        ),
        "Anuri Temple - Press the switches with pots and fruits": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676011,
            rule=lambda state: logic.can_hit_switch_from_a_distance(state, True),
            flags=PhoaFlag.DUNGEONITEM,
            vanillaItem="Anuri Pearlstone",
        ),"Anuri Temple - First item in narrow crawlspace in tree with prickle fruit room": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676134,
            rule=lambda state: logic.can_hit_switch_from_a_distance(state, True),
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Doki Herb",
        ),"Anuri Temple - Second item in narrow crawlspace in tree with prickle fruit room": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676135,
            rule=lambda state: logic.can_hit_switch_from_a_distance(state, True),
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Doki Herb",
        ),
        "Anuri Temple - Side entrance room - First Lizard": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676055,
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Anuri Temple - Carry pot across the water steps": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676012,
            flags=PhoaFlag.ENERGYGEM,
            vanillaItem="Energy Gem",
        ),
        "Anuri Temple - Lizard in water steps room": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676054,
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Anuri Temple - Stackable pots room - Hidden item": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676013,
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Anuri Temple - Stackable pots room - Lizard": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676053,
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Anuri Temple - Stackable pots room - Anuri Skeleton": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676065,
            flags=PhoaFlag.RINCONTAINERS,
            vanillaItem="15 Rin",
        ),
        "Anuri Temple - Sprint-jump on timed switches": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676014,
            flags=PhoaFlag.DUNGEONITEM,
            vanillaItem="Anuri Pearlstone",
        ),
        "Anuri Temple - Hit three switches in many pots room": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676019,
            flags=PhoaFlag.DUNGEONITEM,
            vanillaItem="Anuri Pearlstone",
        ),
        "Anuri Temple - Mouse in pot in many pots room": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676091,
            rule=lambda state: logic.can_reasonably_kill_mice(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Anuri Temple - Skeleton at bottom of right elevator room": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676064,
            rule=lambda state: logic.can_deal_damage(state),
            flags=PhoaFlag.RINCONTAINERS,
            vanillaItem="15 Rin",
        ),
        "Anuri Temple - Side entrance room - Second Lizard": PhoaLocationData(
            region="anuri_temple(side_entrance)",
            address=7676056,
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Anuri Temple - Side entrance first item": PhoaLocationData(
            region="anuri_temple(side_entrance)",
            address=7676038,
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Doki Herb",
        ),
        "Anuri Temple - Side entrance second item": PhoaLocationData(
            region="anuri_temple(side_entrance)",
            address=7676039,
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Doki Herb",
        ),
        "Anuri Temple - Moveable bridges room": PhoaLocationData(
            region="anuri_temple(moveable_bridge_area)",
            address=7676017,
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Anuri Temple - Lizard in movable bridge room": PhoaLocationData(
            region="anuri_temple(moveable_bridge_area)",
            address=7676052,
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Anuri Temple - Slingshot the switch with surfacing Toads": PhoaLocationData(
            region="anuri_temple(moveable_bridge_area)",
            address=7676018,
            rule=lambda state: logic.has_slingshot(state),
            flags=PhoaFlag.DUNGEONITEM,
            vanillaItem="Anuri Pearlstone",
        ),
        "Anuri Temple - Tall tower puzzle behind locked door": PhoaLocationData(
            region="anuri_temple(tall_tower_puzzle_room)",
            address=7676015,
            flags=PhoaFlag.HEARTRUBY,
            vanillaItem="Heart Ruby",
        ),
        "Anuri Temple - Tall tower puzzle side item": PhoaLocationData(
            region="anuri_temple(tall_tower_puzzle_room)",
            address=7676040,
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Doki Herb",
        ),
        "Anuri Temple Basement - Hit the switch hidden under breakable tomb": PhoaLocationData(
            region="anuri_temple(basement)",
            address=7676020,
            rule=lambda state: logic.has_explosives(state),
            flags=PhoaFlag.DUNGEONITEM,
            vanillaItem="Anuri Pearlstone",
        ),
        "Anuri Temple Basement - Push metal pot onto switch from above": PhoaLocationData(
            region="anuri_temple(basement)",
            address=7676021,
            flags=PhoaFlag.DUNGEONITEM,
            vanillaItem="Anuri Pearlstone",
        ),
        "Anuri Temple Basement - Within sarcophagus": PhoaLocationData(
            region="anuri_temple(basement)",
            address=7676022,
            rule=lambda state: logic.has_explosives(state),
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Anuri Temple Basement - Defeat the glowing Slargummy": PhoaLocationData(
            region="anuri_temple(basement)",
            address=7676023,
            rule=lambda state: logic.has_light_source(state)
                               and logic.can_reasonably_kill_enemies(state),
            flags=PhoaFlag.DUNGEONITEM,
            vanillaItem="Anuri Pearlstone",
        ),
        "Anuri Temple Basement - Big pot in tomb tunnel": PhoaLocationData(
            region="anuri_temple(basement)",
            address=7676067,
            rule=lambda state: logic.can_break_big_object_with_tools(state),
            flags=PhoaFlag.RINCONTAINERS,
            vanillaItem="20 Rin",
        ),
        "Anuri Temple - Fishing Spot After Slargummy": PhoaLocationData(
            region="anuri_temple(pond)",
            address=7676025,
            rule=lambda state: logic.has_fishing_rod(state),
            flags=PhoaFlag.FISHINGSPOT,
            vanillaItem="Moonstone",
        ),
        "Anuri Temple - Bart's head crater": PhoaLocationData(
            region="anuri_temple(pond)",
            address=7676075,
            flags=PhoaFlag.MAINQUEST,
            vanillaItem="Mysterious Golem Head",
        ),
        "Anuri Temple - Use slingshot to hit the switches below": PhoaLocationData(
            region="anuri_temple(post_pond)",
            address=7676026,
            rule=lambda state: logic.has_slingshot(state)
                               or logic.has_sonic_spear(state),
            flags=PhoaFlag.DUNGEONITEM,
            vanillaItem="Anuri Pearlstone",
        ),
        "Anuri Temple - Lizard at treasure room before century toad": PhoaLocationData(
            region="anuri_temple(post_pond)",
            address=7676057,
            rule=lambda state: logic.can_hit_switch_from_a_distance(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Anuri Temple - Dive down in long vertical room": PhoaLocationData(
            region="anuri_temple(dive_room)",
            address=7676027,
            rule=lambda state: state.has("Life Saver", player),
            flags=PhoaFlag.LUNARARTIFACT,
            vanillaItem="Lunar Frog",
        ),
        "Anuri Temple - Strange Urn": PhoaLocationData(
            region="anuri_temple(urn_room)",
            address=7676194,
            flags=PhoaFlag.MISC,
            vanillaItem="Strange Urn",
        ),
        "Sunflower Road - East - First item on sunflower leaf": PhoaLocationData(
            region="panselo_region",
            address=7676094,
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Nectear",
        ),
        "Sunflower Road - East - Second item on sunflower leaf": PhoaLocationData(
            region="panselo_region",
            address=7676095,
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Sunflower Road - East - Third item on sunflower leaf": PhoaLocationData(
            region="panselo_region",
            address=7676096,
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Nectear",
        ),
        "Sunflower Road - East - First item hanging from sunflower stem": PhoaLocationData(
            region="panselo_region",
            address=7676097,
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Nectear",
        ),
        "Sunflower Road - East - Fourth item on sunflower leaf": PhoaLocationData(
            region="panselo_region",
            address=7676098,
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Nectear",
        ),
        "Sunflower Road - East - Chest on sunflower leaf": PhoaLocationData(
            region="panselo_region",
            address=7676099,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="35 Rin",
        ),
        "Sunflower Road - East - Second item hanging from sunflower stem": PhoaLocationData(
            region="panselo_region",
            address=7676100,
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Nectear",
        ),
        "Sunflower Road - East - Fifth item on sunflower leaf": PhoaLocationData(
            region="panselo_region",
            address=7676101,
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Nectear",
        ),
        "Sunflower Road - East - Item high up on sunflower leaf": PhoaLocationData(
            region="panselo_region",
            address=7676102,
            rule=lambda state: state.has("Rocket Boots", player),
            flags=PhoaFlag.HEARTRUBY,
            vanillaItem="Heart Ruby",
        ),
        "Sunflower Road - Honey Bee Lab and Inn - Item on sunflower leaf on the right": PhoaLocationData(
            region="panselo_region",
            address=7676103,
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Nectear",
        ),
        "Sunflower Road - Honey Bee Lab and Inn - Item on sunflower leaf on the left": PhoaLocationData(
            region="panselo_region",
            address=7676104,
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Nectear",
        ),
        "Sunflower Road - Honey Bee Lab and Inn - Mr. Planto's reward": PhoaLocationData(
            region="panselo_region",
            address=7676105,
            flags=PhoaFlag.PLANTO,
            vanillaItem="20 Rin",
        ),
        "Sunflower Road - Honey Bee Lab and Inn - Shop Item 1": PhoaLocationData(
            region="panselo_region",
            address=7676106,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Honey Bun",
        ),
        "Sunflower Road - Honey Bee Lab and Inn - Shop Item 2": PhoaLocationData(
            region="panselo_region",
            address=7676107,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Honey Brew",
        ),
        "Sunflower Road - Honey Bee Lab and Inn - Shop Item 3": PhoaLocationData(
            region="panselo_region",
            address=7676108,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Honey Drop",  # 3 of them
        ),
        "Sunflower Road - Honey Bee Lab and Inn - Inside box in shop attic": PhoaLocationData(
            region="panselo_region",
            address=7676109,
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Honey Drop",
        ),
        "Sunflower Road - West - First item hanging from sunflower stem": PhoaLocationData(
            region="panselo_region",
            address=7676110,
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Nectear",
        ),
        "Sunflower Road - West - First item on sunflower leaf": PhoaLocationData(
            region="panselo_region",
            address=7676111,
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Nectear",
        ),
        "Sunflower Road - West - Item on sunflower leaf under bee parkour": PhoaLocationData(
            region="panselo_region",
            address=7676112,
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Sunflower Road - West - Item on sunflower leaf after bee parkour": PhoaLocationData(
            region="panselo_region",
            address=7676113,
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Nectear",
        ),
        "Sunflower Road - West - Item surrounded by bees": PhoaLocationData(
            region="panselo_region",
            address=7676114,
            flags=PhoaFlag.ENERGYGEM,
            vanillaItem="Energy Gem",
        ),
        "Sunflower Road - West - Chest on sunflower leaf": PhoaLocationData(
            region="panselo_region",
            address=7676115,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="35 Rin",
        ),
        "Sunflower Road - West - Second item hanging from sunflower stem": PhoaLocationData(
            region="panselo_region",
            address=7676131,
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Nectear",
        ),
        "Sunflower Road - West - Third item hanging from sunflower stem": PhoaLocationData(
            region="panselo_region",
            address=7676116,
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Nectear",
        ),
        "Panselo Region - Chest in dark cave": PhoaLocationData(
            region="panselo_region",
            address=7676117,
            rule=lambda state: logic.has_light_source(state),
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="50 Rin",
        ),
        "Panselo Region - Fish up turtle in dark cave": PhoaLocationData(
            region="panselo_region",
            address=7676118,
            rule=lambda state: logic.has_fishing_rod(state),
            flags=PhoaFlag.FISHINGSPOT,
            vanillaItem="Turtle",
        ),
        "Panselo Region - Perro in treetops": PhoaLocationData(
            region="panselo_region",
            address=7676132,
            flags=PhoaFlag.PERRO,
            vanillaItem="Perro",
        ),
        "Atelo Bridge - Top left box in east tower": PhoaLocationData(
            region="panselo_region",
            address=7676119,
            rule=lambda state: logic.can_break_big_object_with_tools(state),
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Cheese",
        ),
        "Atelo Bridge - Place boxes to fit into crawlspace ": PhoaLocationData(
            region="panselo_region",
            address=7676120,
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Atelo Bridge - Alcove behind boulders": PhoaLocationData(
            region="panselo_region",
            address=7676121,
            rule=lambda state: (logic.has_explosives(state) and state.has("Life Saver", player))
                               or state.has("Rocket Boots", player),
            flags=PhoaFlag.HEARTRUBY,
            vanillaItem="Heart Ruby",
        ),
        "Atelo Bridge - Blue pot on top of middle tower": PhoaLocationData(
            region="panselo_region",
            address=7676191,
            rule=lambda state: logic.has_sonic_spear(state),
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Atelo Bridge - Lizard in middle tower": PhoaLocationData(
            region="panselo_region",
            address=7676122,
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Atelo Bridge - Small box in middle tower": PhoaLocationData(
            region="panselo_region",
            address=7676123,
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Raw Meat",
        ),
        "Atelo Bridge - Chest in middle tower": PhoaLocationData(
            region="panselo_region",
            address=7676124,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="20 Rin",
        ),
        "Atelo Bridge - GEO reward": PhoaLocationData(
            region="panselo_region",
            address=7676125,
            rule=lambda state: logic.has_music_instrument(state)
                               and state.has("GEO Song", player),
            flags=PhoaFlag.GEOCHALLENGE,
            vanillaItem="GEO Ticket",
        ),
        "Atelo Bridge - Chest on top of big box in alcove": PhoaLocationData(
            region="panselo_region",
            address=7676126,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="30 Rin",
        ),
        "Atelo Bridge - Moonstone deep in the water": PhoaLocationData(
            region="panselo_region",
            address=7676127,
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Atelo Bridge - Middle chest": PhoaLocationData(
            region="panselo_region",
            address=7676128,
            flags=PhoaFlag.TRAPCHEST,
            vanillaItem="1 Rin",
        ),
        "Atelo Bridge - Crawlspace blocked by boulders": PhoaLocationData(
            region="panselo_region",
            address=7676129,
            rule=lambda state: logic.has_explosives(state),
            flags=PhoaFlag.ENERGYGEM,
            vanillaItem="Energy Gem",
        ),
        "Atelo Bridge - Puzzle in west tower": PhoaLocationData(
            region="panselo_region",
            address=7676130,
            rule=lambda state: logic.has_sonic_spear(state)
                               or state.has("Rocket Boots", player),
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Atai Town - Dark tower pot": PhoaLocationData(
            region="atai_town",
            address=7676200,
            rule=lambda state: logic.can_break_big_object_with_tools(state),
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Atai Town - Dark tower chest": PhoaLocationData(
            region="atai_town",
            address=7676201,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="30 Rin",
        ),
        "Atai Town - Prison pot": PhoaLocationData(
            region="atai_town",
            address=7676202,
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Atai Town - Prison chest": PhoaLocationData(
            region="atai_town",
            address=7676203,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="40 Rin",
        ),
        "Atai Town - Bandit prince Zeke's reward": PhoaLocationData(
            region="atai_town",
            address=7676199,
            rule=lambda state: state.has("Bottle of Wine", player),
            flags=PhoaFlag.MAINQUEST,
            vanillaItem="Bandit's Flute",
        ),
        "Atai Town - Bandit prince Zeke's song": PhoaLocationData(
            region="atai_town",
            address=7676198,
            # Songfield is always active so the first rule could be left out
            rule=lambda state: state.can_reach_location("Atai Town - Bandit prince Zeke's reward", player)
                               and logic.has_music_instrument(state),
            flags=PhoaFlag.MAINQUEST,
            vanillaItem="Song of Ouroboros",
        ),
        "Atai Town - Storage room hidden behind carpet": PhoaLocationData(
            region="atai_town",
            address=7676204,
            rule=lambda state: logic.can_break_big_object_with_tools(state),
            flags=PhoaFlag.HEARTRUBY,
            vanillaItem="Heart Ruby",
        ),
        "Atai Town - Vegetable shop item 1": PhoaLocationData(
            region="atai_town",
            address=7676205,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Vala Bean",
        ),
        "Atai Town - Vegetable shop item 2": PhoaLocationData(
            region="atai_town",
            address=7676206,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Desert Squash",
        ),
        "Atai Town - Vegetable shop item 3": PhoaLocationData(
            region="atai_town",
            address=7676207,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Moon Kelp",
        ),
        "Atai Town - Meat shop item 1": PhoaLocationData(
            region="atai_town",
            address=7676208,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Big Raw Meat",
        ),
        "Atai Town - Meat shop item 2": PhoaLocationData(
            region="atai_town",
            address=7676209,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Drake Tail",
        ),
        "Atai Town - Meat shop item 3": PhoaLocationData(
            region="atai_town",
            address=7676210,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Prime Fish Fillet",
        ),
        "Atai Town - Weapon shop item 1": PhoaLocationData(
            region="atai_town",
            address=7676211,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Sky Vest",
        ),
        "Atai Town - Weapon shop item 2": PhoaLocationData(
            region="atai_town",
            address=7676212,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Civillian Crossbow",
        ),
        "Atai Town - Weapon shop item 3": PhoaLocationData(
            region="atai_town",
            address=7676213,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Composite Bat",
        ),
        "Atai Town - Weapon shop item 4": PhoaLocationData(
            region="atai_town",
            address=7676214,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Crank Lamp",
        ),
        "Atai Town - Weapon shop item 5": PhoaLocationData(
            region="atai_town",
            address=7676215,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Fishing Rod",
        ),
        "Atai Town - Weapon shop dropper bottom": PhoaLocationData(
            region="atai_town(weapons_shop_dropper)",
            address=7676216,
            flags=PhoaFlag.HEARTRUBY,
            vanillaItem="Heart Ruby",
        ),
        "Atai Town - Weapon shop dropper pot": PhoaLocationData(
            region="atai_town(weapons_shop_dropper)",
            address=7676217,
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Atai Town - Weapon shop dropper chest": PhoaLocationData(
            region="atai_town(weapons_shop_dropper)",
            address=7676218,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="35 Rin",
        ),
        "Atai Town - Weapon shop balcony chest": PhoaLocationData(
            region="atai_town",
            address=7676219,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="30 Rin",
        ),
        "Atai Town - Daycare hidden in balcony": PhoaLocationData(
            region="atai_town",
            address=7676220,
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Atai Town - Daycare hidden in pot": PhoaLocationData(
            region="atai_town",
            address=7676221,
            rule=lambda state: logic.has_sonic_spear(state),
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Atai Town - Fruit shop item 1": PhoaLocationData(
            region="atai_town",
            address=7676222,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Prickle Fruit",
        ),
        "Atai Town - Fruit shop item 2": PhoaLocationData(
            region="atai_town",
            address=7676223,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Berry Fruit",
        ),
        "Atai Town - Fruit shop quest": PhoaLocationData(
            region="atai_town",
            address=7676224,
            rule=lambda state: state.can_reach_region("panselo_region", player),
            flags=PhoaFlag.MISC,
            vanillaItem="25 Rin",
        ),
        "Atai Town - Tavern shop regular item": PhoaLocationData(
            region="atai_town",
            address=7676225,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Milk",
        ),
        "Atai Town - Tavern shop alcoholic item": PhoaLocationData(
            region="atai_town",
            address=7676226,
            rule=lambda state: state.has("Lisa's ID Card", player),
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Bottle of Wine",
        ),
        "Atai Town - Tavern Gustav's gift for filling the item ring": PhoaLocationData(
            region="atai_town",
            address=7676133,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Pooki Jerky",
        ),
        "Atai Town - Guard residence mouse": PhoaLocationData(
            region="atai_town",
            address=7676227,
            rule=lambda state: logic.can_reasonably_kill_mice(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Atai Town - Bo running challenge": PhoaLocationData(
            region="atai_town",
            address=7676228,
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="30 Rin",
        ),
        "Atai Town - Ouroboros shrine": PhoaLocationData(
            region="atai_town(sewer)",
            address=7676229,
            rule=lambda state: logic.has_music_instrument(state)
                               and state.has("Song of Ouroboros", player),
            flags=PhoaFlag.OUROBOROS,
            vanillaItem="Ouroboros Scroll",
        ),
        "Atai Town - Metro chest": PhoaLocationData(
            region="atai_town(metro)",
            address=7676230,
            rule=lambda state: logic.can_break_big_object_with_tools(state),
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="Ouroboros Scroll",
        ),
        "Atai Town - Metro train car crate": PhoaLocationData(
            region="atai_town(metro)",
            address=7676231,
            rule=lambda state: logic.has_explosives(state),
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Atai Town - Lisa's ID gift": PhoaLocationData(
            region="atai_town",
            address=7676298,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Lisa's ID Card",
        ),
        "Atai Town - Mansion chef gift": PhoaLocationData(
            region="atai_town",
            address=7676232,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Cooked Squash",
        ),
        "Atai Town - Mansion storage pot": PhoaLocationData(
            region="atai_town",
            address=7676233,
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Atai Town - Mansion storage chest": PhoaLocationData(
            region="atai_town",
            address=7676234,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="30 Rin",
        ),
        "Atai Town - Mansion west wing lizard": PhoaLocationData(
            region="atai_town",
            address=7676235,
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Atai Town - West sewer pipe room chest": PhoaLocationData(
            region="atai_town(sewer)",
            address=7676236,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="25 Rin",
        ),
        "Atai Town - West sewer crate": PhoaLocationData(
            region="atai_town(sewer)",
            address=7676237,
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Canned Beans",
        ),
        "Atai Town - West residence balcony pot": PhoaLocationData(
            region="atai_town",
            address=7676238,
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Atai Town - Shooting range item 1": PhoaLocationData(
            region="atai_town",
            address=7676239,
            rule=lambda state: logic.can_hit_switch_from_a_distance(state, exclude_bombs=True),
            flags=PhoaFlag.MINIGAMES,
            vanillaItem="Rubber Ducky",
        ),
        "Atai Town - Shooting range item 2": PhoaLocationData(
            region="atai_town",
            address=7676240,
            rule=lambda state: logic.can_hit_switch_from_a_distance(state, exclude_bombs=True),
            flags=PhoaFlag.MINIGAMES,
            vanillaItem="Heart Ruby",
        ),
        "Atai Town - Shooting range item 3": PhoaLocationData(
            region="atai_town",
            address=7676241,
            rule=lambda state: logic.can_clear_atai_expert_gallery(state),
            flags=PhoaFlag.MINIGAMES,
            vanillaItem="Moonstone",
        ),
        "Atai Town - West residence crate under step up": PhoaLocationData(
            region="atai_town",
            address=7676242,
            flags=PhoaFlag.RINCONTAINERS,
            vanillaItem="30 Rin",
        ),
        "Rhodus Checkpoint - East tower commons crate": PhoaLocationData(
            region="atai_region",
            address=7676243,
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Honey Bun",
        ),
        "Rhodus Checkpoint - East tower lizard": PhoaLocationData(
            region="atai_region",
            address=7676244,
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Rhodus Checkpoint - East tower turret guard": PhoaLocationData(
            region="atai_region",
            address=7676245,
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Rhodus Checkpoint - East shop item 1": PhoaLocationData(
            region="atai_region",
            address=7676246,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Honey Brew",
        ),
        "Rhodus Checkpoint - East shop item 2": PhoaLocationData(
            region="atai_region",
            address=7676247,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Chocolates",
        ),
        "Rhodus Checkpoint - Central shop item 1": PhoaLocationData(
            region="atai_region",
            address=7676248,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Rubber Ducky",
        ),
        "Rhodus Checkpoint - Central shop item 2": PhoaLocationData(
            region="atai_region",
            address=7676249,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Refurbished Crank Lamp",
        ),
        "Rhodus Checkpoint - West shop item 1": PhoaLocationData(
            region="atai_region",
            address=7676250,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Saffron Milk",
        ),
        "Rhodus Checkpoint - West shop item 2": PhoaLocationData(
            region="atai_region",
            address=7676251,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Curry Bento",
        ),
        "Rhodus Checkpoint - Golem gift": PhoaLocationData(
            region="atai_region",
            address=7676252,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Dandelion",
        ),
        "Rhodus Checkpoint - West tower top guard gift": PhoaLocationData(
            region="atai_region",
            address=7676253,
            rule=lambda state: state.has("Rocket Boots", player)
                               and state.has("Energy Gem", player, 9),
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Adar's House - Scorpion": PhoaLocationData(
            region="adars_house",
            address=7676254,
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Adar's House - Adar's basement": PhoaLocationData(
            region="adars_house",
            address=7676197,
            flags=PhoaFlag.MAINQUEST,
            vanillaItem="Bombs",
        ),
        "Adar's House - Chest in cave": PhoaLocationData(
            region="adars_house(cave)",
            address=7676192,
            flags=PhoaFlag.TRAPCHEST,
            vanillaItem="1 Rin",
        ),
        "Adar's House - Cave ledge item": PhoaLocationData(
            region="adars_house(cave_top)",
            address=7676255,
            flags=PhoaFlag.ENERGYGEM,
            vanillaItem="Energy Gem",
        ),
        "Ancient Vault - Printer item 1": PhoaLocationData(
            region="ancient_vault(printer_room)",
            address=7676330,
            flags=PhoaFlag.VAULT,
            vanillaItem="Heart Ruby",
        ),
        "Ancient Vault - Printer item 2": PhoaLocationData(
            region="ancient_vault(printer_room)",
            address=7676331,
            flags=PhoaFlag.VAULT,
            vanillaItem="Energy Gem",
        ),
        "Daetai Bridge - Broken bridge chest": PhoaLocationData(
            region="atai_region",
            address=7676190,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="35 Rin",
        ),
        "Daetai Bridge - Songstone chest": PhoaLocationData(
            region="atai_region",
            address=7676189,
            rule=lambda state: logic.has_music_instrument(state),
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="45 Rin",
        ),
        "Atai Region - Northwest cave chest": PhoaLocationData(
            region="atai_region",
            address=7676256,
            rule=lambda state: logic.has_light_source(state),
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="50 Rin",
        ),
        "Atai Region - Northwest cave top path item": PhoaLocationData(
            region="atai_region",
            address=7676257,
            rule=lambda state: logic.has_light_source(state)
                               and logic.has_explosives(state),
            flags=PhoaFlag.HEARTRUBY,
            vanillaItem="Heart Ruby",
        ),
        "Atai Region - Franway songstone chest": PhoaLocationData(
            region="atai_region",
            address=7676258,
            rule=lambda state: logic.has_music_instrument(state),
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="45 Rin",
        ),
        "Atai Region - Franway fish": PhoaLocationData(
            region="atai_region",
            address=7676259,
            rule=lambda state: logic.has_fishing_rod(state),
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Atai Region - Franway cactus": PhoaLocationData(
            region="atai_region",
            address=7676260,
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Prickle Fruit",
        ),
        "Atai Region - Boar boy quest": PhoaLocationData(
            region="atai_region",
            address=7676261,
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="Tusk Strike",
        ),
        "Atai Region - Oasis guard gift": PhoaLocationData(
            region="atai_region",
            address=7676262,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Saffron Milk",
        ),
        "Atai Region - Oasis Mr. planto quest": PhoaLocationData(
            region="atai_region",
            address=7676263,
            rule=lambda state: logic.has_explosives(state),
            flags=PhoaFlag.PLANTO,
            vanillaItem="20 Rin",
        ),
        "Atai Region - Oasis fish": PhoaLocationData(
            region="atai_region",
            address=7676193,
            rule=lambda state: (logic.has_fishing_rod(state)
                                and state.has("Energy Gem", player, 4))
                               or (logic.has_serpant_rod(state)
                                   and state.has("Energy Gem", player, 2)),
            flags=PhoaFlag.FISHINGSPOT,
            vanillaItem="Energy Gem",
        ),
        "Atai Region - Oasis Ouroboros shrine": PhoaLocationData(
            region="atai_region",
            address=7676264,
            rule=lambda state: logic.has_music_instrument(state)
                               and logic.has_sonic_spear(state)
                               and state.has("Song of Ouroboros", player)
                               and state.has("Life Saver", player),
            flags=PhoaFlag.OUROBOROS,
            vanillaItem="Ouroboros Scroll",
        ),
        "Atai Region - Sand Drifts Access lizard": PhoaLocationData(
            region="atai_region",
            address=7676265,
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Atai Region - Sand Drifts Access glowing rock item": PhoaLocationData(
            region="sand_drifts_region(access_cave)",
            address=7676266,
            rule=lambda state: logic.has_explosives(state),
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Sand Drifts Region - Tower lizard": PhoaLocationData(
            region="sand_drifts_region",
            address=7676267,
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Sand Drifts Region - Tower top": PhoaLocationData(
            region="sand_drifts_region",
            address=7676268,
            flags=PhoaFlag.ENERGYGEM,
            vanillaItem="Energy Gem",
        ),
        "Sand Drifts Region - Tower perro": PhoaLocationData(
            region="sand_drifts_region",
            address=7676269,
            flags=PhoaFlag.PERRO,
            vanillaItem="Perro",
        ),
        "Sand Drifts Region - Tower cactus 1": PhoaLocationData(
            region="sand_drifts_region",
            address=7676270,
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Prickle Fruit",
        ),
        "Sand Drifts Region - Tower cactus 2": PhoaLocationData(
            region="sand_drifts_region",
            address=7676271,
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Prickle Fruit",
        ),
        "Sand Drifts Region - Ouroboros shrine": PhoaLocationData(
            region="sand_drifts_region",
            address=7676272,
            rule=lambda state: logic.has_music_instrument(state)
                               and state.has("Song of Ouroboros", player),
            flags=PhoaFlag.OUROBOROS,
            vanillaItem="Ouroboros Scroll",
        ),
        "Sand Drifts Region - Ancient GEO Dungeon solution 1 item": PhoaLocationData(
            region="sand_drifts_region(ancient_geo_dungeon)",
            address=7676273,
            rule=lambda state: logic.has_light_source(state),
            flags=PhoaFlag.GEOCHALLENGE,
            vanillaItem="Antique Pin",
        ),
        "Sand Drifts Region - Ancient GEO Dungeon solution 2 item": PhoaLocationData(
            region="sand_drifts_region(ancient_geo_dungeon)",
            address=7676274,
            rule=lambda state: logic.has_light_source(state),
            flags=PhoaFlag.HEARTRUBY,
            vanillaItem="Heart Ruby",
        ),
        "Sand Drifts Region - South tree crate": PhoaLocationData(
            region="sand_drifts_region",
            address=7676275,
            flags=PhoaFlag.HEARTRUBY,
            vanillaItem="Heart Ruby",
        ),
        "Sand Drifts Region - Thistle Weed encounter": PhoaLocationData(
            region="sand_drifts_region",
            address=7676196,
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Sand Drifts - Shelter mouse": PhoaLocationData(
            region="sand_drifts",
            address=7676276,
            rule=lambda state: logic.can_reasonably_kill_mice(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Sand Drifts - Pot next to metro entrance": PhoaLocationData(
            region="sand_drifts",
            address=7676291,
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Canned Beans",
        ),
        "Sand Drifts - East tower puzzle item": PhoaLocationData(
            region="sand_drifts",
            address=7676277,
            rule=lambda state: logic.has_bombs(state),
            flags=PhoaFlag.HEARTRUBY,
            vanillaItem="Heart Ruby",
        ),
        "Sand Drifts - Above first ruin entrance chest": PhoaLocationData(
            region="sand_drifts",
            address=7676278,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="25 Rin",
        ),
        "Sand Drifts - First ruin trapped chest": PhoaLocationData(
            region="sand_drifts(chest_trap_room)",
            address=7676279,
            flags=PhoaFlag.TRAPCHEST,
            vanillaItem="1 Rin",
        ),
        "Sand Drifts - First ruin storage crate": PhoaLocationData(
            region="sand_drifts(storage_room)",
            address=7676280,
            flags=PhoaFlag.RINCONTAINERS,
            vanillaItem="25 Rin",
        ),
        "Sand Drifts - First ruin center room scorpion": PhoaLocationData(
            region="sand_drifts",
            address=7676281,
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Sand Drifts - Stealer bird plains floor patch": PhoaLocationData(
            region="sand_drifts",
            address=7676282,
            rule=lambda state: logic.has_explosives(state),
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Sand Drifts - Ouroboros Shrine": PhoaLocationData(
            region="sand_drifts(ouroboros_shrine)",
            address=7676283,
            flags=PhoaFlag.OUROBOROS,
            vanillaItem="Ouroboros Scroll",
        ),
        "Forlorn Ruins - Fountain room chest": PhoaLocationData(
            region="forlorn_ruins(fountain_room)",
            address=7676284,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="35 Rin",
        ),
        "Forlorn Ruins - Fountain room dive item": PhoaLocationData(
            region="forlorn_ruins(fountain_room)",
            address=7676285,
            rule=lambda state: state.has("Life Saver", player)
                               and state.can_reach_region("forlorn_ruins(top_path)", player),
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Forlorn Ruins - Fountain room lizard": PhoaLocationData(
            region="forlorn_ruins(fountain_room)",
            address=7676286,
            rule=lambda state: logic.can_hit_switch_from_a_distance(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Forlorn Ruins - Arrow obstacle course behind locked door": PhoaLocationData(
            region="forlorn_ruins(arrow_obstacle_room)",
            address=7676195,
            flags=PhoaFlag.LUNARARTIFACT,
            vanillaItem="Lunar Compass",
        ),
        "Forlorn Ruins - Bombable wall room pot": PhoaLocationData(
            region="forlorn_ruins(bombable_wall)",
            address=7676287,
            rule=lambda state: logic.can_break_big_object_with_tools(state),
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Forlorn Ruins - Bombable wall room mouse": PhoaLocationData(
            region="forlorn_ruins(bombable_wall)",
            address=7676288,
            rule=lambda state: logic.can_reasonably_kill_mice(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Forlorn Ruins - Dragon Snare room chest": PhoaLocationData(
            region="forlorn_ruins",
            address=7676289,
            rule=lambda state: logic.has_explosives(state),
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="35 Rin",
        ),
        "Forlorn Ruins - Stairwell scorpion": PhoaLocationData(
            region="forlorn_ruins",
            address=7676290,
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Forlorn Ruins - Falafel trap": PhoaLocationData(
            region="forlorn_ruins",
            address=7676292,
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Falafel",
        ),
        "Forlorn Ruins - Drake death room pot": PhoaLocationData(
            region="forlorn_ruins(metal_crates_puzzle_area)",
            address=7676293,
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Canned Beans",
        ),
        "Forlorn Ruins - Ceiling switch room pot": PhoaLocationData(
            region="forlorn_ruins(east)",
            address=7676294,
            rule=lambda state: logic.can_hit_switch_from_a_distance(state),
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Canned Beans",
        ),
        "Forlorn Ruins - Trapped chest": PhoaLocationData(
            region="forlorn_ruins(east)",
            address=7676295,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="25 Rin",
        ),
        "Forlorn Ruins - Dragon Snare puzzle pot": PhoaLocationData(
            region="forlorn_ruins(dragon_snare_puzzle_room)",
            address=7676296,
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Forlorn Ruins - Dragon Snare keydoor chest": PhoaLocationData(
            region="forlorn_ruins(dragon_snare_puzzle_room)",
            address=7676297,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="20 Rin",
        ),
        "Forlorn Ruins - Hideout entrance behind a hidden wall": PhoaLocationData(
            region="forlorn_ruins(east)",
            address=7676299,
            rule=lambda state: logic.has_explosives(state),
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Honey Brew",
        ),
        "Ouroboros Hideout - West entrance behind the save book": PhoaLocationData(
            region="ouroboros_hideout",
            address=7676300,
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Pooki Jerky",
        ),
        "Ouroboros Hideout - Main hideout shuriken guard Item": PhoaLocationData(
            region="ouroboros_hideout",
            address=7676301,
            rule=lambda state: logic.can_deal_damage(state),
            flags=PhoaFlag.DUNGEONITEM,
            vanillaItem="Ouro Guard Key",
        ),
        "Ouroboros Hideout - Songstone treasure room mouse item 1": PhoaLocationData(
            region="ouroboros_hideout",
            address=7676302,
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Ouroboros Hideout - Songstone treasure room mouse item 2": PhoaLocationData(
            region="ouroboros_hideout",
            address=7676303,
            flags=PhoaFlag.DUNGEONITEM,
            vanillaItem="Ouro Guard Key",
        ),
        "Ouroboros Hideout - Songstone treasure room pot": PhoaLocationData(
            region="ouroboros_hideout(treasure_room)",
            address=7676304,
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Ouroboros Hideout - Songstone treasure room crate 1": PhoaLocationData(
            region="ouroboros_hideout(treasure_room)",
            address=7676305,
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Prickle Fruit",
        ),
        "Ouroboros Hideout - Songstone treasure room crate 2": PhoaLocationData(
            region="ouroboros_hideout(treasure_room)",
            address=7676306,
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Pooki Jerky",
        ),
        "Ouroboros Hideout - Songstone treasure room bombable wall chest": PhoaLocationData(
            region="ouroboros_hideout(treasure_room)",
            address=7676307,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="40 Rin",
        ),
        "Ouroboros Hideout - Chest at top of watchtower": PhoaLocationData(
            region="ouroboros_hideout(tower_top)",
            address=7676188,
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Ouroboros Hideout - Melody's gift": PhoaLocationData(
            region="ouroboros_hideout",
            address=7676308,
            flags=PhoaFlag.DUNGEONITEM,
            vanillaItem="Ouro Guard Key",
        ),
        "Ouroboros Hideout - Fountain room underwater": PhoaLocationData(
            region="ouroboros_hideout",
            address=7676309,
            rule=lambda state: state.has("Life Saver", player),
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Ouroboros Hideout - Ruby's gift": PhoaLocationData(
            region="ouroboros_hideout(prison)",
            address=7676310,
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="Heart Ruby",
        ),
        "Ouroboros Hideout - Storage item 1": PhoaLocationData(
            region="ouroboros_hideout(storage)",
            address=7676311,
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Prickle Fruit",
        ),
        "Ouroboros Hideout - Storage item 2": PhoaLocationData(
            region="ouroboros_hideout(storage_back)",
            address=7676312,
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Perro Egg",
        ),
        "Ouroboros Hideout - Storage item 3": PhoaLocationData(
            region="ouroboros_hideout(storage_back)",
            address=7676313,
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Stink Root",
        ),
        "Ouroboros Hideout - Storage item 4": PhoaLocationData(
            region="ouroboros_hideout(storage_back)",
            address=7676314,
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Honey Bun",
        ),
        "Ouroboros Hideout - Storage chest": PhoaLocationData(
            region="ouroboros_hideout(storage_back)",
            address=7676315,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="30 Rin",
        ),
        "Ouroboros Hideout - Storage mouse": PhoaLocationData(
            region="ouroboros_hideout(storage_back)",
            address=7676316,
            rule=lambda state: logic.can_reasonably_kill_mice(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Ouroboros Hideout - Box breaker challenge 1": PhoaLocationData(
            region="ouroboros_hideout",
            address=7676317,
            rule=lambda state: logic.can_balo(state),
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Energy Gem",
        ),
        # "Ouroboros Hideout - Box breaker challenge 2": PhoaLocationData(
        #     region="ouroboros_hideout",
        #     address=7676318,
        #     # Needs rule
        #     flags=PhoaFlag.NPCGIFTS,
        #     vanillaItem="Heart Ruby",
        # ),
        "Ouroboros Hideout - Drake hatchery guard": PhoaLocationData(
            region="ouroboros_hideout(infant_drake_arena)",
            address=7676319,
            flags=PhoaFlag.DUNGEONITEM,
            vanillaItem="Ouro Guard Key",
        ),
        "Ouroboros Hideout - Drake hatchery pot 1": PhoaLocationData(
            region="ouroboros_hideout(infant_drake_arena)",
            address=7676320,
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Pooki Jerky",
        ),
        "Ouroboros Hideout - Drake hatchery pot 2": PhoaLocationData(
            region="ouroboros_hideout(infant_drake_arena)",
            address=7676321,
            rule=lambda state: logic.has_slingshot(state) or logic.has_crossbow(state),
            flags=PhoaFlag.LUNARARTIFACT,
            vanillaItem="Lunar Drake",
        ),
        "Ouroboros Hideout - Drake hatchery chest": PhoaLocationData(
            region="ouroboros_hideout(infant_drake_arena)",
            address=7676322,
            rule=lambda state: logic.has_slingshot(state) or logic.has_crossbow(state),
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="35 Rin",
        ),
        "Ouroboros Hideout - Trial 1 guard": PhoaLocationData(
            region="ouroboros_hideout",
            address=7676323,
            rule=lambda state: logic.can_reasonably_kill_enemies(state, exclude_slingshot=True),
            flags=PhoaFlag.DUNGEONITEM,
            vanillaItem="Ouro Guard Key",
        ),
        "Ouroboros Hideout - Trial 1 completion": PhoaLocationData(
            region="ouroboros_hideout",
            address=7676324,
            flags=PhoaFlag.DUNGEONITEM,
            vanillaItem="Ouroboros Proof",
        ),
        "Ouroboros Hideout - Trial 2 completion": PhoaLocationData(
            region="ouroboros_hideout",
            address=7676325,
            rule=lambda state: logic.can_reasonably_kill_enemies(state, exclude_slingshot=True),
            flags=PhoaFlag.DUNGEONITEM,
            vanillaItem="Ouroboros Proof",
        ),
        "Ouroboros Hideout - Trial 3 completion": PhoaLocationData(
            region="ouroboros_hideout",
            address=7676326,
            flags=PhoaFlag.DUNGEONITEM,
            vanillaItem="Ouroboros Proof",
        ),
        # "Ouroboros Hideout - Atri training 1": PhoaLocationData(  # 2 Ouroboros Scrolls
        #     region="ouroboros_hideout(great_drake_arena)",
        #     address=7676327,
        #     flags=PhoaFlag.NPCGIFTS,
        #     rule=lambda state: logic.has_sonic_spear(state),
        #     vanillaItem="Spear Bomb",
        # ),
        # "Ouroboros Hideout - Atri training 2": PhoaLocationData(  # 4 Ouroboros Scrolls Total
        #     region="ouroboros_hideout(great_drake_arena)",
        #     address=7676328,
        #     flags=PhoaFlag.NPCGIFTS,
        #     rule=lambda state: logic.has_sonic_spear(state) and state.has("Prelude of Panselo", player),
        #     vanillaItem="Spell of Rejuvination",
        # ),
        # "Ouroboros Hideout - Atri training 3": PhoaLocationData(  # 6 Ouroboros Scrolls Total
        #     region="ouroboros_hideout(great_drake_arena)",
        #     address=7676329,
        #     flags=PhoaFlag.NPCGIFTS,
        #     rule=lambda state: logic.has_sonic_spear(state) and state.has("Prelude of Panselo", player),
        #     vanillaItem="Baroque of Battle",
        # ),
        # FIXME: from here
        
        # ET
        "Moonlight Ravine - South town shop item 1": PhoaLocationData(
            region="moonlight_ravine(south)",
            address=0,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Fishing Rod",
        ),
        "Moonlight Ravine - South town shop item 2": PhoaLocationData(
            region="moonlight_ravine(south)",
            address=0,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Cooked Knife Krill", # 3 of them
        ),
        "Moonlight Ravine - South town shop item 3": PhoaLocationData(
            region="moonlight_ravine(south)",
            address=0,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Sushi", # 2 of them
        ),
        "Moonlight Ravine - South town shop item 4": PhoaLocationData(
            region="moonlight_ravine(south)",
            address=0,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Fish Skewer",
        ),
        "Moonlight Ravine -  South town crate under shop": PhoaLocationData(
            region="moonlight_ravine(south)",
            address=0,
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Honey Drop",
        ),
        "Moonlight Ravine -  South town hidden NPC": PhoaLocationData(
            region="moonlight_ravine(south)",
            address=0,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Moonstone",
        ),

        "Moonlight Ravine - Wilds room 1 underwater item 1": PhoaLocationData(
            region="moonlight_ravine(wilds)",
            address=0,
            rule=lambda state: state.has("Life Saver", player),
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Moon Kelp",
        ),
        "Moonlight Ravine - Wilds room 1 underwater item 2": PhoaLocationData(
            region="moonlight_ravine(wilds)",
            address=0,
            rule=lambda state: state.has("Life Saver", player),
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Moon Kelp",
        ),
        "Moonlight Ravine - Wilds room 1 underwater item 3": PhoaLocationData(
            region="moonlight_ravine(wilds)",
            address=0,
            rule=lambda state: state.has("Life Saver", player),
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Moon Kelp",
        ),
        "Moonlight Ravine - Wilds room 1 chest": PhoaLocationData(
            region="moonlight_ravine(wilds)",
            address=0,
            rule=lambda state: state.has("Life Saver", player),
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="30 Rin",
        ),
        "Moonlight Ravine - Wilds room 1 underwater item 4": PhoaLocationData(
            region="moonlight_ravine(wilds)",
            address=0,
            rule=lambda state: state.has("Life Saver", player),
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Moon Kelp",
        ),

        "Moonlight Ravine - Wilds room 2 underwater item 1": PhoaLocationData(
            region="moonlight_ravine(wilds)",
            address=0,
            rule=lambda state: state.has("Life Saver", player),
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Moon Kelp",
        ),
        "Moonlight Ravine - Wilds room 2 underwater item 2": PhoaLocationData(
            region="moonlight_ravine(wilds)",
            address=0,
            rule=lambda state: state.has("Life Saver", player),
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Moon Kelp",
        ),
        "Moonlight Ravine - Wilds room 2 pot": PhoaLocationData(
            region="moonlight_ravine(wilds)",
            address=0,
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Moonlight Ravine - Wilds room 2 underwater item 3": PhoaLocationData(
            region="moonlight_ravine(wilds)",
            address=0,
            rule=lambda state: state.has("Life Saver", player),
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Moon Kelp",
        ),
        "Moonlight Ravine - Wilds room 2 underwater item 4": PhoaLocationData(
            region="moonlight_ravine(wilds)",
            address=0,
            rule=lambda state: state.has("Life Saver", player),
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Moon Kelp",
        ),
        "Moonlight Ravine - Wilds room 2 alcove item": PhoaLocationData(
            region="moonlight_ravine(wilds)",
            address=0,
            rule=lambda state: logic.has_explosives(state)
                               and state.has("Life Saver", player),
            flags=PhoaFlag.LUNARARTIFACT,
            vanillaItem="Lunar Crown",
        ),

        "Moonlight Ravine - Wilds room 3 underwater item 1": PhoaLocationData(
            region="moonlight_ravine(wilds)",
            address=0,
            rule=lambda state: state.has("Life Saver", player),
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Moon Kelp",
        ),
        "Moonlight Ravine - Wilds room 3 pot": PhoaLocationData(
            region="moonlight_ravine(wilds)",
            address=0,
            rule=lambda state: logic.has_sonic_spear(state),
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Moonlight Ravine - Wilds room 3 underwater item 2": PhoaLocationData(
            region="moonlight_ravine(wilds)",
            address=0,
            rule=lambda state: state.has("Life Saver", player),
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Moon Kelp",
        ),
        "Moonlight Ravine - Wilds room 3 water crevice pot": PhoaLocationData(
            region="moonlight_ravine(wilds)",
            address=0,
            rule=lambda state: state.has("Life Saver", player)
                               and (logic.can_use_spear_bomb(state)
                               or state.has("Kobold Blaster", player)),
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Moonlight Ravine - Wilds room 3 wall chest": PhoaLocationData(
            region="moonlight_ravine(wilds)",
            address=0,
            rule=lambda state: state.has("Life Saver", player)
                               and logic.has_explosives(state),
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="30 Rin",
        ),
        "Moonlight Ravine - Wilds room 3 underwater item 3": PhoaLocationData(
            region="moonlight_ravine(wilds)",
            address=0,
            rule=lambda state: state.has("Life Saver", player),
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Moon Kelp",
        ),
        "Moonlight Ravine - Wilds room 3 underwater item 4": PhoaLocationData(
            region="moonlight_ravine(wilds)",
            address=0,
            rule=lambda state: state.has("Life Saver", player),
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Moon Kelp",
        ),

        "Moonlight Ravine - Wilds room 4 underwater item 1": PhoaLocationData(
            region="moonlight_ravine(wilds)",
            address=0,
            rule=lambda state: state.has("Life Saver", player),
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Moon Kelp",
        ),
        "Moonlight Ravine - Wilds room 4 lizard": PhoaLocationData(
            region="moonlight_ravine(wilds)",
            address=0,
            rule=lambda state: logic.can_reasonably_kill_mice(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Moonlight Ravine - Wilds room 4 underwater item 2": PhoaLocationData(
            region="moonlight_ravine(wilds)",
            address=0,
            rule=lambda state: state.has("Life Saver", player)
                               and logic.has_sonic_spear(state)
                               and logic.has_explosives(state),
            flags=PhoaFlag.LUNARARTIFACT,
            vanillaItem="Lunar Trident",
        ),
        "Moonlight Ravine - Wilds room 4 underwater item 3": PhoaLocationData(
            region="moonlight_ravine(wilds)",
            address=0,
            rule=lambda state: state.has("Life Saver", player),
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Moon Kelp",
        ),
        "Moonlight Ravine - Wilds room 4 underwater item 4": PhoaLocationData(
            region="moonlight_ravine(wilds)",
            address=0,
            rule=lambda state: state.has("Life Saver", player),
            flags=PhoaFlag.ENERGYGEM,
            vanillaItem="Energy Gem",
        ),
        "Moonlight Ravine - Wilds room 4 underwater item 5": PhoaLocationData(
            region="moonlight_ravine(wilds)",
            address=0,
            rule=lambda state: state.has("Life Saver", player),
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Moon Kelp",
        ),
        "Moonlight Ravine - Wilds room 4 underwater item 6": PhoaLocationData(
            region="moonlight_ravine(wilds)",
            address=0,
            rule=lambda state: state.has("Life Saver", player),
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Moon Kelp",
        ),

        "Moonlight Ravine - North town underwater item 1": PhoaLocationData(
            region="moonlight_ravine(north)",
            address=0,
            rule=lambda state: state.has("Life Saver", player),
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Moon Kelp",
        ),
        "Moonlight Ravine - North town Bo running challenge item": PhoaLocationData(
            region="moonlight_ravine(north)",
            address=0,
            rule=lambda state: state.has("Life Saver", player)
                               or state.has("Rocket Boots", player),
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="40 Rin",
        ),
        "Moonlight Ravine - North town underwater item 2": PhoaLocationData(
            region="moonlight_ravine(north)",
            address=0,
            rule=lambda state: state.has("Life Saver", player),
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Moon Kelp",
        ),
        "Moonlight Ravine - North town underwater item 3": PhoaLocationData(
            region="moonlight_ravine(north)",
            address=0,
            rule=lambda state: state.has("Life Saver", player),
            flags=PhoaFlag.FREESTANDING,
            vanillaItem="Moon Kelp",
        ),
        "Moonlight Ravine - North town fish item": PhoaLocationData( # SOME AMOUNT OF ENERGY NECESSARY
            region="moonlight_ravine(north)",
            address=0,
            rule=lambda state: logic.has_fishing_rod(state),
            flags=PhoaFlag.FISHINGSPOT,
            vanillaItem="Moonstone",
        ),
        "Moonlight Ravine - North town hidden chest": PhoaLocationData(
            region="moonlight_ravine(north)",
            address=0,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="30 Rin",
        ),

        "Kingdom Bridge - South songstone puzzle chest": PhoaLocationData(
            region="kingdom_bridge(south)",
            address=0,
            rule=lambda state: logic.has_music_instrument(state),
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="45 Rin",
        ),
        "Kingdom Bridge - South bridge chest": PhoaLocationData(
            region="kingdom_bridge(south)",
            address=0,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="35 Rin",
        ),
        "Kingdom Bridge - South fish item": PhoaLocationData( # SOME AMOUNT OF ENERGY NECESSARY
            region="kingdom_bridge(south)",
            address=0,
            rule=lambda state: logic.has_fishing_rod(state),
            flags=PhoaFlag.FISHINGSPOT,
            vanillaItem="Moonstone",
        ),
        "Kingdom Bridge - Tower crate 1": PhoaLocationData(
            region="kingdom_bridge(north)",
            address=0,
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Drake Tail",
        ),
        "Kingdom Bridge - Tower crate mouse": PhoaLocationData(
            region="kingdom_bridge(north)",
            address=0,
            rule=lambda state: logic.can_reasonably_kill_mice(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Kingdom Bridge - Tower lower chest": PhoaLocationData(
            region="kingdom_bridge(north)",
            address=0,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="20 Rin",
        ),
        "Kingdom Bridge - Tower crate 2": PhoaLocationData(
            region="kingdom_bridge(north)",
            address=0,
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Saffron Milk",
        ),
        "Kingdom Bridge - North turret pot": PhoaLocationData(
            region="kingdom_bridge(north)",
            address=0,
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Kingdom Bridge - Tower upper turret chest": PhoaLocationData(
            region="kingdom_bridge(north)",
            address=0,
            rule=lambda state: logic.has_sonic_spear(state)
                               and logic.has_music_instrument(state),
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="50 Rin",
        ),
        "Kingdom Bridge - Tower upper turret pot": PhoaLocationData(
            region="kingdom_bridge(north)",
            address=0,
            rule=lambda state: logic.has_sonic_spear(state)
                               and logic.has_music_instrument(state),
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Kingdom Bridge - GEO dungeon item": PhoaLocationData(
            region="kingdom_bridge(north)",
            address=0,
            flags=PhoaFlag.GEOCHALLENGE,
            vanillaItem="GEO Ticket",
        ),
        "Daea City - West side bird lady quest": PhoaLocationData( # FACT CHECK
            region="daea_city",
            address=0,
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="Energy Gem",
        ),
        "Daea City - GEO dungeon item": PhoaLocationData(
            region="daea_city(geo_dungeon)",
            address=0,
            flags=PhoaFlag.GEOCHALLENGE,
            vanillaItem="GEO Ticket",
        ),
        "Daea City - Blacksmith shop item 1": PhoaLocationData(
            region="daea_city",
            address=0,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Crank Lamp",
        ),
        "Daea City - Blacksmith shop item 2": PhoaLocationData(
            region="daea_city",
            address=0,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Steel Bat",
        ),
        "Daea City - Blacksmith shop item 3": PhoaLocationData(
            region="daea_city",
            address=0,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Jade Hauberk",
        ),
        "Daea City - Blacksmith shop item 4": PhoaLocationData(
            region="daea_city",
            address=0,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Civillian Crossbow",
        ),
        "Daea City - Blacksmith shop item 5": PhoaLocationData(
            region="daea_city",
            address=0,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Fishing Rod",
        ),
        "Daea City - Blacksmith dream ore quest": PhoaLocationData(
            region="daea_city",
            address=0,
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="Night Star",
        ),




        "Daea City - Residential house lady quest": PhoaLocationData( # 3 Drake Tails
            region="daea_city",
            address=0,
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="60 Rin",
        ),
        "Daea City - Residential house grandmother": PhoaLocationData(
            region="daea_city",
            address=0,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Moonstone",
        ),
        "Daea City - West alley pot": PhoaLocationData(
            region="daea_city",
            address=0,
            rule=lambda state: logic.has_sonic_spear(state),
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Moonstone",
        ),
        "Daea City - West alley mouse": PhoaLocationData(
            region="daea_city",
            address=0,
            rule=lambda state: logic.can_reasonably_kill_mice(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Daea City - Student dormitory chest": PhoaLocationData(
            region="daea_city",
            address=0,
            rule=lambda state: logic.has_sonic_spear(state),
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="35 Rin",
        ),
        "Daea City - Blue Lobster pantry crate 1": PhoaLocationData(
            region="daea_city",
            address=0,
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Grape Juice",
        ),
        "Daea City - Blue Lobster pantry crate 2": PhoaLocationData(
            region="daea_city",
            address=0,
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Macaron",
        ),
        "Daea City - Blue Lobster pantry mouse": PhoaLocationData(
            region="daea_city",
            address=0,
            rule=lambda state: logic.can_reasonably_kill_mice(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Daea City - Bo running challenge": PhoaLocationData(
            region="daea_city",
            address=0,
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="50 Rin",
        ),
        "Daea City - Blue Lobster shop item 1": PhoaLocationData(
            region="daea_city",
            address=0,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Deli Sandwich",
        ),
        "Daea City - Blue Lobster shop item 2": PhoaLocationData(
            region="daea_city",
            address=0,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="House Soup",
        ),
        "Daea City - Blue Lobster shop item 3": PhoaLocationData(
            region="daea_city",
            address=0,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Blue Lobster Special",
        ),
        "Daea City - Blue Lobster shop item 4": PhoaLocationData(
            region="daea_city",
            address=0,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Milk",
        ),
        "Daea City - Blue Lobster shop item 5": PhoaLocationData(
            region="daea_city",
            address=0,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Honey Brew",
        ),
        "Daea City - Blue Lobster shop item 6": PhoaLocationData(
            region="daea_city",
            address=0,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Grape Juice",
        ),
        "Daea City - Library songstone puzzle": PhoaLocationData(
            region="daea_city",
            address=0,
            rule=lambda state: logic.has_music_instrument(state),
            flags=PhoaFlag.ENERGYGEM,
            vanillaItem="Energy Gem",
        ),
        "Daea City - Troubadours Alto quest item": PhoaLocationData(
            region="daea_city",
            address=0,
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="Heart Ruby",
        ),
        "Daea City - Troubadours Forte quest item": PhoaLocationData( # RECURRING
            region="daea_city",
            address=0,
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="35 Rin",
        ),
        "Daea City - East alley mouse": PhoaLocationData(
            region="daea_city",
            address=0,
            rule=lambda state: logic.can_reasonably_kill_mice(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Daea City - East alley balcony item": PhoaLocationData(
            region="daea_city",
            address=0,
            flags=PhoaFlag.HEARTRUBY,
            vanillaItem="Heart Ruby",
        ),
        "Daea City - East alley Faun Fountain quest (Song of Ouroboros)": PhoaLocationData( # NOT SURE IF THIS IS A SIDEQUEST OR SOMETHING ELSE
            region="daea_city",
            address=0,
            rule=lambda state: logic.has_music_instrument(state)
                               and state.has("Song of Ouroboros", player),
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="20 Rin",
        ),
        "Daea City - East alley Faun Fountain quest (GEO Song)": PhoaLocationData(
            region="daea_city",
            address=0,
            rule=lambda state: logic.has_music_instrument(state)
                               and state.has("GEO Song", player),
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="20 Rin",
        ),
        "Daea City - East alley Faun Fountain quest (Royal Hymn)": PhoaLocationData(
            region="daea_city",
            address=0,
            rule=lambda state: logic.has_music_instrument(state)
                               and state.has("Royal Hymn", player),
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="20 Rin",
        ),
        "Daea City - East alley Faun Fountain quest (Prelude of Panselo)": PhoaLocationData(
            region="daea_city",
            address=0,
            rule=lambda state: logic.has_music_instrument(state)
                               and state.has("Prelude of Panselo", player),
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="20 Rin",
        ),
        "Daea City - East alley Faun Fountain quest (Baroque of Battle)": PhoaLocationData(
            region="daea_city",
            address=0,
            rule=lambda state: logic.has_music_instrument(state)
                               and state.has("Baroque of Battle", player),
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="20 Rin",
        ),
        "Daea City - East alley Faun Fountain quest (Lullaby of Ava)": PhoaLocationData(
            region="daea_city",
            address=0,
            rule=lambda state: logic.has_music_instrument(state)
                               and state.has("Lullaby of Ava", player),
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="20 Rin",
        ),
        "Daea City - East alley Faun Fountain quest (All Songs)": PhoaLocationData( # THIS WILL TRIGGER AT THE SAME TIME AS THE LAST SONG PLAYED
            region="daea_city",
            address=0,
            rule=lambda state: logic.has_music_instrument(state)
                               and state.has("Song of Ouroboros", player)
                               and state.has("GEO Song", player)
                               and state.has("Royal Hymn", player)
                               and state.has("Prelude of Panselo", player)
                               and state.has("Baroque of Battle", player)
                               and state.has("Lullaby of Ava", player),
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="50 Rin",
        ),
        "Daea City - Bakery shop item 1": PhoaLocationData(
            region="daea_city",
            address=0,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Puff Pastry",
        ),
        "Daea City - Bakery shop item 2": PhoaLocationData(
            region="daea_city",
            address=0,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Macarons", # 2 of them
        ),
        "Daea City - Bakery shop item 3": PhoaLocationData(
            region="daea_city",
            address=0,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Grape Cake",
        ),
        "Daea City - Bakery shop item 4": PhoaLocationData(
            region="daea_city",
            address=0,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Chocolates", # 3 of them
        ),
        "Daea City - Shooting gallery item 1": PhoaLocationData( # UNSURE OF IF I WOULD NEED TO MAKE THIS EASIER MAYBE TWEAK THE ENERGY GEM AMOUNTS
            region="daea_city",
            address=0,
            rule=lambda state: logic.can_clear_atai_expert_gallery(state),
            flags=PhoaFlag.MINIGAMES,
            vanillaItem="Rubber Duck",
        ),
        "Daea City - Shooting gallery item 2": PhoaLocationData(
            region="daea_city",
            address=0,
            rule=lambda state: logic.can_clear_atai_expert_gallery(state),
            flags=PhoaFlag.MINIGAMES,
            vanillaItem="Heart Ruby",
        ),
        "Daea City - Shooting gallery item 3": PhoaLocationData(
            region="daea_city",
            address=0,
            rule=lambda state: logic.can_clear_atai_expert_gallery(state),
            flags=PhoaFlag.MINIGAMES,
            vanillaItem="Moonstone",
        ),
        "Daea City - Guard tower balcony crate": PhoaLocationData(
            region="daea_city",
            address=0,
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Grape Cake",
        ),
        "Daea City - Dojo Teraka shop item": PhoaLocationData( # NOT SURE IF THIS IS SHOPSANITY
            region="daea_city",
            address=0,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Concentrate",
        ),
        "Daea City - Dojo Teraka quest": PhoaLocationData(
            region="daea_city",
            address=0,
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="Moonstone",
        ),
        "Daea City - Noodle shop item": PhoaLocationData(
            region="daea_city",
            address=0,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Spicy Noodles",
        ),
        "Daea City - Tunnel pantry crate 1": PhoaLocationData(
            region="daea_city",
            address=0,
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Big Raw Meat",
        ),
        "Daea City - Tunnel pantry crate 2": PhoaLocationData(
            region="daea_city",
            address=0,
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Gourmet Fish Fillet",
        ),
        "Daea City - Tunnel pantry chest": PhoaLocationData(
            region="daea_city",
            address=0,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="100 Rin",
        ),
        "Daea City - Tunnel kitchen crate": PhoaLocationData(
            region="daea_city",
            address=0,
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Raw Bird",
        ),
        "Daea City - Tunnel kitchen Chef Basil quest 1": PhoaLocationData( # THESE WILL LIKELY NEED REGION ACCESS LOGIC
            region="daea_city",
            address=0,
            flags=PhoaFlag.SIDEQUEST, # Knife Krill
            vanillaItem="10 Rin",
        ),
        "Daea City - Tunnel kitchen Chef Basil quest 2": PhoaLocationData(
            region="daea_city",
            address=0,
            flags=PhoaFlag.SIDEQUEST, # Desert Squash
            vanillaItem="20 Rin",
        ),
        "Daea City - Tunnel kitchen Chef Basil quest 3": PhoaLocationData(
            region="daea_city",
            address=0,
            flags=PhoaFlag.SIDEQUEST, # Amber Fish Fillet
            vanillaItem="Moonstone",
        ),
        "Daea City - Tunnel kitchen Chef Basil quest 4": PhoaLocationData(
            # ARBOAR MEAT CAN BE GAINED FROM THAT ONE COSETTE ROOM BUT IT'S A ONE-TIME CHANCE
            # MAYBE WE JUST ALLOW THE ARBOAR TO ALWAYS SPAWN OR REQUIRE IT AFTER AURANTIA
            region="daea_city",
            address=0,
            flags=PhoaFlag.SIDEQUEST, # Arboar Meat
            vanillaItem="Elixir",
        ),
        "Daea City - Ballroom under the stage": PhoaLocationData(
            region="daea_city",
            address=0,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="75 Rin",
        ),
        "Daea City - Ballroom piano lady quest": PhoaLocationData(
            region="daea_city",
            address=0,
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="Moonstone",
        ),
        "Daea City - Tunnel White Towers entrance item": PhoaLocationData(
            region="daea_city",
            address=0,
            rule=lambda state: logic.has_music_instrument(state)
                               and state.has("Royal Hymn", player),
            flags=PhoaFlag.HEARTRUBY,
            vanillaItem="Heart Ruby",
        ),
        

        # 13 Moonstone
        # 4 Heart Ruby
        # 4 Energy Gem
        
        # 8 20 Rin
        # 3 30 Rin
        # 3 35 Rin
        # 1 40 Rin
        # 1 45 Rin
        # 3 50 Rin
        # 1 60 Rin
        # 1 75 Rin
        # 1 100 Rin

        # 2 Fishing Rod
        # 1 Crank Lamp
        # 1 Steel Bat
        # 1 Jade Hauberk
        # 1 Civillian Crossbow
        # 1 Night Star
        # 1 Concentrate

        # 1 Lunar Crown
        # 1 Lunar Trident
        # 2 GEO Ticket
        
        # 5 Mystery Meat

        # 1 Cooked Knife Krill 3x
        # 1 Sushi 2x
        # 1 Fish Skewer
        # 1 Honey Drop
        # 19 Moon Kelp
        # 1 Drake Tail
        # 1 Saffron Milk
        # 2 Grape Juice
        # 1 Macaron (Singular)
        # 1 Macarons (Set of 2)
        # 1 Deli Sandwich
        # 1 House Soup
        # 1 Blue Lobster Special
        # 1 Milk
        # 1 Honey Brew
        # 1 Puff Pastry
        # 2 Grape Cake
        # 1 Chocolates (Set of 3)
        # 1 Rubber Duck
        # 1 Spicy Noodles
        # 1 Big Raw Meat
        # 1 Gourmet Fish Fillet
        # 1 Raw Bird
        # 1 Elixir        


        # fight4day
        "Daea Region - Cave chest": PhoaLocationData(
            region="daea_region",
            address=7676500,
            rule=lambda state: logic.has_light_source(state)
                               and logic.has_explosives(state)
                               and (state.has("Life Saver", player)
                                 or state.has("Rocket Boots", player)),
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="40 Rin",
        ),
        "Daea Region - Cave ledge item": PhoaLocationData(
            region="daea_region",
            address=7676501,
            rule=lambda state: state.has("Rocket Boots", player)
                               or (logic.has_light_source(state)
                                 and logic.has_explosives(state)
                                 and state.has("Life Saver", player)
                                 and logic.has_sonic_spear(state)),
            flags=PhoaFlag.ENERGYGEM,
            vanillaItem="Energy Gem",
        ),
        "Daea Region - Perro Hide and Seek": PhoaLocationData(
            region="daea_region",
            address=7676502,
            flags=PhoaFlag.PERRO,
            vanillaItem="Perro",
        ),
        "Daea Region - Cupid's Fountain Ouroboros shrine": PhoaLocationData(
            region="daea_region",
            address=7676503,
            # Possible without bat
            rule=lambda state: logic.has_music_instrument(state)
                               and state.has("Song of Ouroboros", player)
                               and logic.has_bombs(state)
                               and logic.has_crossbow(state),
            flags=PhoaFlag.OUROBOROS,
            vanillaItem="Ouroboros Scroll",
        ),
        "Daea Region - GEO house reward": PhoaLocationData(
            region="daea_region",
            address=7676504,
            flags=PhoaFlag.GEOCHALLENGE,
            rule=lambda state: logic.has_music_instrument(state)
                               and state.has("GEO Song", player),
            vanillaItem="GEO Ticket",
        ),
        "Daea Region - GEO house Mr. planto's reward": PhoaLocationData(
            region="daea_region",
            address=7676505,
            flags=PhoaFlag.PLANTO,
            vanillaItem="20 Rin",
        ),
        "Lake Laboratory - Fran freedom quest": PhoaLocationData(
            region="lake_laboratory",
            address=7676506,
            rule=lambda state: logic.can_do_fran_quest_chain(state, 0),
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="Tailoring Voucher",
        ),
        "Lake Laboratory - Fran 1st moonstone batch": PhoaLocationData(
            region="lake_laboratory",
            address=7676507,
            rule=lambda state: logic.can_do_fran_quest_chain(state, 1),
            flags=PhoaFlag.MOONSTONE_SHOP,
            vanillaItem="Heart Ruby",
        ),
        "Lake Laboratory - Fran 2nd moonstone batch": PhoaLocationData(
            region="lake_laboratory",
            address=7676508,
            rule=lambda state: logic.can_do_fran_quest_chain(state, 2),
            flags=PhoaFlag.MOONSTONE_SHOP,
            vanillaItem="Tailoring Voucher",
        ),
        "Lake Laboratory - Fran 3rd moonstone batch": PhoaLocationData(
            region="lake_laboratory",
            address=7676509,
            rule=lambda state: logic.can_do_fran_quest_chain(state, 3),
            flags=PhoaFlag.MOONSTONE_SHOP,
            vanillaItem="Energy Gem",
        ),
        "Lake Laboratory - Fran 4th moonstone batch": PhoaLocationData(
            region="lake_laboratory",
            address=7676510,
            rule=lambda state: logic.can_do_fran_quest_chain(state, 4),
            flags=PhoaFlag.MOONSTONE_SHOP,
            vanillaItem="Moon Crystal",
        ),
        "Lake Laboratory - Fran 5th moonstone batch": PhoaLocationData(
            region="lake_laboratory",
            address=7676511,
            rule=lambda state: logic.can_do_fran_quest_chain(state, 5),
            flags=PhoaFlag.MOONSTONE_SHOP,
            vanillaItem="Heart Ruby",
        ),
        # TODO: these gift checks are missable
        "Lake Laboratory - Lan gift after 1st moonstone batch": PhoaLocationData(
            region="lake_laboratory",
            address=0,
            rule=lambda state: logic.can_do_fran_quest_chain(state, 1),
            flags=[PhoaFlag.MOONSTONE_SHOP, PhoaFlag.NPCGIFTS],
            vanillaItem="Saffron Milk",
        ),
        "Lake Laboratory - Van gift after 2nd moonstone batch": PhoaLocationData(
            region="lake_laboratory",
            address=0,
            rule=lambda state: logic.can_do_fran_quest_chain(state, 2),
            flags=[PhoaFlag.MOONSTONE_SHOP, PhoaFlag.NPCGIFTS],
            vanillaItem="Grape Cake",
        ),
        "Lake Laboratory - Van gift after 3rd moonstone batch": PhoaLocationData(
            region="lake_laboratory",
            address=0,
            rule=lambda state: logic.can_do_fran_quest_chain(state, 3),
            flags=[PhoaFlag.MOONSTONE_SHOP, PhoaFlag.NPCGIFTS],
            vanillaItem="Cooked Drake Tail",
        ),
        "Lake Laboratory - Lan gift after 4th moonstone batch": PhoaLocationData(
            region="lake_laboratory",
            address=0,
            rule=lambda state: logic.can_do_fran_quest_chain(state, 4),
            flags=[PhoaFlag.MOONSTONE_SHOP, PhoaFlag.NPCGIFTS],
            vanillaItem="Spicy Noodles",
        ),
        "GEO Base - Prize counter item 1": PhoaLocationData(
            region="daea_region",
            address=0,
            rule=lambda state: state.has("GEO Ticket", player, 10),
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Golden Egg",
        ),
        "GEO Base - Prize counter item 2": PhoaLocationData(
            region="daea_region",
            address=0,
            rule=lambda state: state.has("GEO Ticket", player, 10),
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Heart Ruby",
        ),
        "GEO Base - Prize counter item 3": PhoaLocationData(
            region="daea_region",
            address=0,
            rule=lambda state: state.has("GEO Ticket", player, 10),
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Energy Gem",
        ),
        "GEO Base - Prize counter item 4": PhoaLocationData(
            region="daea_region",
            address=0,
            rule=lambda state: state.has("GEO Ticket", player, 10),
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="GEO Jacket",
        ),
        "GEO Base - Georgia quest 1": PhoaLocationData(
            region="daea_region",
            address=0,
            rule=lambda state: state.has("GEO Ticket", player),
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="Lucky Earrings",
        ),
        "GEO Base - Georgia quest 2": PhoaLocationData(
            region="daea_region",
            address=0,
            rule=lambda state: state.has("GEO Ticket", player, 2),
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="Heart Ruby",
        ),
        "GEO Base - Attic crate": PhoaLocationData(
            region="daea_region",
            address=0,
            rule=lambda state: logic.can_deal_damage(state),
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Honey Drop",
        ),
        "GEO Base - GEO reward": PhoaLocationData(
            region="daea_region",
            address=0,
            rule=lambda state: logic.has_music_instrument(state)
                               and state.has("GEO Song", player)
                               and (logic.has_slingshot(state)
                                 or (logic.has_sonic_spear(state)
                                   and (logic.has_bombs(state) or logic.has_crossbow(state))
                                 )
                               ),
            flags=PhoaFlag.GEOCHALLENGE,
            vanillaItem="GEO Ticket",
        ),
        "GEO Base - Pond fish": PhoaLocationData(
            region="daea_region",
            address=0,
            rule=lambda state: logic.has_fishing_rod(state),
            flags=PhoaFlag.FISHINGSPOT,
            vanillaItem="Moonstone",
        ),
        "Thomas's Lab - Reception bribe": PhoaLocationData( # TODO: currently missable
            region="daea_region",
            address=0,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="50 Rin",
        ),
        "Thomas's Lab - Vending machine": PhoaLocationData(
            region="daea_region",
            address=0,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Calory Slush",
        ),
        "Thomas's Lab - Binary room": PhoaLocationData(
            region="daea_region",
            address=0,
            rule=lambda state: logic.has_music_instrument(state),
            flags=PhoaFlag.ENERGYGEM,
            vanillaItem="Energy Gem",
        ),
        "Thomas's Lab - Room 1-1": PhoaLocationData(
            region="daea_region",
            address=0,
            rule=lambda state: logic.can_hit_switch_from_a_distance(state),
            flags=PhoaFlag.MAINQUEST,
            vanillaItem="Blue Golem Medallion",
        ),
        "Thomas's Lab - Room 1-2": PhoaLocationData(
            region="daea_region",
            address=0,
            flags=PhoaFlag.MAINQUEST,
            vanillaItem="Blue Golem Medallion",
        ),
        "Thomas's Lab - Room 1-3": PhoaLocationData(
            region="daea_region",
            address=0,
            # Possible with all ranged weapons
            rule=lambda state: logic.can_hit_switch_from_a_distance(state),
            flags=PhoaFlag.MAINQUEST,
            vanillaItem="Blue Golem Medallion",
        ),
        "Thomas's Lab - Room 1-4": PhoaLocationData(
            region="daea_region",
            address=0,
            rule=lambda state: logic.can_reasonably_kill_flying_enemies(state),
            flags=PhoaFlag.MAINQUEST,
            vanillaItem="Blue Golem Medallion",
        ),
        "Thomas's Lab - Room 2-1": PhoaLocationData(
            region="daea_region",
            address=0,
            flags=PhoaFlag.MAINQUEST,
            vanillaItem="Red Golem Medallion",
        ),
        "Thomas's Lab - Room 2-2": PhoaLocationData(
            region="daea_region",
            address=0,
            flags=PhoaFlag.MAINQUEST,
            vanillaItem="Red Golem Medallion",
        ),
        "Thomas's Lab - Room 2-3": PhoaLocationData(
            region="daea_region",
            address=0,
            flags=PhoaFlag.MAINQUEST,
            vanillaItem="Red Golem Medallion",
        ),
        "Thomas's Lab - Room 2-4": PhoaLocationData(
            region="daea_region",
            address=0,
            rule=lambda state: logic.can_reasonably_kill_flying_enemies(state),
            flags=PhoaFlag.MAINQUEST,
            vanillaItem="Red Golem Medallion",
        ),
        "Thomas's Lab - Punching bag minigame": PhoaLocationData(
            region="daea_region",
            address=0,
            rule=lambda state: logic.has_bat(state),
            flags=PhoaFlag.MINIGAMES,
            vanillaItem="Heart Ruby",
        ),
        "Thomas's Lab - Diary room crate": PhoaLocationData(
            region="daea_region",
            address=0,
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Pumpkin Muffin",
        ),
        "Thomas's Lab - Crate behind wrecker room": PhoaLocationData(
            region="daea_region",
            address=0,
            rule=lambda state: state.has("Defeat Wrecker boss", player),
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Calory Slush",
        ),
        "Thomas's Lab - Reception blue medallion quest": PhoaLocationData(
            region="daea_region",
            address=0,
            rule=lambda state: state.has("Defeat Wrecker boss", player)
                               and state.has("Blue Golem Medallion", player, 4),
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="Moonstone",
        ),
        "Thomas's Lab - Reception red medallion quest": PhoaLocationData(
            region="daea_region",
            address=0,
            rule=lambda state: state.has("Defeat Wrecker boss", player)
                               and state.has("Red Golem Medallion", player, 4),
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="Moonstone",
        ),
        "Thomas's Lab - Wrecker room Floret quest": PhoaLocationData( # TODO: quest should be active earlier
            region="daea_region",
            address=0,
            # Ensure player can buy chocolate
            rule=lambda state: state.has("Defeat Wrecker boss", player)
                               and (state.can_reach_region("atai_region", player)
                                 or state.can_reach_region("daea_city", player)),
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="Heart Ruby",
        ),
        # TODO: artifacts aren't getting removed from inventory?
        "Antique Shop - Deliver Lunar Artifact 1": PhoaLocationData(
            region="daea_region",
            address=0,
            rule=lambda state: logic.has_lunar_artifacts(1, state),
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="40 Rin",
        ),
        "Antique Shop - Deliver Lunar Artifact 2": PhoaLocationData(
            region="daea_region",
            address=0,
            rule=lambda state: logic.has_lunar_artifacts(2, state),
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="40 Rin",
        ),
        "Antique Shop - Deliver Lunar Artifact 3": PhoaLocationData(
            region="daea_region",
            address=0,
            rule=lambda state: logic.has_lunar_artifacts(3, state),
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="40 Rin",
        ),
        "Antique Shop - Deliver Lunar Artifact 4": PhoaLocationData(
            region="daea_region",
            address=0,
            rule=lambda state: logic.has_lunar_artifacts(4, state),
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="40 Rin",
        ),
        "Antique Shop - Deliver Lunar Artifact 5": PhoaLocationData(
            region="daea_region",
            address=0,
            rule=lambda state: logic.has_lunar_artifacts(5, state),
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="40 Rin",
        ),
        "Antique Shop - Deliver Lunar Artifact 6": PhoaLocationData(
            region="daea_region",
            address=0,
            rule=lambda state: logic.has_lunar_artifacts(6, state),
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="40 Rin",
        ),
        "Antique Shop - Deliver Lunar Artifact 7": PhoaLocationData(
            region="daea_region",
            address=0,
            rule=lambda state: logic.has_lunar_artifacts(7, state),
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="40 Rin",
        ),
        "Antique Shop - Deliver Lunar Artifact 8": PhoaLocationData(
            region="daea_region",
            address=0,
            rule=lambda state: logic.has_lunar_artifacts(8, state),
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="40 Rin",
        ),
        "Antique Shop - Deliver Lunar Artifact 9": PhoaLocationData(
            region="daea_region",
            address=0,
            rule=lambda state: logic.has_lunar_artifacts(9, state),
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="40 Rin",
        ),
        "Antique Shop - Deliver Lunar Artifact 10": PhoaLocationData(
            region="daea_region",
            address=0,
            rule=lambda state: logic.has_lunar_artifacts(10, state),
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="40 Rin",
        ),
        "Antique Shop - Deliver Lunar Artifact 11": PhoaLocationData(
            region="daea_region",
            address=0,
            rule=lambda state: logic.has_lunar_artifacts(11, state),
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="40 Rin",
        ),
        "Antique Shop - Deliver Lunar Artifact 12": PhoaLocationData(
            region="daea_region",
            address=0,
            rule=lambda state: logic.has_lunar_artifacts(12, state),
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="40 Rin",
        ),
        "Antique Shop - Deliver Lunar Artifact 4 bonus": PhoaLocationData(
            region="daea_region",
            address=0,
            rule=lambda state: logic.has_lunar_artifacts(4, state),
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="Energy Gem",
        ),
        "Antique Shop - Deliver Lunar Artifact 8 bonus": PhoaLocationData(
            region="daea_region",
            address=0,
            rule=lambda state: logic.has_lunar_artifacts(8, state),
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="Antique Cast Iron",
        ),
        "Antique Shop - Deliver Lunar Artifact 12 bonus": PhoaLocationData(
            region="daea_region",
            address=0,
            rule=lambda state: logic.has_lunar_artifacts(12, state),
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="Heart Ruby",
        ),
        "Antique Shop - Basement mouse": PhoaLocationData(
            region="daea_region",
            address=0,
            rule=lambda state: logic.can_reasonably_kill_mice(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Antique Shop - Basement puzzle": PhoaLocationData(
            region="daea_region",
            address=0,
            rule=lambda state: logic.has_crossbow(state),
            flags=PhoaFlag.HEARTRUBY,
            vanillaItem="Heart Ruby",
        ),
        "First Wall - Bottom right guard room crate": PhoaLocationData(
            region="daea_region",
            address=0,
            # Crate near ceiling
            rule=lambda state: logic.can_reasonably_kill_enemies(state, False, True),
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "First Wall - Turret item": PhoaLocationData( # TODO: also first wall needs to be opened
            region="daea_region",
            address=0,
            rule=lambda state: logic.has_sonic_spear(state)
                               and state.has("Rocket Boots", player),
            flags=PhoaFlag.ENERGYGEM,
            vanillaItem="Energy Gem",
        ),
        "First Wall - Cafeteria crate": PhoaLocationData(
            region="daea_region",
            address=0,
            # Crate near ceiling
            rule=lambda state: logic.can_reasonably_kill_enemies(state, False, True),
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Cheese",
        ),
        "First Wall - Storage crate": PhoaLocationData(
            region="daea_region",
            address=0,
            flags=PhoaFlag.BREAKABLE,
            vanillaItem="Raw Meat",
        ),
        "First Wall - Cafeteria waiter quest": PhoaLocationData(
            region="daea_region",
            address=0,
            # Can reach Doki Herb and Stink Root
            rule=lambda state: state.can_reach_region("panselo_region", player)
                               and state.can_reach_region("ouroboros_hideout(storage_back)", player),
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="Heart Ruby",
        ),
        "First Wall - Mother/daughter quest": PhoaLocationData(
            region="daea_region",
            address=0,
            flags=PhoaFlag.SIDEQUEST,
            vanillaItem="Moonstone",
        ),
        # FIXME: to here
        # Events
        "Anuri Temple - Side entrance gate opened": PhoaLocationData(
            region="anuri_temple(main)",
            address=None,
        ),
        "Slargummy boss defeated": PhoaLocationData(
            region="anuri_temple(slargummy_boss)",
            address=None,
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
        ),
        "Defeat Sand Dragon": PhoaLocationData(
            region="ouroboros_hideout(great_drake_arena)",
            address=None,
            rule=lambda state: logic.can_defeat_great_drake(state),
        ),
        "Defeat Wrecker boss": PhoaLocationData(
            region="daea_region",
            address=None,
            rule=lambda state: logic.can_defeat_wrecker(state),
        ),
    }

    if not options:
        return locations

    filters = [
        (options.enable_main_quest_locations > 0, PhoaFlag.MAINQUEST),
        (options.enable_heart_ruby_locations > 0, PhoaFlag.HEARTRUBY),
        (options.enable_energy_gem_locations > 0, PhoaFlag.ENERGYGEM),
        (options.enable_moonstone_locations > 0, PhoaFlag.MOONSTONE),
        (options.enable_lunar_artifacts_locations > 0, PhoaFlag.LUNARARTIFACT),
        (options.enable_fishing_spots > 0, PhoaFlag.FISHINGSPOT),
        (options.enable_npc_gifts > 0, PhoaFlag.NPCGIFTS),
        (options.enable_planto_rewards > 0, PhoaFlag.PLANTO),
        (options.enable_misc > 0, PhoaFlag.MISC),
        (options.shop_sanity > 0, PhoaFlag.SHOPSANITY),
        (options.enable_small_animal_drops > 0, PhoaFlag.SMALLANIMALS),
        (options.enable_rin_locations > 0, PhoaFlag.RINCHESTS),
        (options.enable_rin_locations > 1, PhoaFlag.RINCONTAINERS),
        (options.enable_geo_challenge_rewards > 0, PhoaFlag.GEOCHALLENGE),
        (options.enable_breakables > 0, PhoaFlag.BREAKABLE),
        (options.enable_sidequests > 0, PhoaFlag.SIDEQUEST),
        (options.enable_freestanding > 0, PhoaFlag.FREESTANDING),
        (options.enable_minigames > 0, PhoaFlag.MINIGAMES),
        (options.enable_trap_chests > 0, PhoaFlag.TRAPCHEST),
        (options.enable_ouroboros_shrines > 0, PhoaFlag.OUROBOROS),
        (options.enable_moonstone_shops > 0, PhoaFlag.MOONSTONE_SHOP),
        (options.enable_perros > 0, PhoaFlag.PERRO),
        (options.enable_ancient_vault > 0, PhoaFlag.VAULT),
        (True, PhoaFlag.DUNGEONITEM),
        (True, PhoaFlag.DEFAULT),
    ]

    active_flags = [flag for option, flag in filters if option]

    # Could refactor later to just put all flags in lists and avoid this to_list
    def to_list(flag: PhoaFlag | list[PhoaFlag]) -> list[PhoaFlag]:
        return flag if isinstance(flag, list) else [flag]

    locations = {
        name: data for name, data in locations.items() if all(flag in active_flags for flag in to_list(data.flags))
    }

    # TODO: only for development
    locations = {
        name: data for name, data in locations.items() if data.address != 0
    }

    return locations
