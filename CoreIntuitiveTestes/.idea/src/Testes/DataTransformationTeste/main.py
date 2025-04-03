import os
from src.data_transformation_pipeline import DataTransformationPipeline

def main():
    print("Current directory:", os.getcwd())

    save_directory_path = os.path.join(os.getcwd(), 'save_directory.txt')
    if os.path.exists(save_directory_path):
        with open(save_directory_path, "r") as f:
            save_directory = f.read().strip() 
    else:
        print(f"Arquivo {save_directory_path} não encontrado.")
        exit()

    pdf_path = os.path.join(save_directory, 'Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf')
    csv_output_path = 'datas.csv'

    abbreviation_substitutions = {'OD': 'Descrição Completa OD', 'AMB': 'Descrição Completa AMB'}

    pipeline = DataTransformationPipeline(pdf_path, csv_output_path, abbreviation_substitutions)
    pipeline.execute()

if __name__ == "__main__":
    main()