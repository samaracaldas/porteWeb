from rolepermissions.roles import AbstractUserRole 


class Comercial(AbstractUserRole):
    available_permissions = {'ver_metas': True, 'criar_metas': True}
    
class Administrativo(AbstractUserRole):
    available_permissions = {'ver_estoque': True, 'cadastro_clientes': True, 'ver_metas': True}