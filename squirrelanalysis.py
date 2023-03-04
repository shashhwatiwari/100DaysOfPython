import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data.to_dict())
# dict having count in order of gray,cinnamon and black

gray_sq_count = len(data[data["Primary Fur Color"] == "Gray"])  # treats this as a list. hence we can use the len
# function too

cin_sq_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

red_sq_count = len(data[data["Primary Fur Color"] == "Black"])

# converting dictionary into dataframe
colour = {
    "color": ["Gray", "Red", "Black"],
    "count": [gray_sq_count, cin_sq_count, red_sq_count]
          }
colour_df = pandas.DataFrame(colour)
colour_df.to_csv("colourcount.csv")

