class ChaiCup:
    size = "Medium"

    def describe(self):
         return f"This is a {self.size} chai cup."


cup = ChaiCup()
print(f"cup1 size: {cup.size}")  # Output: Medium
print(cup.describe())  # Output: Medium
print(ChaiCup.describe(cup))  # Output: Medium


cup2=ChaiCup()
cup2.size="Large"
# print(cup2.describe())  
print(ChaiCup.describe(cup2))  # Output: Large