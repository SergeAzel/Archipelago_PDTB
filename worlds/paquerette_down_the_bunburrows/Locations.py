from .RawLocations import pinkLocations, sunkenLocations, hayLocations, \
        spookyLocations, forgottenUpperLocations, forgottenMiddleLocations, \
        forgottenLowerLocations, templeLocations, \
        falseHellLocations, sleepHellLocations, crumblingHellLocations, \
        hellTempleLocations, pillarsLocations, south20Location, \
        southTempleLocations, forgotten9Location

from BaseClasses import Location, CollectionState
from .Consts import PaqueretteGame
from .Items import item_name_to_id


# The truth is, all these "locations" are
# actually bnuuys that could be captured.


class PaqueretteLocation(Location):
    game: str = PaqueretteGame
    dependencies = []
    alternateDependencies = None

    def access_rule(self, state: CollectionState):
        noDependents = len(self.dependencies) == 0

        allSatisfied = all(state.has(dependency, self.player) for dependency in self.dependencies)

        # If Alternate is None, it is NOT free - also, short-circuit if needed
        if self.alternateDependencies == None or noDependents or allSatisfied:
            return noDependents or allSatisfied

        alternateFree = (self.alternateDependencies == [])
        alternateSatisfied = all(state.has(dependency, self.player) for dependency in self.alternateDependencies)

        return noDependents or allSatisfied or alternateFree or alternateSatisfied


def makeLocationName(mapName, index):
    return mapName + "-" + str(index)


def makeLocation(playerId, mapName, index, dependencies, expertDependencies):
    name = makeLocationName(mapName, index)
    location = PaqueretteLocation(playerId, name, location_name_to_id[name])

    if mapName in item_name_to_id:
        location.dependencies = [mapName] + (dependencies or [])
    else:
        location.dependencies = dependencies or []

    if expertDependencies is not None:
        if mapName in item_name_to_id:
            location.alternateDependencies = [mapName] + expertDependencies
        else:
            location.alternateDependencies = expertDependencies

    return location


def makeLocations(playerId, mapName, count, dependencies, expertDependencies):
    return [makeLocation(playerId, mapName, index, dependencies, expertDependencies)
            for index in range(1, count + 1, 1)]


def generateLocationsFromRaw(playerId, rawLocation, expertRouting: bool):
    match rawLocation:
        case str():
            return makeLocations(playerId, rawLocation, 1, [], None)
        case (map, count):
            return makeLocations(playerId, map, count, [], None)
        case (map, count, dependencies):
            return makeLocations(playerId, map, count, dependencies, None)
        case (map, count, standardDependencies, expertDependencies):
            return makeLocations(playerId, map, count, standardDependencies, expertDependencies if expertRouting else None)
    return []


def generateRegionLocations(playerId, regionLocations, expertRouting: bool):
    return [
            location
            for locations in regionLocations
            for location in generateLocationsFromRaw(playerId, locations, expertRouting)
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

        case (map, count, _, _):
            result = [(makeLocationName(map, index), getNextLocationID())
                      for index in range(1, count + 1, 1)]
            return result

    return []


last_location_id = 1

list_of_credits_bunnies = generateLocationTuples(pinkLocations,
                                         sunkenLocations,
                                         hayLocations,
                                         spookyLocations,
                                         forgottenUpperLocations,
                                         forgottenMiddleLocations,
                                         forgotten9Location,
                                         forgottenLowerLocations,
                                         templeLocations)



list_of_bunnies = list_of_credits_bunnies + generateLocationTuples(falseHellLocations,
                                         sleepHellLocations,
                                         crumblingHellLocations,
                                         southTempleLocations,
                                         south20Location,
                                         hellTempleLocations,
                                         pillarsLocations)

list_of_locations = list_of_bunnies

location_name_to_id = {location[0]: location[1]
                       for location in list_of_locations}
location_id_to_name = {location[1]: location[0]
                       for location in list_of_locations}

