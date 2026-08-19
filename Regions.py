from typing import Dict, Callable, Optional, NamedTuple

from BaseClasses import MultiWorld, Region, Location, CollectionState
from worlds.phoa import get_location_data, PhoaOptions
from worlds.phoa.Locations import PhoaLocationData
from worlds.phoa.LogicExtensions import PhoaLogic


class PhoaExit(NamedTuple):
    name: str
    region: str
    connection: str
    rule: Optional[Callable[[CollectionState], bool]] = None
    one_way: bool = False


def get_exit_data(player: int, options: PhoaOptions) -> list[PhoaExit]:
    logic = PhoaLogic(player)

    exits: list[PhoaExit] = [
        # Menu
        PhoaExit(
            name="game_start",
            region="Menu",
            connection="panselo_village",
            one_way=True,
        ),
        # panselo_village
        PhoaExit(
            name="panselo_gate",
            region="panselo_village",
            connection="panselo_region",
            rule=lambda state: logic.can_deal_damage(state)
                               or options.open_panselo_gates > 0,
        ),
        PhoaExit(
            name="rutea's_lab_gate",
            region="panselo_village",
            connection="panselo_village_rutea's_lab",
            rule=lambda state: logic.can_hit_switch_from_a_distance(state),
        ),
        # panselo_region
        PhoaExit(
            name="anuri_temple_entrance",
            region="panselo_region",
            connection="anuri_temple(main_entrance)",
            rule=lambda state: logic.can_hit_switch_from_a_distance(state),
        ),
        PhoaExit(
            name="anuri_temple_side_entrance",
            region="panselo_region",
            connection="anuri_temple(side_entrance)",
            rule=lambda state: logic.has_explosives(state),
        ),
        PhoaExit(
            name="over_anuri_temple",
            region="panselo_region",
            connection="anuri_temple(slargummy_boss)",
            rule=lambda state: logic.has_sonic_spear(state),
            one_way=True,
        ),
        PhoaExit(
            name="panselo_region_to_atai_region",
            region="panselo_region",
            connection="atai_region",
        ),
        PhoaExit(
            name="panselo_region_to_lake_laboratory",
            region="panselo_region",
            connection="lake_laboratory",
            rule=lambda state: logic.can_use_franway(state, "Panselo", options),
        ),
        # anuri_temple(main_entrance)
        PhoaExit(
            name="anuri_temple_main_exit",
            region="anuri_temple(main_entrance)",
            connection="panselo_region",
        ),
        PhoaExit(
            name="anuri_temple_pearl_entrance",
            region="anuri_temple(main_entrance)",
            connection="anuri_temple(main)",
            rule=lambda state: logic.has_anuri_pearlstones(state, 1)
        ),
        PhoaExit(
            name="anuri_temple_top_floor_boulder",
            region="anuri_temple(main_entrance)",
            connection="anuri_temple(top_floor)",
            rule=lambda state: logic.has_explosives(state)
                               or (logic.has_sonic_spear(state)
                                   and state.has("Rocket Boots", player)),
        ),
        # anuri_temple(top_floor)
        PhoaExit(
            name="anuri_temple_drop_to_throne",
            region="anuri_temple(top_floor)",
            connection="anuri_temple(main)",
            one_way=True,
        ),
        PhoaExit(
            name="anuri_temple_door_to_scaber_maze",
            region="anuri_temple(top_floor)",
            connection="anuri_temple(scaber_switch_maze)",
            rule=lambda state: logic.has_anuri_pearlstones(state, 10)
        ),
        # anuri_temple(main)
        PhoaExit(
            name="anuri_temple_to_main_entrance",
            region="anuri_temple(main)",
            connection="anuri_temple(main_entrance)",
        ),
        PhoaExit(
            name="anuri_temple_to_tall_tower_puzzle_room",
            region="anuri_temple(main)",
            connection="anuri_temple(tall_tower_puzzle_room)",
            rule=lambda state: logic.has_anuri_pearlstones(state, 10),
        ),
        PhoaExit(
            name="anuri_temple_to_side_entrance",
            region="anuri_temple(main)",
            connection="anuri_temple(side_entrance)",
        ),
        PhoaExit(
            name="anuri_temple_to_basement",
            region="anuri_temple(main)",
            connection="anuri_temple(basement)",
            rule=lambda state: logic.has_explosives(state),
        ),
        PhoaExit(
            name="anuri_temple_bridge_switch",
            region="anuri_temple(main)",
            connection="anuri_temple(moveable_bridge_area)",
            rule=lambda state: logic.can_hit_switch_from_a_distance(state)
                               or state.has("Rocket Boots", player),
        ),
        PhoaExit(
            name="anuri_temple_to_slargummy",
            region="anuri_temple(main)",
            connection="anuri_temple(slargummy_boss)",
            rule=lambda state: logic.has_anuri_pearlstones(state, 6),
        ),
        # anuri_temple(side_entrance)
        PhoaExit(
            name="anuri_temple_side_exit",
            region="anuri_temple(side_entrance)",
            connection="panselo_region",
            rule=lambda state: logic.has_explosives(state),
        ),
        PhoaExit(
            name="anuri_temple_side_to_main",
            region="anuri_temple(side_entrance)",
            connection="anuri_temple(main)",
            rule=lambda state: state.has("Anuri Temple - Side entrance gate opened", player),
        ),
        # anuri_temple(slargummy_boss)
        PhoaExit(
            name="anuri_temple_slargummy_to_main",
            region="anuri_temple(slargummy_boss)",
            connection="anuri_temple(main)",
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
        ),
        PhoaExit(
            name="anuri_temple_slargummy_to_pond",
            region="anuri_temple(slargummy_boss)",
            connection="anuri_temple(pond)",
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
        ),
        # anuri_temple(pond)
        PhoaExit(
            name="anuri_temple_to_post_pond",
            region="anuri_temple(pond)",
            connection="anuri_temple(post_pond)",
            rule=lambda state: logic.has_anuri_pearlstones(state, 9),
        ),
        # anuri_temple(post_pond)
        PhoaExit(
            name="anuri_temple_to_dive_room",
            region="anuri_temple(post_pond)",
            connection="anuri_temple(dive_room)",
            rule=lambda state: logic.has_anuri_pearlstones(state, 10),
        ),
        PhoaExit(
            name="anuri_temple_to_urn_room",
            region="anuri_temple(post_pond)",
            connection="anuri_temple(urn_room)",
            rule=lambda state: logic.has_bombs(state)
                               or state.has("Rocket Boots", player),
        ),
        # atai_region
        PhoaExit(
            name="atai_region_to_panselo",
            region="atai_region",
            connection="panselo_region",
        ),
        PhoaExit(
            name="atai_region_to_adars_house",
            region="atai_region",
            connection="adars_house",
        ),
        PhoaExit(
            name="atai_region_to_town",
            region="atai_region",
            connection="atai_town",
        ),
        PhoaExit(
            name="atai_region_to_sand_drifts_access_cave",
            region="atai_region",
            connection="sand_drifts_region(access_cave)",
        ),
        PhoaExit(
            name="atai_region_to_moonlight_ravine_south",
            region="atai_region",
            connection="moonlight_ravine(south)",
        ),
        PhoaExit(
            name="kingdom_bridge_south_kingdom_bridge_north",
            region="atai_region",
            connection="daea_region",
            rule=lambda state: (state.has("Life Saver", player)
                                and logic.has_sonic_spear(state))
                               or state.has("Rocket Boots", player),
        ),
        PhoaExit(
            name="atai_region_to_lake_laboratory",
            region="atai_region",
            connection="lake_laboratory",
            rule=lambda state: logic.can_use_franway(state, "Atai", options),
        ),
        # adars_house
        PhoaExit(
            name="adars_house_east_exit",
            region="adars_house",
            connection="atai_region",
        ),
        PhoaExit(
            name="adars_house_to_cave",
            region="adars_house",
            connection="adars_house(cave)",
            rule=lambda state: logic.has_explosives(state),
        ),
        PhoaExit(
            name="adars_house_to_top_of_cave",
            region="adars_house",
            connection="adars_house(cave_top)",
            rule=lambda state: state.has("Rocket Boots", player),
        ),
        # adars_house(cave)
        PhoaExit(
            name="adars_cave_to_top",
            region="adars_house(cave)",
            connection="adars_house(cave_top)",
        ),
        PhoaExit(
            name="adars_cave_to_ancient_vault",
            region="adars_house(cave)",
            connection="ancient_vault",
            rule=lambda state: logic.has_light_source(state)
                               and logic.has_explosives(state)
                               and state.has("Spheralis", player),
        ),
        # adars_house(cave_top)
        PhoaExit(
            name="adar_top_of_cave_to_main_cave",
            region="adars_house(cave_top)",
            connection="adars_house(cave)",
            rule=lambda state: logic.has_explosives(state),
        ),
        # ancient_vault
        PhoaExit(
            name="ancient_vault_to_printer_room",
            region="ancient_vault",
            connection="ancient_vault(printer_room)",
            rule=lambda state: logic.can_clear_ancient_vault(state),
        ),
        # atai_town
        PhoaExit(
            name="atai_town_exit",
            region="atai_town",
            connection="atai_region",
        ),
        PhoaExit(
            name="atai_town_to_weapon_shop_dropper",
            region="atai_town",
            connection="atai_town(weapons_shop_dropper)",
            rule=lambda state: state.has("Rocket Boots", player),
        ),
        PhoaExit(
            name="atai_town_to_sewer",
            region="atai_town",
            connection="atai_town(sewer)",
            rule=lambda state: logic.has_light_source(state),
        ),
        # atai_town(metro)
        PhoaExit(
            name="atai_town_metro_to_sand_drifts",
            region="atai_town(metro)",
            connection="sand_drifts(metro_stairwell)",
            rule=lambda state: logic.has_ouro_guard_keys(state, 5),
        ),
        PhoaExit(
            name="atai_metro_to_town",
            region="atai_town(metro)",
            connection="atai_town(sewer)",
            rule=lambda state: logic.has_light_source(state),
        ),
        # atai_town(sewer)
        PhoaExit(
            name="atai_sewer_to_town",
            region="atai_town(sewer)",
            connection="atai_town",
        ),
        PhoaExit(
            name="atai_sewer_to_metro",
            region="atai_town(sewer)",
            connection="atai_town(metro)",
            rule=lambda state: state.has_any({"Life Saver", "Rocket Boots"}, player),
        ),
        # sand_drifts_region(access_cave)
        PhoaExit(
            name="sand_drifts_access_cave_to_atai_region",
            region="sand_drifts_region(access_cave)",
            connection="atai_region",
        ),
        PhoaExit(
            name="sand_drifts_access_cave_to_sand_drifts_region",
            region="sand_drifts_region(access_cave)",
            connection="sand_drifts_region",
            rule=lambda state: logic.has_music_instrument(state)
                               and state.has("Song of Ouroboros", player),
        ),
        # sand_drifts_region
        PhoaExit(
            name="sand_drifts_region_to_access_cave",
            region="sand_drifts_region",
            connection="sand_drifts_region(access_cave)",
            rule=lambda state: logic.has_music_instrument(state)
                               and state.has("Song of Ouroboros", player),
        ),
        PhoaExit(
            name="sand_drifts_region_to_ancient_geo_dungeon",
            region="sand_drifts_region",
            connection="sand_drifts_region(ancient_geo_dungeon)",
            rule=lambda state: logic.has_music_instrument(state)
                               or (logic.has_sonic_spear(state)
                                   and state.has_any({"Life Saver", "Rocket Boots"}, player)),
        ),
        PhoaExit(
            name="sand_drifts_region_to_main",
            region="sand_drifts_region",
            connection="sand_drifts",
        ),
        # sand_drifts
        PhoaExit(
            name="sand_drifts_east_exit",
            region="sand_drifts",
            connection="sand_drifts_region",
        ),
        PhoaExit(
            name="sand_drifts_to_metro_stairwell",
            region="sand_drifts",
            connection="sand_drifts(metro_stairwell)",
            rule=lambda state: logic.has_explosives(state),
        ),
        PhoaExit(
            name="sand_drifts_to_ouroboros_hideout_tower_top",
            region="sand_drifts",
            connection="ouroboros_hideout(tower_top)",
            rule=lambda state: logic.has_sonic_spear(state)
                               or state.has("Rocket Boots", player),
        ),
        PhoaExit(
            name="sand_drifts_to_chest_trap",
            region="sand_drifts",
            connection="sand_drifts(chest_trap_room)",
            rule=lambda state: logic.can_deal_damage(state, exclude_lamp=True),
        ),
        PhoaExit(
            name="sand_drifts_to_storage_room",
            region="sand_drifts",
            connection="sand_drifts(storage_room)",
            rule=lambda state: logic.can_deal_damage(state, exclude_lamp=True),
        ),
        PhoaExit(
            name="sand_drifts_to_shrine",
            region="sand_drifts",
            connection="sand_drifts(ouroboros_shrine)",
            rule=lambda state: logic.has_music_instrument(state)
                               and state.has_all({"Song of Ouroboros", "Rocket Boots"}, player),
        ),
        PhoaExit(
            name="sand_drifts_to_forlorn_ruins",
            region="sand_drifts",
            connection="forlorn_ruins",
            rule=lambda state: logic.has_music_instrument(state)
                               and state.has("Song of Ouroboros", player),
        ),
        PhoaExit(
            name="sand_drifts_to_forlorn_ruins_top_path",
            region="sand_drifts",
            connection="forlorn_ruins(top_path)",
            rule=lambda state: state.has("Rocket Boots", player),
        ),
        # sand_drifts(metro_stairwell)
        # Could use an exit to ouroboros hideout but logic doesn't require one
        PhoaExit(
            name="sand_drifts_metro_stairwell_to_main",
            region="sand_drifts(metro_stairwell)",
            connection="sand_drifts",
        ),
        PhoaExit(
            name="sand_drifts_metro_stairwell_to_atai_metro",
            region="sand_drifts(metro_stairwell)",
            connection="atai_town(metro)",
            rule=lambda state: logic.has_ouro_guard_keys(state, 5),
        ),
        # ouroboros_hideout(tower_top)
        PhoaExit(
            name="ouroboros_tower_top_to_sand_drifts",
            region="ouroboros_hideout(tower_top)",
            connection="sand_drifts",
        ),
        PhoaExit(
            name="ouroboros_tower_downwards",
            region="ouroboros_hideout(tower_top)",
            connection="ouroboros_hideout(tower)",
            one_way=True,
        ),
        # ouroboros_hideout(tower)
        PhoaExit(
            name="ouroboros_hideout_tower_to_top",
            region="ouroboros_hideout(tower)",
            connection="ouroboros_hideout(tower_top)",
            rule=lambda state: logic.has_sonic_spear(state),
        ),
        PhoaExit(
            name="ouroboros_hideout_tower_to_main",
            region="ouroboros_hideout(tower)",
            connection="ouroboros_hideout",
        ),
        # forlorn_ruins(top_path)
        PhoaExit(
            name="forlorn_ruins_top_path_to_main",
            region="forlorn_ruins(top_path)",
            connection="forlorn_ruins",
            one_way=True,
        ),
        PhoaExit(
            name="forlorn_ruins_top_path_to_fountain",
            region="forlorn_ruins(top_path)",
            connection="forlorn_ruins(fountain_room)",
            rule=lambda state: state.has("Rocket Boots", player)
                               or logic.has_sonic_spear(state),
            one_way=True,
        ),
        # forlorn_ruins(fountain_room)
        PhoaExit(
            name="forlorn_ruins_fountain_to_main",
            region="forlorn_ruins(fountain_room)",
            connection="forlorn_ruins",
        ),
        PhoaExit(
            name="forlorn_ruins_fountain_to_top_path",
            region="forlorn_ruins(fountain_room)",
            connection="forlorn_ruins(top_path)",
            rule=lambda state: logic.has_sonic_spear(state),
        ),
        # forlorn_ruins
        PhoaExit(
            name="forlorn_ruins_to_top_path",
            region="forlorn_ruins",
            connection="forlorn_ruins(top_path)",
            rule=lambda state: logic.has_sonic_spear(state),
        ),
        PhoaExit(
            name="forlorn_ruins_to_fountain",
            region="forlorn_ruins",
            connection="forlorn_ruins(fountain_room)",
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
        ),
        PhoaExit(
            name="forlorn_ruins_to_bombable_wall",
            region="forlorn_ruins",
            connection="forlorn_ruins(bombable_wall)",
            rule=lambda state: logic.has_explosives(state),
        ),
        PhoaExit(
            name="forlorn_ruins_through_key_door_to_obstacle_course",
            region="forlorn_ruins",
            connection="forlorn_ruins(arrow_obstacle_room)",
            rule=lambda state: logic.has_ouro_guard_keys(state, 5),
        ),
        PhoaExit(
            name="forlorn_ruins_to_metal_crates_puzzle_area",
            region="forlorn_ruins",
            connection="forlorn_ruins(metal_crates_puzzle_area)",
            rule=lambda state: logic.has_bombs(state)
                               or logic.has_sonic_spear(state),
        ),
        # forlorn_ruins(metal_crates_puzzle_area)
        PhoaExit(
            name="forlorn_ruins_puzzle_area_to_main",
            region="forlorn_ruins(metal_crates_puzzle_area)",
            connection="forlorn_ruins",
            one_way=True,
        ),
        PhoaExit(
            name="forlorn_ruins_puzzle_area_to_trap_switches",
            region="forlorn_ruins(metal_crates_puzzle_area)",
            connection="forlorn_ruins(trap_switches_puzzle_area)",
            rule=lambda state: logic.has_explosives(state),
        ),
        # forlorn_ruins(trap_switches_puzzle_area)
        PhoaExit(
            name="forlorn_ruins_trap_switches_to_metal_creates_puzzle_area",
            region="forlorn_ruins(trap_switches_puzzle_area)",
            connection="forlorn_ruins(metal_crates_puzzle_area)",
            rule=lambda state: logic.has_explosives(state),
        ),
        PhoaExit(
            name="forlorn_ruins_trap_switches_puzzle_area_to_east",
            region="forlorn_ruins(trap_switches_puzzle_area)",
            connection="forlorn_ruins(east)",
            rule=lambda state: logic.has_slingshot(state)
                               or logic.has_bombs(state)
                               or state.has("Kobold Blaster", player)
                               or logic.has_sonic_spear(state),
        ),
        # forlorn_ruins(east)
        PhoaExit(
            name="forlorn_ruins_east_to_trap_switches_puzzle_area",
            region="forlorn_ruins(east)",
            connection="forlorn_ruins(trap_switches_puzzle_area)",
            one_way=True,
        ),
        PhoaExit(
            name="forlorn_ruins_east_key_door_in_basement",
            region="forlorn_ruins(east)",
            connection="forlorn_ruins(dragon_snare_puzzle_room)",
            rule=lambda state: logic.has_ouro_guard_keys(state, 5),
        ),
        PhoaExit(
            name="forlorn_ruins_to_ouroboros_hideout",
            region="forlorn_ruins(east)",
            connection="ouroboros_hideout",
            rule=lambda state: logic.has_explosives(state)
                               and logic.has_music_instrument(state)
                               and state.has("Song of Ouroboros", player),
        ),
        # ouroboros_hideout
        PhoaExit(
            name="ouroboros_hideout_to_forlorn_ruins",
            region="ouroboros_hideout",
            connection="forlorn_ruins(east)",
            rule=lambda state: logic.has_explosives(state)
                               and logic.has_music_instrument(state)
                               and state.has("Song of Ouroboros", player),
        ),
        PhoaExit(
            name="ouroboros_hideout_to_prison",
            region="ouroboros_hideout",
            connection="ouroboros_hideout(prison)",
            rule=lambda state: logic.has_ouro_guard_keys(state, 5),
        ),
        PhoaExit(
            name="ouroboros_hideout_to_storage",
            region="ouroboros_hideout",
            connection="ouroboros_hideout(storage)",
            rule=lambda state: logic.has_ouro_guard_keys(state, 5),
        ),
        PhoaExit(
            name="ouroboros_hideout_to_infant_drake_arena",
            region="ouroboros_hideout",
            connection="ouroboros_hideout(infant_drake_arena)",
            rule=lambda state: logic.can_reasonably_kill_enemies(state, exclude_slingshot=True),
        ),
        PhoaExit(
            name="ouroboros_hideout_to_treasure_room",
            region="ouroboros_hideout",
            connection="ouroboros_hideout(treasure_room)",
            rule=lambda state: logic.has_music_instrument(state),
        ),
        PhoaExit(
            name="sand_drifts_metro_stairwell_to_ouroboros_hideout",
            region="ouroboros_hideout",
            connection="sand_drifts(metro_stairwell)",
            rule=lambda state: logic.has_bat(state)
                               or state.has("Kobold Blaster", player),
        ),
        PhoaExit(
            name="ouroboros_hideout_to_great_drake_arena",
            region="ouroboros_hideout",
            connection="ouroboros_hideout(great_drake_arena)",
            rule=lambda state: state.has("Ouroboros Proof", player, 3),
        ),
        # ouroboros_hideout(storage)
        PhoaExit(
            name="ouroboros_hideout_storage_to_back_side",
            region="ouroboros_hideout(storage)",
            connection="ouroboros_hideout(storage_back)",
            rule=lambda state: logic.has_bombs(state),
        ),
        # ouroboros_hideout(treasure_room)
        PhoaExit(
            name="ouroboros_hideout_treasure_room_to_hidden_area",
            region="ouroboros_hideout(treasure_room)",
            connection="ouroboros_hideout(treasure_room_hidden_area)",
            rule=lambda state: logic.has_explosives(state),
        ),
        # moonlight_ravine(south)
        PhoaExit(
            name="moonlight_ravine_south_to_atai",
            region="moonlight_ravine(south)",
            connection="atai_region",
        ),
        PhoaExit(
            name="moonlight_ravine_south_to_wilds",
            region="moonlight_ravine(south)",
            connection="moonlight_ravine(wilds)",
            rule=lambda state: state.has("Life Saver", player)
                               or state.has("Rocket Boots", player),
        ),
        # moonlight_ravine(wilds)
        PhoaExit(
            name="moonlight_ravine_wilds_to_south",
            region="moonlight_ravine(wilds)",
            connection="moonlight_ravine(south)",
            rule=lambda state: state.has("Life Saver", player)
                               or state.has("Rocket Boots", player),
        ),
        PhoaExit(
            name="moonlight_ravine_wilds_to_north",
            region="moonlight_ravine(wilds)",
            connection="moonlight_ravine(north)",
            rule=lambda state: state.has("Life Saver", player)
                               or state.has("Rocket Boots", player),
        ),
        # moonlight_ravine(north)
        PhoaExit(
            name="moonlight_ravine_north_to_wilds",
            region="moonlight_ravine(north)",
            connection="moonlight_ravine(wilds)",
            rule=lambda state: state.has("Life Saver", player)
                               or state.has("Rocket Boots", player),
        ),
        PhoaExit(
            name="moonlight_ravine_north_to_daea_region",
            region="moonlight_ravine(north)",
            connection="daea_region",
        ),
        # daea_region
        PhoaExit(
            name="daea_region_to_daea_city",
            region="daea_region",
            connection="daea_city",
        ),
        PhoaExit(
            name="daea_region_to_thomas_lab_2",
            region="daea_region",
            connection="thomas_lab_2",
            rule=lambda state: logic.has_golem_medallions(state, 3, "Blue"),
        ),
        PhoaExit(
            name="daea_region_to_lake_laboratory",
            region="daea_region",
            connection="lake_laboratory",
        ),
        # thomas_lab_2
        PhoaExit(
            name="thomas_lab_2_to_daea_region",
            region="thomas_lab_2",
            connection="daea_region",
        ),
        PhoaExit(
            name="thomas_lab_2_to_thomas_lab_3",
            region="thomas_lab_2",
            connection="thomas_lab_3",
            rule=lambda state: logic.has_golem_medallions(state, 3, "Red"),
        ),
        # thomas_lab_3
        PhoaExit(
            name="thomas_lab_3_to_thomas_lab_2",
            region="thomas_lab_3",
            connection="thomas_lab_2",
        ),
        # Franways
        PhoaExit(
            name="lake_laboratory_to_daea_region",
            region="lake_laboratory",
            connection="daea_region",
        ),
        PhoaExit(
            name="lake_laboratory_to_panselo_region",
            region="lake_laboratory",
            connection="panselo_region",
            rule=lambda state: logic.can_use_franway(state, "Panselo", options),
        ),
        PhoaExit(
            name="lake_laboratory_to_atai_region",
            region="lake_laboratory",
            connection="atai_region",
            rule=lambda state: logic.can_use_franway(state, "Atai", options),
        ),
        PhoaExit(
            name="lake_laboratory_to_cosette_region",
            region="lake_laboratory",
            connection="cosette_region",
            rule=lambda state: logic.can_use_franway(state, "Cosette", options),
        ),
        # daea_city
        PhoaExit(
            name="daea_city_to_geo_dungeon",
            region="daea_city",
            connection="daea_city(geo_dungeon)",
            rule=lambda state: state.has("Rocket Boots", player),
        ),
        PhoaExit(
            name="daea_city_to_seer",
            region="daea_city",
            connection="daea_city(seer)",
            rule=lambda state: state.has("Rocket Boots", player),
        ),
        PhoaExit(
            name="daea_city_to_tunnels",
            region="daea_city",
            connection="daea_tunnel_top_left",
        ),
        # daea_tunnel_top_left
        PhoaExit(
            name="daea_tunnel_top_left_to_middle",
            region="daea_tunnel_top_left",
            connection="daea_tunnel_middle_and_bottom_right",
        ),
        PhoaExit(
            name="daea_tunnel_top_left_to_top_right",
            region="daea_tunnel_top_left",
            connection="daea_tunnel_top_right",
            rule=lambda state: state.has("Rocket Boots", player),
        ),
        # daea_tunnel_middle_and_bottom_right
        PhoaExit(
            name="daea_tunnel_middle_to_top_left",
            region="daea_tunnel_middle_and_bottom_right",
            connection="daea_tunnel_top_left",
            rule=lambda state: logic.has_slingshot(state)
                               or logic.has_bombs(state)
                               or logic.has_sonic_spear(state)
                               or state.has("Rocket Boots", player),
        ),
        PhoaExit(
            name="daea_tunnel_middle_to_top_right",
            region="daea_tunnel_middle_and_bottom_right",
            connection="daea_tunnel_top_right",
            rule=lambda state: state.has("Daea tunnel gate opened", player) and
                               (logic.has_slingshot(state)
                                or logic.has_bombs(state)
                                or logic.has_sonic_spear(state)
                                or state.has("Rocket Boots", player)),
        ),
        PhoaExit(
            name="daea_tunnel_middle_to_bottom_left",
            region="daea_tunnel_middle_and_bottom_right",
            connection="daea_tunnel_bottom_left",
            rule=lambda state: logic.has_light_source(state),
        ),
        # daea_tunnel_top_right
        PhoaExit(
            name="daea_tunnel_top_right_to_middle",
            region="daea_tunnel_top_right",
            connection="daea_tunnel_middle_and_bottom_right",
            rule=lambda state: state.has("Daea tunnel gate opened", player)
                               or state.has("Life Saver", state),
        ),
        PhoaExit(
            name="daea_tunnel_top_right_to_top_left",
            region="daea_tunnel_top_right",
            connection="daea_tunnel_top_left",
            rule=lambda state: state.has("Rocket Boots", player),
        ),
        PhoaExit(
            name="daea_tunnel_top_right_to_castle_dungeon",
            region="daea_tunnel_top_right",
            connection="castle_dungeon",
        ),
        # castle_dungeon
        PhoaExit(
            name="castle_dungeon_to_white_towers_entrance",
            region="castle_dungeon",
            connection="white_towers(entrance)",
            rule=lambda state: logic.has_sonic_spear(state),
        ),
        PhoaExit(
            name="castle_dungeon_post_control_room_fight",
            region="castle_dungeon",
            connection="castle_dungeon(post_control_room_fight)",
            rule=lambda state: logic.can_reasonably_defeat_medium_encounters(state),
        ),
        PhoaExit(
            name="castle_dungeon_to_c_hall",
            region="castle_dungeon",
            connection="castle_dungeon(c_hall)",
            rule=lambda state: state.has("Master Keycard C", player),
        ),
        PhoaExit(
            name="castle_dungeon_to_b_hall",
            region="castle_dungeon",
            connection="castle_dungeon(b_hall)",
            rule=lambda state: state.has("Master Keycard B", player),
        ),
        PhoaExit(
            name="castle_dungeon_to_a_hall",
            region="castle_dungeon",
            connection="castle_dungeon(a_hall)",
            rule=lambda state: state.has("Master Keycard A", player),
        ),
        # castle_dungeon(post_control_room_fight)
        PhoaExit(
            name="castle_dungeon_post_fight_return",
            region="castle_dungeon(post_control_room_fight)",
            connection="castle_dungeon",
        ),
        PhoaExit(
            name="castle_dungeon_post_fight_to_c_hall",
            region="castle_dungeon(post_control_room_fight)",
            connection="castle_dungeon(c_hall)",
            rule=lambda state: logic.has_keycards(state, 1, "C"),
        ),
        PhoaExit(
            name="castle_dungeon_post_fight_to_b_hall",
            region="castle_dungeon(post_control_room_fight)",
            connection="castle_dungeon(b_hall)",
            rule=lambda state: logic.has_keycards(state, 1, "B"),
        ),
        PhoaExit(
            name="castle_dungeon_post_fight_to_a_hall",
            region="castle_dungeon(post_control_room_fight)",
            connection="castle_dungeon(a_hall)",
            rule=lambda state: logic.has_keycards(state, 1, "A"),
        ),
        # castle_dungeon(c_hall)
        PhoaExit(
            name="c_hall_to_c_jail_cell",
            region="castle_dungeon(c_hall)",
            connection="castle_dungeon(c_jail_cell)",
            rule=lambda state: logic.has_keycards(state, 3, "C")
                               or (logic.has_sonic_spear(state) and logic.has_keycards(state, 1, "C")),
        ),
        # castle_dungeon(b_hall)
        PhoaExit(
            name="b_hall_to_b_jail_cell",
            region="castle_dungeon(b_hall)",
            connection="castle_dungeon(b_jail_cell)",
            rule=lambda state: logic.has_keycards(state, 3, "B"),
        ),
        # castle_dungeon(c_hall)
        PhoaExit(
            name="castle_dungeon_a_hall_to_main",
            region="castle_dungeon(a_hall)",
            connection="castle_dungeon",
            rule=lambda state: logic.has_keycards(state, 2, "A")
                               or logic.has_sonic_spear(state),
        ),
        PhoaExit(
            name="a_hall_to_arena",
            region="castle_dungeon(a_hall)",
            connection="castle_dungeon(a_hall_arena)",
            rule=lambda state: logic.has_keycards(state, 2, "A")
                               or logic.has_sonic_spear(state),
        ),
        # white_towers(entrance)
        PhoaExit(
            name="white_towers_entrance_to_puzzle_room",
            region="white_towers(entrance)",
            connection="white_towers(puzzle_room)",
            rule=lambda state: state.has("Rocket Boots", player)
                               and state.has("Energy Gem", player, 4),
        ),
        PhoaExit(
            name="white_towers_entrance_to_daea_region",
            region="white_towers(entrance)",
            connection="daea_region",
            rule=lambda state: logic.can_deal_damage(state),
        ),
        # NOTE: Logically (for regions), I'll assume the player has the sonic spear from here
        PhoaExit(
            name="white_towers_entrance_to_first_floor",
            region="white_towers(entrance)",
            connection="white_towers(main)",
            rule=lambda state: logic.has_sonic_spear(state),  # Treble shot (even slingshot) also activates switch
        ),
        # white_towers(main)
        PhoaExit(
            name="white_towers_main_to_entrance",
            region="white_towers(main)",
            connection="white_towers(entrance)",
        ),
        PhoaExit(
            name="white_towers_elevator_to_upper",
            region="white_towers(main)",
            connection="white_towers(upper)",
            rule=lambda state: logic.has_bombs(state)
                               or logic.has_slingshot(state),
        ),
        # white_towers(upper)
        PhoaExit(
            name="white_towers_upper_to_main",
            region="white_towers(upper)",
            connection="white_towers(main)",
        ),
        PhoaExit(
            name="white_towers_gates_to_katash",
            region="white_towers(upper)",
            connection="white_towers(katash)",
            rule=lambda state: logic.has_bombs(state)
                               or logic.has_slingshot(state)
                               or logic.has_crossbow(state)
                               or logic.can_use_spear_bomb(state),
        ),
        # white_towers(upper)
        PhoaExit(
            name="white_towers_katash_to_upper",
            region="white_towers(katash)",
            connection="white_towers(upper)",
        ),
        # cosette_region
        PhoaExit(
            name="cosette_region_to_lake_laboratory",
            region="cosette_region",
            connection="lake_laboratory",
            rule=lambda state: logic.can_use_franway(state, "Cosette", options),
        ),
    ]

    return exits


