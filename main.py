import components.sellers.service as seller
import components.sellers.service as customer


# print(seller.create_one({
#       "name": "Продавец",
#       "flowers_id": [
#           1,
#           2
#       ],
#       "contacts": {
#           "email": "www.A@gmail.com",
#           "phone": "+795878787"
#       }}))
#
# print(seller.get_all())
#
# print(seller.get_one_by_id(1))
#
# print(seller.update_one_by_id(4, {
#       "name": "Цветова Роза",
#       "contacts": {
#           "email": "www.cvetova@gmail.com",
#           "phone": "+7953598913"
#       }}))
# print(seller.delete_one_by_id(id))


while True:
    print("Меню:")
    print("1. Создать продавца")
    print("11. Создать покупателя")
    print("2. Получить список всех продавцов")
    print("22. Получить список всех покупателей")
    print("3. Получить информацию о продавце по ID")
    print("33. Получить информацию о покупателе по ID")
    print("4. Обновить информацию о продавце по ID")
    print("44. Обновить информацию о покупателе по ID")
    print("5. Удалить продавца по ID")
    print("55. Удалить покупателя по ID")

    choice = input("Выберите пункт меню (1-55): ")

    if choice == "1":
        name = input("Введите имя продавца: ")
        flowers_id = input("Введите ID отдела цветов (через запятую): ")
        contacts_email = input("Введите email продавца: ")
        contacts_phone = input("Введите телефон продавца: ")

        flowers_id = [int(id.strip()) for id in flowers_id.split(",")] #даление лишних пробелы в начале и конце строки

        result = seller.create_one({
            "name": name,
            "flowers_id": flowers_id,
            "contacts": {
                "email": contacts_email,
                "phone": contacts_phone
            }
        })

        print(result)
    elif choice == "11":
        name = input("Введите имя покупателя: ")
        metro = input("Введите станцию метро покупателя: ")
        contacts_email = input("Введите email покупателя : ")
        contacts_phone = input("Введите телефон покупателя: ")

        metro = [str(id.strip()) for id in metro.split(",")] #даление лишних пробелы в начале и конце строки

        result = customer.create_one({
            "name": name,
            "metro": metro,
            "contacts": {
                "email": contacts_email,
                "phone": contacts_phone
            }
        })

        print(result)

    elif choice == "2":
        result = seller.get_all()
        print(result)
    elif choice == "22":
        result = customer.get_all()
        print(result)

    elif choice == "3":
        seller_id = input("Введите ID продавца: ")
        result = seller.get_one_by_id(int(seller_id))
        print(result)
    elif choice == "33":
        customer_id = input("Введите ID покупателя: ")
        result = customer.get_one_by_id(int(customer_id))
        print(result)

    elif choice == "4":
        seller_id = input("Введите ID продавца: ")
        name = input("Введите новое имя продавца: ")
        contacts_email = input("Введите новый email продавца: ")
        contacts_phone = input("Введите новый телефон продавца: ")

        result = seller.update_one_by_id(int(seller_id), {
            "name": name,
            "contacts": {
                "email": contacts_email,
                "phone": contacts_phone
            }
        })

        print(result)
    elif choice == "44":
        customer_id = input("Введите ID покупателя: ")
        name = input("Введите новое имя покупателя: ")
        contacts_email = input("Введите новый email покупателя: ")
        contacts_phone = input("Введите новый телефон покупателя: ")

        result = customer.update_one_by_id(int(customer_id), {
            "name": name,
            "contacts": {
                "email": contacts_email,
                "phone": contacts_phone
            }
        })

        print(result)

    elif choice == "5":
        seller_id = input("Введите ID продавца: ")
        result = seller.delete_one_by_id(int(seller_id))
        print(result)
    elif choice == "55":
        customer_id = input("Введите ID покупателя: ")
        result = customer.delete_one_by_id(int(customer_id))
        print(result)


        break

    else:
        print("Неверный выбор. Попробуйте снова.")