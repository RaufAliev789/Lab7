import utils.json_service as json_service


def get_one_by_id(id):
    db = json_service.get_database()

    for elem in db["sellers"]:
        if elem["id"] == id:
            return elem

    return {"message": f"Элемент с {id} не найден"}


def get_all():
    db = json_service.get_database()

    return db["sellers"]


def update_one_by_id(id, seller):
    db = json_service.get_database()

    for i, elem in enumerate(db["sellers"]):
        if elem["id"] == id:

            elem["name"] = seller["name"]
            elem["contacts"] = seller["contacts"]

            json_service.set_database(db)
            return elem

    return {"message": f"Элемент с {id} не найден"}


def delete_one_by_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["sellers"]):
        if elem["id"] == id:

            candidate = db["sellers"].pop(i)
            json_service.set_database(db)

            return candidate

    return {"message": f"Элемент с {id} не найден"}


def create_one(seller):
    db = json_service.get_database()

    last_seller_id = get_all()[-1]["id"]
    db["sellers"].append({"id": last_seller_id + 1, **seller})

    json_service.set_database(db)

