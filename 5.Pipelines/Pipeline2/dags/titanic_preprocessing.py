from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Define the DAG
dag = DAG(
    'titanic_preprocessing',
    start_date=datetime(2023, 7, 18),
    schedule=None,
)


# Define the functions for each step
def clean_data(ti):
    df = pd.read_csv('../data/titanic.csv')
    df = df.dropna()
    ti.xcom_push(key='clean_data', value=df)


def encode_features(ti):
    df = ti.xcom_pull(key='clean_data', task_ids='clean_data_task')
    encoder = LabelEncoder()
    df['Sex'] = encoder.fit_transform(df['Sex'])
    df['Embarked'] = encoder.fit_transform(df['Embarked'])
    ti.xcom_push(key='encoded_data', value=df)


def split_data(ti):
    df = ti.xcom_pull(key='encoded_data', task_ids='encode_features_task')
    train, valid = train_test_split(df, test_size=0.2, random_state=42)
    ti.xcom_push(key='train_data', value=train)
    ti.xcom_push(key='valid_data', value=valid)


def save_data(ti):
    train = ti.xcom_pull(key='train_data', task_ids='split_data_task')
    valid = ti.xcom_pull(key='valid_data', task_ids='split_data_task')
    train.to_csv('../data/train_processed.csv', index=False)
    valid.to_csv('../data/valid_processed.csv', index=False)


# Define the tasks
clean_data_task = PythonOperator(
    task_id='clean_data_task',
    python_callable=clean_data,
    dag=dag,
)

encode_features_task = PythonOperator(
    task_id='encode_features_task',
    python_callable=encode_features,
    dag=dag,
)

split_data_task = PythonOperator(
    task_id='split_data_task',
    python_callable=split_data,
    dag=dag,
)

save_data_task = PythonOperator(
    task_id='save_data_task',
    python_callable=save_data,
    dag=dag,
)

# Set task dependencies
clean_data_task >> encode_features_task >> split_data_task >> save_data_task
