import enum


class Characters(enum.Enum):
    Shaggy = {"name": "Shaggy", "slug": "character_shaggy"}
    Reindog = {"name": "Reindog", "slug": "character_creature"}
    StevenUniverse = {"name": "Steven Universe", "slug": "character_steven"}
    Garnet = {"name": "Garnet", "slug": "character_garnet"}
    HarleyQuinn = {"name": "Harley Quinn", "slug": "character_harleyquinn"}
    AryaStark = {"name": "Arya Stark", "slug": "character_arya"}
    Finn = {"name": "Finn", "slug": "character_finn"}
    Taz = {"name": "Taz", "slug": "character_taz"}
    WonderWoman = {"name": "Wonder Woman", "slug": "character_wonder_woman"}
    Jake = {"name": "Jake", "slug": "character_jake"}
    Superman = {"name": "Superman", "slug": "character_superman"}
    Batman = {"name": "Batman", "slug": "character_batman"}
    BugsBunny = {"name": "BugsBunny", "slug": "character_bugs_bunny"}
    TomAndJerry = {"name": "Tom & Jerry", "slug": "character_tom_and_jerry"}
    Velma = {"name": "Velma", "slug": "character_velma"}
    IronGiant = {"name": "Iron Giant", "slug": "character_C017"}
    LebronJames = {"name": "Lebron James", "slug": "character_c16"}

def get_character_from_slug(slug):
    for char in Characters:
        if char.value["slug"] == slug:
            return char

def slug_to_display(slug):
    for char in Characters:
        if char.value["slug"] == slug:
            return char.value["name"]


def display_to_slug(name):
    for char in Characters:
        if char.value["name"] == name:
            return char.value["slug"]


class RatingKeys(enum.Enum):
    Mean = "mean"
    Deviance = "deviance"
    Confidence = "confidence"
    Streak = "streak"
    LastUpdateTimeStamp = "lastUpdateTimestamp"
    Character = "character"


# For request regarding players rating
class GamemodeRating(enum.Enum):
    """For request regarding players rating"""

    OneVsOne = "1v1shuffle"
    TwoVsTwo = "2v2shuffle"


# For request regarding players matches
class GamemodeMatches(enum.Enum):
    """For request regarding players matches"""

    OneVsOne = "1v1"
    TwoVsTwo = "2v2"
    FreeForAll = "ffa"

# For request regarding player rank
class GamemodeRank(enum.Enum):
    """For request regarding players matches"""

    OneVsOne = "1v1"
    TwoVsTwo = "2v2"

class Packs(enum.Enum):
    FoundersPackThree = "FoundersPack3"
    FoundersPackThree_Steam = "FoundersPack3_steam"
    FounderPackCoolNameFlag = "founderpackcoolnameflag"
    ClosedAlpha_BattlePass_Complete = "closed_alpha_battlepass_complete"


class Networks(enum.Enum):
    WarnerBrosNetwork = "wb_network"
    Twitch = "twitch"
    Discord = "discord"
    Steam = "steam"
    PlayStation4 = "ps4"


