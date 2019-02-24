import pandas as pd
from data_infos import Information


class Clean():

    def __init_(self, data):
        self.data = None

    def clean(self):
        # StateHoliday is a string and not so important to know what kind of holiday (a, b or c).
        data["StateHoliday"] = self.data["StateHoliday"].map(
            {0: 0, "0": 0, "a": 1, "b": 1, "c": 1})

        # Outliers:
        # lets delete the times, where the stores were opened with no sales because of days in inventory.
        self.data.drop(self.data[(self.data.Open == 0) & (self.data.Sales == 0)].index)
        self.data.reset_index(drop=True)  # to ge the indexes back to 0, 1, 2,etc.

        # Store Data
        # Since we have here some outlier, its better to input the median value to those few missing values.
        self.data["CompetitionDistance"].fillna(
            self.data["CompetitionDistance"].median(), inplace=True)

        # The missing values, are not there, because the stores had no competition.
        # So I would suggest to fill the missing values with zeros.
        self.data["CompetitionOpenSinceMonth"].fillna(0, inplace=True)
        self.data["CompetitionOpenSinceYear"].fillna(0, inplace=True)

        # so if no promo has been made, then we should replace the NaN from Promo since Week and Year with zero
        self.data["Promo2SinceWeek"].fillna(0, inplace=True)
        self.data["Promo2SinceYear"].fillna(0, inplace=True)
        self.data["PromoInterval"].fillna(0, inplace=True)

        ############ Create a new Variable #####################
        self.data["Avg_Customer_Sales"] = self.data["Sales"] / self.data["Customers"]
        self.data["Month"] = self.data.Date.dt.month
        self.data["Year"] = self.data.Date.dt.year
        self.data["Day"] = self.data.Date.dt.day

        # The competitions are continous numbers, so we need to convert them into a categories. Lets a create a new variable.
        self.data["CompetitionDistance_Cat"] = pd.cut(self.data["CompetitionDistance"], 5)

        # self.data["Promo"] = self.data["Promo"].astype("category") # it's already numerica
        # self.data["SchoolHoliday"] = self.data["SchoolHoliday"].astype("category") # it's already numerica
        self.data["StoreType"] = self.data["StoreType"].astype("category")
        self.data["Assortment"] = self.data["Assortment"].astype("category")
        # self.data["Promo2"] = self.data["Promo2"].astype("category") # it's already numerica
        self.data["PromoInterval"] = self.data["PromoInterval"].astype("category")

        self.data["StoreType_cat"] = self.data["StoreType"].cat.codes
        self.data["Assortment_cat"] = self.data["Assortment"].cat.codes
        self.data["PromoInterval_cat"] = self.data["Assortment"].cat.codes

        self.data["StateHoliday_cat"] = self.data["StateHoliday_cat"].astype("float")
        self.data["StoreType_cat"] = self.data["StoreType_cat"].astype("float")
        self.data["Assortment_cat"] = self.data["Assortment_cat"].astype("float")
        self.data["PromoInterval_cat"] = self.data["PromoInterval_cat"].astype("float")

    def save(self):
        pass

# MERGING the both tables:
# self.data = pd.merge(train_df, store_df, how = "left", on = "Store")


df = pd.read_csv("../../Data/store.csv")

data = Information()
data.info(df)
