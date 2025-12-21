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


class ElevatorTrapOdds(Range):
    """Odds of generating an Elevator trap instead of junk"""
    display_name = "Elevator Trap Odds"
    range_start = 0
    range_end = 99
    default = 0


class SurfaceTrapOdds(Range):
    """Odds of generating a Return to Surface trap instead of junk"""
    display_name = "Surface Trap Odds"
    range_start = 0
    range_end = 99
    default = 0


class DeathLink(Toggle):
    """Should deathlink be enabled?"""
    display_name = "DeathLink"
    default = 1


class DeathLinkBehavior(Choice):
    """Deaths through Death Link will activate a trap.

    - **Surface**: Returns Paquerette to the surface!
    - **Elevator**: Elevator :)"""
    display_name = "Death Link Behavior"
    rich_text_doc = True
    option_surface = 0
    option_elevator = 1
    default = 0


class ElevatorTrapDepth(Range):
    """How long of an Elevator Ride should you have?"""
    display_name = "Elevator Trap Depth"
    range_start = 1
    range_end = 100
    default = 10


class ElevatorTrapIncrement(Range):
    """Every time you ride, the ride gets longer!"""
    display_name = "Elevator Trap Increment"
    range_start = 0
    range_end = 20
    default = 0


@dataclass
class PaqueretteOptions(PerGameCommonOptions):
    home_captures: HomeCaptures
    expert_routing: ExpertRouting
    victory_condition: VictoryCondition
    golden_fluffles: GoldenFluffleCount
    unlock_computer: UnlockComputer
    unlock_map: UnlockMap
    elevator_trap_odds: ElevatorTrapOdds
    surface_trap_odds: SurfaceTrapOdds
    death_link: DeathLink
    death_link_behavior: DeathLinkBehavior
    elevator_trap_depth: ElevatorTrapDepth
    elevator_trap_increment: ElevatorTrapIncrement


options_presets = {
        "Standard": {
            "home_captures": False,
            "expert_routing": False,
            "victory_condition": VictoryCondition.option_credits,
            "golden_fluffles": 1,
            "unlock_computer": False,
            "unlock_map": False,
            "elevator_trap_odds": 0,
            "surface_trap_odds": 0,
            "death_link": True,
            "death_link_behavior": DeathLinkBehavior.option_surface,
            "elevator_trap_depth": 10,
            "elevator_trap_increment": 0
        },
        "Advanced": {
            "home_captures": False,
            "expert_routing": False,
            "victory_condition": VictoryCondition.option_golden_bunny,
            "golden_fluffles": 1,
            "unlock_computer": False,
            "unlock_map": False,
            "elevator_trap_odds": 0,
            "surface_trap_odds": 0,
            "death_link": True,
            "death_link_behavior": DeathLinkBehavior.option_surface,
            "elevator_trap_depth": 10,
            "elevator_trap_increment": 0,
        },
        "Expert": {
            "home_captures": True,
            "expert_routing": True,
            "victory_condition": VictoryCondition.option_golden_fluffle,
            "golden_fluffles": 6,
            "unlock_computer": False,
            "unlock_map": False,
            "elevator_trap_odds": 0,
            "surface_trap_odds": 0,
            "death_link": True,
            "death_link_behavior": DeathLinkBehavior.option_surface,
            "elevator_trap_depth": 10,
            "elevator_trap_increment": 0,

        },
    }
