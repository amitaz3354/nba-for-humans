from typing import Dict, List

from nba_api.stats.endpoints import DraftHistory


class DraftClassExtractor:
    def __init__(self, year: int):
        self.draft_history = DraftHistory(season_year_nullable=year)

    def get_draft_class(self, only_first_round: bool = True) -> List[Dict]:
        all_history = self.draft_history.get_normalized_dict()["DraftHistory"]
        if only_first_round:
            return all_history[0:30]
