from dataset import train_data as df
import pandas as pd

df.describe()

# Get the count of NaN values
df_header = list(df.columns.values)
null_count = df.isnull().sum().tolist()
null_count_percentage = round(df.isnull().sum() / df.shape[0] * 100, 2)
null_count = {
    "Coloum Name": df_header,
    "Null Count": null_count,
    "Null Count (%)": null_count_percentage,
}
df_nullcount = pd.DataFrame(null_count)


# Based of the Boxplot we decided to Fill Age for Pclass 1 as 37,
# Pclass 2 as 29 and Pclass 3 as 24
def input_age(table):
    Age = table[0]
    Pclass = table[1]
    if pd.isnull(Age):
        if Pclass == 1:
            return 37
        elif Pclass == 2:
            return 29
        else:
            return 24
    else:
        return Age


df["Age"] = df[["Age", "Pclass"]].apply(input_age, axis=1)

# Droping Cabin Coloum Since 77% is empty
df.drop(["Cabin"], axis=1, inplace=True)

# Filling Embarked NaN with Mod value.
mode_value = df["Embarked"].mode()[0]
df.fillna({"Embarked": mode_value}, inplace=True)
