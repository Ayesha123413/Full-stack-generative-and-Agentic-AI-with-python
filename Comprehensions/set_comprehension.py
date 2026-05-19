chai=[
    "masala chai ",
    "iced peach tea",
    "lemon iced tea",
    "green tea",
    "masala chai ",
    "green tea"
]

# unique_chai={tea for tea in chai} # this is a set , which give you unique values automatically  
my_chai={tea for tea in chai if len(tea) > 10} # this is a set , which give you unique values automatically
print(my_chai)



recipes={
    "masala_chai": ["cinamon", "ginger", "cloves"],
    "iced_peach_tea": ["peach", "tea", "ice"],
    "lemon_iced_tea": ["lemon", "tea", "ice"],
    "green_tea": ["green tea leaves", "water"],
    "Elachi_chai": ["cardamom", "milk", "sugar"],
    "chai": ["milk", "sugar", "tea leaves", "cloves"]
}


unique_ingredients={spices for ingredients in recipes.values() for spices in ingredients} # this is a set , which give you unique values automatically
print(unique_ingredients)