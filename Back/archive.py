def write(path: str, line: str) -> None:
    archive = open(path, 'a')
    archive.write(f'{line}\n')
    archive.close()

    # file.write(f"[{datetime.today().strftime('%d/%m/%Y %H:%M:%S')}]: {message}\n")