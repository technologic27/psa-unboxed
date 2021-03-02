import pandas as pd
from datetime import datetime as dt

filename = 'samples.csv'
date_time_format = '%Y/%m/%d %H:%M:%S'

def preprocess(filename, delimiter = ';'):
    data = pd.read_csv(filename, sep = delimiter)
    
    data['EVENT_PURPOSE'] = data['EVENT_C'] + '_' + data['DERIVED_CNTR_PURP_C']
    
    # data["BTR1_DATE"] = [dt.strptime(x, date_time_format).date() for x in data.BTR1]
    data["ATD1_DATE"] = [dt.strptime(x, date_time_format).date() for x in data.ATD1]
    # data["ATU1_DATE"] = [dt.strptime(x, date_time_format).date() for x in data.ATU1]
    # data["BTR2_DATE"] = [dt.strptime(x, date_time_format).date() for x in data.BTR2]
    data["ATD2_DATE"] = [dt.strptime(x, date_time_format).date() for x in data.ATD2]
    # data["ATU2_DATE"] = [dt.strptime(x, date_time_format).date() for x in data.ATU2]
    
    data['DIFF_ATD1_BTR1'] = [(dt.strptime(row['ATD1'], date_time_format) - dt.strptime(row['BTR1'], date_time_format)).total_seconds() / 60 \
                          for index, row in data.iterrows()]
    data['DIFF_ATU1_ATD1'] = [(dt.strptime(row['ATU1'], date_time_format) - dt.strptime(row['ATD1'], date_time_format)).total_seconds() / 60 \
                              for index, row in data.iterrows()]
    data['DIFF_ATD2_BTR2'] = [(dt.strptime(row['ATD2'], date_time_format) - dt.strptime(row['BTR2'], date_time_format)).total_seconds() / 60 \
                              for index, row in data.iterrows() if not pd.isna(row['BTR2']) and not pd.isna(row['ATD2'])]
    data['DIFF_ATU2_ATD2'] = [(dt.strptime(row['ATU2'], date_time_format) - dt.strptime(row['ATD2'], date_time_format)).total_seconds() / 60 \
                              for index, row in data.iterrows() if not pd.isna(row['ATU2']) and not pd.isna(row['ATD2'])]
    
    data['DIFF_ATU2_ATD1'] = [(dt.strptime(row['ATU2'], date_time_format) - dt.strptime(row['ATD1'], date_time_format)).total_seconds() / 60 \
                          for index, row in data.iterrows() if not pd.isna(row['ATU2'])]
    
    data = data.drop(columns = ['EVENT_C', 'ABBR_VESSEL_M1', 'BTR1', 'ATD1', 'ATU1', 'SERVICE_TYPE_DESC_X1', \
                            'CONSORTIUM_C1', 'ABBR_VESSEL_M2', 'BTR2', 'ATD2', 'ATU2', 'SERVICE_TYPE_DESC_X2', \
                            'CONSORTIUM_C2', 'OPR_GROUP_C', 'SUMOFBOX_Q'])
    return data