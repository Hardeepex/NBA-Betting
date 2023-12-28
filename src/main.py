import os

from src.DataProviders import SbrOddsProvider
from src.Train-Models.XGBoost_Model_UO import acc_results
from src.Train_Models import XGBoost_Model_ML, XGBoost_Model_UO
from src.Utils import tools


def main():
    # Load the trained models
    model_ml = XGBoost_Model_ML.load_model(os.path.join('..', 'Models', 'XGBoost_{}%_ML-3.json'.format(max(acc_results))))
    model_uo = XGBoost_Model_UO.load_model(os.path.join('..', 'Models', 'XGBoost_{}%_UO-20-01.json'.format(max(acc_results))))

    # Get today's games
    odds_provider = SbrOddsProvider.SbrOddsProvider()
    todays_games = odds_provider.get_odds()

    # Generate the AI's predictions
    predictions_ml = model_ml.predict(todays_games)
    predictions_uo = model_uo.predict(todays_games)

    # Use the AI's predictions to place bets
    bets_to_place = determine_bets(predictions_ml, predictions_uo)

    # Place the bets
    place_bets(bets_to_place)

def determine_bets(predictions_ml, predictions_uo):
    # This function should use the AI's predictions to determine which bets to place
    # The implementation of this function will depend on the specific betting strategy you want to use
    pass

def place_bets(bets_to_place):
    # This function should place the bets determined by the determine_bets function
    # The implementation of this function will depend on the specific betting platform you are using
    pass

if __name__ == "__main__":
    main()
