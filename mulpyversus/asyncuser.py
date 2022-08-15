import string
from mulpyversus.utils import *

class UserNetwork:
    """Represent a UserNetwork object
    ::
    A network linked to the users account
    ::
    Args:
        data: data provided by an other class
        ::    
    """
    def __init__(self, data : dict, networkName : string, accountID : string):
        self.accountID = accountID
        self.rawData = data
        self.networkName = networkName
    
    def __repr__(self):
        return str(self.rawData)

    def get_network_name(self):
        """Returns the name of the network.
        ::
        Exemple:
            "wb_network", "twitch", "steam"
            ::    
        """
        return self.networkName

    def get_network_user_id(self):
        """Returns the users id on that network.
        ::  
        Returns None if the network has no ID 
        """
        return self.rawData[0]["id"] if "id" in self.rawData[0] else None

    def get_network_user_avatar(self):
        """Returns the users avatar on that network.
        ::  
        Returns None or null if the network has no avatar 
        """
        return self.rawData[0]["avatar"] if "avatar" in self.rawData[0] else None
   
    def get_network_user_username(self):
        """Returns the users username on that network.
        ::  
        Returns None or null if the network has no username 
        """
        return self.rawData[0]["username"] if "username" in self.rawData[0] else None

    def get_network_user_created_at(self):
        """Returns the users created_at on that network.
        ::  
        Returns None or null if the network has no created_at 
        """
        return self.rawData[0]["created_at"] if "created_at" in self.rawData[0] else None

    def get_related_account_id(self) -> string:
        """Represent the account_id of the user related to this page"""
        return self.accountID

class PerkPage:

    """Represent a PerkPage object
    ::
    Args:
        data: data provided by an other class
        ::    
    """

    def __init__(self, data : dict, name: string, accountID : string):
        self.accountID = accountID
        self.rawData = data
        self.character_name = name

    def __repr__(self):
        return str(self.rawData)

    def get_character(self) -> string:
        return self.character_name

    def get_page_name(self) -> string:
        return self.rawData["PerkPages"][0]["PageName"]

    def get_main_perk(self) -> Perks:
        """Represent the main perk for this page
        ::
        To get specific data from a perk, use the PerkValue Enum
        ::
        Exemple: somePerk.value[PerkValue.Level.value]
        ::
        List of values: Slug, HydraName, DisplayName, Description, AssociatedCharacterName, Category, Rarity, GoldPrice, GoldSalePrice"""
        return Perks[self.rawData["PerkPages"][0]["PerkSlugs"][0]] if self.rawData["PerkPages"][0]["PerkSlugs"][0] != "" else None

    def get_first_perk(self) -> Perks:
        """Represent the first "small" for this page
        ::
        To get specific data from a perk, use the PerkValue Enum
        ::
        Exemple: somePerk.value[PerkValue.Level.value]
        ::
        List of values: Slug, HydraName, DisplayName, Description, AssociatedCharacterName, Category, Rarity, GoldPrice, GoldSalePrice"""
        return Perks[self.rawData["PerkPages"][0]["PerkSlugs"][1]] if self.rawData["PerkPages"][0]["PerkSlugs"][1] != "" else None

    def get_second_perk(self) -> Perks:
        """Represent the second "small" for this page
        ::
        To get specific data from a perk, use the PerkValue Enum
        ::
        Exemple: somePerk.value[PerkValue.Level.value]
        ::
        List of values: Slug, HydraName, DisplayName, Description, AssociatedCharacterName, Category, Rarity, GoldPrice, GoldSalePrice"""
        return Perks[self.rawData["PerkPages"][0]["PerkSlugs"][2]] if self.rawData["PerkPages"][0]["PerkSlugs"][2] != "" else None

    def get_third_perk(self) -> Perks:
        """Represent the third "small" for this page
        ::
        To get specific data from a perk, use the PerkValue Enum
        ::
        Exemple: somePerk.value[PerkValue.Level.value]
        ::
        List of values: Slug, HydraName, DisplayName, Description, AssociatedCharacterName, Category, Rarity, GoldPrice, GoldSalePrice"""
        return Perks[self.rawData["PerkPages"][0]["PerkSlugs"][3]] if self.rawData["PerkPages"][0]["PerkSlugs"][3] != "" else None

    def get_related_account_id(self) -> string:
        """Represent the account_id of the user related to this page"""
        return self.accountID


