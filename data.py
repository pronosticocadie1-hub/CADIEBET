import pandas as pd

def load_data():

    urls = [
        "https://www.football-data.co.uk/mmz4281/2324/SP1.csv",
        "https://www.football-data.co.uk/mmz4281/2324/E0.csv",
        "https://www.football-data.co.uk/mmz4281/2324/I1.csv"
    ]

    df = pd.concat([pd.read_csv(u) for u in urls])

    df = df[["HomeTeam","AwayTeam","FTHG","FTAG"]]
    df.columns = ["home","away","gh","ga"]

    return df
