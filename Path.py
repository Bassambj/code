# PYTHON - BIBLIOTECAS
import pathlib
import inspect #inspect file

class Path(type(pathlib.Path())):
    @staticmethod
    def script_dir():
        print(inspect.stack()[1].filename) #obtendo um nome pelo print
        p = pathlib.Path(inspect.stack()[1].filename)
        return p.parent.resolve()
# tem-se o retorno do diretório pai através da função return.
# pos-graduação python Unicesumar - cod. e teste sob análise.