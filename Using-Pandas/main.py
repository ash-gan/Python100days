import pandas as pd
#read CSV
squ_data = pd.read_csv("Squirrel_Data.csv")

count_gray_fur_squ = len(squ_data[squ_data["Primary Fur Color"] == "Gray"])
count_red_fur_squ = len(squ_data[squ_data["Primary Fur Color"] == "Cinnamon"])
count_black_fur_squ = len(squ_data[squ_data["Primary Fur Color"] == "Black"])
data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [count_gray_fur_squ, count_red_fur_squ, count_black_fur_squ]
}
new_data = pd.DataFrame(data_dict)
new_data.to_csv("just_colors_and_count.csv")












