from dataclasses import dataclass
from datetime import datetime
from Options import DeathLink, Choice, Range, Toggle, PerGameCommonOptions, Visibility

class UsePier(Toggle):#UNIMPLEMENTED
    """
    Adds the Pier of the Unknown locations and items
    """
    display_name = "Use Pier of the Unknown"
    #visibility = Visibility.none

class ShuffleChestLootTables(Toggle):#UNIMPLEMENTED
    """
    Shuffles the randomized loot table pulls that chests
      give into the item pool

    Most chests will gain a second location, replacing
      their randomized loot
    """
    display_name = "Shuffle Chest Loot Tables"

class Traps(Choice):#UNIMPLEMENTED
    """
    Adds trap items to the item pool before filler items
    
    None - No traps

    Few - About 5% of unfilled items become traps

    Some - About 20% of unfilled items become traps

    Many - About half of unfilled items become with traps
    """
    display_name = "Traps"
    option_none = 0
    option_few  = 1
    option_some = 2
    option_many = 3
    default = 0

class Shopsanity(Toggle):#UNIMPLEMENTED
    """
    Put Archipelago items in the Town Hall shop
      and Fused Shards in the item pool
    """
    display_name = "Shopsanity"

class Trainersanity(Toggle):#UNIMPLEMENTED
    """
    Make defeating optional trainers into locations
      and put their loot into the item pool
    """
    display_name = "Trainersanity"

class Tapesanity(Choice):#UNIMPLEMENTED
    """
    Adds recording tapes as locations
      and blank tapes to the item pool

    None - No tapes are locations

    Specific - Each tape has its own location

    Percentage - Getting a total number of unique tapes up
      to a certain percentage are locations
    """
    display_name = "Tapesanity"
    option_none = 0
    option_specific = 1
    option_percentage = 2
    default = 0

class TapesanityPercentage(Range):#UNIMPLEMENTED
    """
    The percentage of tapes that must be recorded to
      obtain all items
    """
    display_name = "Tapesanity Percentage"
    range_start = 20
    range_end = 100
    default = 50

class TapesanityPercentageItemCount(Range):#UNIMPLEMENTED
    """
    The number of Tapesanity locations for percentage

    If the number of tapes to record is less then the
      number of locations, then the item count will be
      reduced so that one tapes give one item
    """
    display_name = "Tapesanity Percentage Item Count"
    range_start = 1
    range_end = 128
    default = 64

class Bootlegsanity(Choice):#UNIMPLEMENTED
    """
    Adds recording bootleg tapes as locations
      and bootleg related items to the item pool

    None - No bootlegs are locations

    Per Tape - Each tape has one location for any bootleg

    Specific - Each tape has 14 locations, one for each
      bootleg, yes tapes can be bootlegs of their
      original type

    Percentage Tape - Getting a total number of unique
      tapes that are bootleg to a certain percentage
      are location

    Percentage All - Getting a total number of different
      bootlegs of unique tapes are locations
    """
    display_name = "Bootlegsanity"
    option_none = 0
    option_per_tape = 1
    option_specific = 2
    option_percentage_tape = 3
    option_percentage_all = 4
    default = 0
    if datetime.today().month != 3:
        visibility = Visibility.none

class BootlegsanityPercentage(Range):#UNIMPLEMENTED
    """
    The percentage of bootleg tapes that must be recorded to
      obtain all items
    """
    display_name = "Bootlegsanity Percentage"
    range_start = 1
    range_end = 100
    default = 1
    if datetime.today().month != 3:
        visibility = Visibility.none

class BootlegsanityPercentageItemCount(Range):#UNIMPLEMENTED
    """
    The number of Bootlegsanity locations for percentage

    If the number of tapes to record is less then the
      number of locations, then the item count will be
      reduced so that one tape gives one item
    """
    display_name = "Bootlegsanity Percentage Item Count"
    range_start = 1
    range_end = 512
    default = 4
    if datetime.today().month != 3:
        visibility = Visibility.none

class Fusionsanity(Toggle):#UNIMPLEMENTED
    """
    Adds encountering or fusing into fusions as locations

    Many Pear Fusilli will be added to the item pool
    """
    display_name = "Fusionsanity"
    if datetime.today().month != 3:
        visibility = Visibility.none

class FusionsanityAmount(Range):#UNIMPLEMENTED
    """
    The number of fusions that must be seen or fused
      into to obtain all items
    Without the Pier of the Unknown dlc, the max
      amount is 16384
    """
    display_name = "Fusionsanity Amount"
    range_start = 1
    range_end = 139**2
    default = 32
    if datetime.today().month != 3:
        visibility = Visibility.none

class FusionsanityItemCount(Range):#UNIMPLEMENTED
    """
    The number of Fusionsanity locations

    If the number of fusions seen is less then the
      number of locations, then the item count will be
      reduced so that one fusion gives one item
    """
    display_name = "Fusionsanity Item Count"
    range_start = 1
    range_end = 2048
    default = 16
    if datetime.today().month != 3:
        visibility = Visibility.none

@dataclass
class CassetteBeastsOptions(PerGameCommonOptions):
    death_link: DeathLink
    use_pier: UsePier
    shuffle_chest_loot_tables: ShuffleChestLootTables
    traps: Traps
    shopsanity: Shopsanity
    trainersanity: Trainersanity
    tapesanity: Tapesanity
    tapesanity_percentage: TapesanityPercentage
    tapesanity_percentage_item_count: TapesanityPercentageItemCount
    bootlegsanity: Bootlegsanity
    bootlegsanity_percentage: BootlegsanityPercentage
    bootlegsanity_percentage_item_count: BootlegsanityPercentageItemCount
    fusionsanity: Fusionsanity
    fusionsanity_amount: FusionsanityAmount
    fusionsanity_item_count: FusionsanityItemCount