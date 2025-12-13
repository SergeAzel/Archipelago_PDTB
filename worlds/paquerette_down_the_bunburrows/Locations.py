from .RawLocations import pinkLocations, sunkenLocations, hayLocations, \
        spookyLocations, forgottenUpperLocations, forgottenMiddleLocations, \
        forgottenLowerLocations, templeLocations, \
        falseHellLocations, sleepHellLocations, crumblingHellLocations, \
        hellTempleLocations, pillarsLocations

from BaseClasses import Location, CollectionState
from .Consts import PaqueretteGame
from .Items import item_name_to_id


# The truth is, all these "locations" are
# actually bnuuys that could be captured.


class PaqueretteLocation(Location):
    game: str = PaqueretteGame
    dependencies = []

    def access_rule(self, state: CollectionState):
        noDependents = len(self.dependencies) == 0

        allSatisfied = all(state.has(dependency, self.player)
                    for dependency in self.dependencies)

        return noDependents or allSatisfied


def makeLocationName(mapName, index):
    return mapName + "-" + str(index)


def makeLocation(playerId, mapName, index, dependencies):
    if mapName == "W-7":
        x = 5

    name = makeLocationName(mapName, index)
    location = PaqueretteLocation(playerId, name, location_name_to_id[name])

    if mapName in item_name_to_id:
        location.dependencies = [mapName] + (dependencies or [])
    else:
        location.dependencies = dependencies or []

    return location


def makeLocations(playerId, mapName, count, dependencies):
    return [makeLocation(playerId, mapName, index, dependencies)
            for index in range(1, count + 1, 1)]


def generateLocationsFromRaw(playerId, rawLocation):
    match rawLocation:
        case str():
            return makeLocations(playerId, rawLocation, 1, [])
        case (map, count):
            return makeLocations(playerId, map, count, [])
        case (map, count, dependencies):
            return makeLocations(playerId, map, count, dependencies)
    return []


def generateRegionLocations(playerId, regionLocations):
    return [
            location
            for locations in regionLocations
            for location in generateLocationsFromRaw(playerId, locations)
            ]


# locations dictionary generation


def getNextLocationID():
    global last_location_id
    last_location_id += 1
    return last_location_id


def generateLocationTuples(*locationCollections):
    return [
            location
            for locationCollection in locationCollections
            for locations in locationCollection
            for location in generateLocationTupleFromRaw(locations)
            ]


def generateLocationTupleFromRaw(rawLocation):
    match rawLocation:
        case str():
            result = [(makeLocationName(rawLocation, 1),
                      getNextLocationID())]
            return result

        case (map, count):
            result = [(makeLocationName(map, index), getNextLocationID())
                      for index in range(1, count + 1, 1)]
            return result

        case (map, count, _):
            result = [(makeLocationName(map, index), getNextLocationID())
                      for index in range(1, count + 1, 1)]
            return result

    return []


last_location_id = 1

list_of_bunnies = generateLocationTuples(pinkLocations,
                                         sunkenLocations,
                                         hayLocations,
                                         spookyLocations,
                                         forgottenUpperLocations,
                                         forgottenMiddleLocations,
                                         forgottenLowerLocations,
                                         templeLocations,
                                         falseHellLocations,
                                         sleepHellLocations,
                                         crumblingHellLocations,
                                         hellTempleLocations,
                                         pillarsLocations)

list_of_locations = list_of_bunnies

location_name_to_id = {location[0]: location[1]
                       for location in list_of_locations}
location_id_to_name = {location[1]: location[0]
                       for location in list_of_locations}
