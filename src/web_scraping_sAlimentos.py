import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def main():

    # Get the html code
    request = requests.get('https://www.superalimentos.pro/')

    html_soup = BeautifulSoup(request.content, 'html.parser')
    
    data_dic = {'text':[]}
    
    # Get the titles
    superAlimentos = html_soup.find_all('strong')
    #print(superAlimentos)
    # Extract superAlimentos
    #for notice in superAlimentos:
     #   timestamp = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
      #  data_dic['text'].append(notice.text)
       # data_dic['timestamp'].append(timestamp)

    # Create dataframe
    df_superA = pd.DataFrame(data_dic)

    # Descarto columnas que tengan menos de 10 palabras (las ponogo a Nan)
    df_superA.loc[df_superA['text'].str.len()<3,'text'] = None
    print(df_superA)
    # Descarto columnas con Nan
    df_superA = df_superA.dropna()
    print(df_superA)

if __name__ == '__main__':
    main()