from typing import Dict

from nba_api.stats.endpoints.playercareerstats import PlayerCareerStats
from nba_api.stats.library.parameters import PerModeSimple, PerMode36

from lib.src.career_stats.exceptions import SeasonalDataNotFoundException
from lib.src.career_stats.types import StatsMode


class CareerStatsExtractor:
    def __init__(self, player_id: int, stats_mode: StatsMode):
        self.player_id = player_id
        self.stats_mode = stats_mode
        self.career_stats = None
        match stats_mode:
            case StatsMode.REGULAR:
                self.career_stats = PlayerCareerStats(player_id=player_id, per_mode36=PerModeSimple.per_game)
            case StatsMode.PER_36:
                self.career_stats = PlayerCareerStats(player_id=player_id, per_mode36=PerMode36.per_36)

    def collect_seasonal_stats(self, season: str) -> Dict:
        all_data = self.career_stats.get_normalized_dict()["SeasonTotalsRegularSeason"]
        for seasonal_data in all_data:
            if seasonal_data['SEASON_ID'] == season:
                return seasonal_data

        raise SeasonalDataNotFoundException("no season found for the player")
