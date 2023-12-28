import unittest
from unittest.mock import patch

from Flask import app
from src import main


class TestIntegration(unittest.TestCase):
    @patch('src.main.determine_bets')
    def test_determine_bets(self, mock_determine_bets):
        mock_predictions = {'team1': 0.9, 'team2': 0.1}
        main.determine_bets(mock_predictions)
        mock_determine_bets.assert_called_once_with(mock_predictions)

    @patch('src.main.place_bets')
    def test_place_bets(self, mock_place_bets):
        mock_bets = ['bet1', 'bet2']
        main.place_bets(mock_bets)
        mock_place_bets.assert_called_once_with(mock_bets)

    @patch('Flask.app.get_ai_predictions')
    def test_get_ai_predictions(self, mock_get_ai_predictions):
        mock_predictions = {'team1': 0.9, 'team2': 0.1}
        app.get_ai_predictions()
        mock_get_ai_predictions.assert_called_once()

    @patch('Flask.app.index')
    def test_index(self, mock_index):
        mock_data = {'fanduel': {}, 'draftkings': {}, 'betmgm': {}, 'ai_predictions': {'team1': 0.9, 'team2': 0.1}}
        app.index()
        mock_index.assert_called_once()

if __name__ == '__main__':
    unittest.main()
