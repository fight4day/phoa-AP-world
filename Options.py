from dataclasses import dataclass
from typing import Any

from Options import Toggle, PerGameCommonOptions, DeathLink, Choice, DefaultOnToggle, OptionGroup


class EnableMainQuestLocations(DefaultOnToggle):
    """Include locations usually containing items to complete the main quest. When disabled, core items will stay in the item pool and filler items are placed at these locations"""
    display_name = "Main quest item locations"


class EnableHeartRubyLocations(DefaultOnToggle):
    """Include Heart ruby locations."""
    display_name = "Heart Ruby locations"


class EnableEnergyGemLocations(DefaultOnToggle):
    """Include Energy gem locations."""
    display_name = "Energy Gem locations"


class EnableAncientVault(Toggle):
    """Include upgrades from Ancient Vault.
    Warning: The logical requirement to clear this is bare minimum. Even while having every item in the game I consider these checks extremely difficult. God gamers only."""
    display_name = "Ancient Vault upgrades"


class EnableMoonstoneLocations(DefaultOnToggle):
    """Include Moonstone locations."""
    display_name = "Moonstone locations"


class KeepExcludedStatusUpgradesInItemPool(DefaultOnToggle):
    """When enabled, Heart rubies, Energy gems and Moonstones will stay in the item pool if not included. Filler items are placed at the disabled locations.
    When disabled, these items can be acquired at their vanilla locations.
    Warning: disabling this setting is incompatible with certain other settings as these items are required in the pool"""
    display_name = "Keep status upgrades and moonstones in item pool when locations are excluded"


class EnableLunarArtifactLocations(DefaultOnToggle):
    """Include Lunar Artifact locations"""
    display_name = "Include Lunar Artifact locations"


class EnableFishingSpots(DefaultOnToggle):
    """Include items gotten from catching fish"""
    display_name = "Include fishing spots"


class EnableNpcGifts(Toggle):
    """Include free gifts from NPCs"""
    display_name = "Include NPC gifts"


class EnablePlantoRewards(Toggle):
    """Include rewards from Mr. Planto after giving them food units"""
    display_name = "Include Planto rewards"


class EnableItemsInBreakables(Toggle):
    """Include utility items found in breakable objects like pots and boxes"""
    display_name = "Include items in breakables objects"


class EnableSidequests(Toggle):
    """Include checks related to sidequests"""
    display_name = "Include sidequests"


class EnableFreestandingItems(Toggle):
    """Include utility items found in freestanding locations"""
    display_name = "Include freestanding items"


class EnableMinigames(Toggle):
    """Include items won through minigames"""
    display_name = "Include minigames"


class EnablePerros(Toggle):
    """Include findable Perros"""
    display_name = "Include Perros"


class EnableMisc(Toggle):
    """Include miscellaneous locations (Strange Urn & Atai berry selling reward)"""
    display_name = "Include miscellaneous"


class EnableShopSanity(Toggle):
    """Includes items that can be bought it shops"""
    display_name = "Shop sanity"


class EnableSmallAnimalDrops(Toggle):
    """Includes drops from animals like lizards, mice and scorpions"""
    display_name = "Include small animal drops"


class EnableRinLocations(Choice):
    """Includes rin pickups from chests and other breakables that give at least 5 rin"""
    display_name = "Include rin locations"
    option_no = 0
    option_chests_only = 1
    option_everything = 2
    default = 1


class EnableTrapChests(Toggle):
    """Includes chests that usually contain only 1 Rin"""
    display_name = "Include trap chests"


class EnableGEOChallengeRewards(Toggle):
    """Includes the rewards you get from completing GEO challenges"""
    display_name = "Include GEO challenge rewards"


class EnableOuroborosShrines(Toggle):
    """Includes the rewards at the end of Ouroboros Shrines"""
    display_name = "Include Ouroboros shrines"


