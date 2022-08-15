from math import ceil
import string
import requests
import aiohttp
import asyncio
import json
from mulpyversus.asyncleaderboards import *
from mulpyversus.asyncuser import AsyncUser
from mulpyversus.asyncmatches import AsyncMatch
from mulpyversus.utils import *

class AsyncUsernameSearchResult():
    """Represent a response to a search by username.
    ::
    Set the argument canReturnNone to true to return None if no user is found (otherwise will return an empty list)
    """
    def __init__(self, mlpyvrs, username : string, limit : int, canReturnNone : bool = False):
        self.currentPage = 1
        self.page_ammount = ceil(self.get_total_result()/self.limit)
        self.mlpyvrs = mlpyvrs
        self.username = username
        self.limit = limit
        self.canReturnNone = canReturnNone

    async def init(self):
        self.rawData = await self.mlpyvrs.request_data("profiles/search_queries/get-by-username/run?username=" + str(self.username) + "&limit=" + str(self.limit) + "")
        if self.rawData["count"] == 0 and self.canReturnNone:
            return None
        else: 
            return self

    def __repr__(self):
        return str(self.rawData)

    def set_limit(self, limit: int):
        self.limit = limit

    def get_total_result(self):
        return self.rawData["total"]

    def get_start(self):
        return self.rawData["start"]

    def get_current_cursor(self):
        return self.rawData["cursor"]

    def get_current_page(self):
        self.currentPage

    def get_page_by_number(self, pageNumber: int):
        """Set the UserNamePage Object to specified page number if it exist
        ::
        Last page otherwise"""
        if pageNumber<=self.page_ammount:
            for i in range(pageNumber-self.currentPage):
                self.next_page()
        else:
            for i in range(self.page_ammount-self.currentPage):
                self.next_page()

    async def get_user_by_number_in_page(self, number : int):
        """IS ASYNC : Returns User Object for specified user number if it exist
        ::
        Last User in page otherwise"""
        if number <= self.limit:
            user = AsyncUser(self.rawData["results"][number-1]["result"]["account_id"], self.mlpyvrs)
            await user.init()
            return user
        else:
            user = AsyncUser(self.rawData["results"][self.get_amount_of_user_in_current_page()-1]["result"]["account_id"], self.mlpyvrs)
            await user.init()
            return user
        
    def get_ammount_of_page(self):
        return self.page_ammount

    def next_page(self):
        self.rawData = json.loads(self.mlpyvrs.request_data("profiles/search_queries/get-by-username/run?username=" + str(self.username) + "&limit=" + str(self.limit) + "&cursor=" + str(self.get_current_cursor())))
        self.currentPage += 1

    def get_amount_of_user_in_current_page(self)->int:
        return len(self.rawData["results"])

    async def get_users_in_page(self) -> list[AsyncUser]:
        """IS ASYNC : Returns a list of users (Object) in the current page"""
        users = []
        for user in self.rawData["results"]:
            newUser = AsyncUser(self.rawData["results"][self.get_amount_of_user_in_current_page()-1]["result"]["account_id"], self.mlpyvrs)
            await newUser.init()
            users.append(newUser)
        return users

class AsyncMulpyVersus:
    """Asynchronous Multiversus API wrapper.
    Represent the basic client.
    ::
    Args:
        steamToken: The steam encrypted app ticket token
    Usage Example:
        from mulpyversus import MulpyVersus
        ::
        mulpyversus = MulpyVersus("yourSteamToken")
    """
    def __init__(self, steamToken = None):
        if not steamToken is None:
            self.url = "https://dokken-api.wbagora.com/"
            self.steamToken = steamToken
            self.session = aiohttp.ClientSession()

    async def init(self):
        await self.refresh_token()
    
    async def refresh_token(self, steamToken : string = None):
        """IS ASYNC : This method will refresh the token used by the API
        ::
        The token  generated when you create a MulpyVersus object with a Steam Encrypted Key is usable for 24hours
        ::
        Must be refreshed at least everyone 24hours, is automatically refreshed if request doesnt' work
        ::
        Optional: You can pass a new steam token if you want to change it
        Usage Example:
            ::
                mulpyversus.refresh_token()
                or
                mulpyversus.refresh_token("aNewSteamToken")
        """
        if not steamToken is None:
            self.steamToken = steamToken
        tempHeaders = {'x-hydra-api-key':'51586fdcbd214feb84b0e475b130fce0','x-hydra-user-agent':'Hydra-Cpp/1.132.0','Content-Type':'application/json','x-hydra-client-id':'47201f31-a35f-498a-ae5b-e9915ecb411e'}
        tempBody = { "auth": { "fail_on_missing": 1, "steam": self.steamToken }, "options": [ "wb_network" ] }
        req = await self.session.post("https://dokken-api.wbagora.com/access", json=tempBody, headers=tempHeaders)
        req = await req.json()
        self.token = req["token"]
        self.header = {'x-hydra-api-key':'51586fdcbd214feb84b0e475b130fce0','x-hydra-user-agent':'Hydra-Cpp/1.132.0','Content-Type':'application/json','x-hydra-access-token': self.token}
        
    async def close_session(self):
        await self.session.close()

    async def request_data(self, rqst : string):
        """DON'T USE - Used by other classes"""
        req = await self.session.get(self.url + rqst, headers=self.header)
        req = await req.json()
        if "msg" in req and "User session" in req["msg"]:
            await self.refresh_token()
            req = await self.session.get(self.url + rqst, headers=self.header)
        return req

    async def get_match_by_id(self, id:string) -> AsyncMatch:
        match = AsyncMatch(id, self)
        await match.init()
        return match

    async def get_user_by_id(self, id:string) -> AsyncUser:
        user = AsyncUser(id, self)
        await user.init()
        return user

    async def get_users_by_username(self, username:string, limit : int = 15, canReturnNone : bool = False):
        """IS ASYNC : Returns a UsernameSearchResult object containing results for the search
        ::
        Usefull if you want all the results for that name
        ::
        Set the argument canReturnNone to true to return None if no user is found
        """
        search = AsyncUsernameSearchResult(self, username, limit, canReturnNone)
        search = search.init()
        return search

    async def get_global_leaderbord_in_gamemode(self, gamemode : GamemodeRank, countLimit:int = 10):
        """IS ASYNC
        ::
        Returns a GlobalLeaderboard object
        ::
        Attributes:
        ::
            countLimit : limits the amount of result you get 
        """
        leaderbord = AsyncGlobalLeaderboard(self, gamemode, countLimit)
        leaderbord.init()
        return leaderbord

    async def get_user_leaderboard_in_gamemode(self, gamemode : GamemodeRank, id):
        """IS ASYNC
        ::
        Returns a UserLeaderboard object
        ::
        """
        leaderbord = AsyncUserLeaderboard(self, gamemode, id)
        leaderbord.init()
        return leaderbord