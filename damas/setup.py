from cx_Freeze import setup, Executable


setup(
    name="Jogo de Damas",
    version="0.1",
    description="Um jogo de damas em Python com Pygame",
    executables=[Executable("main.py", base="Win32GUI")] 
)
