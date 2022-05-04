# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 02:33:19 2015

@author: nymph
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime as dt
import seaborn as sns

############################## Your code for loading and preprocess the data ##

def check_missing_values(df):
    if '?' in df.values:
        return True
    return False
def load_and_preprocess(file_name):
    df = pd.read_table(file_name, delimiter=';', low_memory=False)
    # Convert `Date` column from object type to datetime type
    df['Date'] = pd.to_datetime(df['Date'])
    # Extract row from given date range
    # mask = (df['Date'] == dt.datetime(2007,2,2))
    mask = (df['Date'] >= dt.datetime(2007,2,1)) & (df['Date'] <= dt.datetime(2007,2,2))
    df = df.loc[mask]
    # Convert `Date` values to Day_Of_Week form
    df['Date'] = df['Date'].dt.strftime("%A")
    # Convert `Global_active_power`,
    #         `Global_reactive_power`,
    #         `Voltage`,
    #         `Sub_metering_1`,`Sub_metering_2`,`Sub_metering_3`
    # column to float type
    df['Global_active_power'] = df['Global_active_power'].astype(float)
    df['Global_reactive_power'] = df['Global_reactive_power'].astype(float)
    df['Voltage'] = df['Voltage'].astype(float)
    df['Sub_metering_1'] = df['Sub_metering_1'].astype(float)
    df['Sub_metering_2'] = df['Sub_metering_2'].astype(float)
    df['Sub_metering_3'] = df['Sub_metering_3'].astype(float)
    # Check if found missing values (contains character `?`)
    if check_missing_values(df) == False:
        return df


############################ Complete the following 4 functions ###############
def plot1(df):
    plt.figure(figsize = (8,7))
    sns.histplot(x="Global_active_power", data=df,bins = 21, kde=False, color = 'red')
    plt.title('Global Active Power',weight='bold')
    plt.xlabel('Global Active Power (kilowatts)')
    plt.ylabel('Frequency')
    plt.yticks(rotation=90)
    plt.savefig('plot1.png')


def plot2(df):
    mask = (df['Time'] >= '05:00:00') & (df['Time'] <= '23:00:00')
    df = df.loc[mask]

    plt.figure(figsize = (15,7))
    plt.plot(df['Time'],df['Global_active_power'], color="black")
    plt.ylabel('Global Active Power (kilowatts)')
    plt.yticks(rotation=90)
    plt.xticks(rotation=90)
    plt.title('Linechart showing the trend of Global_Active_Power in hours in Feb 2007 ', y=-0.1,fontsize=13)

    frame = plt.gca()
    frame.axes.get_xaxis().set_visible(False)
    plt.savefig('plot2.png')


def plot3(df):
    mask = (df['Time'] >= '05:00:00') & (df['Time'] <= '23:00:00')
    df = df.loc[mask]
    plt.figure(figsize = (25,5))
    plt.plot(df['Time'], df['Sub_metering_1'], label = "Sub_metering_1", color = "black")
    plt.plot(df['Time'], df['Sub_metering_2'], label = "Sub_metering_2", color = "red")
    plt.plot(df['Time'], df['Sub_metering_3'], label = "Sub_metering_3", color = "blue")
    plt.ylabel('Energy sub metering',fontsize=13)
    plt.legend(loc = "upper left")

    plt.title('Linechart showing the trend of 3 Sub_metering in hours in Feb 2007 ', y=-0.1,fontsize=13)
    frame = plt.gca()
    frame.axes.get_xaxis().set_visible(False)
    plt.savefig('plot3.png')

def plot4(df):
    mask = (df['Time'] >= '05:00:00') & (df['Time'] <= '23:00:00')
    df = df.loc[mask]
    fig, axs = plt.subplots(2,2,figsize=(20,10))
    axs[0][0].plot(df['Time'],df['Global_active_power'], color="black")
    axs[0][0].set_xticks([])
    axs[0][0].set_xlabel('Linechart showing the trend of Global_Active_Power in hours in Feb 2007')
    axs[0][0].set_ylabel('Global Active Power (kilowatts)')

    axs[1][0].plot(df['Time'], df['Sub_metering_1'], label = "Sub_metering_1", color = "black")
    axs[1][0].plot(df['Time'], df['Sub_metering_2'], label = "Sub_metering_2", color = "red")
    axs[1][0].plot(df['Time'], df['Sub_metering_3'], label = "Sub_metering_3", color = "blue")
    axs[1][0].legend(loc="upper left",prop={'size': 5})
    axs[1][0].set_xticks([])
    axs[1][0].set_xlabel('Linechart showing the trend of 3 Sub_metering in hours in Feb 2007')
    axs[1][0].set_ylabel('Energy sub metering')

    axs[0][1].plot(df['Time'],df['Voltage'], color="black")
    axs[0][1].set_xticks([])
    axs[0][1].set_xlabel('Linechart showing the trend of Voltage in hours in Feb 2007')
    axs[0][1].set_ylabel('Voltage (volts)')

    axs[1][1].plot(df['Time'],df['Global_reactive_power'], color="black")
    axs[1][1].set_xticks([])
    axs[1][1].set_xlabel('Linechart showing the trend of Global_reactive_power in hours in Feb 2007')
    axs[1][1].set_ylabel('Global_reactive_power (kilowatts)')
    plt.savefig('plot4.png')

############################## Main function ###################################
if __name__ == "__main__":
    df = load_and_preprocess('household_power_consumption.txt')
    plot1(df)
    plot2(df)
    plot3(df)
    plot4(df)

