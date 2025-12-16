from Options import Toggle, PerGameCommonOptions, Choice, Range
from dataclasses import dataclass

from worlds.stardew_valley.stardew_rule import true_


class HomeCaptures(Toggle):
    """Intended for players familiar with deeper mechanics of Paquerette:
    Enabling this will mean only home-captures are sufficient to unlock an item."""
    display_name = "Home Captures Only"


class VictoryCondition(Choice):
    """Determines your victory condition.
    For short games or new players, we recommend Credits.

    - **Credits**: Reach the Credits! Beginner-friendliest choice.
    - **Golden Bunny**: Find the Golden Bunny!
    - **Golden Fluffle**: Capture bunnies until you find all Golden Fluffles!
    - **Full Clear**: Capture all bunnies!"""
    display_name = "Victory Condition"
    rich_text_doc = True
    option_credits = 0
    option_golden_bunny = 1
    option_golden_fluffle = 2
    option_full_clear = 3
    default = 0


class GoldenFluffleCount(Range):
    """**GOLDEN FLUFFLE RUNS ONLY**
    Determines how many Golden Fluffles will be scattered through your world!
    """
    display_name = "Golden Fluffles"
    rich_text_doc = True
    range_start = 1
    range_end = 20
    default = 6


class ExpertRouting(Toggle):
    """Enabling this feature may create routes that require advanced techniques or have complicating pathing."""
    display_name = "Expert Routing"


class UnlockComputer(Toggle):
    """Unlock the portable computer by default"""
    display_name = "Unlock Computer"


class UnlockMap(Toggle):
    """Unlock the map in the computer by default"""
    display_name = "Unlock Map"


class Traps(Range):
    """Whether or not to include traps, and how many"""
    display_name = "Enable Traps"
    range_start = 0
    range_end = 10
    default = 0


class DeathLink(Toggle):
    """Should deathlink be enabled?"""
    display_name = "DeathLink"


class DeathLinkBehavior(Choice):
    """Deaths through Death Link will activate a trap.

    - **RNG**: Picks a trap at random (NonDeterministic)!
    - **Surface**: Returns Paquerette to the surface!
    - **Elevator**: Elevator :)"""
    display_name = "Death Link Behavior"
    rich_text_doc = True
    option_rng = 0
    option_surface = 1
    option_elevator = 2


class ElevatorTrapDepth(Range):
    """How long of an Elevator Ride should you have?"""
    display_name = "Elevator Trap Depth"
    range_start = 1
    range_end = 100


class ElevatorTrapIncrement(Range):
    """Every time you ride, the ride gets longer!"""
    display_name = "Elevator Trap Increment"
    range_start = 0
    range_end = 20


@dataclass
class PaqueretteOptions(PerGameCommonOptions):
    home_captures: HomeCaptures
    expert_routing: ExpertRouting
    victory_condition: VictoryCondition
    golden_fluffles: GoldenFluffleCount
    unlock_computer: UnlockComputer
    unlock_map: UnlockMap
    trap_count: Traps
    death_link: DeathLink
    death_link_behavior: DeathLinkBehavior
    elevator_trap_depth: ElevatorTrapDepth
    elevator_trap_increment: ElevatorTrapIncrement


options_presets = {
        "Standard Difficulty": {
            "home_captures": False,
            "expert_routing": False,
            "victory_condition": "credits",
            "golden_fluffles": 1,
            "unlock_computer": False,
            "unlock_map": False,
            "trap_count": False,
            "death_link": False,
            "death_link_behavior": "rng",
            "elevator_trap_depth": 10,
            "elevator_trap_increment": 0
        },
        "Advanced Difficulty": {
            "home_captures": False,
            "expert_routing": False,
            "victory_condition": "golden_bunny",
            "golden_fluffles": 1,
            "unlock_computer": False,
            "unlock_map": False,
            "trap_count": False,
            "death_link": False,
            "death_link_behavior": "rng",
            "elevator_trap_depth": 10,
            "elevator_trap_increment": 0,
        },
        "Expert Difficulty": {
            "home_captures": True,
            "expert_routing": True,
            "victory_condition": "golden_fluffle",
            "golden_fluffles": 6,
            "unlock_computer": False,
            "unlock_map": False,
            "trap_count": False,
            "death_link": False,
            "death_link_behavior": "rng",
            "elevator_trap_depth": 10,
            "elevator_trap_increment": 0,

        },
    }
