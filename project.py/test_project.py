import pytest
from project import search_summoner_by_name, get_puuid, get_match_info, get_match_id, get_placement


def test_search_summoner_by_name(mocker):
    mock_api_data = {
        "puuid": "VbFO4NoDy7lqLrftt50XztcxKzfvo_Pehgmnt72UIiSq_NfrSpUVhfoJ8FOsfMzqvB6yh-E6Y3rnPA",
        "gameName": "4nit5ug4",
        "tagLine": "EUW"
        }
    mock_api_response = mocker.MagicMock()
    mock_api_response.json.return_value = mock_api_data
    mocker.patch("requests.get", return_value=mock_api_response)

    test_api_mock = search_summoner_by_name("europe", "4nit5ug4", "euw", "API_KEY")

    assert test_api_mock == mock_api_data
    assert type(test_api_mock) is dict
    assert test_api_mock["tagLine"] == "EUW"
    assert test_api_mock["tagLine"] != "NA"
    assert test_api_mock["gameName"] != "Name"

def test_search_summoner_sysexit():
    with pytest.raises(SystemExit):
        search_summoner_by_name("americas", "Name", "NA", "API_KEY")

def test_get_puuid():
    mock_summoner_data = {
        "puuid": "VbFO4NoDy7lqLrftt50XztcxKzfvo_Pehgmnt72UIiSq_NfrSpUVhfoJ8FOsfMzqvB6yh-E6Y3rnPA",
        "gameName": "4nit5ug4",
        "tagLine": "EUW"
        }
    
    mock_wrong_summoner_data = {
        "Weather": "Sunny",
        "Temperature": "30º",
        "City": "Vigo"
        }
    
    assert get_puuid(mock_summoner_data) == "VbFO4NoDy7lqLrftt50XztcxKzfvo_Pehgmnt72UIiSq_NfrSpUVhfoJ8FOsfMzqvB6yh-E6Y3rnPA"
    assert get_puuid(mock_wrong_summoner_data) == None

def test_get_match_id(mocker):
    mock_match_id = ["EUW1_6989764596"]
    mock_api_response = mocker.MagicMock()
    mock_api_response.json.return_value = mock_match_id
    mocker.patch("requests.get", return_value=mock_api_response)

    test_match_id_mock = get_match_id("europe", "VbFO4NoDy7lqLrftt50XztcxKzfvo_Pehgmnt72UIiSq_NfrSpUVhfoJ8FOsfMzqvB6yh-E6Y3rnPA", "API_KEY", "1")

    assert test_match_id_mock == mock_match_id
    assert isinstance(test_match_id_mock, list)
    assert test_match_id_mock[0] == "EUW1_6989764596"
    assert test_match_id_mock != "Kingston"

def test_match_id_sysexit():
    with pytest.raises(SystemExit):
        get_match_id("kingston", "abcde123", "API_KEY", "cat")

def test_get_match_info(mocker):
    mock_api_data = {
        'metadata': {
            'data_version': '5',
            'match_id': 'EUW1_6989764596',
            'participants': [
                '2uZFQ5dnPHFq_oIXzyB22H6XOAvdHZy9O1mYjY6YQKALvp8Fui3FyRvpogVPnS4xLHlMGV1wNLBXzQ',
                'SruiQIJAboAhW_J_QMeQ5MvJ0DNMuo0L3lWE89Lbf-Jxmd668KA2b5rGWQD6WcPKtZBGnuJ0mV36xw',
                'MuusgrIVRuqAuhTA3FPDijick4SxFDzkAVUoUUftBphGOW2J7H6WFMCmnr5_4lKwTKqwKoiZl1mrjg',
                'b_4hITq9IGhAXS0fnLoAbTPgwlnMBNYI8xi53UfValv4A-8H3IQkry99Q0m3xPomyxqKDbr8aPd9_w',
                'VbFO4NoDy7lqLrftt50XztcxKzfvo_Pehgmnt72UIiSq_NfrSpUVhfoJ8FOsfMzqvB6yh-E6Y3rnPA',
                'W_8Y8VwDnAgCcmq8RgzJJt7pDWx1k_-BGA7aWV1ojhgKIzUZz4AcsPgNBCz6O19IjvJ2v4vkJn0TSQ',
                'jikIV6MFE6ARo0lXF8ySS17x_TTR06X0762BSXU_C7yY2OzZxH4p3R2HWqCemAOfgnbzgLAzDhSW3A',
                'lS6vP8YUjmBN9CP--hw4u6E-FL7qyhW_n7GlwofbHZ2ehWwACshGCV_8Dt0rwqtKbF_QFXLl0FiOww'
            ]
        },
        'info': {
            'endOfGameResult': 'GameComplete',
            'gameCreation': 1719745813000,
            'gameId': 6989764596,
            'game_datetime': 1719748269517,
            'game_length': 2371.92578125,
            'game_version': 'Linux Version 14.13.596.7996 (Jun 21 2024/16:23:19) [PUBLIC] <Releases/14.13>',
            'mapId': 22,
            'participants': [
                {
                    'augments': [
                        'TFT9_Augment_GargantuanResolve',
                        'TFT9_Augment_JeweledLotus',
                        'TFT11_Augment_DynamicDuo'
                    ],
                    'companion': {
                        'content_ID': '24b65469-d9a1-40ad-8ffa-629a3bf3fc95',
                        'item_ID': 27005,
                        'skin_ID': 5,
                        'species': 'PetChoncc'
                    },
                    'gold_left': 0,
                    'last_round': 33,
                    'level': 8,
                    'missions': {
                        'PlayerScore2': 102
                    },
                    'placement': 5,
                    'players_eliminated': 0,
                    'puuid': '2uZFQ5dnPHFq_oIXzyB22H6XOAvdHZy9O1mYjY6YQKALvp8Fui3FyRvpogVPnS4xLHlMGV1wNLBXzQ',
                    'time_eliminated': 2033.9293212890625,
                    'total_damage_to_players': 94
                }
                    ]
            }
        }

    mock_api_response = mocker.MagicMock()
    mock_api_response.json.return_value = mock_api_data
    mocker.patch("requests.get", return_value=mock_api_response)

    test_mock_match_info = get_match_info("europe", "match", "API_KEY")

    assert test_mock_match_info == mock_api_data
    assert type(test_mock_match_info) is dict
    assert test_mock_match_info.get("info", {}).get("endOfGameResult") == "GameComplete"
    assert test_mock_match_info.get("info", {}).get("participants", [{}])[0].get("gold_left") == 0
    assert test_mock_match_info.get("info", {}).get("participants", [{}])[0].get("gold_left") != 10

