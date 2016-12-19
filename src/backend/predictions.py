import io
import json

with io.open('../../resources/monthly_orders.json') as monthly_orders_file:
    order_stats = json.load(monthly_orders_file)

import timeseries_nnet
timeseries = map(lambda x: len(x), order_stats[0][1].values())
model = timeseries_nnet.TimeSeriesNnet(
    timeseries=timeseries,
    hidden_layers=[15, 10, 5],
    activation_functions=['sigmoid', 'relu', 'relu'],
    lag=11)
model.fit(verbose=1, epochs=5000)
print(timeseries, model.predict_ahead(3))