class EnableOuroborosScrollRewards(Toggle):
    """Includes rewards from Atri for retrieving Ouroboros Scrolls"""
    display_name = "Include Ouroboros Scroll rewards"


class EnableLunarArtifactQuest(Toggle):
    """Includes Astrid's rewards for finding Lunar artifacts"""
    display_name = "Include Lunar Artifact rewards"


class EnableGEOShop(Toggle):
    """Includes the rewards from handing in GEO tickets at the GEO base"""
    display_name = "Include GEO shop"


class EnableMoonstoneShops(Toggle):
    """
    Includes the rewards from Fran's quest chain and Thomas' shop
    Note that this makes ALL moonstones progression items. Enabling these rewards requires you to add enough locations
    """
    display_name = "Include Moonstone shops"


# Dungeon item shuffle

class DungeonItemShuffle(Choice):
    """Determines where dungeon items can be placed.
    - **Vanilla**: Places dungeon items at their vanilla location
    - **Own Dungeon**: Places dungeon items shuffled within their dungeon
    - **Anywhere**: Dungeon items can be found across the multiworld"""
    display_name = "Dungeon item shuffle"
    option_vanilla = 0
    option_own_dungeon = 1
    option_anywhere = 2
    default = 1


class AnuriPearlstoneShuffle(DungeonItemShuffle):
    """Determines where Anuri Pearlstones can be placed.
    - **Vanilla**: Places Anuri Pearlstones at their vanilla location
    - **Own Dungeon**: Places Anuri Pearlstones shuffled within their dungeon
    - **Anywhere**: Anuri Pearlstones can be found across the multiworld"""
    display_name = "Anuri Pearlstone shuffle"
    default = 1


class OuroGuardKeyShuffle(DungeonItemShuffle):
    """Determines where Ouro Guard Keys can be placed.
    - **Vanilla**: Places Ouro Guard Keys at their vanilla location
    - **Own Dungeon**: Places Ouro Guard Keys shuffled within their dungeon
    - **Anywhere**: Ouro Guard Keys can be found across the multiworld"""
    display_name = "Ouro Guard Key shuffle"
    default = 1


class GolemMedallionShuffle(DungeonItemShuffle):
    """Determines where Blue and Red Golem Medallions can be placed.
    - **Vanilla**: Places Golem Medallions at their vanilla location
    - **Own Dungeon**: Places Golem Medallions shuffled within their dungeon
    - **Anywhere**: Golem Medallions can be found across the multiworld"""
    display_name = "Golem Medallion shuffle"
    default = 1


class KeycardShuffle(DungeonItemShuffle):
    """Determines where Keycards can be placed.
    - **Vanilla**: Keeps Keycards at the corresponding guards
    - **Own Dungeon**: Places Keycards shuffled within their dungeon
    - **Anywhere**: Keycards can be found across the multiworld"""
    display_name = "Keycard shuffle"
    default = 0


# Quality of life settings

class StartWithWoodenBat(DefaultOnToggle):
    """Start out with wooden bat"""
    display_name = "Start with wooden bat"


class BundleMoonstones(Toggle):
    """Bundles Moonstones in bundles of 10 greatly decreasing the amount of progression items.
    Recommended when location count is low"""
    display_name = "Bundle Moonstones"


class BundleAnuriPearlstones(Toggle):
    """Bundles Anuri Pearlstones into an Anuri Pearlstone necklace with infinite uses"""
    display_name = "Bundle Anuri Pearlstones"


class BundleOuroGuardKeys(Toggle):
    """Bundles Ouro Guard Keys into an Ouro Guard Keyring with infinite uses"""
    display_name = "Bundle Ouro Guard Keys"


class BundleGolemMedallions(Toggle):
    """Bundles Blue and Red Golem Medallion into a single medallion"""
    display_name = "Bundle Golem Medallions"


