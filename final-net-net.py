import pandas as pd
inp= pd.read_csv("modified_file-flmem-time-fin.csv")

#inp['Server name'] = 'Ap-net'
inp=inp.drop('Server name', axis=1)

inp.insert(2,'Server', 'DB')

inp.to_csv("modified_file-flmem-time-fin.csv", index=False)