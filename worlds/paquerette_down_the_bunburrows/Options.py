from Options import Toggle, PerGameCommonOptions
from dataclasses import dataclass


class ExpertDifficultyMode(Toggle):
    """For players familiar with Paquerette, only home-captures are sufficient to act as locations."""
    display_name = "Expert Difficulty"


@dataclass
class PaqueretteOptions(PerGameCommonOptions):
    expert_difficulty: ExpertDifficultyMode


options_presets = {
        "Standard Difficulty": {
            "expert_difficulty": False,
            },
        "Expert Difficulty": {
            "expert_difficulty": True,
            }
        }
