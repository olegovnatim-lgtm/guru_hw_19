from config import BASE_URL
from utils import api
from utils.validator import validate


def test_get_clubs():
    response = api.get(f"{BASE_URL}/clubs/")

    assert response.status_code == 200
    validate(response.json(), "schema_get_clubs_list")


def test_get_clubs_with_page_size():
    page_size = 5
    response = api.get(f"{BASE_URL}/clubs/", params={"page_size": page_size})

    assert response.status_code == 200
    assert len(response.json()["results"]) == page_size
    validate(response.json(), "schema_get_clubs_list")


def test_get_clubs_from_search_book_title():
    book_title = "vile"
    response = api.get(f"{BASE_URL}/clubs/", params={"search": book_title})
    data = response.json()

    assert response.status_code == 200
    validate(data, "schema_get_clubs_list")
    for club in data["results"]:
        assert book_title in club["bookTitle"].lower()


def test_get_club_with_id():
    club = api.get(f"{BASE_URL}/clubs/").json()["results"][1]
    response = api.get(f"{BASE_URL}/clubs/{club['id']}")

    assert response.status_code == 200
    assert club == response.json()
