import pandas as pd
def read_data(data): 
    
    data.reset_index(inplace = True)
    data.rename(columns={'level_0': 'Time'}, inplace = True)
    data.rename(columns={'x-axis (deg/s).4': 'Raw Brainwave Signal '}, inplace = True)
    data.rename(columns={'Unnamed: 42': 'Tag'}, inplace = True)
    
    TimeStamp = data.iloc[:,0]
    ankle = data.iloc[: , 1:8]
    pocket = data.iloc[:, 8:15]
    waist = data.iloc[:,15:22]
    neck = data.iloc[:,22:29]
    wrist = data.iloc[:,29:36]
    EEG = data.iloc[:,36]
    Infraded = data.iloc[:,37:43]
    label = data.iloc[:,46]
        
    ankle.columns = ['X-axis Accelerometer (g)', 'Y-axis Accelerometer (g)' , 'Z-axis Accelerometer (g)',
                     'Roll Gyroscrope (deg/s)', 'Pitch Gyroscope (deg/s)', 'Yaw Gyroscope (deg/s)' ,'Luminosity (lux)']

    pocket.columns = ['X-axis Accelerometer (g)', 'Y-axis Accelerometer (g)' , 'Z-axis Accelerometer (g)',
                     'Roll Gyroscrope (deg/s)', 'Pitch Gyroscope (deg/s)', 'Yaw Gyroscope (deg/s)' ,'Luminosity (lux)']

    waist.columns = ['X-axis Accelerometer (g)', 'Y-axis Accelerometer (g)' , 'Z-axis Accelerometer (g)',
                     'Roll Gyroscrope (deg/s)', 'Pitch Gyroscope (deg/s)', 'Yaw Gyroscope (deg/s)' ,'Luminosity (lux)']

    neck.columns = ['X-axis Accelerometer (g)', 'Y-axis Accelerometer (g)' , 'Z-axis Accelerometer (g)',
                     'Roll Gyroscrope (deg/s)', 'Pitch Gyroscope (deg/s)', 'Yaw Gyroscope (deg/s)' ,'Luminosity (lux)']

    wrist.columns = ['X-axis Accelerometer (g)', 'Y-axis Accelerometer (g)' , 'Z-axis Accelerometer (g)',
                     'Roll Gyroscrope (deg/s)', 'Pitch Gyroscope (deg/s)', 'Yaw Gyroscope (deg/s)' ,'Luminosity (lux)']

    Infraded.columns = ['Infrared 1', 'Infrared 2', 'Infrared 3', 'Infrared 4', 'Infrared 5', 'Infrared 6']

    handled_data = pd.concat([TimeStamp, ankle,pocket,waist,neck,wrist,EEG,Infraded ], 
                            axis = 1, 
                            keys = ['TimeStamp','Wearable Ankle', 'Wearable Pocket','Wearable Waist', 
                                    'Wearable Neck', 'Wearable Wrist','EEG Headset'  ,'Infrared'],
                             
                            names = ['Deviece Name', 'Channel Name'])
    handled_data[('Tag' , 'Label')]= label
    
    return handled_data

data = pd.read_csv(r'dataset\CompleteDataSet.csv', skiprows = 1)

pd.concat

handled = read_data(data=data)
print(handled)
print(data.shape[0])