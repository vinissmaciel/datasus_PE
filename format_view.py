import glob

arquivos = glob.glob("csvfiles/*.csv") + glob.glob("txtfiles/*.txt")

with open("visualizacao_resumida.txt", "w", encoding="utf-8") as outfile:
    for fname in arquivos:
        with open(fname, "r", encoding="utf-8") as infile:
            outfile.write(infile.read())
            outfile.write("\n")  #
