import pytest
from lib.src.career_stats.career_stats_extractor import CareerStatsExtractor, StatsMode, SeasonalDataNotFoundException

EXPECTED_STATS_DATA = {
    StatsMode.REGULAR: {
        "2020-21": {'PLAYER_ID': 2544, 'SEASON_ID': '2020-21', 'LEAGUE_ID': '00', 'TEAM_ID': 1610612747,
                    'TEAM_ABBREVIATION': 'LAL', 'PLAYER_AGE': 36.0, 'GP': 45, 'GS': 45, 'MIN': 33.4, 'FGM': 9.4,
                    'FGA': 18.3, 'FG_PCT': 0.513, 'FG3M': 2.3, 'FG3A': 6.3, 'FG3_PCT': 0.365, 'FTM': 4.0, 'FTA': 5.7,
                    'FT_PCT': 0.698, 'OREB': 0.6, 'DREB': 7.0, 'REB': 7.7, 'AST': 7.8, 'STL': 1.1, 'BLK': 0.6,
                    'TOV': 3.7, 'PF': 1.6, 'PTS': 25.0},
    },
    StatsMode.PER_36: {
        "2020-21": {'PLAYER_ID': 2544, 'SEASON_ID': '2020-21', 'LEAGUE_ID': '00', 'TEAM_ID': 1610612747,
                    'TEAM_ABBREVIATION': 'LAL', 'PLAYER_AGE': 36.0, 'GP': 45, 'GS': 45, 'MIN': 1504.0, 'FGM': 10.1,
                    'FGA': 19.7, 'FG_PCT': 0.513, 'FG3M': 2.5, 'FG3A': 6.8, 'FG3_PCT': 0.365, 'FTM': 4.3, 'FTA': 6.1,
                    'FT_PCT': 0.698, 'OREB': 0.7, 'DREB': 7.6, 'REB': 8.3, 'AST': 8.4, 'STL': 1.1, 'BLK': 0.6,
                    'TOV': 4.0, 'PF': 1.7, 'PTS': 27.0}

    }
}


# test collecting seasonal data - valid seasons / different mode
@pytest.mark.parametrize("stats_mode", [StatsMode.REGULAR, StatsMode.PER_36])
def test_collecting_seasonal_data(stats_mode):
    player_id = 2544
    expected_stats_data = EXPECTED_STATS_DATA[stats_mode]
    stats_extractor = CareerStatsExtractor(player_id, stats_mode)
    print(stats_extractor.career_stats.parameters)

    for season, expected_stats in expected_stats_data.items():
        seasonal_stats = stats_extractor.collect_seasonal_stats(season)
        print(seasonal_stats)
        assert seasonal_stats == expected_stats

# test collecting seasonal data - invalid season


def test_collecting_seasonal_data_with_invalid_year():
    player_id = 2544
    stats_extractor = CareerStatsExtractor(player_id, StatsMode.PER_36)

    with pytest.raises(SeasonalDataNotFoundException):
        stats_extractor.collect_seasonal_stats(season="2030-31")



def test_comparing_stat_modes():
    player_id = 2544

    # Regular (Per Game Stats)
    stats_extractor = CareerStatsExtractor(player_id, StatsMode.REGULAR)
    per_game_stats = stats_extractor.collect_seasonal_stats(season="2020-21")

    # per 36 stats
    stats_extractor = CareerStatsExtractor(player_id, StatsMode.PER_36)
    per_36_stats = stats_extractor.collect_seasonal_stats(season="2020-21")

    assert per_game_stats != per_36_stats







# test collecting seasonal data - compare between per36/per game
