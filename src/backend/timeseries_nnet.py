# Modified code from https://github.com/hawk31/nnet-ts
import logging
import numpy as np
from keras.optimizers import SGD
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from sklearn.preprocessing import StandardScaler

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class TimeSeriesNnet(object):
    def __init__(self, timeseries, hidden_layers=[20, 15, 5],
                 activation_functions=['relu', 'relu', 'relu'],
                 optimizer=SGD(), loss='mean_absolute_error',
                 lag=11):
        self._hidden_layers = hidden_layers
        self._activation_functions = activation_functions
        self._optimizer = optimizer
        self._loss = loss

        self._lag = lag
        self._timeseries = self._prepare_data(timeseries)
        self._scaler = StandardScaler()
        self._nn = Sequential()

        if len(self._hidden_layers) != len(self._activation_functions):
            raise Exception('hidden_layers size must match'
                            'activation_functions size')

    def _prepare_data(self, timeseries):
        return np.array(timeseries, dtype='float64')

    def fit(self, epochs=10000, verbose=0):
        timeseries_len = len(self._timeseries)
        if self._lag >= timeseries_len:
            raise ValueError('Lag is higher than length of the timeseries')

        X = np.zeros((timeseries_len - self._lag, self._lag), dtype='float64')
        y = np.log(self._timeseries[self._lag:])

        # Building X matrixs
        logging.info('Building regressor matrix')
        for i in range(0, timeseries_len - self._lag):
            X[i, :] = self._timeseries[range(i, i + self._lag)]

        logging.info('Scaling data')
        self._scaler.fit(X)
        X = self._scaler.transform(X)

        # Neural net architecture
        logging.info('Checking network consistency')
        self._nn.add(Dense(self._hidden_layers[0], input_shape=(X.shape[1],)))
        self._nn.add(Activation(self._activation_functions[0]))

        for layer_size, activation_function in zip(
                self._hidden_layers[1:], self._activation_functions[1:]):
            self._nn.add(Dense(layer_size))
            self._nn.add(Activation(activation_function))

        # Add final node
        self._nn.add(Dense(1))
        self._nn.add(Activation('linear'))
        self._nn.compile(loss=self._loss, optimizer=self._optimizer)

        # Train neural net
        logging.info('Training neural net')
        self._nn.fit(X, y, nb_epoch=epochs, verbose=verbose)

    def predict_ahead(self, n_ahead=1):
        # Store predictions and predict iteratively
        predictions = np.zeros(n_ahead)

        timeseries = self._timeseries

        for i in range(n_ahead):
            current_x = self._scaler.transform(
                timeseries[-self._lag:].reshape((1, self._lag)))
            next_pred = self._nn.predict(current_x)
            predictions[i] = np.exp(next_pred[0, 0])
            timeseries = np.concatenate((
                timeseries, np.exp(next_pred[0, :])), axis=0)

        return predictions
