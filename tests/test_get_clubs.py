from utils import api
from utils.validator import validate


def test_get_clubs(base_url):
    response = api.get(f"{base_url}/clubs/")

    assert response.status_code == 200
    validate(response.json(), "schema_get_clubs_list")


def test_get_clubs_with_page_size(base_url):
    page_size = 5
    response = api.get(f"{base_url}/clubs/", params={"page_size": page_size})

    assert response.status_code == 200
    assert len(response.json()["results"]) == page_size
    validate(response.json(), "schema_get_clubs_list")


def test_get_clubs_from_search_book_title(base_url):
    book_title = "vile"
    response = api.get(f"{base_url}/clubs/", params={"search": book_title})
    data = response.json()

    assert response.status_code == 200
    validate(data, "schema_get_clubs_list")
    for club in data["results"]:
        assert book_title in club["bookTitle"].lower()


def test_get_club_with_id(base_url):
    club = api.get(f"{base_url}/clubs/").json()["results"][1]
    response = api.get(f"{base_url}/clubs/{club['id']}")

    assert response.status_code == 200
    validate(response.json(), "schema_get_club") #эта проверка скорее излишне, но не стала удалять
    assert club == response.json()