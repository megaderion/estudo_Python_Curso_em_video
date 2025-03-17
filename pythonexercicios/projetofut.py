import requests
import pandas as pd

# Sua chave de API
api_key = 'SUA_CHAVE_DE_API'

# URL da API para obter os resultados de uma liga específica
url = 'https://api-football-v1.p.rapidapi.com/v3/fixtures'

# Parâmetros da requisição
params = {
    'league': 'ID_DA_LIGA',
    'season': 'TEMPORADA'
}

# Cabeçalhos da requisição
headers = {
    'x-rapidapi-host': 'api-football-v1.p.rapidapi.com',
    'x-rapidapi-key': api_key
}

# Fazer a requisição HTTP
response = requests.get(url, headers=headers, params=params)
data = response.json()

# Listas para armazenar os dados
home_teams = []
away_teams = []
home_goals = []
away_goals = []

# Extrair os dados de cada partida
for fixture in data['response']:
    home_team = fixture['teams']['home']['name']
    away_team = fixture['teams']['away']['name']
    home_score = fixture['goals']['home']
    away_score = fixture['goals']['away']
    
    home_teams.append(home_team)
    away_teams.append(away_team)
    home_goals.append(home_score)
    away_goals.append(away_score)

# Criar um DataFrame com os dados
df = pd.DataFrame({
    'Home Team': home_teams,
    'Away Team': away_teams,
    'Home Goals': home_goals,
    'Away Goals': away_goals
})

# Calcular a média de gols por partida
df['Total Goals'] = df['Home Goals'] + df['Away Goals']
average_goals = df['Total Goals'].mean()

print(f'Média de gols por partida: {average_goals:.2f}')