class BundleKeycards(Choice):
    """Bundles each type of Keycard into a single Master Keycard.
    - Yes: Bundles keycards, but keeps the 4 remaining gifts of the terminal guards as locations
    - Yes plus locations: Removes the 4 remaining gifts of the terminal guards as locations"""
    display_name = "Bundle Keycards Keys"
    option_no = 0
    option_yes = 1
    option_yes_plus_locations = 2


class OpenPanseloGates(Toggle):
    """Opens the Panselo gates by default. The gates require a weapon to be opened. Enabling this setting will increase the amount of starting locations"""
    display_name = "Open Panselo gates"


class FranwayUnlockMode(Choice):
    """
    How the Franway teleporters are unlocked
    disabled - Keeps teleporters disabled at all times excluding them from logic. Backtracking can still be done by savewarping
    vanilla* - unlocks them by following Fran's questline. If this is chosen and Moonstone shops are disabled, Franways are considered out of logic
    automatic* - Unlocks teleporters automatically after acquiring 10-20-30 moonstones.
    items - adds an unlock item for each teleporter to the item pool.
    unlocked - starts with all Franways unlocked.
    *Makes ALL moonstones progression items. Enabling these rewards requires you to add enough locations
    """
    display_name = "Franway unlock mode"
    option_disabled = 0
    option_vanilla = 1
    option_automatic = 2
    option_items = 3
    option_unlocked = 4
    default = 2


class UpgradableBats(Toggle):
    """Instead of finding bats of random tiers, upgrade up one tier every time you find a bat"""
    display_name = "Upgradable bats"


class UpgradableTools(Toggle):
    """Upgradable tools are found in order. e.g. civilian crossbow is always found before double crossbow"""
    display_name = "Upgradable moonstone tools"


class UpgradableSpear(Toggle):
    """Instead of Sonic Spear and Spear Bomb being two separate items, you will always find Sonic Spear first and then upgrade with the Spear Bomb"""
    display_name = "Upgradable Spear"


class UpgradablePrelude(Toggle):
    """Instead of Prelude of Panselo and the Spell of Rejuvenation being two separate items, you will always find Prelude of Panselo first and then upgrade it with the Spell of Rejuvenation first"""
    display_name = "Upgradable Prelude of Panselo"


