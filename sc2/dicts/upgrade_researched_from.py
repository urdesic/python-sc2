# THIS FILE WAS AUTOMATICALLY GENERATED BY "generate_dicts_from_data_json.py" DO NOT CHANGE MANUALLY!
# ANY CHANGE WILL BE OVERWRITTEN

from ..ids.unit_typeid import UnitTypeId
from ..ids.ability_id import AbilityId
from ..ids.upgrade_id import UpgradeId

# from ..ids.buff_id import BuffId
# from ..ids.effect_id import EffectId

from typing import Dict, List, Set, Union

UPGRADE_RESEARCHED_FROM: Dict[UpgradeId, UnitTypeId] = {
    UpgradeId.HISECAUTOTRACKING: UnitTypeId.ENGINEERINGBAY,
    UpgradeId.TERRANBUILDINGARMOR: UnitTypeId.ENGINEERINGBAY,
    UpgradeId.TERRANINFANTRYWEAPONSLEVEL1: UnitTypeId.ENGINEERINGBAY,
    UpgradeId.TERRANINFANTRYARMORSLEVEL1: UnitTypeId.ENGINEERINGBAY,
    UpgradeId.TERRANINFANTRYWEAPONSLEVEL2: UnitTypeId.ENGINEERINGBAY,
    UpgradeId.TERRANINFANTRYWEAPONSLEVEL3: UnitTypeId.ENGINEERINGBAY,
    UpgradeId.TERRANINFANTRYARMORSLEVEL2: UnitTypeId.ENGINEERINGBAY,
    UpgradeId.TERRANINFANTRYARMORSLEVEL3: UnitTypeId.ENGINEERINGBAY,
    UpgradeId.PERSONALCLOAKING: UnitTypeId.GHOSTACADEMY,
    UpgradeId.TERRANVEHICLEWEAPONSLEVEL1: UnitTypeId.ARMORY,
    UpgradeId.TERRANSHIPWEAPONSLEVEL1: UnitTypeId.ARMORY,
    UpgradeId.TERRANVEHICLEWEAPONSLEVEL2: UnitTypeId.ARMORY,
    UpgradeId.TERRANVEHICLEWEAPONSLEVEL3: UnitTypeId.ARMORY,
    UpgradeId.TERRANSHIPWEAPONSLEVEL2: UnitTypeId.ARMORY,
    UpgradeId.TERRANSHIPWEAPONSLEVEL3: UnitTypeId.ARMORY,
    UpgradeId.TERRANVEHICLEARMORSLEVEL1: UnitTypeId.ARMORY,
    UpgradeId.TERRANVEHICLEARMORSLEVEL2: UnitTypeId.ARMORY,
    UpgradeId.TERRANVEHICLEARMORSLEVEL3: UnitTypeId.ARMORY,
    UpgradeId.BATTLECRUISERENABLESPECIALIZATIONS: UnitTypeId.FUSIONCORE,
    UpgradeId.STIMPACK: UnitTypeId.BARRACKSTECHLAB,
    UpgradeId.SHIELDWALL: UnitTypeId.BARRACKSTECHLAB,
    UpgradeId.PUNISHERGRENADES: UnitTypeId.BARRACKSTECHLAB,
    UpgradeId.HIGHCAPACITYBARRELS: UnitTypeId.FACTORYTECHLAB,
    UpgradeId.CYCLONELOCKONDAMAGEUPGRADE: UnitTypeId.FACTORYTECHLAB,
    UpgradeId.BANSHEECLOAK: UnitTypeId.STARPORTTECHLAB,
    UpgradeId.RAVENCORVIDREACTOR: UnitTypeId.STARPORTTECHLAB,
    UpgradeId.BANSHEESPEED: UnitTypeId.STARPORTTECHLAB,
    UpgradeId.MEDIVACINCREASESPEEDBOOST: UnitTypeId.STARPORTTECHLAB,
    UpgradeId.LIBERATORMORPH: UnitTypeId.STARPORTTECHLAB,
    UpgradeId.PROTOSSGROUNDWEAPONSLEVEL1: UnitTypeId.FORGE,
    UpgradeId.PROTOSSGROUNDARMORSLEVEL1: UnitTypeId.FORGE,
    UpgradeId.PROTOSSSHIELDSLEVEL1: UnitTypeId.FORGE,
    UpgradeId.PROTOSSGROUNDWEAPONSLEVEL2: UnitTypeId.FORGE,
    UpgradeId.PROTOSSGROUNDWEAPONSLEVEL3: UnitTypeId.FORGE,
    UpgradeId.PROTOSSGROUNDARMORSLEVEL2: UnitTypeId.FORGE,
    UpgradeId.PROTOSSGROUNDARMORSLEVEL3: UnitTypeId.FORGE,
    UpgradeId.PROTOSSSHIELDSLEVEL2: UnitTypeId.FORGE,
    UpgradeId.PROTOSSSHIELDSLEVEL3: UnitTypeId.FORGE,
    UpgradeId.CHARGE: UnitTypeId.TWILIGHTCOUNCIL,
    UpgradeId.PHOENIXRANGEUPGRADE: UnitTypeId.FLEETBEACON,
    UpgradeId.BLINKTECH: UnitTypeId.TWILIGHTCOUNCIL,
    UpgradeId.ADEPTPIERCINGATTACK: UnitTypeId.TWILIGHTCOUNCIL,
    UpgradeId.PSISTORMTECH: UnitTypeId.TEMPLARARCHIVE,
    UpgradeId.DARKTEMPLARBLINKUPGRADE: UnitTypeId.DARKSHRINE,
    UpgradeId.OBSERVERGRAVITICBOOSTER: UnitTypeId.ROBOTICSBAY,
    UpgradeId.GRAVITICDRIVE: UnitTypeId.ROBOTICSBAY,
    UpgradeId.EXTENDEDTHERMALLANCE: UnitTypeId.ROBOTICSBAY,
    UpgradeId.PROTOSSAIRWEAPONSLEVEL1: UnitTypeId.CYBERNETICSCORE,
    UpgradeId.PROTOSSAIRARMORSLEVEL1: UnitTypeId.CYBERNETICSCORE,
    UpgradeId.WARPGATERESEARCH: UnitTypeId.CYBERNETICSCORE,
    UpgradeId.PROTOSSAIRWEAPONSLEVEL2: UnitTypeId.CYBERNETICSCORE,
    UpgradeId.PROTOSSAIRWEAPONSLEVEL3: UnitTypeId.CYBERNETICSCORE,
    UpgradeId.PROTOSSAIRARMORSLEVEL2: UnitTypeId.CYBERNETICSCORE,
    UpgradeId.PROTOSSAIRARMORSLEVEL3: UnitTypeId.CYBERNETICSCORE,
    UpgradeId.OVERLORDSPEED: UnitTypeId.HIVE,
    UpgradeId.BURROW: UnitTypeId.HIVE,
    UpgradeId.ZERGLINGMOVEMENTSPEED: UnitTypeId.SPAWNINGPOOL,
    UpgradeId.ZERGLINGATTACKSPEED: UnitTypeId.SPAWNINGPOOL,
    UpgradeId.ZERGMELEEWEAPONSLEVEL1: UnitTypeId.EVOLUTIONCHAMBER,
    UpgradeId.ZERGGROUNDARMORSLEVEL1: UnitTypeId.EVOLUTIONCHAMBER,
    UpgradeId.ZERGMISSILEWEAPONSLEVEL1: UnitTypeId.EVOLUTIONCHAMBER,
    UpgradeId.ZERGMELEEWEAPONSLEVEL2: UnitTypeId.EVOLUTIONCHAMBER,
    UpgradeId.ZERGMELEEWEAPONSLEVEL3: UnitTypeId.EVOLUTIONCHAMBER,
    UpgradeId.ZERGGROUNDARMORSLEVEL2: UnitTypeId.EVOLUTIONCHAMBER,
    UpgradeId.ZERGGROUNDARMORSLEVEL3: UnitTypeId.EVOLUTIONCHAMBER,
    UpgradeId.ZERGMISSILEWEAPONSLEVEL2: UnitTypeId.EVOLUTIONCHAMBER,
    UpgradeId.ZERGMISSILEWEAPONSLEVEL3: UnitTypeId.EVOLUTIONCHAMBER,
    UpgradeId.EVOLVEGROOVEDSPINES: UnitTypeId.HYDRALISKDEN,
    UpgradeId.EVOLVEMUSCULARAUGMENTS: UnitTypeId.HYDRALISKDEN,
    UpgradeId.ZERGFLYERWEAPONSLEVEL1: UnitTypeId.GREATERSPIRE,
    UpgradeId.ZERGFLYERARMORSLEVEL1: UnitTypeId.GREATERSPIRE,
    UpgradeId.ZERGFLYERWEAPONSLEVEL2: UnitTypeId.GREATERSPIRE,
    UpgradeId.ZERGFLYERWEAPONSLEVEL3: UnitTypeId.GREATERSPIRE,
    UpgradeId.ZERGFLYERARMORSLEVEL2: UnitTypeId.GREATERSPIRE,
    UpgradeId.ZERGFLYERARMORSLEVEL3: UnitTypeId.GREATERSPIRE,
    UpgradeId.ANABOLICSYNTHESIS: UnitTypeId.ULTRALISKCAVERN,
    UpgradeId.CHITINOUSPLATING: UnitTypeId.ULTRALISKCAVERN,
    UpgradeId.INFESTORENERGYUPGRADE: UnitTypeId.INFESTATIONPIT,
    UpgradeId.NEURALPARASITE: UnitTypeId.INFESTATIONPIT,
    UpgradeId.DIGGINGCLAWS: UnitTypeId.LURKERDENMP,
}
