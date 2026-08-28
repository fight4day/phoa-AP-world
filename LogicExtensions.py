import math

from BaseClasses import CollectionState
from .Options import PhoaOptions


class PhoaLogic:
    player: int

    def __init__(self, player: int):
        self.player = player

    def has_bat(self, state: CollectionState) -> bool:
        return (state.has_any({"Wooden Bat", "Composite Bat"}, self.player)
                or state.has("Progressive Bat", self.player, 1))

    def has_slingshot(self, state: CollectionState) -> bool:
        return (state.has_any({"Slingshot", "Treble Shot"}, self.player)
                or state.has("Progressive Slingshot", self.player, 1))

    def has_treble_shot(self, state: CollectionState) -> bool:
        return (state.has("Treble Shot", self.player)
                or state.has("Progressive Slingshot", self.player, 2))

    def has_bombs(self, state: CollectionState) -> bool:
        return (state.has_any({"Bombs", "Remote Bombs"}, self.player)
                or state.has("Progressive Bombs", self.player, 1))

    def has_crossbow(self, state: CollectionState) -> bool:
        return (state.has_any({"Civilian Crossbow", "Double Crossbow"}, self.player)
                or state.has("Progressive Crossbow", self.player, 1))

    def has_double_crossbow(self, state: CollectionState) -> bool:
        return (state.has("Double Crossbow", self.player)
                or state.has("Progressive Crossbow", self.player, 2))

    def has_sonic_spear(self, state: CollectionState) -> bool:
        return (state.has("Sonic Spear", self.player)
                or state.has("Progressive Spear", self.player, 1))

    def has_fishing_rod(self, state: CollectionState) -> bool:
        return (state.has_any({"Fishing Rod", "Serpent Rod"}, self.player)
                or state.has("Progressive Fishing Rod", self.player, 1))

    def has_serpant_rod(self, state: CollectionState) -> bool:
        return (state.has("Serpent Rod", self.player)
                or state.has("Progressive Fishing Rod", self.player, 2))

    def has_music_instrument(self, state: CollectionState):
        return state.has_any({"Bandit's Flute", "Spheralis"}, self.player)

    def has_light_source(self, state: CollectionState) -> bool:
        return (state.has_any({"Refurbished Crank Lamp", "Crank Lamp", "Neutron Lamp"}, self.player)
                or state.has("Progressive Crank Lamp", self.player, 1))

    def has_prelude_of_panselo(self, state: CollectionState) -> bool:
        return (state.has("Prelude of Panselo", self.player)
                or state.has("Progressive Prelude of Panselo", self.player))

    def has_moonstones(self, state: CollectionState, amount: int) -> bool:
        return (state.has("Moonstone", self.player, amount)
                or state.has("Moonstone Bundle", self.player, int(math.ceil(amount / 10))))

    def has_anuri_pearlstones(self, state: CollectionState, amount: int) -> bool:
        return (state.has("Anuri Pearlstone", self.player, amount)
                or state.has("Anuri Pearlstone Necklace", self.player))

    def has_ouro_guard_keys(self, state: CollectionState, amount: int) -> bool:
        return (state.has("Ouro Guard Key", self.player, amount)
                or state.has("Ouro Guard Keyring", self.player))

    def has_golem_medallions(self, state: CollectionState, amount: int, color: str) -> bool:
        return (state.has(f"{color} Golem Medallion", self.player, amount)
                or state.has(f"Big {color} Golem Medallion", self.player))

    def has_keycards(self, state: CollectionState, amount: int, card_type: str) -> bool:
        return (state.has(f"Keycard {card_type}", self.player, amount)
                or state.has(f"Master Keycard {card_type}", self.player))

    def has_lunar_artifacts(self, amount: int, state: CollectionState) -> bool:
        return state.has_from_list([
            "Lunar Drake",
            "Lunar Compass",
            "Lunar Comb",
            "Lunar Watch",
            "Lunar Goblet",
            "Lunar Frog",
            "Lunar Vase",
            "Lunar Trident",
            "Lunar Crown",
            "Lunar Medal",
            "Lunar Key",
            "Lunar Egg",
        ], self.player, amount)

    def can_use_spear_bomb(self, state: CollectionState) -> bool:
        return (state.has_all({"Sonic Spear", "Spear Bomb"}, self.player)
                or state.has("Progressive Spear", self.player, 2))

    def can_use_spear_bomb_midair(self, state: CollectionState) -> bool:
        return state.has("Temperance", self.player) and (
                 state.has_all({"Sonic Spear", "Spear Bomb"}, self.player)
                 or state.has("Progressive Spear", self.player, 2)
               )

    def can_use_whirlwind(self, state: CollectionState) -> bool:
        return (state.has_all({"Whirlwind", "Temperance"}, self.player)
                and self.has_bat(state))

    def has_explosives(self, state: CollectionState) -> bool:
        return (self.has_bombs(state)
                or self.can_use_spear_bomb(state)
                or state.has("Kobold Blaster", self.player))

    def has_explosives_midair(self, state: CollectionState) -> bool:
        return (self.has_bombs(state)
                or self.can_use_spear_bomb_midair(state)
                or state.has("Kobold Blaster", self.player))

    def can_deal_damage(self, state: CollectionState, exclude_rocket_boots=False, exclude_lamp=False) -> bool:
        return (self.has_bat(state)
                or self.has_slingshot(state)
                or self.has_bombs(state)
                or self.has_crossbow(state)
                or self.has_sonic_spear(state)
                or (state.has("Rocket Boots", self.player) and not exclude_rocket_boots)
                or (state.has("Refurbished Crank Lamp", self.player) and not exclude_lamp)
                or state.has("Kobold Blaster", self.player))

    def can_reasonably_kill_enemies(self, state: CollectionState, exclude_slingshot: bool = False,
                                    exclude_rocket_boots: bool = False) -> bool:
        return (self.has_bat(state)
                or (self.has_slingshot(state) and not exclude_slingshot)
                or self.has_bombs(state)
                or self.has_crossbow(state)
                or self.has_sonic_spear(state)
                or state.has("Kobold Blaster", self.player)
                or state.has("Rocket Boots", self.player) and not exclude_rocket_boots)

    def can_reasonably_kill_flying_enemies(self, state: CollectionState, exclude_slingshot: bool = False) -> bool:
        return ((self.has_slingshot(state) and not exclude_slingshot)
                or self.has_bombs(state)
                or self.has_crossbow(state)
                or state.has("Kobold Blaster", self.player))

    def can_reasonably_defeat_medium_encounters(self, state: CollectionState) -> bool:
        # TODO: should include health/stamina requirements
        return (self.has_bat(state)
                or self.has_double_crossbow(state)
                or self.has_sonic_spear(state)
                or state.has("Kobold Blaster", self.player))

    def can_break_big_object_with_tools(self, state: CollectionState, exclude_spear: bool = False) -> bool:
        return (self.has_bat(state)
                or self.has_slingshot(state)
                or self.has_bombs(state)
                or self.has_crossbow(state)
                or (self.has_sonic_spear(state) and not exclude_spear)
                or state.has_any({"Kobold Blaster", "Rocket Boots"}, self.player))

    def can_hit_switch_from_a_distance(self, state: CollectionState,
                                       exclude_slingshot: bool = False,
                                       exclude_bombs: bool = False) -> bool:
        return ((self.has_slingshot(state) and not exclude_slingshot)
                or (self.has_bombs(state) and not exclude_bombs)
                or self.has_crossbow(state)
                or self.has_sonic_spear(state)
                or state.has("Kobold Blaster", self.player))

    def can_reasonably_kill_mice(self, state: CollectionState) -> bool:
        return (self.has_bat(state)
                or self.has_slingshot(state)
                or self.has_crossbow(state)
                or state.has("Kobold Blaster", self.player))

    def can_balo(self, state: CollectionState) -> bool:
        return (self.has_bat(state)
                or self.has_treble_shot(state)
                or self.has_bombs(state)
                or self.has_sonic_spear(state)
                or self.has_double_crossbow(state)
                or state.has_any({"Kobold Blaster", "Rocket Boots"}, self.player))

    def can_clear_atai_expert_gallery(self, state: CollectionState) -> bool:
        return (self.has_treble_shot(state)
                or self.has_double_crossbow(state) and state.has("Energy Gem", self.player, 4)
                or self.can_use_spear_bomb(state)
                or state.has("Kobold Blaster", self.player))

    def can_clear_ancient_vault(self, state: CollectionState) -> bool:
        # TODO: Even with this it's almost impossible
        return (state.has("Spheralis", self.player)
                and self.has_double_crossbow(state)
                and state.has("Rocket Boots", self.player)
                and state.has("Kobold Blaster", self.player)
                and state.has("Energy Gem", self.player, 8))

    def can_defeat_great_drake(self, state: CollectionState) -> bool:
        return (state.has("Heart Ruby", self.player, 2)
                and (
                 (self.has_bombs(state) and self.has_bat(state))
                 or state.has("Kobold Blaster", self.player)
                ))

    def can_defeat_wrecker(self, state: CollectionState) -> bool:
        return (state.has("Heart Ruby", self.player, 5)
                and self.has_bat(state))

    def can_defeat_katash(self, state: CollectionState) -> bool:
        return (state.has("Heart Ruby", self.player, 8)
                and self.has_sonic_spear(state)
                and (self.has_crossbow(state) or self.has_slingshot(state)))

    def can_do_fran_quest_chain(self, state: CollectionState, quest_number: int) -> bool:
        # TODO: adjust moonstone cost for Thomas shop later
        return (self.has_explosives(state) and (state.can_reach_region("panselo_region", self.player))  # Free Fran
                and (self.has_moonstones(state, quest_number * 10)) if quest_number > 0 else True)

    FRANWAY_QUEST_NUMBERS = {"Panselo": 1, "Atai": 2, "Cosette": 3}

    def can_use_franway(self, state: CollectionState, franway_region: str, options: PhoaOptions) -> bool:
        quest_number = self.FRANWAY_QUEST_NUMBERS.get(franway_region)
        if quest_number is None:
            raise Exception(f"Unknown region received: {franway_region}")

        if options.franway_unlock_mode.value == 0:
            return False
        if options.franway_unlock_mode.value == 1:
            return self.can_do_fran_quest_chain(state, quest_number)
        if options.franway_unlock_mode.value == 2:
            return self.has_moonstones(state, quest_number * 10)
        if options.franway_unlock_mode.value == 3:
            return state.has(f"{franway_region} Franway Teleporter", self.player)
        return True
