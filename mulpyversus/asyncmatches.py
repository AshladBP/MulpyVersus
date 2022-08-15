import string
from mulpyversus.asyncuser import AsyncUser
import json

class AsyncPlayerMatchData:
    """Represent a PlayerData object from a Match
    ::
    Contains all the informations about a player for this match
    ::
    Ex: damage dealt, ringounts ect
    ::
    Usage Example:
        ::
    """
    def __init__(self, data : dict, mlpyvrs):
        self.rawData = data
        self.mlpyvrs = mlpyvrs

    def __repr__(self):
        return str(self.rawData)

    def get_account_id(self) -> string:
        return self.rawData['AccountId']

    def get_character_slug(self) -> string:
        """A string representing the character played this match by the player
        ::
        You can get a display name of the character using Utils.slug_to_display(theSlugName)
        """
        return self.rawData['CharacterSlug']

    def get_damage_dealt(self) -> string:
        return self.rawData['DamageDone']

    def get_death_amount(self) -> string:
        return self.rawData['Deaths']
    
    def get_guild_id(self) -> string:
        return self.rawData['GuildId']

    def is_guilded_match(self) -> bool:
        return self.rawData['IsGuildedMatch']

    def get_played_plateform(self) -> string:
        return self.rawData['PlayedPlatform']

    def get_player_index(self) -> int:
        return self.rawData['PlayerIndex']

    def get_ringouts_dealt(self) -> int:
        return self.rawData['Ringouts']

    def get_score(self) -> int:
        return self.rawData['Score']

    def get_team_index(self) -> int:
        return self.rawData['TeamIndex']

    def get_username(self) -> string:
        return self.rawData['Username']
    
    async def get_user(self) -> AsyncUser:
        """IS ASYNC"""
        user = AsyncUser(self.get_account_id(), self.mlpyvrs)
        await user.init()
        return user



class AsyncMatch:
    """Represent a match object
    ::
    Args:
        data: result of a match request
    Usage Example:
        ::
            a
    Attributes:
    """
    def __init__(self, id : string, mlpyvrs):
        self.mlpyvrs = mlpyvrs
        self.id = id
        
    async def init(self):
        self.rawData = await self.mlpyvrs.request_data("matches/" + self.id)

    def __repr__(self):
        return str(self.rawData)

    def get_raw_data(self):
        return self.rawData

    def get_player_ammount_in_match(self) -> int:
        """Gets the amount of player in the match.
        ::
        Returns:
            int: ammount of players.
            ::
        Examples:
            >>> amounfOfPlayer = matches.get_player_ammount_in_match()
        """
        return len(self.rawData['server_data']['PlayerData'])

    def get_match_id(self) -> string:
        """Gets the id of the match.
        ::
        Returns:
            int: id.
        ::
        Examples:
            >>> matchId = matches.get_match_id()
        """
        return self.rawData['id']
    
    def get_created_at(self) -> string:
        return self.rawData['created_at']

    def get_updated_at(self) -> string:
        return self.rawData['updated_at']
    
    def get_completion_time(self) -> string:
        return self.rawData['completion_time']

    def get_access_level(self) -> string :
        """Gets the access level of the match (private etc..).
        ::
        Returns:
            string: the access level.
        """
        return self.rawData['access_level']

    def get_name(self) -> string:
        return self.rawData['name']

    async def get_winners(self) -> list[AsyncUser]:
        """IS ASYNC : Returns a list of winner in this match.
        ::
        You can access a specific winner with get_winner()[index]
        ::
        Returns:
            list[user]: a list of winner.
        """
        users = []
        for id in self.rawData['win']:
            newUser = AsyncUser(id, self.mlpyvrs)
            await newUser.init()
            users.append(newUser)
        return users

    async def get_losers(self)-> list[AsyncUser] :
        """IS ASYNC : Returns a list of loosers in this match.
        ::
        You can access a specific looser with get_losers()[index]
        ::
        Returns:
            list[User]: a list of loosers.
        """
        users = []
        for id in self.rawData['loss']:
            newUser = AsyncUser(id, self.mlpyvrs)
            await newUser.init()
            users.append(newUser)
        return users

    def is_draw(self):
        return self.rawData['draw']
    
    def is_custom_match(self):
        return self.rawData['server_data']['IsCustomMatch']

    def get_map(self):
        return self.rawData['map']

    def get_player_data_by_id(self, id : int):
        if self.get_player_ammount_in_match()-1 <= id and id>0:
            return AsyncPlayerMatchData(self.rawData['server_data']['PlayerData'][id], self.mlpyvrs)
        else:
            raise ValueError('The id you passed is invalid (too big or too small) - Use get_player_ammount_in_match() to know total ammount of players.')
        
    def get_all_players_data_in_match(self) -> list[AsyncPlayerMatchData]:
        return [AsyncPlayerMatchData(data , self.mlpyvrs) for data in self.rawData['server_data']['PlayerData']]

    def get_team_score_by_id(self, id : int) -> int:
        if self.get_player_ammount_in_match()-1 <= id and id>0:
            return self.rawData['server_data']['TeamScores'][id]
        else:
            raise ValueError('The id you passed is invalid (too big or too small) - Use get_player_ammount_in_match() to know total ammount of players.')

    def get_winning_team_id(self) -> int:
        return self.rawData['server_data']['WinningTeamId']

    def get_match_template_name(self) -> string:
        return self.rawData['template']['name']
    
    def get_match_max_player(self)-> int:
        return self.rawData['template']['max_players']
    
    def get_match_min_players(self)-> int:
        return self.rawData['template']['min_players']



