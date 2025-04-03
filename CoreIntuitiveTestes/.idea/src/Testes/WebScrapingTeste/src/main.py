from src.scrapers.web_scraper import WebScraper

def main():
    save_directory = './downloaded_files'
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    
    web_scraper = WebScraper(url, save_directory)

    web_scraper.access_site()

    file_urls = [
        'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf', 
        'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf'
    ]

    web_scraper.download_files(file_urls)

    web_scraper.compress_files()

    web_scraper.close_browser()

    return save_directory

save_directory = main()

with open("save_directory.txt", "w") as f:
    f.write(save_directory)