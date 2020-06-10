import pandas as pd
import pymorphy2
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/data_stat/yandex-stat-q.csv"
morph = pymorphy2.MorphAnalyzer()
df = pd.read_csv(url)
lstPhrases = [j for i, j in enumerate(df["Поисковая фраза"].str.lower())]
splitedPhrases = list(map(lambda x: x.split(), lstPhrases))
flat_list = [morph.parse(item)[0].normal_form for sublist in splitedPhrases for item in sublist]
