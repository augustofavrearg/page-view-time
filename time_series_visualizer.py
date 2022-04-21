
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=True,index_col='date')

# Clean data
df = df_filter = df[(df["value"] > df["value"].quantile(0.025))&
               (df["value"] < df["value"].quantile(0.975))]





def draw_line_plot():
    
    
    fig = sns.lineplot(x=df_filter.index.tolist(), y="value", data=df_filter)
    fig.set(xlabel ="Date", ylabel = "Page Views", title ="Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    
    return fig





def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df.reset_index(inplace=True)
    #.agg agrega una columna con el promedio de value
    #.unstack le da el formato de doble entrada
    #groupby agrupa los datos
    df_bar = df.groupby([df['date'].dt.year.rename('Years'),
               df['date'].dt.month.rename('Months')]).agg('mean')['value'].unstack()
    
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(12,8))
    df_bar.plot(kind='bar', ax=ax)
    plt.legend(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
          

                
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    
    return fig
  


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date] 
 

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1,2,figsize=(20,5))

    plt.ylim(10000,180000)
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    #tight_layout permite ajustar las etiquetas en el espacio para evitar superposiciones
    plt.tight_layout()
    plt.title("Year-Wise Box Plot (Trend)")
    #ax=ax[1] ubicacion del grafico en el lugar 1
    sns.boxplot(x='year',y='value', data=df_box, ax=ax[1])
    
    plt.ylim(10000,180000)
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    #tight_layout permite ajustar las etiquetas en el espacio para evitar superposiciones
    plt.tight_layout()
    plt.title("Month-Year Box Plot (Seasonality)")
    #ax=ax[0] ubicacion del grafico en el lugar 0
    sns.boxplot(x='month',y='value', data=df_box,  ax=ax[0])
    
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

