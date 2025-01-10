import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('healthcare_dataset.csv')

conn = sqlite3.connect('health_dataa.db')


data.to_sql('health_statistics', conn, if_exists='replace', index=False)


query = "SELECT * FROM health_statistics LIMIT 5;"
print(pd.read_sql_query(query, conn))


query = """
SELECT 
    "Blood Type", 
    "Medical Condition", 
    COUNT(*) AS frequency
FROM health_statistics
GROUP BY "Blood Type", "Medical Condition"
ORDER BY frequency DESC;
"""
blood_condition_frequency = pd.read_sql_query(query, conn)
print(blood_condition_frequency)


plt.figure(figsize=(12, 6))
sns.barplot(data=blood_condition_frequency, x="Blood Type", y="frequency", hue="Medical Condition")
plt.title("Frequency of Medical Conditions by Blood Type")
plt.ylabel("Frequency")
plt.ylim(0, 1300)  # Limitar o eixo Y até 1300
plt.xticks(rotation=45)
plt.legend(title="Medical Condition", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


conn.close()