def match_info_sysexit():
    with pytest.raises(SystemExit):
        get_match_info("Kingston", "1234", "000356")

def test_get_placement():
    mock_match_info = {
        'metadata': {
            'data_version': '5',
            'match_id': 'EUW1_6989764596',
            'participants': [
                '2uZFQ5dnPHFq_oIXzyB22H6XOAvdHZy9O1mYjY6YQKALvp8Fui3FyRvpogVPnS4xLHlMGV1wNLBXzQ',
                'SruiQIJAboAhW_J_QMeQ5MvJ0DNMuo0L3lWE89Lbf-Jxmd668KA2b5rGWQD6WcPKtZBGnuJ0mV36xw',
                'MuusgrIVRuqAuhTA3FPDijick4SxFDzkAVUoUUftBphGOW2J7H6WFMCmnr5_4lKwTKqwKoiZl1mrjg',
                'b_4hITq9IGhAXS0fnLoAbTPgwlnMBNYI8xi53UfValv4A-8H3IQkry99Q0m3xPomyxqKDbr8aPd9_w',
                'VbFO4NoDy7lqLrftt50XztcxKzfvo_Pehgmnt72UIiSq_NfrSpUVhfoJ8FOsfMzqvB6yh-E6Y3rnPA',
                'W_8Y8VwDnAgCcmq8RgzJJt7pDWx1k_-BGA7aWV1ojhgKIzUZz4AcsPgNBCz6O19IjvJ2v4vkJn0TSQ',
                'jikIV6MFE6ARo0lXF8ySS17x_TTR06X0762BSXU_C7yY2OzZxH4p3R2HWqCemAOfgnbzgLAzDhSW3A',
                'lS6vP8YUjmBN9CP--hw4u6E-FL7qyhW_n7GlwofbHZ2ehWwACshGCV_8Dt0rwqtKbF_QFXLl0FiOww'
            ]
        },
        'info': {
            'endOfGameResult': 'GameComplete',
            'gameCreation': 1719745813000,
            'gameId': 6989764596,
            'game_datetime': 1719748269517,
            'game_length': 2371.92578125,
            'game_version': 'Linux Version 14.13.596.7996 (Jun 21 2024/16:23:19) [PUBLIC] <Releases/14.13>',
            'mapId': 22,
            'participants': [
                {
                    'augments': [
                        'TFT9_Augment_GargantuanResolve',
                        'TFT9_Augment_JeweledLotus',
                        'TFT11_Augment_DynamicDuo'
                    ],
                    'companion': {
                        'content_ID': '24b65469-d9a1-40ad-8ffa-629a3bf3fc95',
                        'item_ID': 27005,
                        'skin_ID': 5,
                        'species': 'PetChoncc'
                    },
                    'gold_left': 0,
                    'last_round': 33,
                    'level': 8,
                    'missions': {
                        'PlayerScore2': 102
                    },
                    'placement': 5,
                    'players_eliminated': 0,
                    'puuid': '2uZFQ5dnPHFq_oIXzyB22H6XOAvdHZy9O1mYjY6YQKALvp8Fui3FyRvpogVPnS4xLHlMGV1wNLBXzQ',
                    'time_eliminated': 2033.9293212890625,
                    'total_damage_to_players': 94
                }
                    ]
            }
        }

    mock_puuid = "2uZFQ5dnPHFq_oIXzyB22H6XOAvdHZy9O1mYjY6YQKALvp8Fui3FyRvpogVPnS4xLHlMGV1wNLBXzQ"

    assert get_placement(mock_match_info, mock_puuid) == 5
    assert get_placement(mock_match_info, "123456") == None