def create_regions_and_locations(world: MultiWorld, player: int, options: PhoaOptions):
    locations_per_region: Dict[str, Dict[str, PhoaLocationData]] = split_locations_per_region(
        get_location_data(player, options))

    regions = [
        create_region(world, player, locations_per_region, "Menu"),
        create_region(world, player, locations_per_region, "panselo_village"),
        create_region(world, player, locations_per_region, "panselo_village_rutea's_lab"),
        create_region(world, player, locations_per_region, "panselo_region"),
        create_region(world, player, locations_per_region, "anuri_temple(main_entrance)"),
        create_region(world, player, locations_per_region, "anuri_temple(top_floor)"),
        create_region(world, player, locations_per_region, "anuri_temple(scaber_switch_maze)"),
        create_region(world, player, locations_per_region, "anuri_temple(main)"),
        create_region(world, player, locations_per_region, "anuri_temple(tall_tower_puzzle_room)"),
        create_region(world, player, locations_per_region, "anuri_temple(side_entrance)"),
        create_region(world, player, locations_per_region, "anuri_temple(basement)"),
        create_region(world, player, locations_per_region, "anuri_temple(moveable_bridge_area)"),
        create_region(world, player, locations_per_region, "anuri_temple(slargummy_boss)"),
        create_region(world, player, locations_per_region, "anuri_temple(pond)"),
        create_region(world, player, locations_per_region, "anuri_temple(post_pond)"),
        create_region(world, player, locations_per_region, "anuri_temple(dive_room)"),
        create_region(world, player, locations_per_region, "anuri_temple(urn_room)"),
        create_region(world, player, locations_per_region, "atai_region"),
        create_region(world, player, locations_per_region, "adars_house"),
        create_region(world, player, locations_per_region, "atai_town"),
        create_region(world, player, locations_per_region, "atai_town(sewer)"),
        create_region(world, player, locations_per_region, "atai_town(weapons_shop_dropper)"),
        create_region(world, player, locations_per_region, "atai_town(metro)"),
        create_region(world, player, locations_per_region, "adars_house(cave)"),
        create_region(world, player, locations_per_region, "adars_house(cave_top)"),
        create_region(world, player, locations_per_region, "ancient_vault"),
        create_region(world, player, locations_per_region, "ancient_vault(printer_room)"),
        create_region(world, player, locations_per_region, "sand_drifts_region(access_cave)"),
        create_region(world, player, locations_per_region, "sand_drifts_region"),
        create_region(world, player, locations_per_region, "sand_drifts_region(ancient_geo_dungeon)"),
        create_region(world, player, locations_per_region, "sand_drifts"),
        create_region(world, player, locations_per_region, "sand_drifts(metro_stairwell)"),
        create_region(world, player, locations_per_region, "sand_drifts(chest_trap_room)"),
        create_region(world, player, locations_per_region, "sand_drifts(storage_room)"),
        create_region(world, player, locations_per_region, "sand_drifts(ouroboros_shrine)"),
        create_region(world, player, locations_per_region, "forlorn_ruins"),
        create_region(world, player, locations_per_region, "forlorn_ruins(top_path)"),
        create_region(world, player, locations_per_region, "forlorn_ruins(fountain_room)"),
        create_region(world, player, locations_per_region, "forlorn_ruins(bombable_wall)"),
        create_region(world, player, locations_per_region, "forlorn_ruins(arrow_obstacle_room)"),
        create_region(world, player, locations_per_region, "forlorn_ruins(metal_crates_puzzle_area)"),
        create_region(world, player, locations_per_region, "forlorn_ruins(trap_switches_puzzle_area)"),
        create_region(world, player, locations_per_region, "forlorn_ruins(east)"),
        create_region(world, player, locations_per_region, "forlorn_ruins(dragon_snare_puzzle_room)"),
        create_region(world, player, locations_per_region, "ouroboros_hideout"),
        create_region(world, player, locations_per_region, "ouroboros_hideout(tower_top)"),
        create_region(world, player, locations_per_region, "ouroboros_hideout(tower)"),
        create_region(world, player, locations_per_region, "ouroboros_hideout(prison)"),
        create_region(world, player, locations_per_region, "ouroboros_hideout(storage)"),
        create_region(world, player, locations_per_region, "ouroboros_hideout(storage_back)"),
        create_region(world, player, locations_per_region, "ouroboros_hideout(infant_drake_arena)"),
        create_region(world, player, locations_per_region, "ouroboros_hideout(treasure_room)"),
        create_region(world, player, locations_per_region, "ouroboros_hideout(treasure_room_hidden_area)"),
        create_region(world, player, locations_per_region, "ouroboros_hideout(great_drake_arena)"),
        create_region(world, player, locations_per_region, "moonlight_ravine(south)"),
        create_region(world, player, locations_per_region, "moonlight_ravine(wilds)"),
        create_region(world, player, locations_per_region, "moonlight_ravine(north)"),
        create_region(world, player, locations_per_region, "daea_city"),
        create_region(world, player, locations_per_region, "daea_city(geo_dungeon)"),
        create_region(world, player, locations_per_region, "daea_city(seer)"),
        create_region(world, player, locations_per_region, "thomas_lab_2"),
        create_region(world, player, locations_per_region, "thomas_lab_3"),
        create_region(world, player, locations_per_region, "daea_region"),
        create_region(world, player, locations_per_region, "lake_laboratory"),
        create_region(world, player, locations_per_region, "cosette_region"),
        create_region(world, player, locations_per_region, "daea_tunnel_top_left"),
        create_region(world, player, locations_per_region, "daea_tunnel_middle_and_bottom_right"),
        create_region(world, player, locations_per_region, "daea_tunnel_bottom_left"),
        create_region(world, player, locations_per_region, "daea_tunnel_top_right"),
        create_region(world, player, locations_per_region, "castle_dungeon"),
        create_region(world, player, locations_per_region, "castle_dungeon(post_control_room_fight)"),
        create_region(world, player, locations_per_region, "castle_dungeon(c_hall)"),
        create_region(world, player, locations_per_region, "castle_dungeon(c_jail_cell)"),
        create_region(world, player, locations_per_region, "castle_dungeon(b_hall)"),
        create_region(world, player, locations_per_region, "castle_dungeon(b_jail_cell)"),
        create_region(world, player, locations_per_region, "castle_dungeon(a_hall)"),
        create_region(world, player, locations_per_region, "castle_dungeon(a_hall_arena)"),
        create_region(world, player, locations_per_region, "white_towers(entrance)"),
        create_region(world, player, locations_per_region, "white_towers(puzzle_room)"),
        create_region(world, player, locations_per_region, "white_towers(main)"),
        create_region(world, player, locations_per_region, "white_towers(upper)"),
        create_region(world, player, locations_per_region, "white_towers(katash)"),
    ]

    world.regions += regions

    connect_regions(world, player, get_exit_data(player, options))


