import pandas as pd
import numpy as np
import sys

homeworld = sys.argv[1]
print(homeworld)
unit_type = sys.argv[2]
print(unit_type)

model = pd.read_pickle('../trained_model.pkl')
troop_data = pd.read_csv('../troop_movements.csv')

X = troop_data[['homeworld','unit_type']]

inputs_array = np.array([[homeworld, unit_type]])
inputs_df = pd.DataFrame(inputs_array)
print(inputs_df)
inputs_df.columns = ['homeworld','unit_type']
X = X.append(inputs_df, ignore_index=True)
# print(inputs_df)
encoded_list = pd.get_dummies(X)

prediction = model.predict(encoded_list)
# woohoo!
print(prediction[-1])
# print(X.tail(5))

