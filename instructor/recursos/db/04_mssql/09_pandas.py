import numpy as np
import matplotlib.pyplot as plt

import pandas as pd

import pymssql
#import mysql.connector as database

from base.connection import create_connection


df = None

def exec_db_load_data():
    global df

    conn = create_connection("")

    print("--------------------- LOAD DATA ------------------")

    df = pd.read_sql('SELECT * FROM factura;', conn, index_col='id')


def exec_db_head():
    print(df.head())

def exec_db_general():
    print("--------------------- Datos Generales ------------------")

    print(df.shape)
    print(df.info())

def exec_db_describe():
    print("--------------------- Describe ------------------")

    print(df.describe())

    print(df['total'].mean())


exec_db_load_data()

exec_db_head()
exec_db_general()
exec_db_describe()