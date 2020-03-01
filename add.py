import controller

try:
    controller.CrudTipo.atualizarTipo(1, "adm")
    str = controller.CrudTipo.tipoPorId(1)
    print(str.tipo)
except:
    print("Erro")
