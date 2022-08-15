from math import ceil
import string
import requests
import json
from mulpyversus.matches import Match
from mulpyversus.user import User
from mulpyversus.leaderboards import *
from mulpyversus.utils import *

class UsernameSearchResult():
    """Represent a response to a search by username.
    ::
    Set the argument canReturnNone to true to return None if no user is found (otherwise will return an empty list)
    """
    def __init__(self, mlpyvrs, username : string, limit : int, canReturnNone : bool = False):
        self.currentPage = 1
        self.page_ammount = ceil(self.get_total_result()/self.limit)

    def __new__(cls, mlpyvrs, username : string, limit : int = 15, canReturnNone : bool = False):
        obj = super().__new__(cls)
        obj.rawData = json.loads(mlpyvrs.request_data("profiles/search_queries/get-by-username/run?username=" + str(username) + "&limit=" + str(limit) + "").content)
        if obj.rawData["count"] == 0 and canReturnNone:
            return None
        obj.mlpyvrs = mlpyvrs
        obj.username = username
        obj.limit = limit
        return obj
        

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

    def get_user_by_number_in_page(self, number : int):
        """Returns User Object for specified user number if it exist
        ::
        Last User in page otherwise"""
        if number <= self.limit:
            return User(self.rawData["results"][number-1]["result"]["account_id"], self.mlpyvrs)
        else:
            return User(self.rawData["results"][self.get_amount_of_user_in_current_page()-1]["result"]["account_id"], self.mlpyvrs)

    def get_ammount_of_page(self):
        return self.page_ammount

    def next_page(self):
        self.rawData = json.loads(self.mlpyvrs.request_data("profiles/search_queries/get-by-username/run?username=" + str(self.username) + "&limit=" + str(self.limit) + "&cursor=" + str(self.get_current_cursor())))
        self.currentPage += 1

    def get_amount_of_user_in_current_page(self)->int:
        return len(self.rawData["results"])

    def get_users_in_page(self) -> list[User]:
        """Returns a list of users (Object) in the current page"""
        return [User(user["result"]["account_id"], self.mlpyvrs) for user in self.rawData["results"]]

class MulpyVersus:
    """Synchronous Multiversus API wrapper.
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
            self.session = requests.Session()
            self.refresh_token(self.steamToken)

    def refresh_token(self, steamToken : string = None):
        """This method will refresh the token used by the API
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
        req = self.session.post("https://dokken-api.wbagora.com/access", json=tempBody, headers=tempHeaders).json()
        self.token = req["token"]
        self.header = {'x-hydra-api-key':'51586fdcbd214feb84b0e475b130fce0','x-hydra-user-agent':'Hydra-Cpp/1.132.0','Content-Type':'application/json','x-hydra-access-token': self.token}


    def request_data(self, rqst : string):
        """DON'T USE - Used by other classes"""
        req = self.session.get(self.url + rqst, headers=self.header)
        if "msg" in json.loads(req.content) and "User session" in json.loads(req.content)["msg"] :
            self.refresh_token()
            req = self.session.get(self.url + rqst, headers=self.header)
        return req

    def get_match_by_id(self, id:string) -> Match:
        return Match(id, self)

    def get_user_by_id(self, id:string) -> User:
        return User(id, self)

    def get_users_by_username(self, username:string, limit : int = 15, canReturnNone : bool = False) -> UsernameSearchResult:
        """Returns a UsernameSearchResult object containing results for the search
        ::
        Usefull if you want all the results for that name
        ::
        Set the argument canReturnNone to true to return None if no user is found
        """
        return UsernameSearchResult(self, username, limit, canReturnNone)

    def get_user_by_username(self, username:string, limit : int = 15, canReturnNone : bool = False) -> User:
        """Returns a User object for that username
        ::
        If many results are found, returns the first one
        ::
        Usefull if you are confident what the username is
        """
        return UsernameSearchResult(self, username, limit, canReturnNone).get_user_by_number_in_page(1)

    def refresh_user(self, user:User):
        """Used to refresh a User object (all its data)
        You can also use User.refresh() to refresh a User
        Usage Example:
            ::
            MulpyVersus.refresh_user(someone)
        """
        user.__init__(user.get_account_id(), self)

    def get_global_leaderbord_in_gamemode(self, gamemode : GamemodeRank, countLimit:int = 10):
        """Returns a GlobalLeaderboard object
        ::
        Attributes:
        ::
        countLimit : limits the amount of result you get 
        """
        return GlobalLeaderboard(self, gamemode, countLimit)

    def get_user_leaderboard_in_gamemode(self, gamemode : GamemodeRank, id):
        """Returns a UserLeaderboard object
        ::
        """
        return UserLeaderboard(self, gamemode, id)