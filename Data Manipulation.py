import pandas as pd

# Loader vores datasæt fra en csv fil. Der er to muligheder
# data = pd.read_csv('cc_approvals.data')
# df = pd.DataFrame(data)

# Eller
df = pd.read_csv('cc_approvals.data')

# Vi kan bruge metoderne head og tail til, at udskrive de første 5(default) eller de sidste 5
print(df.head())
print('\n')
print(df.tail())
print('\n')

# Man kan gemme på flere måder
# Gemmer til en csv fil
# df.to_csv('name.csv', encoding='uft-8')

# Gemmer til et python dictionary
# dictionary = df.to_dict()

# Gemmer til string
# dataString = df.to_string()

# Info giver os informationer om indeholdet i vores dataframe
print(df.info())
print('\n')
# Describe giver os kolonnestatistikker
print(df.describe())
print('\n')


# Giver os hvor mange rækker og kolonner der er
# Hvis man kune ville vide antal kolonner kunne man skrive df.shape[1]
print(df.shape)
print('\n')
