import pandas as pd

class Information():

    def __init__(self):
        print("Let's see how the date looks after ETL")

    def _get_missing_values(self, data):
        missing_values = data.isnull().sum()
        missing_values.sort_values(ascending = False, inplace = True)
        return missing_values

    def info(self, data):
        feature_dtypes = data.dtypes
        self.missing_values = self._get_missing_values(data)
        print("=" * 50)

        print("{:16} {:16} {:25} {:16}".format("Feature Name".upper(),
                                            "Data Format".upper(),
                                            "# of Missing Values".upper(),
                                            "Samples".upper()))
        for feature_name, dtype, missing_value in zip(self.missing_values.index.values,
                                                      feature_dtypes[self.missing_values.index.values],
                                                      self.missing_values.values):
            print("{:18} {:19} {:19} ".format(feature_name, str(dtype), str(missing_value)), end="")
            for v in data[feature_name].values[:3]:
                print(v, end=",")
            print()

        print("="*20, data.shape, "="*20)



# df = pd.read_csv("../../Data/raw/apartments.csv")
#
# data = Information()
# data.info(df)
