# Import data
cvs_url = 'https://replit.com/@NikolayPodkopae/boilerplate-medical-data-visualizer#medical_examination.csv'
df = pd.read_csv(cvs_url)

# Add 'overweight' column
df['overweight'] = 0
df['overweight'] = df.loc[(((df['weight']) / ((df['height'] / 100) ** 2)) > 25.0), 'overweight'] = 1

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df["cholesterol"] = np.where(df["cholesterol"] == 1, 0, 1)  # делаем cholesterol и gluc со значениями только 0 и 1 (разными способами)
df["gluc1"] = 0
df["gluc1"] = df["gluc1"].where(df["gluc"] <= 1, 1)
df["gluc"] = df["gluc1"]  # удаляем gluc1
del df['gluc1']