import seaborn as sns
import matplotlib.pyplot as plt
from dataset import train_data as df

# Survived
plt.figure(figsize=(8, 5))
sns.countplot(x="Survived", hue="Survived", data=df)
plt.title("Survival Count")
plt.savefig("../reports/figures/survived_count.png", dpi=300, bbox_inches="tight")
plt.close()

# Survived male or female
plt.figure(figsize=(8, 5))
sns.countplot(x="Survived", hue="Sex", data=df)
plt.title("Survival Sex Count")
plt.savefig("../reports/figures/survived_Sex_count.png", dpi=300, bbox_inches="tight")
plt.close()

# Survived per class
plt.figure(figsize=(8, 5))
sns.countplot(x="Survived", hue="Pclass", data=df)
plt.title("Survival Pclass Count")
plt.savefig("../reports/figures/survived_pclass.png", dpi=300, bbox_inches="tight")
plt.close()

# Sibling
plt.figure(figsize=(8, 5))
sns.countplot(x="SibSp", hue="SibSp", data=df)
plt.title("Sibling Count")
plt.savefig("../reports/figures/sibling_count.png", dpi=300, bbox_inches="tight")
plt.close()

# Boxplot to fill in NaN in Age
plt.figure(figsize=(8, 5))
sns.boxplot(x="Pclass", y="Age", hue="Pclass", data=df)
plt.title("Sibling Count")
plt.savefig("../reports/figures/sibling_count.png", dpi=300, bbox_inches="tight")
plt.close()

# Boxplot Values for Age
box_plot_values = df.groupby("Pclass")["Age"].describe()[
    ["min", "25%", "50%", "75%", "max"]
]
box_plot_values.columns = ["Min", "Q1 (25%)", "Median (50%)", "Q3 (75%)", "Max"]
