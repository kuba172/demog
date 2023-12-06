import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
import os

# Funkcja do wczytywania danych z pliku .csv z imputacją brakujących wartości
def load_data(file_path):
    df = pd.read_csv(file_path, header=None)
    df.replace('-', 0, inplace=True)  # Zamiana '-' na 0
    df.columns = ['wiek', 'ludzie', 'mezczyzni', 'kobiety', 'miasto_ludzie', 'miasto_mezczyzni', 'miasto_kobiety',
                  'wies_ludzie', 'wies_mezczyzni', 'wies_kobiety']

    # Uzupełnienie brakujących wartości za pomocą IterativeImputer
    imputer = IterativeImputer(max_iter=10, random_state=42)
    df.iloc[:, 1:] = imputer.fit_transform(df.iloc[:, 1:])

    return df.astype(int)

# Funkcja do budowania modelu
def build_model(data):
    X = data[['wiek']]
    y = data.drop(['wiek'], axis=1)
    model = RandomForestRegressor(n_estimators=100, random_state=42, warm_start=True)
    model.fit(X, y)
    return model

# Funkcja do generowania predykcji dla zadanego roku
def generate_predictions(model, years, data_frames):
    all_predictions = []

    for i, year in enumerate(years):
        current_data = pd.concat(data_frames[:i + 1])  # Dane treningowe do bieżącego roku

        X_train = current_data[['wiek']]
        y_train = current_data.drop(['wiek'], axis=1)

        # Aktualizacja modelu
        model.n_estimators += 10  # Zwiększ liczbę drzew (dowolna wartość, można dostosować)
        model.fit(X_train, y_train)

        # Generowanie predykcji
        predictions = pd.DataFrame({'wiek': range(0, 71)})
        predicted_values = model.predict(predictions[['wiek']]).astype(int)

        # Dodanie predykcji do listy
        all_predictions.append(pd.DataFrame(data=predicted_values, columns=y_train.columns))

    return all_predictions

# Ścieżka do folderu zawierającego pliki .csv
folder_path = r'C:\Users\kubar\Desktop\SYSTEMY INFORMATYCZNE - MODEL\\' #Ścieżke zmienić w zależności od tego gdzie są dane

# Wczytanie danych z wszystkich plików
years = range(2002, 2021)
data_frames = []

for year in years:
    file_path = folder_path + f'{year}.csv'
    data_frames.append(load_data(file_path))

# Połączenie danych z różnych lat w jedną ramkę danych
all_data = pd.concat(data_frames)

# Budowa modelu na podstawie zebranych danych
model = build_model(all_data)

# Generowanie predykcji dla lat 2021-2060
prediction_years = range(2021, 2061)
all_predictions = generate_predictions(model, prediction_years, data_frames)

# Wprowadzenie roku predykcji przez użytkownika
try:
    user_year = int(input("Podaj rok, dla którego chcesz otrzymać plik CSV: "))
except ValueError:
    print("Podano nieprawidłowy rok. Upewnij się, że podajesz liczbę.")
    exit()

# Pobranie wcześniej przygotowanej predykcji dla użytkownika
user_data = all_predictions[prediction_years.index(user_year)]

# Dodanie kolumny z wiekiem
user_data.insert(0, 'wiek', range(0, 71))

# Zapisanie wyników do pliku .csv
user_output_file_path = os.path.join(folder_path, f'predicted_{user_year}_user.csv')
user_data.to_csv(user_output_file_path, index=False, header=False)