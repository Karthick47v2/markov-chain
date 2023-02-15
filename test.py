import pandas as pd
import numpy as np
import random as rm
import time

def calc_transition_matrix(df):
    """
    Calculates the transition matrix for a Markov model based on the historical data of passenger 
    density.

    Parameters:
        df (pandas DataFrame): A pandas DataFrame that contains historical data of passenger 
        density.

    Returns:
        tuple of two numpy arrays: The transition matrix & transition name
    """

    df['Passengers_Density_Next_Month'] = df['Passengers_Density'].shift(-1)
    df = df.dropna()

    temp = df.groupby('Passengers_Density')['Passengers_Density_Next_Month']
    transition_matrix = temp.value_counts() / temp.count()

    return transition_matrix.values.reshape(3, -1), np.array([f'{x[0]}-{x[1]}' for x in transition_matrix.index]).reshape(3, -1)


def passenger_density_forecast(months, current_density=None):
    """
    Uses a Markov model to forecast the passenger density of an airline over a given number of 
    months, starting from a specified state or a random state.

    Parameters:
        months (int): The number of months to forecast.
        current_density (str, optional): The starting state of passenger density, which can be 
        'Low', 'Medium', or 'High'. If not specified, a random state is chosen.

    Returns:
        array-like: numpy array of predicted density

    Raises:
        ValueError: If the probabilities in the transition matrix do not add up to exactly 1.
    """
    # There is no reason to start from one state or another, let's just
    # pick one randomly
    if current_density == None:
        current_density = rm.choice(states)
    i = 0

    pred = []

    print('Starting Passenger Density: ', current_density)
    while i < months:
        if current_density == 'Low':
            change = np.random.choice(
                transition_name[0], replace=True, p=transition_matrix[0])
        elif current_density == 'Medium':
            change = np.random.choice(
                transition_name[1], replace=True, p=transition_matrix[1])
        else:
            change = np.random.choice(
                transition_name[2], replace=True, p=transition_matrix[2])

        current_density = change.split('-')[1]
        pred.append(current_density)
        print(current_density)

        i += 1
        time.sleep(0.2)

    return np.array(pred)


df = pd.read_csv('AirPassengers.csv')

# Let's define the statespace
states = ['Low', 'Medium', 'High']

# Discretize
df['Passengers_Density'] = pd.qcut(df['#Passengers'], q=3, labels=states)

# Transition matrix and name
transition_matrix, transition_name = calc_transition_matrix(df)

print(transition_matrix, transition_name)


# Check that probabilities add to 1. If not, raise ValueError
if sum(transition_matrix[0])+sum(transition_matrix[1])+sum(transition_matrix[2]) != 3:
    print('Error!!!! Probabilities MUST ADD TO 1. Check transition matrix!!')
    raise ValueError('Probabilities MUST ADD TO 1')


# # FOR DEBUGGING
# passenger_density_forecast(50, 'Low')
# passenger_density_forecast(50, 'Medium')
# passenger_density_forecast(50, 'High')

# # FOR TESTING
# test_n = 100
# df = df.iloc[test_n:,:]

# y_pred = passenger_density_forecast(df.shape[0], df['Passengers_Density'][test_n])
# print(f'Error Rate: {round(np.sum(y_pred != df["Passengers_Density"]) / y_pred.shape[0], 2)}')


# We forecast the weather for next 60 months
passenger_density_forecast(60)


