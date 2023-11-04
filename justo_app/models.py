from django.db import models

OPC_BOOL = (('S','Si'),('N','No'))

OPC_CLASEDOC  = (
        ('C', 'Cédula de Ciudadanía'),
        ('T', 'Tarjeta de Identidad'),
        ('N', 'Nit'),
        ('R', 'Registro Civil'),
        ('E', 'Cédula de Extranjería'),
        ('P', 'Pasaporte'),
        ('O', 'Otros'),
    )

OPC_REGIMEN  = (
        ('48', 'Responsable'),
        ('99', 'No Responsable'),
        ('Comun', 'Comun'),
    )

OPC_TIPTER  = (
        ('N', 'Persona Natural'),
        ('J', 'Persona Jurídica'),
        ('O', 'Otro'),
    )

OPC_PRODUCTO  = (
        ('AP', 'Aportes'),
        ('AH', 'Ahorros'),
        ('CR', 'Créditos'),
        ('CC', 'Cuenta por Cobrar'),
        ('CP', 'Cuenta por Pagar'),
        ('CO', 'Contable'),
        ('BA', 'Bancos'),
    )

OPC_CANALES  = (
        ('ATM', 'Red de Cajeros'),
        ('POS', 'Compras en Comercios'),
        ('IVR', 'Audio Respuesta'),
        ('TRA', 'Transferencia'),
        ('CON', 'Consignación'),
        ('EFE', 'Efectivo'),
        ('CHE', 'Cheque'),
        ('GIR', 'Giro'),
        ('WEB', 'Portal Transaccional'),
        ('MOV', 'Banca Móvil'),
        ('OFI', 'Oficina'),
        ('CNB', 'Corresponsales Bancarios'),
        ('RAL', 'Redes Aliadas')
    )

OPC_NAT  = (
        ('D', 'Débito'),
        ('C', 'Crédito'),
    )

OPC_TERMINO  = (
        ('D', 'Definido'),
        ('I', 'Indefinido'),
    )

OPC_PER_LIQ_INT  = (
        ('D', 'Diario'),
        ('M', 'Mensual'),
        ('C', 'Cdat'),
        ('V', 'Vencimiento'),
    )

OPC_EST_CTA_AHO  = (
        ('A', 'Activa'),
        ('I', 'Inactiva'),
        ('C', 'Cancelada'),
        ('E', 'Embargada'),
    )

OPC_SEXO = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('N', 'No Aplica'),
    )

OPC_LIQ_INT_AHO  = (
        ('C', 'Causación Final'),
        ('D', 'Causación Diaria'),
        ('M', 'Causación Mensual'),
        ('V', 'Causación Vencimiento'),
        ('P', 'Pago'),
    )

OPC_CRE_TERMINO  = (
        ('D', 'Definido'),
        ('C', 'Cupo'),
        ('R', 'Rotativo'),
    )

OPC_CRE_FOR_PAG  = (
        ('P', 'Personal'),
        ('L', 'Libranza'),
    )

OPC_CRE_EST_JUR = (
        ('N', 'Normal'),
        ('P', 'Persuasivo'),
        ('J', 'Cobro Jurídico'),
        ('C', 'Condonación'),
        ('T', 'Castigado'),
    )

OPC_CRE_CATEGORIA = (
        ('A', 'Normal'),
        ('B', 'Apreciable'),
        ('C', 'En Peligro'),
        ('D', 'En Mora'),
        ('E', 'Irrecuperable'),
        ('F', 'Castigado'),
    )

OPC_EST_CRE = (
        ('X', 'Por Causar'),
        ('A', 'Activo'),
        ('C', 'Cancelado'),
        ('T', 'Terminado Cupo'),
    )
