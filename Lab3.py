import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import f_oneway


# Step 1: Load the dataset
df = pd.read_csv("WorldEnergy.csv")

print("Dataset shape:")
print(df.shape)

print("\nFirst five rows:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())


# Step 2: Select countries
selected_countries = ["China", "United States", "India", "Germany", "Japan"]

print("\nCheck selected countries:")
for country in selected_countries:
    print(country, country in df["country"].unique())


# Step 3: Filter selected countries and selected years
data = df[
    (df["country"].isin(selected_countries)) &
    (df["year"] >= 2000) &
    (df["year"] <= 2022)
]


# Step 4: Select variables for ANOVA
anova_data = data[["country", "year", "primary_energy_consumption"]].dropna()

print("\nSelected ANOVA data:")
print(anova_data.head())

print("\nSelected data shape:")
print(anova_data.shape)

print("\nNumber of records by country:")
print(anova_data["country"].value_counts())


# Step 5: Descriptive statistics
print("\nDescriptive statistics by country:")
descriptive_stats = anova_data.groupby("country")["primary_energy_consumption"].describe()
print(descriptive_stats)

descriptive_stats.to_csv("Lab3_Descriptive_Statistics.csv")


# Step 6: Separate data into groups
china = anova_data[anova_data["country"] == "China"]["primary_energy_consumption"]
usa = anova_data[anova_data["country"] == "United States"]["primary_energy_consumption"]
india = anova_data[anova_data["country"] == "India"]["primary_energy_consumption"]
germany = anova_data[anova_data["country"] == "Germany"]["primary_energy_consumption"]
japan = anova_data[anova_data["country"] == "Japan"]["primary_energy_consumption"]


# Step 7: Perform One-way ANOVA
f_statistic, p_value = f_oneway(china, usa, india, germany, japan)

print("\nOne-way ANOVA Result")
print("F-statistic:", f_statistic)
print("p-value:", p_value)


# Step 8: Interpret result
alpha = 0.05

if p_value < alpha:
    decision = "Reject H0"
    conclusion = "There is a statistically significant difference in mean primary energy consumption among the selected countries."
else:
    decision = "Fail to reject H0"
    conclusion = "There is no statistically significant difference in mean primary energy consumption among the selected countries."

print("\nConclusion:")
print(decision)
print(conclusion)


# Step 9: Save ANOVA result
anova_result = pd.DataFrame({
    "Test": ["One-way ANOVA"],
    "Variable": ["primary_energy_consumption"],
    "F-statistic": [f_statistic],
    "p-value": [p_value],
    "Alpha": [alpha],
    "Decision": [decision],
    "Conclusion": [conclusion]
})

anova_result.to_csv("Lab3_ANOVA_Result.csv", index=False)


# Step 10: Create boxplot
plt.figure(figsize=(10, 6))
anova_data.boxplot(column="primary_energy_consumption", by="country")

plt.title("Primary Energy Consumption by Country (2000-2022)")
plt.suptitle("")
plt.xlabel("Country")
plt.ylabel("Primary Energy Consumption")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("Lab3_ANOVA_Boxplot.png")
plt.show()


# Step 11: Create mean bar chart
mean_values = anova_data.groupby("country")["primary_energy_consumption"].mean()

plt.figure(figsize=(10, 6))
mean_values.plot(kind="bar")

plt.title("Mean Primary Energy Consumption by Country (2000-2022)")
plt.xlabel("Country")
plt.ylabel("Mean Primary Energy Consumption")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("Lab3_ANOVA_Mean_BarChart.png")
plt.show()