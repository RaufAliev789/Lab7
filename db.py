db = {
    "flower_shop": "Цветландия",
    "address": "ул. Ромашковая, 2",
    "customers": [
        {
            "id": 1,
            "name": "Смирнов Илья",
            "age": 25,
            "contacts": {
                "email": "www.smirnov@gmail.com",
                "phone": "+7953467913"
            },
            "neighbourhood_id": 1
        },
        {
            "id": 2,
            "name": "Соболев Никита",
            "age": 52,
            "contacts": {
                "email": "www.sobolev@gmail.com",
                "phone": "+7952645915"
            },
            "neighbourhood_id": 2
        },
        {
            "id": 3,
            "name": "Иванов Александр",
            "age": 45,
            "contacts": {
                "email": "www.ivanov@gmail.com",
                "phone": "+7953597515"
            },
            "neighbourhood_id": 1
        },
        {
            "id": 3,
            "name": "Ильин Петр",
            "age": 27,
            "contacts": {
                "email": "www.ilyin@gmail.com",
                "phone": "+7953784512"
            },
            "neighbourhood_id": 2
        }
    ],
    "neighbourhoods": [
        {
            "id": 1,
            "metro": "Ленинский пр.",
            "house": "12",
            "neighbourhood_seller_id": 1,
            "customers_id": [
                1,
                3
            ],
            "flowers_id": [
                1,
                2,
                3
            ]
        },
        {
            "id": 2,
            "metro": "Озерки",
            "house": "87",
            "neighbourhood_seller_id": 2,
            "customers_id": [
                2,
                4
            ],
            "flowers_id": [
                1,
                3
            ]
        }
    ],
    "sellers": [
        {
            "id": 1,
            "name": "Цветова Роза",
            "flowers_id": [
                1,
                2
            ],
            "contacts": {
                "email": "www.cvetova@gmail.com",
                "phone": "+7953598913"
            }
        },
        {
            "id": 2,
            "name": "Лисова Наталья",
            "flowers_id": [
                3
            ],
            "contacts": {
                "email": "www.lisova@gmail.com",
                "phone": "+7953776655"
            }
        },
        {
            "id": 3,
            "name": "Соловьев Дмитрий",
            "flowers_id": [
                1
            ],
            "contacts": {
                "email": "www.soloviev@gmail.com",
                "phone": "+7953165916"
            }
        }
    ],
    "flowers": [
        {
            "id": 1,
            "name": "Розы",
            "sellers_id": [
                1
            ]
        },
        {
            "id": 2,
            "name": "Ромашки",
            "sellers_id": [
                3
            ]
        },
        {
            "id": 3,
            "name": "Декор",
            "sellers_id": [
                1,
                2
            ]
        }
    ]
}
