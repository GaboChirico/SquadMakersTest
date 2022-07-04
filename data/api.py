import requests

def get_joke(url: str) -> dict:
    """
    Get a joke from an API url

    Args:
        url (str): Api url 

    Returns:
        dict: Api response 
    """
    headers = {
        'Accept': 'application/json',
        'User-Agent': 'Get ramdon jokes (https://github.com/GaboChirico/SquadMakerTest.git)'}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data