class AsyncUser:
    """Represent a user object
    ::
    Args:
        data: result of a user request
        ::
    Usage Example:
            a
    Attributes:
    """
    def __init__(self, id : string, mlpyvrs):
        self.id = id
        self.mlpyvrs = mlpyvrs

    async def init(self):
        self.profileData = await self.mlpyvrs.request_data("profiles/" + str(self.id))
        self.accountData = await self.mlpyvrs.request_data("accounts/" + str(self.id))

    def __repr__(self):
        return str(self.profileData)

    async def refresh(self):
        """IS ASYNC : Used to refresh a User object 
        Usage Example:
            ::
            await someone.refresh_user()
        """
        await self.init(self.get_account_id(), self)

    def get_id(self) -> string:
        return self.profileData['id']

    def get_account_id(self) -> string:
        return self.profileData['account_id']
    
    def get_updated_at(self) -> string:
        return self.profileData['updated_at']

    def get_created_at(self) -> string:
        return self.profileData['created_at']

    def get_last_login(self) -> string:
        return  self.profileData['last_login']

    def get_points(self):
        return self.profileData['points']

    def is_child_account(self) -> bool:
        return self.profileData['data']['IsChildAccount']

    def get_perk_preferences(self) -> list[PerkPage]:
        """Returns a list of PerkPage objects
        ::
        Usage Example:
            >>> .get_perk_preferences()[1].get_main_perk()
        """
        return [PerkPage(self.profileData['data']['PerkPreferences']['Characters'][name], name, self.get_account_id()) for name in self.profileData['data']['PerkPreferences']['Characters'] ]

    def get_perk_preference_by_character(self, character : Characters):
        """Returns PerkPage objects for specified Character
        ::
        Returns False if Character not found in PerkPreferences
        ::
        Usage Example:
            >>> .get_perk_preference_by_character(Characters.WonderWoman).get_main_perk()
        """
        return PerkPage(self.profileData['data']['PerkPreferences']['Characters'][character.value["slug"]], character.value["name"], self.get_account_id()) if character.value["slug"] in self.profileData['data']['PerkPreferences']['Characters'] else False

    def get_public_id(self):
        return self.accountData['public_id']
    
    def get_default_username(self):
        return self.accountData['identity']['username']
    
    def is_username_default_username(self):
        return self.accountData['identity']['default_username']

    def get_user_networks(self) -> list[UserNetwork]:
        return [UserNetwork(self.accountData['identity']['alternate'][name], name, self.get_account_id()) for name in self.accountData['identity']['alternate'] ]
    
    def has_network(self, network : Networks):
        """Returns Network objects for specified network
        ::
        Returns False if network not found in the user's network list
        """
        return UserNetwork(self.accountData['identity']['alternate'][network.value], network.value, self.get_account_id()) if network.value in self.accountData['identity']['alternate'] else False

    def get_last_login_platform(self) -> string:
        return self.accountData['data']['LastLoginPlatform'] if 'LastLoginPlatform' in self.accountData['data'] else None

    def get_last_played_character(self) -> string:
        return self.accountData['data']['LastPlayedCharacterSlug'] if 'LastPlayedCharacterSlug' in self.accountData['data'] else None

    def get_last_login_time(self) -> string:
        return self.accountData['server_data']['LastLoginTime'] if 'LastLoginTime' in self.profileData['server_data'] else 0
    
    def get_last_logout_time(self) -> string:
        return self.accountData['server_data']['LastLogoutTime'] if 'LastLoginTime' in self.profileData['server_data'] else 0

    def get_character_level(self, characterName : Characters) -> int:
        """Return the level of the character
        ::
        To use this, use Characters.NAMEOFCHARS
        ::
        Usage Example:
            >>> .get_character_level(Characters.WonderWoman)
        """
        if  characterName.value["slug"] in self.accountData['server_data']['Characters'] :
            return self.accountData['server_data']['Characters'][characterName.value["slug"]]["Mastery"]["Level"]
        else:
            return 0

    def get_character_current_exp(self, characterName : Characters) -> int:
        """Return the current experience of the charachter
        ::
        To use this, use Characters.NAMEOFCHARS
        ::
        Usage Example:
            >>> .get_character_current_exp(Characters.WonderWoman)
        """
        if  characterName.value["slug"] in self.accountData['server_data']['Characters'] :
            return self.accountData['server_data']['Characters'][ characterName.value["slug"]]["Mastery"]["CurrentXP"]
        else:
            return 0

    def get_user_level(self) -> int:
        return self.accountData['server_data']['Level'] if 'Level' in self.accountData['server_data'] else 0

    def get_user_current_expires_in(self) -> int:
        return self.accountData['server_data']['CurrentXP'] if 'CurrentXP' in self.accountData['server_data'] else 0

    def get_user_first_claim_time(self) -> int:
        return self.accountData['server_data']['FirstWinClaimTime'] if 'FirstWinClaimTime' in self.accountData['server_data'] else None

    def get_anti_cheat_server_kick(self) -> bool:
        return self.accountData['server_data']['AntiCheatServerKick'] if "AntiCheatServerKick" in self.accountData['server_data'] else 0
        
    def get_debug_all_unlocked(self) -> int:
        return self.profileData['server_data']['debug_all_unlocked'] if 'debug_all_unlocked' in self.profileData['server_data'] else None

    def get_battlepass_id(self) -> string:
        return self.profileData['server_data']['BattlepassID'] if "BattlepassID" in self.profileData['server_data'] else None

    def get_highest_damage_dealt(self) -> int:
        return self.profileData['server_data']['stat_trackers']['HighestDamageDealt'] if 'HighestDamageDealt' in self.profileData['server_data']['stat_trackers'] else 0

    def get_total_ringout_leader(self) -> int:
        return self.profileData['server_data']['stat_trackers']['TotalRingoutLeader'] if 'TotalRingoutLeader' in self.profileData['server_data']['stat_trackers'] else 0

    def get_total_ringouts(self) -> int:
        return self.profileData['server_data']['stat_trackers']['TotalRingouts'] if 'TotalRingouts' in self.profileData['server_data']['stat_trackers'] else 0

    def get_total_wins(self) -> int:
        return self.profileData['server_data']['stat_trackers']['TotalWins'] if 'TotalWins' in self.profileData['server_data']['stat_trackers'] else 0

    def get_total_loss(self) -> int:
        return self.get_matches_played()-self.get_total_wins()

    def get_wins_with_character(self, characterName : Characters) -> int:
        """Return the number of winss with the character
        ::
        To use this, use Characters.NAMEOFCHARS
        ::
        Usage Example:
            >>> .get_wins_with_character(Characters.WonderWoman)
        """
        if characterName.value["slug"] in self.profileData['server_data']['stat_trackers']['character_wins'] :
            return self.profileData['server_data']['stat_trackers']['character_wins'][characterName.value["slug"]]
        else:
            return 0

    def get_total_attacks_dodged(self) -> int:
        return self.profileData['server_data']['stat_trackers']['TotalAttacksDodged'] if 'TotalAttacksDodged' in self.profileData['server_data']['stat_trackers'] else 0

    def get_total_assits(self) -> int:
        return self.profileData['server_data']['stat_trackers']['TotalAssists'] if 'TotalAssists' in self.profileData['server_data']['stat_trackers'] else 0

    def get_unclaimed_character_rewards(self, characterName : Characters):
        """Return unclaimed rewards for the charachter
        ::
        FOR NOW, THIS WILL RETURN ALL INFORMATIONS AS JSON
        ::
        To use this, use Characters.NAMEOFCHARS
        ::
        Usage Example:
            >>> .get_unclaimed_character_rewards(Characters.WonderWoman)
        """
        if characterName.value["slug"] in self.accountData['server_data']['UnclaimedCharacterMasteryRewards'] :
            return self.accountData['server_data']['UnclaimedCharacterMasteryRewards']

    def get_lifetime_damage(self) -> int:
        return self.profileData['server_data']['stat_trackers']['lifetime_damage'] if 'lifetime_damage' in self.profileData['server_data']['stat_trackers'] else 0

    def get_lifetime_ringouts(self) -> int:
        return self.profileData['server_data']['stat_trackers']['lifetime_ringouts'] if 'lifetime_ringouts' in self.profileData['server_data']['stat_trackers'] else 0

    def get_loss_streak(self) -> int:
        return self.profileData['server_data']['loss_streak'] if 'loss_streak' in self.profileData['server_data'] else 0

    def get_matches_played(self) -> int:
        return self.profileData['server_data']['matches_played'] if 'matches_played' in self.profileData['server_data'] else 0

    def get_sets_played(self) -> int:
        return self.profileData['server_data']['sets_played'] if 'sets_played' in self.profileData['server_data'] else 0

    def get_all_owned_perks(self) -> list[Perks]:
        """To get specific data from a perk, use the PerkValue Enum
        ::
        Exemple: somePerk.value[PerkValue.WANTEDVALUE.value]
        ::
        List of values: Slug, HydraName, DisplayName, Description, AssociatedCharacterName, Category, Rarity, GoldPrice, GoldSalePrice
        """
        AllPerks = []
        for charName in self.profileData['server_data']['OwnedPerks']:
            for name in self.profileData['server_data']['OwnedPerks'][charName]:
                AllPerks.append(Perks[name])
        return AllPerks

    def get_owned_perks_by_character(self, character : Characters):
        """To get specific data from a perk, use the PerkValue Enum
        ::
        Exemple: somePerk.value[PerkValue.Level.value]
        ::
        List of values: Slug, HydraName, DisplayName, Description, AssociatedCharacterName, Category, Rarity, GoldPrice, GoldSalePrice
        """
        if character.value["slug"] in self.profileData['server_data']['OwnedPerks']:
            return [Perks[name] for name in self.profileData['server_data']['OwnedPerks'][character.value["slug"]]]

    def get_character_rating(self, character : Characters, rating : RatingKeys, gm : GamemodeRating):
        """Return the asked rating for a character
        If none, return -1.0
        ::
        Args:
            To use this, use Characters.NAMEOFCHARS
            To use this, use RatingKeys.RATINGKEY
            To use this, use GamemodeRating.NAMEOFGAMEMODE
        ::
        Usage Example:
            >>> .get_character_rating(Characters.WonderWoman, RatingKeys.Deviance, GamemodeRating.OneVsOne)
        """
        if gm.value in self.profileData['server_data']:
            maxKey = 0
            for key in self.profileData['server_data'][gm.value]:
                maxKey = int(key) if int(key)>maxKey else maxKey
            if character.value["slug"] in self.profileData['server_data'][gm.value][str(maxKey)]["ratings"]:
                if rating.value in self.profileData['server_data'][gm.value][str(maxKey)]["ratings"][character.value["slug"]]:
                    return self.profileData['server_data'][gm.value][str(maxKey)]["ratings"][character.value["slug"]][rating.value]
        return -1.0

    def get_top_ranked_character_in_gamemode(self, gm : GamemodeRating):
        """Return the top ranked character in given GamemodeRating
        ::
        Args:
            To use this, use GamemodeRating.NAMEOFGAMEMODE
        ::
        Usage Example:
            >>> .get_top_ranked_character(GamemodeRating.NAMEOGAMEMODE)
        """
        maxKey = 0
        for key in self.profileData['server_data'][gm.value]:
            maxKey = int(key) if int(key)>maxKey else maxKey
        if "topRating" in self.profileData['server_data'][gm.value][str(maxKey)]:
            if "character" in self.profileData['server_data'][gm.value][str(maxKey)]["topRating"]:
                return self.profileData['server_data'][gm.value][str(maxKey)]["topRating"]["character"]

    def get_top_rated_character_ratings(self, rating : RatingKeys, gm : GamemodeRating):
        """Return the asked rating for the top ranked character in the given gamemode
        If none, return -1.0
        ::
        Args:
            To use this, use RatingKeys.RATINGKEY
            To use this, use GamemodeRating.NAMEOFGAMEMODE
        ::
        Usage Example:
            >>> .get_top_ratings(RatingKeys.Deviance, GamemodeRating.NAMEOGAMEMODE)
        """
        maxKey = 0
        for key in self.profileData['server_data'][gm.value]:
            maxKey = int(key) if int(key)>maxKey else maxKey
        if "topRating" in self.profileData['server_data'][gm.value][str(maxKey)]:
            if rating.value in self.profileData['server_data'][gm.value][str(maxKey)]["topRating"]:
                self.profileData['server_data'][gm.value][str(maxKey)]["topRating"][rating.value]

    def get_ally_perk_sharing(self, character : Characters):
        if character.value["slug"] in self.profileData['server_data']["Characters"]:
            return self.profileData['server_data']["Characters"]["ally_perk_sharing"]

    def perk_training_enabled(self, character : Characters):
        if character.value["slug"] in self.profileData['server_data']["Characters"]:
            return self.profileData['server_data']["Characters"]["ally_perk_sharing"]

    def is_2v2_prompt_shown(self):
        return self.profileData['data']['2v2_prompt_shown']

    def has_pack(self, pack : Packs):
        return pack.value in self.profileData['server_data']
    
    def get_match_lost_count(self, gm : GamemodeMatches):
        """Return amount of games lost in specified GamemodeMatches
        ::
        Args:
            To use this, use GamemodeMatches.NAMEOFGAMEMODE
        ::
        Usage Example:
            >>> .get_match_lost_count(GamemodeMatches.NAMEOGAMEMODE)
        """
        return self.profileData['matches'][gm.value]["loss"] if gm.value in self.profileData['matches'] else 0

    def get_match_won_count(self, gm : GamemodeMatches):
        """Return amount of games won in specified GamemodeMatches
        ::
        Args:
            To use this, use GamemodeMatches.NAMEOFGAMEMODE
        ::
        Usage Example:
            >>> .get_match_won_count(GamemodeMatches.NAMEOGAMEMODE)
        """
        return self.profileData['matches'][gm.value]["win"] if gm.value in self.profileData['matches'] else 0

    def get_win_streak_count(self, gm : GamemodeMatches):
        """Return current winstreak in specified GamemodeMatches
        ::
        Args:
            To use this, use GamemodeMatches.NAMEOFGAMEMODE
        ::
        Usage Example:
            >>> .get_win_streak_count(GamemodeMatches.NAMEOGAMEMODE)
        """
        return self.profileData['matches'][gm.value]["win_streak"] if gm.value in self.profileData['matches'] else 0

    def get_longest_win_streak(self, gm : GamemodeMatches):
        """Return return longest winstreak specified GamemodeMatches
        ::
        Args:
            To use this, use GamemodeMatches.NAMEOFGAMEMODE
        ::
        Usage Example:
            >>> .get_win_streak_count(GamemodeMatches.NAMEOGAMEMODE)
        """
        return self.profileData['matches'][gm.value]["longest_win_streak"] if gm.value in self.profileData['matches'] else 0
