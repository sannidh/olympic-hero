# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Path of the file
#Code starts here
data = pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'}, inplace=True)
data.head(10)


# --------------
#Code starts here
data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'],'Summer', 
                                np.where(data['Total_Summer']==data['Total_Winter'],'Both','Winter'))
better_event = data['Better_Event'].value_counts().idxmax()


# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries.drop(top_countries.tail(1).index, inplace=True)
def top_ten(df, col_name):
    top_10 = df.nlargest(10, col_name)
    country_list = list(top_10['Country_Name'])
    return country_list
top_10_summer = top_ten(top_countries, 'Total_Summer')
top_10_winter = top_ten(top_countries, 'Total_Winter')
top_10 = top_ten(top_countries, 'Total_Medals')
common = [x for x in top_10_summer if x in top_10_winter and x in top_10]


# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]
summer_df.plot(kind='bar', x='Country_Name', y='Total_Summer', figsize=(15,10))
plt.ylabel('Total Summer Medals')
winter_df.plot(kind='bar', x='Country_Name', y='Total_Winter', figsize=(15,10))
plt.ylabel('Total Winter Medals')
top_df.plot(kind='bar', x='Country_Name', y='Total_Medals', figsize=(15,10))
plt.ylabel('Total Medals')


# --------------
#Code starts here
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = summer_df['Country_Name'][summer_df['Golden_Ratio']==summer_max_ratio].item()
winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = winter_df['Country_Name'][winter_df['Golden_Ratio']==winter_max_ratio].item()
top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df['Country_Name'][top_df['Golden_Ratio']==top_max_ratio].item()


# --------------
#Code starts here
data_1 = data.drop(data.tail(1).index)
data_1['Total_Points'] = 3 * data_1['Gold_Total'] + 2 * data_1['Silver_Total'] + 1 * data_1['Bronze_Total']
most_points = data_1['Total_Points'].max()
best_country = data_1['Country_Name'][data_1['Total_Points']==most_points].item()


# --------------
#Code starts here
best = data[data['Country_Name']==best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


