STD = 0
TAIKO = 1
CTB = 2
MANIA = 3

def getGameModeForDB(gameMode):
	"""
	Convert a game mode number to string for database table/column

	:param gameMode: game mode number
	:return: game mode readable string for db
	"""

	if gameMode == STD:
		return "std"
	elif gameMode == TAIKO:
		return "taiko"
	elif gameMode == CTB:
		return "ctb"
	else:
		return "mania"

def getGamemodeFull(gameMode):
	"""
	Get game mode name from game mode number

	:param gameMode: game mode number
	:return: game mode readable name
	"""
	if gameMode == STD:
		return "osu!"
	elif gameMode == TAIKO:
		return "osu!taiko"
	elif gameMode == CTB:
		return "osu!catch"
	else:
		return "osu!mania"

def getGameModeForPrinting(gameMode):
	"""
	Convert a gamemode number to string for showing to a user (e.g. !last)

	:param gameMode: gameMode int or variable (ex: gameMode.std)
	:return: game mode readable string for a human
	"""
	if gameMode == STD:
		return "osu!"
	elif gameMode == TAIKO:
		return "osu!taiko"
	elif gameMode == CTB:
		return "osu!catch"
	else:
		return "osu!mania"