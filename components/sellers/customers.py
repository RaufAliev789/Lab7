import utils.json_service as json_service


def get_one_by_id(id):
    db = json_service.get_database()

    for elem in db["customers"]:
        if elem["id"] == id:
            return elem

    return {"message": f"Элемент с {id} не найден"}


def get_all():
    db = json_service.get_database()

    return db["customers"]


def update_one_by_id(id, customer):
    db = json_service.get_database()

    for i, elem in enumerate(db["customers"]):
        if elem["id"] == id:

            elem["name"] = customer["name"]
            elem["contacts"] = customer["contacts"]

            json_service.set_database(db)
            return elem

    return {"message": f"Элемент с {id} не найден"}


def delete_one_by_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["customers"]):
        if elem["id"] == id:

            candidate = db["customers"].pop(i)
            json_service.set_database(db)

            return candidate

    return {"message": f"Элемент с {id} не найден"}


def create_one(customer):
    db = json_service.get_database()

    last_customer_id = get_all()[-1]["id"]
    db["sellers"].append({"id": last_customer_id + 1, **customer})

    json_service.set_database(db)
