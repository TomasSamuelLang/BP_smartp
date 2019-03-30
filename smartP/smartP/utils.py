from .models import ParkingLot,OldCapacityData
import pandas as pd


def calculatePeakHours(parkingData):

    historyData = parkingData.oldcapacitydata_set.all()

    sums = {x: 0 for x in range(0, 24)}
    counts = {x: 0 for x in range(0, 24)}

    for x in historyData:

        hour = x.date.hour
        counts[hour] += 1
        sums[hour] += x.parkedcars

    results = [int(sums[x]/counts[x]) if counts[x] > 0 else 0 for x in range(0, 24)]

    return results


def calculatePeakDays(parkingData):

    historyData = parkingData.oldcapacitydata_set.all()

    sums = {x: 0 for x in range(0, 7)}
    counts = {x: 0 for x in range(0, 7)}

    data = {
        'date': [x.date for x in historyData],
        'parkedcars': [x.parkedcars for x in historyData]
    }

    data_df = pd.DataFrame(data=data)

    data_df['day'] = data_df['date'].apply(lambda x: x.day)
    data_df['weekday'] = data_df['date'].apply(lambda x: x.weekday())

    temp = data_df.groupby(['day', 'weekday'])['parkedcars'].sum().reset_index()
    results = temp.groupby('weekday')['parkedcars'].mean().tolist()


    print(results)
    return results