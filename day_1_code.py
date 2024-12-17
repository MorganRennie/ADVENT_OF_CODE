import pandas as pd

location_ids = pd.read_csv ('INPUT.txt',
                            sep=' ', 
                            names=["team_1", "_", "__", "team_2"])

##

columns_to_drop = ['_', '__']
location_ids = location_ids.drop(columns = columns_to_drop)

##

team_1_data = location_ids['team_1']
t1 = team_1_data.sort_values(ascending=True)
t1 = t1.to_frame()

t1['row_number'] = range(1, len(t1) + 1)
t1 = t1.set_index('row_number')

##

team_2_data = location_ids['team_2']
t2 = team_2_data.sort_values(ascending=True)
t2 = t2.to_frame()

t2['row_number'] = range(1, len(t1) + 1)
t2 = t2.set_index('row_number')

##

t3 = t1.join(t2)

t3['difference'] = abs(t3['team_1'] - t3['team_2'])

##

total_difference = t3['difference'].sum()

total_difference

##Output: 2742123
##

t2_list = t3['team_2'].tolist()

t3['count'] = t3['team_1'].apply(lambda x: t2_list.count(x))

t3['sim_score'] = t3['team_1'] * t3['count']

total_sim = t3['sim_score'].sum()

total_sim

## output: 21328497
## End of Code 