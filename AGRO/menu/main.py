import subprocess

def main():

    opcion=int(input("¿Que desea ejecutar?\n \t1.ScraperIterativo \t2.ScraperConsumos \t3.ScraperSuperAlimentos \t4.Transformar \t5.Modelo\n"))
    if opcion==0:
        quit()
    elif opcion==1:
        lanzaScrapper1()
    elif opcion==2:
        lanzaScrapper2()
        subprocess.run(["docker", "run", "/Compose/Dockerfile"])
    elif opcion==3:
        lanzaScrapper3()
        subprocess.run(["docker", "run", "/Modelo/"])
    elif opcion==4:
        lanzarLimpiar()
    elif opcion==5:
        lanzarModelo()
    else:
        print("Esa opción no es correcta")

def lanzaScrapper1():

    subprocess.run(["docker", "run", "/src/DockerfileIt"], shell=True, check=True, capture_output=True)

def lanzaScrapper2():

    subprocess.run(["docker", "run", "/src/DockerfileCCAA"], shell=True, check=True, capture_output=True)

def lanzaScrapper3():

    subprocess.run(["docker", "run", "/src/DockerfileSA"], shell=True, check=True, capture_output=True)

def lanzarLimpiar():
    print("hi")

def lanzarModelo():
    print("Modelo")

main()