@dataclass
class PhoaOptions(PerGameCommonOptions):
    enable_main_quest_locations: EnableMainQuestLocations
    enable_heart_ruby_locations: EnableHeartRubyLocations
    enable_energy_gem_locations: EnableEnergyGemLocations
    enable_ancient_vault: EnableAncientVault
    enable_moonstone_locations: EnableMoonstoneLocations
    enable_lunar_artifacts_locations: EnableLunarArtifactLocations
    enable_fishing_spots: EnableFishingSpots
    enable_npc_gifts: EnableNpcGifts
    enable_planto_rewards: EnablePlantoRewards
    enable_breakables: EnableItemsInBreakables
    enable_sidequests: EnableSidequests
    enable_freestanding: EnableFreestandingItems
    enable_minigames: EnableMinigames
    enable_perros: EnablePerros
    enable_misc: EnableMisc
    shop_sanity: EnableShopSanity
    enable_small_animal_drops: EnableSmallAnimalDrops
    enable_rin_locations: EnableRinLocations
    enable_trap_chests: EnableTrapChests
    enable_geo_challenge_rewards: EnableGEOChallengeRewards
    enable_ouroboros_shrines: EnableOuroborosShrines
    enable_ouroboros_scroll_rewards: EnableOuroborosScrollRewards
    enable_lunar_artifact_quest: EnableLunarArtifactQuest
    enable_geo_shop: EnableGEOShop
    enable_moonstone_shops: EnableMoonstoneShops
    anuri_pearlstone_shuffle: AnuriPearlstoneShuffle
    ouro_guard_key_shuffle: OuroGuardKeyShuffle
    golem_medallion_shuffle: GolemMedallionShuffle
    keycard_shuffle: KeycardShuffle
    start_with_wooden_bat: StartWithWoodenBat
    bundle_moonstones: BundleMoonstones
    bundle_anuri_pearlstones: BundleAnuriPearlstones
    bundle_ouro_guard_keys: BundleOuroGuardKeys
    bundle_golem_medallions: BundleGolemMedallions
    bundle_keycards: BundleKeycards
    upgradable_bats: UpgradableBats
    upgradable_tools: UpgradableTools
    upgradable_spear: UpgradableSpear
    upgradable_prelude: UpgradablePrelude
    open_panselo_gates: OpenPanseloGates
    franway_unlock_mode: FranwayUnlockMode
    keep_excluded_status_upgrades_in_item_pool: KeepExcludedStatusUpgradesInItemPool
    death_link: DeathLink

    def get_slot_data_dict(self) -> dict[str, Any]:
        return self.as_dict(
            "enable_main_quest_locations",
            "enable_heart_ruby_locations",
            "enable_energy_gem_locations",
            "enable_ancient_vault",
            "enable_moonstone_locations",
            "enable_lunar_artifacts_locations",
            "enable_fishing_spots",
            "enable_npc_gifts",
            "enable_planto_rewards",
            "enable_breakables",
            "enable_sidequests",
            "enable_freestanding",
            "enable_minigames",
            "enable_perros",
            "enable_misc",
            "shop_sanity",
            "enable_small_animal_drops",
            "enable_rin_locations",
            "enable_trap_chests",
            "enable_geo_challenge_rewards",
            "enable_ouroboros_shrines",
            "enable_ouroboros_scroll_rewards",
            "enable_lunar_artifact_quest",
            "enable_geo_shop",
            "enable_moonstone_shops",
            "anuri_pearlstone_shuffle",
            "ouro_guard_key_shuffle",
            "golem_medallion_shuffle",
            "keycard_shuffle",
            "start_with_wooden_bat",
            "bundle_moonstones",
            "bundle_anuri_pearlstones",
            "bundle_ouro_guard_keys",
            "bundle_golem_medallions",
            "bundle_keycards",
            "upgradable_bats",
            "upgradable_tools",
            "upgradable_spear",
            "upgradable_prelude",
            "open_panselo_gates",
            "franway_unlock_mode",
            "keep_excluded_status_upgrades_in_item_pool",
            "death_link",
        )


phoa_option_groups: list[OptionGroup] = [
    OptionGroup(
        "Progress Locations",
        [
            EnableMainQuestLocations,
            EnableHeartRubyLocations,
            EnableEnergyGemLocations,
            EnableAncientVault,
            EnableMoonstoneLocations,
            EnableLunarArtifactLocations,
            EnableFishingSpots,
            EnableNpcGifts,
            EnablePlantoRewards,
            EnableItemsInBreakables,
            EnableSidequests,
            EnableFreestandingItems,
            EnableMinigames,
            EnablePerros,
            EnableMisc,
            EnableGEOShop,
            EnableShopSanity,
            EnableSmallAnimalDrops,
            EnableRinLocations,
            EnableTrapChests,
            EnableGEOChallengeRewards,
            EnableOuroborosShrines,
            EnableOuroborosScrollRewards,
            EnableLunarArtifactQuest,
            EnableMoonstoneShops,
        ],
    ),
    OptionGroup(
        "Dungeon Item Shuffle",
        [
            AnuriPearlstoneShuffle,
            OuroGuardKeyShuffle,
            KeycardShuffle,
            GolemMedallionShuffle,
        ],
    ),
    OptionGroup(
        "Item Randomizer Modes",
        [
            KeepExcludedStatusUpgradesInItemPool,
            StartWithWoodenBat,
            BundleMoonstones,
            BundleAnuriPearlstones,
            BundleOuroGuardKeys,
            BundleGolemMedallions,
            BundleKeycards,
            OpenPanseloGates,
            FranwayUnlockMode,
            UpgradableBats,
            UpgradableTools,
            UpgradableSpear,
            UpgradablePrelude,
        ],
    ),
]
