from db_manage.db_update import add_scenario

scenario={
        "scenario": [
            {
                "who": "muba",
                "intent": "인사"
            },
            {
                "who": "user",
                "intent": "음식이름"
            },
            {
                "who": "muba",
                "intent": "특정 음식 음식점 보여주기"
            },
            {
                "who": "user",
                "intent": "음식점이름"
            },
            {
                "who": "muba",
                "intent": "음식점 메뉴 보여주기"
            },
            {
                "who": "user",
                "intent": "메뉴주문"
            },
            {
                "who": "muba",
                "intent": "주문 보여주기"
            }
        ],
}

print(add_scenario(scenario))
