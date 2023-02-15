### Dataset - Air Passengers Table

The Air Passengers Forecast Dataset is a time series dataset that contains the number of passengers (in thousands per month) on international airline flights from January 1949 to December 1960. The dataset consists of 144 observations and two columns

| Column      | Example Entry |
| ----------- | ------------- |
| Month       | 1949-01       |
| #Passengers | 112           |

- `Month`: date of the observation in "YYYY-MM" format.
- `#Passengers`: number of passengers on the corresponding month.

[Dataset link](https://www.kaggle.com/datasets/yasserh/air-passengers-forecast-dataset)

| Column      | Minimum | Maximum | Mean   | Standard deviation |
| ----------- | ------- | ------- | ------ | ------------------ |
| Month       | Nil     | Nil     | Nil    | Nil                |
| #Passengers | 104     | 622     | 280.30 | 119.97             |

> NOTE: As month is categorical data, required statistics won't be calculated

### Markov Chain

> Error rate = 0.32 (Trained with 100 and test 44)

**Transition Matrix**

|        | Low  | Medium | High |
| ------ | ---- | ------ | ---- |
| Low    | 0.92 | 0.08   | 0.00 |
| Medium | 0.06 | 0.81   | 0.16 |
| High   | 0.00 | 0.11   | 0.89 |

> NOTE: All values are rounded to 2 decimal values
