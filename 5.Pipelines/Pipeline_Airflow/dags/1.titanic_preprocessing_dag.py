from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Define the DAG
dag = DAG(
    'titanic_preprocessing_dag',
    start_date=datetime(2023, 7, 20),
    schedule=None,
)


# Define the functions for each step
def load_data(ti):
    """This function is used to load the data from a csv file."""
    df = pd.read_csv('../data/titanic.csv')
    ti.xcom_push(key='data', value=df)


def divide_data(ti):
    """This function divides the dataset into 2 equal parts."""
    df = ti.xcom_pull(key='data', task_ids='load_data_task')
    part1, part2 = df.iloc[:int(len(df)/2)], df.iloc[int(len(df)/2):]
    ti.xcom_push(key='part1', value=part1)
    ti.xcom_push(key='part2', value=part2)


def clean_data(part_name, ti):
    """This function clears the data from the missing values."""
    df = ti.xcom_pull(key=part_name, task_ids=f'divide_data_task')
    df = df.dropna()
    ti.xcom_push(key=f'clean_{part_name}', value=df)


def encode_features(part_name, ti):
    """This function applies OHE on the categorical variables."""
    df = ti.xcom_pull(key=f'clean_{part_name}', task_ids=f'clean_{part_name}_task')
    encoder = LabelEncoder()
    df['Sex'] = encoder.fit_transform(df['Sex'])
    df['Embarked'] = encoder.fit_transform(df['Embarked'])
    ti.xcom_push(key=f'encoded_{part_name}', value=df)


def combine_data(ti):
    """This function combines 2 parts of data into one."""
    part1 = ti.xcom_pull(key='encoded_part1', task_ids='encode_part1_features_task')
    part2 = ti.xcom_pull(key='encoded_part2', task_ids='encode_part2_features_task')
    df = pd.concat([part1, part2])
    ti.xcom_push(key='combined_data', value=df)


def save_data(ti):
    """This function saves the data as a csv."""
    df = ti.xcom_pull(key='combined_data', task_ids='combine_data_task')
    df.to_csv('../data/train_processed.csv', index=False)


# Define the tasks
load_data_task = PythonOperator(
    task_id='load_data_task',
    python_callable=load_data,
    dag=dag,
)

divide_data_task = PythonOperator(
    task_id='divide_data_task',
    python_callable=divide_data,
    dag=dag,
)

clean_part1_task = PythonOperator(
    task_id='clean_part1_task',
    python_callable=clean_data,
    op_kwargs={'part_name': 'part1'},
    dag=dag,
)

clean_part2_task = PythonOperator(
    task_id='clean_part2_task',
    python_callable=clean_data,
    op_kwargs={'part_name': 'part2'},
    dag=dag,
)

encode_part1_features_task = PythonOperator(
    task_id='encode_part1_features_task',
    python_callable=encode_features,
    op_kwargs={'part_name': 'part1'},
    dag=dag,
)

encode_part2_features_task = PythonOperator(
    task_id='encode_part2_features_task',
    python_callable=encode_features,
    op_kwargs={'part_name': 'part2'},
    dag=dag,
)

combine_data_task = PythonOperator(
    task_id='combine_data_task',
    python_callable=combine_data,
    dag=dag,
)

save_data_task = PythonOperator(
    task_id='save_data_task',
    python_callable=save_data,
    dag=dag,
)

# Set task dependencies
load_data_task >> divide_data_task
divide_data_task >> clean_part1_task >> encode_part1_features_task
divide_data_task >> clean_part2_task >> encode_part2_features_task
encode_part1_features_task >> combine_data_task
encode_part2_features_task >> combine_data_task
combine_data_task >> save_data_task
