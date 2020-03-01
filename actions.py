import models

class CrudTipo:

    def inserirTipo(arg):
        try:
            models.Tipo.create(tipo= arg)
            return True
        except:
            return False
    
    def lerTodosTipo():
        return models.Tipo.select()
    
    def tipoPorId(id):
        return models.Tipo.get(models.Tipo.id == id)
    
    def deletarTipo(id):
        tipo = models.Tipo.get(models.Tipo.id == id)
        tipo.delete_instance()
        return True
    
    def atualizarTipo(id, arg):
        tipo = models.Tipo.get(models.Tipo.id == id)
        tipo.tipo = arg
        tipo.save()
        return True
