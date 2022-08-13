# MulpyVersus - Python Wrapper for MultiVersus API 

	This library will help you to use the MultiVersus API with Python easily.
	It is still under development, please report any issue you encounter. Python > 3.9

![mulpyversus](https://cdn.discordapp.com/attachments/361240816397582336/1006703539365617674/mulpyversus.png)


# Usage
    pip install mulpyversus 

With this version, you will need a **Steam Ecrypted App Ticket**. You get get yours [**here**](https://github.com/brianbaldner/multiversus-api-docs/tree/main/steam-ticket-generator). *Future* version should include **the possibility to use an API that doesn't require any sort of token**.

## Get the API working

Initializing the MulpyVersus class is the first step. With this object, you will be able to call any search function.

    from mulpyversus.mulpyversus import MulpyVersus
    mlp = MulpyVersus("youSteamEcryptedAppTicket")

Now also support Async. Make sure to call init on the AsyncMulpyVersus object after creating it. 

    from mulpyversus.async.mulpyversus import AsyncMulpyVersus
    mlp = AsyncMulpyVersus("youSteamEcryptedAppTicket")
    await mlp.init()
    
    --Do Stuff--
    
    await mlp.close_session()

By giving your Steam Ecrypted App Ticket, your access_token will automatically be refreshed whenever it is no longer valid. 
**So no need to manually change it every 24h !** 

# Exemples

## Get information about a Match

You can store all the information about a match like this : 

    match = mlp.get_match_by_id("62f030a5b6460ad6562b7118")
    
    print(match.get_all_players_data_in_match()[0].get_user().get_top_ranked_character_in_gamemode(GamemodeRating.TwoVsTwo)
    
    print(match.get_losers()[0].get_wins_with_character(Characters.Finn)
The first print shows you how to **get the top ranked character on the specified GameMode for the player number 1 of the match** (this list can contain a single element or more depending on the gamemode).

The second one shows you **how much win with Finn has the loser number 1 of this match** (this list can contain a single element or more depending on the gamemode).

## Get information about a User 

You can store all the information about a user like this : 

    user = mlp.get_user_by_id("62eb10309f54a8d97a42c15d")
    
    print(user.get_matches_played())
    
    print(user.has_network(Networks.Twitch))
The first print shows you how to **get the amount of match a User has played**.

The second one returns you **informations about the specified network if it is linked to the users account or False otherwise** (this will be improved in future version).
## Utils file

To make it easier to use this library, every character name, network name, perk id, gamemode names, ect. are stored in enumes that you will find in the utils.py file. 
Exemple : 

	 class  Characters(enum.Enum):
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
    
**Everytime** one of theses attributs is necessary(a gamemode, a charachter, cet), use theses **enums**. 
The file also contains **methods** to convert from slug to name and vice versa.


# Classes

## MulpyVersus

	Synchronous Multiversus API wrapper.
	Represent the basic client.
	Args: steamToken = The steam encrypted app ticket token
	Usage Example :
	   from mulpyversus.mulpyversus import MulpyVersus
	   mlp = MulpyVersus("youSteamEcryptedAppTicket")


**refresh_token(steamToken : string)**

> This method will refresh the token used by the API
The token generated when you create a MulpyVersus object with a Steam Encrypted Key is usable for 24hours
It should be refreshed at least everyone 24hours, but it is automatically refreshed if a request doesn't work
Optional: You can pass a new steam token if you want to change it
Usage Example :
mulpyversus.refresh_token()
or
mulpyversus.refresh_token("aNewSteamToken")

**get_match_by_id(id : string)**

> To get a match using its ID


**get_user_by_id(id : string)**

> To get a user by its ID

**get_match_by_id(id : string)**

> To get a match using its ID

**get_users_by_username(username : string, limit : int, canReturnNone : bool)**

> Returns a instance of the class UsernameSearchResult containing results for the search
Usefull if you want all the results for that name
By default, will return a UsernameSearchResult even if no result are found
Set the argument canReturnNone to true to return None if no user is found

**get_user_by_username(username : string, limit : int, canReturnNone : bool)**

> Returns a User object for that username
If many results are found, returns the first one
Usefull if you are confident what the username is

**refresh_user(user : User)**

> Used to refresh a User object.
> Use this when you want to get up to date info about a user for whom you already have a User object.
> You can also use User.refresh() to refresh a User
MulpyVersus.refresh_user(someone)



## Match

	Represent a match object
**get_player_ammount_in_match()**

> Gets the amount of player in the match.
> Examples: amounfOfPlayer = matches.get_player_ammount_in_match()

**get_match_id()**

> Gets the id of the match.
> Examples: matchId = matches.get_match_id()

**get_created_at()**

> When the match was created

**get_updated_at()**

> When the match was last updated

**get_completion_time()**

> When the match was completed

**get_access_level()**

> Gets the access level of the match (private etc..).

**get_name()**

> Gets the name of the match

**get_winners()**

> Return a list of instance of the class User
> You can access a specific winner with get_winner()[index]

**get_losers()**

> Return a list of instance of the class **User**
> You can access a specific loser with **get_winner**()[index]

**is_draw()**

> If the match is a draw

**is_custom_match()**

> If the match is a custom match

**get_map()**

> Return the map

**get_all_players_data_in_match()**

> Return  a list with instances of the class **PlayerMatchData** of all players in the match

**get_player_data_by_id()**

> Return an  instance of the class **PlayerMatchData** for the specified player in the match

**get_winning_team_id()**

> Return the id of the winning team

**get_match_max_player()**

> Return max ammount of players allowed in this match

**get_match_min_players()**

> Return max ammount of players allowed in this match

**get_match_template_name()**

> Return the match template name

## PlayerMatchData

	Represent a PlayerData object from a Match
	Contains all the informations about a player for this match
	Ex: damage dealt, ringounts ect


**get_account_id()**

> Return the account id for the player related to this Object

**get_character_slug()**

>A string representing the character played this match by the player
You can get a display name of the character using **Utils.slug_to_display(theSlugName)**

**get_damage_dealt()**

> Return the amount of damage this player dealt during the match

**get_death_amount()**

> Return the amount of death for this user in this match

**get_guild_id()**

> Return the guild id

**is_guilded_match()**

> Return if the match is a guilded match

**get_played_plateform()**

> Return the platform this player played on (PC ect)

**get_player_index()**

> Return the player index in the match

**get_ringouts_dealt()**

> Return the amount of ringouts this player dealt during this match

**get_score()**

> Return this players score for this match

**get_team_index()**

> Return this player team index for this match

**get_username()**

> Return the username of this player 

**get_user()**

> Return an instance of instance of the class **User** for this player

## User

	Represent a match object
**refresh()**

> Used to refresh a User object
> Use this when you want to get up to date info about a user for whom you already have a User object.

**get_id()**

> Gets the id of the user.

**get_account_id()**

> Gets the account id of the user.

**get_updated_at()**

> When the userwas last updated

**get_created_at()**

> When the usercreated his account

**get_last_login()**

> When the user was last logged in

**get_points()**

> Gets the points

**is_child_account()**

> If this account is a child account

**get_perk_preferences()**

> Returns a list of PerkPage objects related to this user

**get_perk_preference_by_character(character : Characters)**

> Returns PerkPage objects for specified Character
Returns False if the Character is not found

**get_public_id()**

> Gets the public id

**get_default_username()**

> Gets default username

**is_username_default_username()**

> If the username is a default username given by warner bros network

**get_user_networks()**

> Return a list of instance of the class **UserNetwork** 

**has_network(network : Networks)**

> Returns Network objects for specified network
> Returns False if the network is not found in the user's network list

**get_last_login_platform()**

> Return the last platform the user was logged in with

**get_last_played_character()**

> Return the last character the user played

**get_last_login_time()**

> Return the last time the user logged in

**get_last_logout_time()**

> Return the last time the user logged out

**get_character_level(characterName : Characters)**

> Return the level of the given character for this user
> To use this, use Characters.NAMEOFCHARS

**get_character_current_exp()**

> Return the current experience of the given character for this user
To use this, use Characters.NAMEOFCHARS

**get_user_level()**

> Gets user level

**get_user_first_claim_time()**

> Gets the user first claim time

**get_anti_cheat_server_kick()**

> If the user ever go kicked by anti cheat

**get_debug_all_unlocked()**

> If the user unlocked everything

**get_match_min_players()**

> Return max ammount of players allowed in this match

**get_battlepass_id()**

> Return the battlepass id

**get_highest_damage_dealt()**

> Return the highest amount of damage this user dealt

**get_total_ringout_leader()**

> Return max amount of time this player had the most ringouts dealt

**get_total_ringouts()**

> Return the total amount of ringouts this user dealt 

**get_total_wins()**

> Return the total amount of wins this user has

**get_wins_with_character(characterName : Characters)**

> Return the number of winss with the character
To use this, use Characters.NAMEOFCHARS

**get_total_attacks_dodged()**

> Return the total amount of attack this user dodged

**get_total_assits()**

> Return the total amount of assist this user has

**get_unclaimed_character_rewards(characterName : Characters)**

> Return unclaimed rewards for the charachter
FOR NOW, THIS WILL RETURN ALL INFORMATIONS AS JSON
To use this, use Characters.NAMEOFCHARS

**get_lifetime_damage()**

> Return the total amount of damage this user ever dealt

**get_lifetime_ringouts()**

> Return the total amount of ringouts this user ever dealt

**get_loss_streak()**

> Return the current los streak 

**get_matches_played()**

> Return the total amount of match this user played

**get_sets_played()**

> Return the total ammount of sets this user played

**get_all_owned_perks()**

> Return a list of instances of the class **Perks**
> To get specific data from a perk, use the PerkValue Enum
Exemple: somePerk.value[PerkValue.WANTEDVALUE.value]
List of values : Slug, HydraName, DisplayName, Description, AssociatedCharacterName, Category, Rarity, GoldPrice, GoldSalePrice

**get_owned_perks_by_character(character : Characters)**

> Return a list of instances of the class **Perks** for the specified character
> To get specific data from a perk, use the PerkValue Enum
Exemple: somePerk.value[PerkValue.WANTEDVALUE.value]
List of values : Slug, HydraName, DisplayName, Description, AssociatedCharacterName, Category, Rarity, GoldPrice, GoldSalePrice

**get_character_rating(character : Characters, rating : RatingKeys, gm : GamemodeRating)**

> Return the value of the desired Rating for the specified Character on the specified Gamemode
If the user has not rating for this character, this return -1.0
To use this, use Characters.NAMEOFCHARS
To use this, use RatingKeys.RATINGKEY
To use this, use GamemodeRating.NAMEOFGAMEMODE

**get_top_ranked_character_in_gamemode(gm : GamemodeRating)**

> Return the top ranked character in given GamemodeRating
To use this, use GamemodeRating.NAMEOFGAMEMODE

**get_top_rated_character_ratings()**

> Return the asked rating for the top ranked character in the given gamemode
If the user has not rating for this gamemode, this return -1.0
To use this, use RatingKeys.RATINGKEY
To use this, use GamemodeRating.NAMEOFGAMEMODE

**get_ally_perk_sharing(character : Characters)**

> Return ally perk shring for given character 

**perk_training_enabled()**

> Return perk traning enabled for given character

**is_2v2_prompt_shown()**

> If the 2v2 prompt is shown 

**has_pack(pack : Packs)**

> If the user has the specified pack

**get_match_lost_count(gm : GamemodeMatches)**

> Return amount of games lost in specified GamemodeMatches
To use this, use GamemodeMatches.NAMEOFGAMEMODE

**get_match_won_count(gm : GamemodeMatches)**

>  Return amount of games won in specified GamemodeMatches
To use this, use GamemodeMatches.NAMEOFGAMEMODE

**get_win_streak_count()**

> Return current winstreak in specified GamemodeMatches
To use this, use GamemodeMatches.NAMEOFGAMEMODE

**get_longest_win_streak()**

>Return return longest winstreak in specified GamemodeMatches
To use this, use GamemodeMatches.NAMEOFGAMEMODE

## PerkPage

	Represent a PerkPage object

**refresh()**

> Used to refresh a User object
> Use this when you want to get up to date info about a user for whom you already have a User object.

**get_character()**

> Gets the character related to this PerkPage

**get_page_name()**

> Gets the name of the page

**get_main_perk()**

> Represent the main perk for this page
To get specific data from a perk, use the PerkValue Enum
Exemple: somePerk.value[PerkValue.WANTEDVALUE.value]
List of values : Slug, HydraName, DisplayName, Description, AssociatedCharacterName, Category, Rarity, GoldPrice, GoldSalePrice

**get_first_perk()**

> Represent the first "small" perk for this page
To get specific data from a perk, use the PerkValue Enum
Exemple: somePerk.value[PerkValue.WANTEDVALUE.value]
List of values : Slug, HydraName, DisplayName, Description, AssociatedCharacterName, Category, Rarity, GoldPrice, GoldSalePrice

**get_second_perk()**

> Represent the second "small" perk for this page
To get specific data from a perk, use the PerkValue Enum
Exemple: somePerk.value[PerkValue.WANTEDVALUE.value]
List of values : Slug, HydraName, DisplayName, Description, AssociatedCharacterName, Category, Rarity, GoldPrice, GoldSalePrice

**get_third_perk()**

> Represent the third "small" perk for this page
To get specific data from a perk, use the PerkValue Enum
Exemple: somePerk.value[PerkValue.WANTEDVALUE.value]
List of values : Slug, HydraName, DisplayName, Description, AssociatedCharacterName, Category, Rarity, GoldPrice, GoldSalePrice

**get_related_account_id()**

> Gets the account_id of the user related to this page

## UserNetwork

	Represent a UserNetwork object
	A network linked to the users account

**get_network_name()**

> Returns the name of the network.
Exemple: "wb_network", "twitch", "steam"

**get_network_user_id()**

> Returns the users id on that network.
Returns None if the network has no ID

**get_network_user_avatar()**

> Returns the users avatar on that network.
Returns None or null if the network has no avatar

**get_network_user_username()**

> Returns the users username on that network.
Returns None or null if the network has no username

**get_network_user_created_at()**

> Returns the users created_at on that network.
Returns None or null if the network has no created_at

**get_related_account_id()**

> Represent the account_id of the user related to this page


## UsernameSearchResult

	Represent a response to a search by username.
	Set the argument canReturnNone to true to return None if no user is found.
	You can navigate all its pages

**set_limit()**

> To set the limit per page for this UsernameSearchResult

**get_total_result()**

> Get the total amount of users found by this search

**get_start()**

> Get at what index the current page starts

**get_current_page()**

> Get the current page number

**get_page_by_number(pageNumber: int)**

> Set the UserNamePage Object to the specified page number if it exist
Last page otherwise

**get_user_by_number_in_page(number : int)**

> Returns a User Object for specified user number if it exist
Last User in page otherwise

**get_ammount_of_page()**

> Returns the total amount of pages for this search


**next_page()**

> Set this UsernameSearchResult to its next page


**get_amount_of_user_in_current_page()**

> Returns the amount of users in the current page


**get_users_in_page()**

> Returns a list of User Object for every user in the current page"