class Perks(enum.Enum):
    perk_general_jumpspeed_medium = {
        "Slug": "perk_general_jumpspeed_medium",
        "HydraName": "Perk: Jump Speed (Med)",
        "DisplayName": "STAR Labs Aerodynamics",
        "Description": "20% increased jump speed",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Medium",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_jumpspeed_large = {
        "Slug": "perk_general_jumpspeed_large",
        "HydraName": "Perk: Jump Speed (Large)",
        "DisplayName": "STAR Labs Aerodynamics",
        "Description": "30% increased jump speed",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Large",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_evaderechargetime_medium = {
        "Slug": "perk_general_evaderechargetime_medium",
        "HydraName": "Perk: Evade Recharge Time (Med)",
        "DisplayName": "Boundless Energy",
        "Description": "Dodges recharge 20% faster",
        "AssociatedCharacterName": "Base",
        "Category": "Defense",
        "Level": "Medium",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_evaderechargetime_large = {
        "Slug": "perk_general_evaderechargetime_large",
        "HydraName": "Perk: Evade Recharge Time (Large)",
        "DisplayName": "Boundless Energy",
        "Description": "Dodges recharge 30% faster",
        "AssociatedCharacterName": "Base",
        "Category": "Defense",
        "Level": "Large",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_directionalinfluence_medium = {
        "Slug": "perk_general_directionalinfluence_medium",
        "HydraName": "Perk: Directional Influence (Med)",
        "DisplayName": "Tasmanian Trigonometry",
        "Description": "300% increased directional influence",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Medium",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_directionalinfluence_large = {
        "Slug": "perk_general_directionalinfluence_large",
        "HydraName": "Perk: Directional Influence (Large)",
        "DisplayName": "Tasmanian Trigonometry",
        "Description": "400% increased directional influence",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Large",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_C015_teamfightcloud = {
        "Slug": "perk_C015_teamfightcloud",
        "HydraName": "Perk: C015 Team Fight Cloud",
        "DisplayName": "I Gotta Get In There!",
        "Description": "Taz's allies can jump into his dogpile, giving it more damage, more knockback, longer duration, and armor.",
        "AssociatedCharacterName": "C015",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "1245184",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_C015_ironstomach = {
        "Slug": "perk_C015_ironstomach",
        "HydraName": "Perk: C015 Iron Stomach",
        "DisplayName": "Iron Stomach",
        "Description": "After Taz eats a projectile, he will burp an anvil item instead of of the projectile he ate.",
        "AssociatedCharacterName": "C015",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "1245184",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_c016_keeppossession = {
        "Slug": "perk_c016_keeppossession",
        "HydraName": "Perk: C016 Keep Possession",
        "DisplayName": "Keep Possession",
        "Description": "When LeBron or his allies receive a pass, they gain gray health for a few seconds.",
        "AssociatedCharacterName": "C016",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "1310720",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_c016_hothands = {
        "Slug": "perk_c016_hothands",
        "HydraName": "Perk: C016 Hot Hands",
        "DisplayName": "Hot Hands",
        "Description": "If LeBron completes a no-look pass to his ally, the basketball is ignited. If LeBron dunks an ignited basketball, he ignites all",
        "AssociatedCharacterName": "C016",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "1310720",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_c016_distanceshot = {
        "Slug": "perk_c016_distanceshot",
        "HydraName": "Perk: C016 Distance Shot",
        "DisplayName": "For Three!",
        "Description": "LeBron and his allies that hit enemies with a basketball from far away cause the basketball to explode, dealing damage and knock",
        "AssociatedCharacterName": "C016",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "1310720",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_evaderechargetime_small = {
        "Slug": "perk_general_evaderechargetime_small",
        "HydraName": "Perk: Evade Recharge Time (Small)",
        "DisplayName": "Boundless Energy",
        "Description": "Your team receives <callout>10% faster dodge invulnerability recharge.</>",
        "AssociatedCharacterName": "Base",
        "Category": "Defense",
        "Level": "Small",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_c017_scorchedearth = {
        "Slug": "perk_c017_scorchedearth",
        "HydraName": "Perk: C017 Scorched Earth",
        "DisplayName": "Afterburners",
        "Description": "When Iron Giant's rocket boots ignite the ground, they leave behind firewalls.",
        "AssociatedCharacterName": "C017",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "1376256",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_c017_stackthorns = {
        "Slug": "perk_c017_stackthorns",
        "HydraName": "Perk: C017 Thorns Stack",
        "DisplayName": "Static Discharge",
        "Description": "Iron Giant's passive grants a stack of Thorns for each unique source of gray health.",
        "AssociatedCharacterName": "C017",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "1376256",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_c017_fastweaponmode = {
        "Slug": "perk_c017_fastweaponmode",
        "HydraName": "Perk: C017 Fast Weapon Mode",
        "DisplayName": "Wrong Side of the Bed",
        "Description": "Iron Giant spawns with some of his RAGE meter already filled.",
        "AssociatedCharacterName": "C017",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "1376256",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_finn_goingoutofbusiness = {
        "Slug": "perk_finn_goingoutofbusiness",
        "HydraName": "Perk: Finn Going Out Of Business",
        "DisplayName": "Going Out Of Business",
        "Description": "All the items in Finn's shop are discounted by 200 gold for 10 seconds after Finn's ally is rung out. The discount is permanent ",
        "AssociatedCharacterName": "Finn",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "1048576",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_finn_gemoncharge = {
        "Slug": "perk_finn_gemoncharge",
        "HydraName": "Perk: Finn Gem On Charge",
        "DisplayName": "On The House!",
        "Description": "Generate a free gem after connecting a fully charged ground attack.",
        "AssociatedCharacterName": "Finn",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "1048576",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_jumpspeed_small = {
        "Slug": "perk_general_jumpspeed_small",
        "HydraName": "Perk: Jump Speed (Small)",
        "DisplayName": "...in a Single Bound!",
        "Description": "Your team receives <callout>10% increased jump speed.</>",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Small",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_garnet_marker = {
        "Slug": "perk_garnet_marker",
        "HydraName": "Perk: Garnet Marker",
        "DisplayName": "Marker",
        "Description": "Garnet's rocket gauntlets will spawn her marker at their location when they are destroyed. The marker will not spawn if it is on",
        "AssociatedCharacterName": "Garnet",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "983040",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_garnet_electricgroove = {
        "Slug": "perk_garnet_electricgroove",
        "HydraName": "Perk: Garnet Electric Groove",
        "DisplayName": "Electric Groove",
        "Description": "Applying shocked to enemies as Garnet or her ally grant stacks of Garnet's rhythym.",
        "AssociatedCharacterName": "Garnet",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "983040",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_velma_studied = {
        "Slug": "perk_velma_studied",
        "HydraName": "Perk: Velma Studied",
        "DisplayName": "Studied",
        "Description": "Velma spawns with 1 piece of evidence already collected.",
        "AssociatedCharacterName": "Velma",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "1179648",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_velma_knowledgeispower = {
        "Slug": "perk_velma_knowledgeispower",
        "HydraName": "Perk: Velma Knowledge Is Power",
        "DisplayName": "Knowledge Is Power",
        "Description": "Velma's ally receives 7 gray health for a few seconds after picking up evidence.",
        "AssociatedCharacterName": "Velma",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "1180416",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_paintedtarget = {
        "Slug": "perk_general_paintedtarget",
        "HydraName": "Perk: Painted Target",
        "DisplayName": "Painted Target",
        "Description": "Your team deals <callout>5% increased damage</> when hitting enemies that are in hitstun.",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_movespeed_medium = {
        "Slug": "perk_general_movespeed_medium",
        "HydraName": "Perk: Movement Speed (Med)",
        "DisplayName": "Speed Force Assist",
        "Description": "Increases base move speed by 15%",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Medium",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_movespeed_large = {
        "Slug": "perk_general_movespeed_large",
        "HydraName": "Perk: Movement Speed (Large)",
        "DisplayName": "Speed Force Assist",
        "Description": "Increases base move speed by 20%",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Large",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_bugsbunny_shockwave = {
        "Slug": "perk_bugsbunny_shockwave",
        "HydraName": "Perk: Bugs Bunny Shockwave",
        "DisplayName": "Comin' Through Doc",
        "Description": "After leaving an existing tunnel, Bugs Bunny and his allies release a shockwave that damages nearby enemies.",
        "AssociatedCharacterName": "BugsBunny",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "721664",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_bugsbunny_lingeringlove = {
        "Slug": "perk_bugsbunny_lingeringlove",
        "HydraName": "Perk: Bugs Bunny Lingering Love",
        "DisplayName": "Lingering Love",
        "Description": "Bugs' kiss leaves behind a floating heart. Enemies who run into it will be charmed, but the charm's duration is significantly re",
        "AssociatedCharacterName": "BugsBunny",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "721664",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_projectiledamageboost_medium = {
        "Slug": "perk_general_projectiledamageboost_medium",
        "HydraName": "Perk: Projectile Damage Boost (Medium)",
        "DisplayName": "Deadshot",
        "Description": "10% increased damage with projectiles",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Medium",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_projectiledamageboost_large = {
        "Slug": "perk_general_projectiledamageboost_large",
        "HydraName": "Perk: Projectile Damage Boost (Large)",
        "DisplayName": "Deadshot",
        "Description": "15% increased damage with projectiles",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Large",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_evadespeed_medium = {
        "Slug": "perk_general_evadespeed_medium",
        "HydraName": "Perk: Evade Speed (Med)",
        "DisplayName": "Slippery Customer",
        "Description": "18% increased dodge speed",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Medium",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_evadespeed_large = {
        "Slug": "perk_general_evadespeed_large",
        "HydraName": "Perk: Evade Speed (Large)",
        "DisplayName": "Slippery Customer",
        "Description": "25% increased dodge speed",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Large",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_c020_signature_2 = {
        "Slug": "perk_c020_signature_2",
        "HydraName": "Perk: c020 signature 2",
        "DisplayName": "null",
        "Description": "Ally projectiles that pass through a portal gain a fire buff.",
        "AssociatedCharacterName": "C020",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "458752",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_c020_signature_1 = {
        "Slug": "perk_c020_signature_1",
        "HydraName": "Perk: c020 signature 1",
        "DisplayName": "It's Called The Buddy System, Morty",
        "Description": "Allies that are knocked into portals have their hitstun negated and velocity reduced.",
        "AssociatedCharacterName": "C020",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "458752",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_dodgearmor = {
        "Slug": "perk_general_dodgearmor",
        "HydraName": "Perk: Dodge Armor",
        "DisplayName": "Sturdy Dodger",
        "Description": "Your team receives <callout>armor for 1 second</> after successfully neutral dodging a projectile.",
        "AssociatedCharacterName": "Base",
        "Category": "Defense",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_evadespeed_small = {
        "Slug": "perk_general_evadespeed_small",
        "HydraName": "Perk: Evade Speed (Small)",
        "DisplayName": "Hit Me If You're Able",
        "Description": "Your team receives <callout>5% increased dodge speed.</>",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Small",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_evadebaseinvulnerability_medium = {
        "Slug": "perk_general_evadebaseinvulnerability_medium",
        "HydraName": "Perk: Evade Base Invulnerability (Med)",
        "DisplayName": "Slippery Customer",
        "Description": "20% longer dodge window",
        "AssociatedCharacterName": "Base",
        "Category": "Defense",
        "Level": "Medium",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_evadebaseinvulnerability_large = {
        "Slug": "perk_general_evadebaseinvulnerability_large",
        "HydraName": "Perk: Evade Base Invulnerability (Large)",
        "DisplayName": "Slippery Customer",
        "Description": "30% longer dodge window",
        "AssociatedCharacterName": "Base",
        "Category": "Defense",
        "Level": "Large",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_harley_smoothmoves = {
        "Slug": "perk_harley_smoothmoves",
        "HydraName": "Perk: Harley Smooth Moves",
        "DisplayName": "Smooth Moves",
        "Description": "Harley's ground and air side specials also become dodges, giving her brief invulnerability at the beginning of the attack.",
        "AssociatedCharacterName": "HarleyQuinn",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "786432",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_harley_confettiexplosion = {
        "Slug": "perk_harley_confettiexplosion",
        "HydraName": "Perk: Harley Confetti Explosion",
        "DisplayName": "Confetti Explosion",
        "Description": "Instead of igniting, at max stacks Harley's Confetti debuff creates a large explosion launching enemies upward",
        "AssociatedCharacterName": "HarleyQuinn",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "786432",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_harley_bullseye = {
        "Slug": "perk_harley_bullseye",
        "HydraName": "Perk: Harley Bullseye",
        "DisplayName": "Glove Control",
        "Description": "Harley can aim the direction she fires her boxing glove on her air down normal attack.",
        "AssociatedCharacterName": "HarleyQuinn",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "786432",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_steven_shieldbounce = {
        "Slug": "perk_steven_shieldbounce",
        "HydraName": "Perk: Steven Shield Bounce",
        "DisplayName": "Bounce Bubble",
        "Description": "Enemies have their hitstun extended and velocity increased after getting knocked into Steven's wall or platform shields.",
        "AssociatedCharacterName": "StevenUniverse",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "851968",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_steven_greenthumb = {
        "Slug": "perk_steven_greenthumb",
        "HydraName": "Perk: Steven Green Thumb",
        "DisplayName": "Green Thumb",
        "Description": "Watermelon Steven grows larger and deals more damage the longer he is alive.",
        "AssociatedCharacterName": "StevenUniverse",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "851968",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_iceprojectile = {
        "Slug": "perk_general_iceprojectile",
        "HydraName": "Perk: Ice Projectile",
        "DisplayName": "Ice to Beat You!",
        "Description": "Your team's projectiles deal <callout>1 stack of ice</> if they knock enemies back.",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_evadebaseinvulnerability_small = {
        "Slug": "perk_general_evadebaseinvulnerability_small",
        "HydraName": "Perk: Evade Base Invulnerability (Small)",
        "DisplayName": "Slippery Customer",
        "Description": "Your team receives a <callout>10% longer dodge invulnerability window.</>",
        "AssociatedCharacterName": "Base",
        "Category": "Defense",
        "Level": "Small",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_collateraldamage = {
        "Slug": "perk_general_collateraldamage",
        "HydraName": "Perk: Collateral Damage",
        "DisplayName": "Collateral Damage",
        "Description": "Your team deals <callout>1 additional damage</> when knocked back enemies collide with a wall or floor.",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_abilityrefundontakeprojectilekb = {
        "Slug": "perk_general_abilityrefundontakeprojectilekb",
        "HydraName": "Perk: Ability Refund On Take Projectile KB",
        "DisplayName": "Absorb 'n' Go",
        "Description": "Your team receives a <callout>7% ability cooldown refund</> after being knocked back by a projectile.",
        "AssociatedCharacterName": "Base",
        "Category": "Defense",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_tomandjerry_dynamitesplit = {
        "Slug": "perk_tomandjerry_dynamitesplit",
        "HydraName": "Perk: Tom And Jerry Dynamite Split",
        "DisplayName": "Dynamite Split",
        "Description": "Reflecting Tom's dynamite with his tennis racket will split it into 3 dynamite sticks.",
        "AssociatedCharacterName": "TomAndJerry",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "917504",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_tomandjerry_bait = {
        "Slug": "perk_tomandjerry_bait",
        "HydraName": "Perk: Bait",
        "DisplayName": "Fly Fisher",
        "Description": "Tom's fishing pole is weaker, but if he hits the ground or a wall with it, he will pull himself to the terrain.",
        "AssociatedCharacterName": "TomAndJerry",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "917504",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_projectileblock = {
        "Slug": "perk_general_projectileblock",
        "HydraName": "Perk: Projectile Block",
        "DisplayName": "School Me Once...",
        "Description": "Your team receives a <callout>projectile block buff for 2 seconds</> after being knocked back by a projectile.",
        "AssociatedCharacterName": "Base",
        "Category": "Defense",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_sniper = {
        "Slug": "perk_general_sniper",
        "HydraName": "Perk: Sniper",
        "DisplayName": "Shirt Cannon Sniper",
        "Description": "Your team's projectiles deal <callout>7% increased damage</> to far away victims.",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_fireprojectile = {
        "Slug": "perk_general_fireprojectile",
        "HydraName": "Perk: Fire Projectile",
        "DisplayName": "That's Flammable, Doc!",
        "Description": "For 3 seconds after knocking back an enemy with a projectile, your team can melee attack that enemy to <callout>ignite them for ",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_abilityrefundondodge = {
        "Slug": "perk_general_abilityrefundondodge",
        "HydraName": "Perk: Ability Refund On Dodge",
        "DisplayName": "I Dodge You Dodge We Dodge",
        "Description": "Your team receives a <callout>10% ability cooldown refund</> after dodging an attack.",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_chargearmorbreak = {
        "Slug": "perk_general_chargearmorbreak",
        "HydraName": "Perk: Charge Armor Break",
        "DisplayName": "Armor Crush",
        "Description": "Your team's fully charged attacks <callout>break armor.</>",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_arya_copycat = {
        "Slug": "perk_arya_copycat",
        "HydraName": "Perk: Arya Copy Cat",
        "DisplayName": "Trophy",
        "Description": "When Arya knocks out an enemy, she automatically obtains their face.",
        "AssociatedCharacterName": "Arya",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "65536",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_arya_enrageallies = {
        "Slug": "perk_arya_enrageallies",
        "HydraName": "Perk: Arya Enrage Allies",
        "DisplayName": "Betrayal",
        "Description": "Hitting an ally with Arya's dagger has a longer cooldown, but the ally is given an enraged buff. If Arya dashes to a dagger on a",
        "AssociatedCharacterName": "Arya",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "65536",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_evadedistance_medium = {
        "Slug": "perk_general_evadedistance_medium",
        "HydraName": "Perk: Evade Distance (Med)",
        "DisplayName": "Fancy Footwork",
        "Description": "10% increased dodge distance",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Medium",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_evadedistance_large = {
        "Slug": "perk_general_evadedistance_large",
        "HydraName": "Perk: Evade Distance (Large)",
        "DisplayName": "Fancy Footwork",
        "Description": "15% increased dodge distance",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Large",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_projectilespeed_medium = {
        "Slug": "perk_general_projectilespeed_medium",
        "HydraName": "Perk: Projectile Speed (Med)",
        "DisplayName": "Make It Rain, Dog!",
        "Description": "30% increased projectile speed",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Medium",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_projectilespeed_large = {
        "Slug": "perk_general_projectilespeed_large",
        "HydraName": "Perk: Projectile Speed (Large)",
        "DisplayName": "Make It Rain, Dog!",
        "Description": "40% Increased Projectile Speed",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Large",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_electricprojectile = {
        "Slug": "perk_general_electricprojectile",
        "HydraName": "Perk: Electric Projectile",
        "DisplayName": "Static Electricity",
        "Description": "After allies move on the ground for 4 seconds, their next projectile <callout>applies shocked to enemies.</> Leaving the ground ",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_evadedistance_small = {
        "Slug": "perk_general_evadedistance_small",
        "HydraName": "Perk: Evade Distance (Small)",
        "DisplayName": "Fancy Footwork",
        "Description": "Your team receives <callout>5% increased dodge distance.</>",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Small",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_creature_airsupport = {
        "Slug": "perk_creature_airsupport",
        "HydraName": "Perk: Creature Air Support",
        "DisplayName": "Crystal Pal",
        "Description": "Reindog's crystal follows him as it descends.",
        "AssociatedCharacterName": "ReinDog",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "393216",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_creature_firestorm = {
        "Slug": "perk_creature_firestorm",
        "HydraName": "Perk: Creature Fire Storm",
        "DisplayName": "Fire Fluff",
        "Description": "Reindog's fireball creates a larger firewall upon hitting the ground.",
        "AssociatedCharacterName": "ReinDog",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "393216",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_jumpheight_medium = {
        "Slug": "perk_general_jumpheight_medium",
        "HydraName": "Perk: Jump Height (Med)",
        "DisplayName": "Leg Day Champ",
        "Description": "20% increased jump height",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Medium",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_jumpheight_large = {
        "Slug": "perk_general_jumpheight_large",
        "HydraName": "Perk: Jump Height (Large)",
        "DisplayName": "Leg Day Champ",
        "Description": "30% increased jump height",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Large",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_wallbouncereduction_medium = {
        "Slug": "perk_general_wallbouncereduction_medium",
        "HydraName": "Perk: Wall Bounce Reduction (Med)",
        "DisplayName": "'Toon Elasticity",
        "Description": "Wall bounce velocity reduced by 30%",
        "AssociatedCharacterName": "Base",
        "Category": "Defense",
        "Level": "Medium",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_wallbouncereduction_large = {
        "Slug": "perk_general_wallbouncereduction_large",
        "HydraName": "Perk: Wall Bounce Reduction (Large)",
        "DisplayName": "'Toon Elasticity",
        "Description": "Wall bounce velocity reduced by 40%",
        "AssociatedCharacterName": "Base",
        "Category": "Defense",
        "Level": "Large",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_wallbouncereduction_small = {
        "Slug": "perk_general_wallbouncereduction_small",
        "HydraName": "Perk: Wall Bounce Reduction (Small)",
        "DisplayName": "'Toon Elasticity",
        "Description": "Your team receives a <callout>20% reduction to ground and wall bounce velocity.</>",
        "AssociatedCharacterName": "Base",
        "Category": "Defense",
        "Level": "Small",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_directionalinfluence_small = {
        "Slug": "perk_general_directionalinfluence_small",
        "HydraName": "Perk: Directional Influence (Small)",
        "DisplayName": "Tasmanian Trigonometry",
        "Description": "Your team receives <callout>15% increased base knockback influence.</>",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Small",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_jumpheight_small = {
        "Slug": "perk_general_jumpheight_small",
        "HydraName": "Perk: Jump Height (Small)",
        "DisplayName": "Leg Day Champ",
        "Description": "Your team receives <callout>10% increased jump height.</>",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Small",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_jake_quickstretch = {
        "Slug": "perk_jake_quickstretch",
        "HydraName": "Perk: Jake Quick Stretch",
        "DisplayName": "Sticky",
        "Description": "Enemies that touch Jake while he's stretching are briefly stunned, making them easier to hit with his buns.",
        "AssociatedCharacterName": "Jake",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "524288",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_jake_bouncyhouse = {
        "Slug": "perk_jake_bouncyhouse",
        "HydraName": "Perk: Jake Bouncy House",
        "DisplayName": "Stay Limber, Dude",
        "Description": "Jake's House ability bounces back into the air after hitting the ground.",
        "AssociatedCharacterName": "Jake",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "524288",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_refreshingknockout = {
        "Slug": "perk_general_refreshingknockout",
        "HydraName": "Perk: Refreshing Knock Out",
        "DisplayName": "Second Wind Beneath Your Wings",
        "Description": "Your team <callout>refreshes air special attacks</> after ringing out an enemy.",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_groundmeleedamageboost_medium = {
        "Slug": "perk_general_groundmeleedamageboost_medium",
        "HydraName": "Perk: Ground Melee Damage Boost (Medium)",
        "DisplayName": "Wildcat Brawler",
        "Description": "10% increased damage to melee attacks on the ground",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Medium",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_groundmeleedamageboost_large = {
        "Slug": "perk_general_groundmeleedamageboost_large",
        "HydraName": "Perk: Ground Melee Damage Boost (Large)",
        "DisplayName": "Wildcat Brawler",
        "Description": "15% increased damage to melee attacks on the ground",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Large",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_dodgereflect = {
        "Slug": "perk_general_dodgereflect",
        "HydraName": "Perk: Dodge Reflect",
        "DisplayName": "Clear the Air",
        "Description": "Your team <callout>destroys enemy projectiles</> after successfully neutral dodging the projectile.",
        "AssociatedCharacterName": "Base",
        "Category": "Defense",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_superman_sniperpunch = {
        "Slug": "perk_superman_sniperpunch",
        "HydraName": "Perk: Superman Sniper Punch",
        "DisplayName": "Sniper Punch",
        "Description": "Superman's aim punch range is extended. The damage and knockback from the aim punch are increased at long distances but decrease",
        "AssociatedCharacterName": "Superman",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "589824",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_superman_icebreaker = {
        "Slug": "perk_superman_icebreaker",
        "HydraName": "Perk: Superman Ice Breaker",
        "DisplayName": "Break The Ice",
        "Description": "Superman deals additional damage to fighters debuffed by Ice. The additional damage scales with stacks of Ice.",
        "AssociatedCharacterName": "Superman",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "589824",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_superman_fireslam = {
        "Slug": "perk_superman_fireslam",
        "HydraName": "Perk: Superman Fire Slam",
        "DisplayName": "Flaming Re-Entry",
        "Description": "The landing from Superman's leap attack ignites enemies and leaves a firewall on the ground.",
        "AssociatedCharacterName": "Superman",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "589824",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_projectilespeed_small = {
        "Slug": "perk_general_projectilespeed_small",
        "HydraName": "Perk: Projectile Speed (Small)",
        "DisplayName": "Make It Rain, Dog!",
        "Description": "Your team receives <callout>20% increased projectile speed.</>",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Small",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_horizontalknockbackboost = {
        "Slug": "perk_general_horizontalknockbackboost",
        "HydraName": "Perk: Horizontal Knockback Boost",
        "DisplayName": "Percussive Punch Power",
        "Description": "Your team deals <callout>5% increased damage</> with attacks that knock back enemies horizontally.",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_jumpcount = {
        "Slug": "perk_general_jumpcount",
        "HydraName": "Perk: Jump Count",
        "DisplayName": "Triple Jump",
        "Description": "Your team receives an <callout>extra jump after hitting an enemy</> while in air.",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_projectiledamageboost_small = {
        "Slug": "perk_general_projectiledamageboost_small",
        "HydraName": "Perk: Projectile Damage Boost (Small)",
        "DisplayName": "Deadshot",
        "Description": "Your team deals <callout>5% increased damage</> with projectiles.",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Small",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_groundmeleedamageboost_small = {
        "Slug": "perk_general_groundmeleedamageboost_small",
        "HydraName": "Perk: Ground Melee Damage Boost (Small)",
        "DisplayName": "Wildcat Brawler",
        "Description": "Your team deals <callout>5% increased damage</> with melee attacks on the ground.",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Small",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_fastfall_medium = {
        "Slug": "perk_general_fastfall_medium",
        "HydraName": "Perk: Fast Fall Speed (Med)",
        "DisplayName": "Gravity Manipulation",
        "Description": "15% increased fast fall speed",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Medium",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_fastfall_large = {
        "Slug": "perk_general_fastfall_large",
        "HydraName": "Perk: Fast Fall Speed (Large)",
        "DisplayName": "Gravity Manipulation",
        "Description": "25% increased fast fall speed",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Large",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_aircontrol_medium = {
        "Slug": "perk_general_aircontrol_medium",
        "HydraName": "Perk: Air Control (Medium)",
        "DisplayName": "Cookie Cat Power!",
        "Description": "50% increase in air control",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Medium",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_aircontrol_large = {
        "Slug": "perk_general_aircontrol_large",
        "HydraName": "Perk: Air Control (Large)",
        "DisplayName": "Cookie Cat Power!",
        "Description": "100% increase in air control",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Large",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_aircontrol_small = {
        "Slug": "perk_general_aircontrol_small",
        "HydraName": "Perk: Air Control (Small)",
        "DisplayName": "Aerial Acrobat",
        "Description": "Your team receives <callout>10% increased air acceleration.</>",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Small",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_verticalknockbackboost = {
        "Slug": "perk_general_verticalknockbackboost",
        "HydraName": "Perk: Vertical Knockback Boost",
        "DisplayName": "Up, Up, and A-Slay",
        "Description": "Your team deals <callout>5% increased damage</> with attacks that knock back enemies upward.",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_fastfall_small = {
        "Slug": "perk_general_fastfall_small",
        "HydraName": "Perk: Fast Fall Speed (Small)",
        "DisplayName": "Gravity Manipulation",
        "Description": "Your team receives <callout>10% increased fast fall speed.</>",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Small",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_evadedistanceonhitcancel = {
        "Slug": "perk_general_evadedistanceonhitcancel",
        "HydraName": "Perk: Evade Distance On Hit Cancel",
        "DisplayName": "Slippery When Feint",
        "Description": "Your team receives <callout>10% increased dodge distance</> when dodging out of an attack hit cancel.",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_batman_heavygrapple = {
        "Slug": "perk_batman_heavygrapple",
        "HydraName": "Perk: Batman Heavy Grapple",
        "DisplayName": "Precision Grapple",
        "Description": "Batman's grappling hook emits a powerful blast when Batman arrives at his destination. However, he deals less damage and knockba",
        "AssociatedCharacterName": "Batman",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "131072",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_batman_bouncerang = {
        "Slug": "perk_batman_bouncerang",
        "HydraName": "Perk: Batman Bouncerang",
        "DisplayName": "Bouncerang",
        "Description": "Hitting an enemy with the Batarang while it is returning to Batman will apply maximum stacks of weakened.",
        "AssociatedCharacterName": "Batman",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "131072",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_knockoutbounce = {
        "Slug": "perk_general_knockoutbounce",
        "HydraName": "Perk: Knock Out Bounce",
        "DisplayName": "That's (Not) All, Folks!",
        "Description": "Ringing out enemies while near the blast zone <callout>pushes the attacker back towards the center of the map.</>",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_damageboostondebuffhit = {
        "Slug": "perk_general_damageboostondebuffhit",
        "HydraName": "Perk: Damage Boost On Debuff Hit",
        "DisplayName": "Hit 'Em While They're Down",
        "Description": "Your team deals <callout>5% increased damage</> when hitting debuffed enemies.",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_abilitycooldownreduction_medium = {
        "Slug": "perk_general_abilitycooldownreduction_medium",
        "HydraName": "Perk: Ability Cooldown Reduction (Med)",
        "DisplayName": "Chronos Connection",
        "Description": "20% reduced ability cooldowns",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Medium",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_abilitycooldownreduction_large = {
        "Slug": "perk_general_abilitycooldownreduction_large",
        "HydraName": "Perk: Ability Cooldown Reduction (Large)",
        "DisplayName": "Chronos Connection",
        "Description": "30% reduced ability cooldowns",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Large",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_wonderwoman_projectileblock = {
        "Slug": "perk_wonderwoman_projectileblock",
        "HydraName": "Perk: Wonder Woman Projectile Block",
        "DisplayName": "Shield of Athena",
        "Description": "Dodging creates a barrier that blocks enemy projectiles. The barrier goes on cooldown after a successful block. ",
        "AssociatedCharacterName": "WonderWoman",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "655360",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_wonderwoman_lassotipper = {
        "Slug": "perk_wonderwoman_lassotipper",
        "HydraName": "Perk: Wonder Woman Lasso Tipper",
        "DisplayName": "Whip of Hephaestus",
        "Description": "The tip of Wonder Woman's lasso has a powerful knockback sweetspot.",
        "AssociatedCharacterName": "WonderWoman",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "655360",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_wonderwoman_lassograpple = {
        "Slug": "perk_wonderwoman_lassograpple",
        "HydraName": "Perk: Wonder Woman Lasso Grapple",
        "DisplayName": "Grapple of Hermes",
        "Description": "Wonder Woman's lasso will grapple lightning out of the air and pull her to its location.",
        "AssociatedCharacterName": "WonderWoman",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "655360",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_backtoback = {
        "Slug": "perk_general_backtoback",
        "HydraName": "Perk: Back To Back",
        "DisplayName": "Back To Back",
        "Description": "Your team receives <callout>6% reduced damage</> when near an ally.",
        "AssociatedCharacterName": "Base",
        "Category": "Defense",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_armorondeath = {
        "Slug": "perk_general_armorondeath",
        "HydraName": "Perk: Armor on Death",
        "DisplayName": "Stronger Than Ever",
        "Description": "Your team receives <callout>armor for 5 seconds</> after respawning.",
        "AssociatedCharacterName": "Base",
        "Category": "Defense",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_inmemoriam = {
        "Slug": "perk_general_inmemoriam",
        "HydraName": "Perk: In Memoriam",
        "DisplayName": "The Purest of Motivations",
        "Description": "Your team deals <callout>15% increased damage for 10 seconds</> after an ally is rung out.",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_abilitycooldownreduction_small = {
        "Slug": "perk_general_abilitycooldownreduction_small",
        "HydraName": "Perk: Ability Cooldown Reduction (Small)",
        "DisplayName": "Coffeezilla",
        "Description": "Your team receives <callout>10% reduced ability cooldown duration.</>",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Small",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_airmeleedamageboost_medium = {
        "Slug": "perk_general_airmeleedamageboost_medium",
        "HydraName": "Perk: Air Melee Damage Boost (Medium)",
        "DisplayName": "Air Master",
        "Description": "10% increased damage to melee attacks in the air",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Medium",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_airmeleedamageboost_large = {
        "Slug": "perk_general_airmeleedamageboost_large",
        "HydraName": "Perk: Air Melee Damage Boost (Large)",
        "DisplayName": "Air Master",
        "Description": "15% increased damage to melee attacks in the air",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Large",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_damagereduction_medium = {
        "Slug": "perk_general_damagereduction_medium",
        "HydraName": "Perk: Damage Reduction (Med)",
        "DisplayName": "Kryptonian Skin",
        "Description": "Take 10% reduced damage",
        "AssociatedCharacterName": "Base",
        "Category": "Defense",
        "Level": "Medium",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_damagereduction_large = {
        "Slug": "perk_general_damagereduction_large",
        "HydraName": "Perk: Damage Reduction (Large)",
        "DisplayName": "Kryptonian Skin",
        "Description": "Take 15% reduced damage",
        "AssociatedCharacterName": "Base",
        "Category": "Defense",
        "Level": "Large",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_shaggy_extrahungry = {
        "Slug": "perk_shaggy_extrahungry",
        "HydraName": "Perk: Shaggy Extra Hungry",
        "DisplayName": "Hangry Man",
        "Description": "If Shaggy has a sandwich equipped, he can quickly charge rage at the cost of eating his sandwich.",
        "AssociatedCharacterName": "Shaggy",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "196608",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_shaggy_dyingrage = {
        "Slug": "perk_shaggy_dyingrage",
        "HydraName": "Perk: Shaggy Dying Rage",
        "DisplayName": "One Last Zoinks",
        "Description": "Shaggy gains rage automatically after passing 100 damage.",
        "AssociatedCharacterName": "Shaggy",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "196608",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_projectilegrayhealth = {
        "Slug": "perk_general_projectilegrayhealth",
        "HydraName": "Perk: Projectile Gray Health",
        "DisplayName": "Retaliation-Ready",
        "Description": "Your team grants allies <callout>3 gray health for 3 seconds</> after knocking back enemies with projectiles.",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_movespeed_small = {
        "Slug": "perk_general_movespeed_small",
        "HydraName": "Perk: Movement Speed (Small)",
        "DisplayName": "Speed Force Assist",
        "Description": "Your team receives <callout>4% increased base movement speed.</>",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Small",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_damagereduction_small = {
        "Slug": "perk_general_damagereduction_small",
        "HydraName": "Perk: Damage Reduction (Small)",
        "DisplayName": "Kryptonian Skin",
        "Description": "Your team receives <callout>4% reduced incoming damage.</>",
        "AssociatedCharacterName": "Base",
        "Category": "Defense",
        "Level": "Small",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_airmeleedamageboost_small = {
        "Slug": "perk_general_airmeleedamageboost_small",
        "HydraName": "Perk: Air Melee Damage Boost (Small)",
        "DisplayName": "Lumpy Space Punch",
        "Description": "Your team deals <callout>5% increased damage</> with melee attacks in the air.",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Small",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_laststand = {
        "Slug": "perk_general_laststand",
        "HydraName": "Perk: Last Stand",
        "DisplayName": "Last Stand",
        "Description": "Your team deals <callout>10% increased damage</> after reaching 100 damage.",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_culltheweak = {
        "Slug": "perk_general_culltheweak",
        "HydraName": "Perk: Cull The Weak",
        "DisplayName": "Snowball Effect",
        "Description": "Your team deals <callout>7% increased damage</> against the fighter with the highest damage.",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_abilityrefundondebuffhit = {
        "Slug": "perk_general_abilityrefundondebuffhit",
        "HydraName": "Perk: Ability Refund On Debuff Hit",
        "DisplayName": "I'll Take That",
        "Description": "Your team receives a <callout>0.5 second refund on ability cooldowns</> after hitting debuffed enemies.",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_arya_wounded = {
        "Slug": "perk_arya_wounded",
        "HydraName": "Perk: Arya Wounded",
        "DisplayName": "Wounded",
        "Description": "Enemies hit by Arya's thrown knife will gain stacks of stun debuff when knocked back. Arya's ally knocking back the enemy will a",
        "AssociatedCharacterName": "Arya",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "65536",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_backstab = {
        "Slug": "perk_general_backstab",
        "HydraName": "Perk: Backstab",
        "DisplayName": "Backstab",
        "Description": "TEAM deals 5% increased damage and knockback to enemies when you melee them in the back.",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_inevitable = {
        "Slug": "perk_general_inevitable",
        "HydraName": "Perk: Inevitable",
        "DisplayName": "Inevitable",
        "Description": "TEAM gains attacks that always break armor if your victim has at least 125% damage.",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_aggro = {
        "Slug": "perk_general_aggro",
        "HydraName": "Perk: Aggro",
        "DisplayName": "Aggro",
        "Description": "Start with reduced damage and knockback (80%). Increase your multiplier by repeatedly hitting enemies with melee attacks (max of",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_batman_bombdownspike = {
        "Slug": "perk_batman_bombdownspike",
        "HydraName": "Perk: Batman Bomb Down Spike",
        "DisplayName": "Bomb Down Spike",
        "Description": "Batman's bomb knocks enemies downward instead of upward",
        "AssociatedCharacterName": "Batman",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "131072",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_batman_chimney = {
        "Slug": "perk_batman_chimney",
        "HydraName": "Perk: Batman Chimney",
        "DisplayName": "Chimney",
        "Description": "Increases the vertical size of Batman's smoke bomb but decrease the horizontal size.",
        "AssociatedCharacterName": "Batman",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "131072",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_batman_increasedbatarangcontrol = {
        "Slug": "perk_batman_increasedbatarangcontrol",
        "HydraName": "Perk: Batman Increased Batarang Control",
        "DisplayName": "Increased Batarang Control",
        "Description": "Slow down batarang movement speed but increase damage and the duration it is out for",
        "AssociatedCharacterName": "Batman",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "131072",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_revenge = {
        "Slug": "perk_general_revenge",
        "HydraName": "Perk: Revenge",
        "DisplayName": "Revenge",
        "Description": "After being knocked back, quickly hit an enemy to regain some of the damage you lost.",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_bugsbunny_escapist = {
        "Slug": "perk_bugsbunny_escapist",
        "HydraName": "Perk: Bugs Bunny Escapist",
        "DisplayName": "Escapist",
        "Description": "Upon leaving a tunnel, Bugs Bunny and his allies recieve a large push upward",
        "AssociatedCharacterName": "BugsBunny",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "720896",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_bugsbunny_safey = {
        "Slug": "perk_bugsbunny_safey",
        "HydraName": "Perk: Bugs Bunny Safety",
        "DisplayName": "Heavy Metal",
        "Description": "Enemies can't launch allied safes into allies. However, enemies deal 150% damage to safes.",
        "AssociatedCharacterName": "BugsBunny",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "720896",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_C015_tornadoreflect = {
        "Slug": "perk_C015_tornadoreflect",
        "HydraName": "Perk: C015 Tornado Reflect",
        "DisplayName": "Right Back At You",
        "Description": "Taz's tornado and the buff it gives his allies will reflect incoming projectiles, but the tornado moves slower.",
        "AssociatedCharacterName": "C015",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "1245184",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_c017_allybarriergrayhealth = {
        "Slug": "perk_c017_allybarriergrayhealth",
        "HydraName": "Perk: C017 Ally Barrier Gray Health",
        "DisplayName": "Ally Barrier Gray Health",
        "Description": "Iron Giant's ally barrier no longer reflects damage. Instead, Iron Giant gains a portion of the damage blocked by the barrier as",
        "AssociatedCharacterName": "C017",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "1376256",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_creature_bigbrother = {
        "Slug": "perk_creature_bigbrother",
        "HydraName": "Perk: Creature Big Brother",
        "DisplayName": "Big Brother",
        "Description": "Warps creature to thethered ally. Also reduces cooldown on tether ability.",
        "AssociatedCharacterName": "ReinDog",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "393216",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_creature_wreckingball = {
        "Slug": "perk_creature_wreckingball",
        "HydraName": "Perk: Creature Wrecking Ball",
        "DisplayName": "Wrecking Ball",
        "Description": "When reindog pulls tethered allies back to them, they hit enemies on their way back",
        "AssociatedCharacterName": "ReinDog",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "393216",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_armored_charge = {
        "Slug": "perk_general_armored_charge",
        "HydraName": "Perk: Armored Charge",
        "DisplayName": "Armored Charge",
        "Description": "Replace invincibility with armor on evades. Armor window is longer that invincibility window.",
        "AssociatedCharacterName": "Base",
        "Category": "Defense",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_catch = {
        "Slug": "perk_general_catch",
        "HydraName": "Perk: Catch",
        "DisplayName": "Elven Reflexes",
        "Description": "Touch allies that are knocked back to stop their hitstun and slow them down, provided you aren't already stunned.",
        "AssociatedCharacterName": "Base",
        "Category": "Defense",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_hunkerdown = {
        "Slug": "perk_general_hunkerdown",
        "HydraName": "Perk: Hunter Down",
        "DisplayName": "Bubble Buddies",
        "Description": "YOU receive armor when your damage reaches 100%.",
        "AssociatedCharacterName": "Base",
        "Category": "Defense",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_finn_gemboost = {
        "Slug": "perk_finn_gemboost",
        "HydraName": "Perk: Finn Gem Boost",
        "DisplayName": "Gem 'Splosion",
        "Description": "Finn's gem will repeatedly send out a shockwave that hurts enemies, but it is more expensive. While holding the gem, use its neu",
        "AssociatedCharacterName": "Finn",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "1048576",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_garnet_slow = {
        "Slug": "perk_garnet_slow",
        "HydraName": "Perk: Garnet Slow",
        "DisplayName": "Slow It Down",
        "Description": "Enemy Projectiles that pass into Garnet's sing radius with be slowed. Garnet can also melee projectiles to reflect them while sh",
        "AssociatedCharacterName": "Garnet",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "983040",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_hitstunincrease_large = {
        "Slug": "perk_general_hitstunincrease_large",
        "HydraName": "Perk: Hitstun Increase (Large)",
        "DisplayName": "Hitstun Increase",
        "Description": "null",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Large",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_hitstunincrease_medium = {
        "Slug": "perk_general_hitstunincrease_medium",
        "HydraName": "Perk: Hitstun Increase (Med)",
        "DisplayName": "Hitstun Increase",
        "Description": "null",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Medium",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_hitstunincrease_small = {
        "Slug": "perk_general_hitstunincrease_small",
        "HydraName": "Perk: Hitstun Increase (Small)",
        "DisplayName": "Hitstun Increase",
        "Description": "null",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Small",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_jake_floatybounce = {
        "Slug": "perk_jake_floatybounce",
        "HydraName": "Perk: Jake Floaty Bounce",
        "DisplayName": "Floaty Bounce",
        "Description": "Jake deals a float debuff on enemies when they bounce off him",
        "AssociatedCharacterName": "Jake",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "524288",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_jake_safetynet = {
        "Slug": "perk_jake_safetynet",
        "HydraName": "Perk: Jake Safety Net",
        "DisplayName": "Safety Net",
        "Description": "When allies bounce off of Jake, they recieve Air Superiority and have their air abilities repeatedly refreshed. If they are in h",
        "AssociatedCharacterName": "Jake",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "524288",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_jake_weaponmaster = {
        "Slug": "perk_jake_weaponmaster",
        "HydraName": "Perk: Jake Weapon Master",
        "DisplayName": "Weapon Master",
        "Description": "Switching to Jake's weapon arm gives him a damage boost for his next hit",
        "AssociatedCharacterName": "Jake",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "524288",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_knockbackmitigation_large = {
        "Slug": "perk_general_knockbackmitigation_large",
        "HydraName": "Perk: Knockback Mitigation (Large)",
        "DisplayName": "Density Control",
        "Description": "Take 15% reduced knockback",
        "AssociatedCharacterName": "Base",
        "Category": "Defense",
        "Level": "Large",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_knockbackmitigation_medium = {
        "Slug": "perk_general_knockbackmitigation_medium",
        "HydraName": "Perk: Knockback Mitigation (Med)",
        "DisplayName": "Density Control",
        "Description": "Take 10% reduced knockback",
        "AssociatedCharacterName": "Base",
        "Category": "Defense",
        "Level": "Medium",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_knockbackmitigation_small = {
        "Slug": "perk_general_knockbackmitigation_small",
        "HydraName": "Perk: Knockback Mitigation (Small)",
        "DisplayName": "Lay off the Scooby Snax",
        "Description": "TEAM gains +5% reduced knockback.",
        "AssociatedCharacterName": "Base",
        "Category": "Defense",
        "Level": "Small",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_airmeleeknockbackboost_large = {
        "Slug": "perk_general_airmeleeknockbackboost_large",
        "HydraName": "Perk: Air Melee Knockback Boost (Large)",
        "DisplayName": "Pow-Air Punch",
        "Description": "Deal 15% increased knockback for melee attacks in the air",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Large",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_airmeleeknockbackboost_medium = {
        "Slug": "perk_general_airmeleeknockbackboost_medium",
        "HydraName": "Perk: Air Melee Knockback Boost (Medium)",
        "DisplayName": "Pow-Air Punch",
        "Description": "Deal 10% increased knockback for melee attacks in the air",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Medium",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_airmeleeknockbackboost_small = {
        "Slug": "perk_general_airmeleeknockbackboost_small",
        "HydraName": "Perk: Air Melee Knockback Boost (Small)",
        "DisplayName": "Lumpy Space Punch",
        "Description": "Your team gains 5% increased knockback for melee attacks in the air.",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Small",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_groundmeleeknockbackboost_large = {
        "Slug": "perk_general_groundmeleeknockbackboost_large",
        "HydraName": "Perk: Ground Melee Knockback Boost (Large)",
        "DisplayName": "Tactile Telekinesis",
        "Description": "Deal 15% increased knockback for melee attacks on the ground",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Large",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_groundmeleeknockbackboost_medium = {
        "Slug": "perk_general_groundmeleeknockbackboost_medium",
        "HydraName": "Perk: Ground Melee Knockback Boost (Medium)",
        "DisplayName": "Tactile Telekinesis",
        "Description": "Deal 10% increased knockback for melee attacks on the ground",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Medium",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_groundmeleeknockbackboost_small = {
        "Slug": "perk_general_groundmeleeknockbackboost_small",
        "HydraName": "Perk: Ground Melee Knockback Boost (Small)",
        "DisplayName": "Tactile Telekinesis",
        "Description": "Your team gains 5% increased knockback for melee attacks on the ground.",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Small",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_projectileknockbackboost_large = {
        "Slug": "perk_general_projectileknockbackboost_large",
        "HydraName": "Perk: Projectile Knockback Boost (Large)",
        "DisplayName": "Mithrill Tipped",
        "Description": "Deal 15% increased knockback with projectiles",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Large",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_projectileknockbackboost_medium = {
        "Slug": "perk_general_projectileknockbackboost_medium",
        "HydraName": "Perk: Projectile Knockback Boost (Medium)",
        "DisplayName": "Mithrill Tipped",
        "Description": "Deal 10% increased knockback with projectiles",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Medium",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_projectileknockbackboost_small = {
        "Slug": "perk_general_projectileknockbackboost_small",
        "HydraName": "Perk: Projectile Knockback Boost (Small)",
        "DisplayName": "Boxing Glove Arrow",
        "Description": "Your team gains 5% increased knockback with projectiles.",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Small",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_armorboost_large = {
        "Slug": "perk_general_armorboost_large",
        "HydraName": "Perk: Armor Boost (Large)",
        "DisplayName": "Armor Master",
        "Description": "100% increase in armor strength and 1 extra minimum hit",
        "AssociatedCharacterName": "Base",
        "Category": "Defense",
        "Level": "Large",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_armorboost_medium = {
        "Slug": "perk_general_armorboost_medium",
        "HydraName": "Perk: Armor Boost (Med)",
        "DisplayName": "Armor Master",
        "Description": "100% increase in armor strength",
        "AssociatedCharacterName": "Base",
        "Category": "Defense",
        "Level": "Medium",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_armorboost_small = {
        "Slug": "perk_general_armorboost_small",
        "HydraName": "Perk: Armor Boost (Small)",
        "DisplayName": "Armor Master",
        "Description": "50% increase in armor strength.",
        "AssociatedCharacterName": "Base",
        "Category": "Defense",
        "Level": "Small",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_attackrecoveryspeed_large = {
        "Slug": "perk_general_attackrecoveryspeed_large",
        "HydraName": "Perk: Attack Recovery Speed (Large)",
        "DisplayName": "Attack Recovery Speed",
        "Description": "Recover from attacks 40% faster",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Large",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_attackrecoveryspeed_medium = {
        "Slug": "perk_general_attackrecoveryspeed_medium",
        "HydraName": "Perk: Attack Recovery Speed (Medium)",
        "DisplayName": "Attack Recovery Speed",
        "Description": "Recover from attacks 30% faster",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Medium",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_attackrecoveryspeed_small = {
        "Slug": "perk_general_attackrecoveryspeed_small",
        "HydraName": "Perk: Attack Recovery Speed (Small)",
        "DisplayName": "Attack Recovery Speed",
        "Description": "Recover from attacks 20% faster",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Small",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_sticktowall = {
        "Slug": "perk_general_sticktowall",
        "HydraName": "Perk: Stick to Wall",
        "DisplayName": "Ninja Training",
        "Description": "Hold up while wall sliding to stay put",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_regroup = {
        "Slug": "perk_general_regroup",
        "HydraName": "Perk: Regroup",
        "DisplayName": "Regroup",
        "Description": "You and your allies gain a 7% movement speed increase when moving towards each other.",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_clearheadspace = {
        "Slug": "perk_general_clearheadspace",
        "HydraName": "Perk: Clear Headspace",
        "DisplayName": "Keep Your Distance",
        "Description": "Your team's projectiles deal <callout>7% increased damage</> when there are no other fighters near you.",
        "AssociatedCharacterName": "Base",
        "Category": "Offense",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_abilityrefundonhit = {
        "Slug": "perk_general_abilityrefundonhit",
        "HydraName": "Perk: Ability Refund On Hit",
        "DisplayName": "Ability-Refund-On-Hit",
        "Description": "Hitting an enemy with an ability refunds 50% of its cooldown",
        "AssociatedCharacterName": "Base",
        "Category": "Utility",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_shaggy_scaredycat = {
        "Slug": "perk_shaggy_scaredycat",
        "HydraName": "Perk: Shaggy Scaredy Cat",
        "DisplayName": "Scaredy Cat",
        "Description": "Gain a speed boost on successful evades",
        "AssociatedCharacterName": "Shaggy",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "196608",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_empathydamage = {
        "Slug": "perk_general_empathydamage",
        "HydraName": "Perk: Empathy Damage",
        "DisplayName": "Empathy Damage",
        "Description": "Incoming damage on you ally is reduced by 20%, but that 20% gets transferred to you.",
        "AssociatedCharacterName": "Base",
        "Category": "Defense",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_backtoreality = {
        "Slug": "perk_general_backtoreality",
        "HydraName": "Perk: Back To Reality",
        "DisplayName": "Back To Reality",
        "Description": "Hitstun from attacks will never exceed 1 second on your fighter.",
        "AssociatedCharacterName": "Base",
        "Category": "Defense",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_general_healthy = {
        "Slug": "perk_general_healthy",
        "HydraName": "Perk: Healthy",
        "DisplayName": "Healthy",
        "Description": "YOU gain 25 bonus health when you respawn.",
        "AssociatedCharacterName": "Base",
        "Category": "Defense",
        "Level": "Unsized",
        "Rarity": "None",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_velma_geometric = {
        "Slug": "perk_velma_geometric",
        "HydraName": "Perk: Velma Geometric",
        "DisplayName": "Geometric",
        "Description": "Hitting pieces of evidence with Velma's beam will spawn an additional beam on the evidence. The evidence will auotmatically be p",
        "AssociatedCharacterName": "Velma",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "1179648",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_velma_goodreception = {
        "Slug": "perk_velma_goodreception",
        "HydraName": "Perk: Velma Good Reception",
        "DisplayName": "Good Reception",
        "Description": "When Velma hits a fighter with the last hit of her megahone attack, she attaches a snark marker projectile to them if one does n",
        "AssociatedCharacterName": "Velma",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "1179648",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_wonderwoman_fastfallslam = {
        "Slug": "perk_wonderwoman_fastfallslam",
        "HydraName": "Perk: Wonder Woman Fast Fall Slam",
        "DisplayName": "Wonder Woman Fast Fall Slam",
        "Description": "After fast falling into the ground, create a small explosion",
        "AssociatedCharacterName": "WonderWoman",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "655360",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }
    perk_c020_signature_3 = {
        "Slug": "perk_c020_signature_3",
        "HydraName": "Perk: c020 signature 3",
        "DisplayName": "Portal Melee Buff",
        "Description": "After traveling through a portal, Rick's next attack applies a fire buff",
        "AssociatedCharacterName": "EFighter_MAX",
        "Category": "CharacterSpecific",
        "Level": "Unsized",
        "Rarity": "2424832",
        "GoldPrice": "150",
        "GoldSalePrice": "100",
    }


class PerkValue(enum.Enum):
    Slug = "Slug"
    HydraName = "HydraName"
    DisplayName = "DisplayName"
    Description = "Description"
    AssociatedCharacterName = "AssociatedCharacterName"
    Level = "Level"
    Category = "Category"
    Rarity = "Rarity"
    GoldPrice = "GoldPrice"
    GoldSalePrice = "GoldSalePrice"
