def write_marketplace(path: str, obj: str) -> None:
    archive = open(path, 'a')
    archive.write(f'{obj}\n')
    archive.close()

    # file.write(f"[{datetime.today().strftime('%d/%m/%Y %H:%M:%S')}]: {message}\n")