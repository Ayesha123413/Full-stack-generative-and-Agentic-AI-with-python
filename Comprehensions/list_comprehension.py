chai_menu=[
    "chai1",
    "masala chai ",
    "iced peach tea",
    "lemon iced tea",
    "green tea"
]

# iced_teas = [tea for tea in chai_menu if "iced" in tea]
iced_teas = [tea for tea in chai_menu if len(tea) > 10]
print(iced_teas)