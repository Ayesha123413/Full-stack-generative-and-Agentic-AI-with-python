

chai_types=["Cardamom","Ginger","Saffron","Mint","Ginger"]

filter_out=list(filter(lambda chai: chai!="Ginger",chai_types))
# filter_out=dict(enumerate(filter(lambda chai: chai!="Ginger",chai_types)),start=1)
print(filter_out)