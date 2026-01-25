import pandas as pd
import glob
import os

# pasta de entrada (CSV)
pasta_csv = "data/raw/CLIMA_2000_2025/"
# pasta de saída (XLSX)
pasta_xlsx = "data/processed/CLIMA_2000_2025_XLSX/"

os.makedirs(pasta_xlsx, exist_ok=True)

arquivos = glob.glob(os.path.join(pasta_csv, "*.csv"))

for arquivo in arquivos:
    nome = os.path.basename(arquivo).replace(".csv", ".xlsx")
    
    df = pd.read_csv(
        arquivo,
        sep=";",
        encoding="latin1"
    )
    
    caminho_saida = os.path.join(pasta_xlsx, nome)
    df.to_excel(caminho_saida, index=False)
    
    print(f"Convertido: {nome}")
    
print("Conversão concluída.")