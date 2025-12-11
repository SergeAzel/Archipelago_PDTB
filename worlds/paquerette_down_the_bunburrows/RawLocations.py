# Locations are bnuuys
# either a string for a simple room that (optionally) requires its own tools
# or a tuple of (name, # of buns, [extra tools required])
# locations also are beholden to their region restrictions

pinkLocations = [
        "W-1",
        "W-2",
        "W-3",
        "W-4",
        "W-5",
        ("W-6", 2),
        ("W-7", 1, ["C-7"]),
        "W-8",
        "W-9",
        "W-10",
        "W-11",
        "W-12",
        ]

sunkenLocations = [
        "N-1",
        "N-2",
        "N-3",
        "N-4",
        "N-5",
        "N-6",
        "N-7",
        "N-8",
        "N-9",
        "N-10",
        "N-11"
        ]

hayLocations = [
        "C-1",
        "C-2",
        "C-3",
        "C-4",
        "C-5",
        "C-6",
        "C-7",
        "C-8",
        "C-9",
        "C-10",
        "C-11",
        "C-12"
        ]

spookyLocations = [
        "S-1",
        "S-2",
        "S-3",
        "S-4",
        "S-5",
        "S-6",
        "S-7",
        "S-8",
        "S-9",
        "S-10",
        "S-11",
        "S-12"
        ]

forgottenLocations = [
        "E-1",
        "E-2",
        ("E-3", 4, ["E-2"]),  # TODO- Update to be accurate for C access?
        ("E-4", 1, ["E-3"]),
        ("E-5", 1, ["E-3"]),  # TODO- Update to be accurate for C access?
        ("E-6", 1, ["E-5"]),
        ("E-7", 1, ["E-6"]),
        ("E-8", 1, ["E-7"]),
        ("E-9", 2, ["E-8"]),
        ("E-10", 2, ["E-9"]),
        ("E-12", 2, ["E-11"])
        ]

templeLocations = [
        "C-13",

        "W-13",
        "W-14",
        "W-15",
        "W-16",
        "W-17",
        "W-18",

        "N-12",
        ("N-13", 3),
        "N-14",
        "N-15",
        "N-16",
        "N-17",
        "N-18",

        "S-13",
        "S-14",
        "S-15",
        "S-16",
        "S-17",
        "S-18",
        "S-19",
        ("S-20", 1, ["C-20"])
        ]

falseHellLocations = [
        "C-14",
        "C-15",
        "C-16",
        "C-17",
        "C-18",
        "C-19",
        ]

sleepHellLocations = [
        "E-14",
        "E-15",
        "E-16",
        "E-17",
        "E-18",
        "E-19",
        "E-20",
        ("E-21", 1, ["E-20"]),
        ("E-22", 1, ["E-20"]),
        ]

crumblingHellLocations = [
        "C-20",
        "C-21",
        ("C-22", 1, ["E-22"]),
        "C-23",
        "C-24",

        "W-19",
        "W-20",
        ("W-21", 1, ["C-21"]),

        "N-19",
        ("N-20", 4),
        "N-21",
        ("N-22", 2, ["C-22"]),
        ("N-23", 1, ["C-22"]),

        ("S-21", 2, ["C-21"]),
        ("S-22", 1, ["C-22"]),
        ("S-23", 1, ["S-22"]),
        ("S-24", 2, ["S-23"]),
        ]

hellTempleLocations = [
        "W-23",
        "W-24",
        "W-25",
        ("W-26", 2),

        ("C-26", 1, ["W-26"]),
        ("C-27", 1, ["N-26", "C-26", "C-25", "N-25", "S-25", "S-26",
                     "E-23", "E-24", "E-25", "E-26", "E-27"])
        ]