def create_region(world: MultiWorld, player: int, locations_per_region: Dict[str, Dict[str, PhoaLocationData]],
                  name: str) -> Region:
    region = Region(name, player, world)

    if name in locations_per_region:
        for location_name, location_data in locations_per_region[name].items():
            location = create_location(player, location_name, location_data, region)
            region.locations.append(location)

    return region


def create_location(player: int, location_name: str, location_data: PhoaLocationData, region: Region):
    location = Location(player, location_name, location_data.address, region)

    if location_data.rule:
        location.access_rule = location_data.rule

    return location


def connect_regions(world: MultiWorld, player: int, exits: list[PhoaExit]):
    for regionExit in exits:
        connect(world, player, regionExit.region, regionExit.connection, regionExit.rule, regionExit.name)


def connect(world: MultiWorld, player: int, source: str, target: str,
            rule: Optional[Callable[[CollectionState], bool]] = None, name: str = None):
    source_region = world.get_region(source, player)
    target_region = world.get_region(target, player)
    entrance = source_region.create_exit(name)

    if rule is not None:
        entrance.access_rule = rule

    entrance.connect(target_region)


def split_locations_per_region(locations: Dict[str, PhoaLocationData]):
    locations_per_region: Dict[str, Dict[str, PhoaLocationData]] = {}

    for location_name, location_data in locations.items():
        if location_data.region not in locations_per_region:
            locations_per_region[location_data.region] = {}

        locations_per_region[location_data.region][location_name] = location_data

    return locations_per_region
