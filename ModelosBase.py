from django.db import models
import re
from django.core.exceptions import ValidationError


# Create your models here.
# from django.db import models

def validate_numeric(value):
    if not re.match(r'^[0-9]+$', value):
        raise ValidationError('El número de celular debe contener solo dígitos numéricos.')
    
OPC_BOOL = [('S','Si'),('N','No')]

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
        ('49', 'No Responsable'),
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
        ('CR', 'Creditos'),
        ('CC', 'Cuenta por Cobrar'),
        ('CP', 'Cuenta por Pagar'),
        ('CO', 'Contable'),
        ('BA', 'Bancos'),
    )

OPC_EDUCACION = (
    ('0','No Aplica'),
    ('1','Primaria'),
    ('2','Bachiller'),
    ('3','Tecnico'),
    ('4','Tecnologo'),
    ('5','Profesional'),
    ('6','Post Grado'),
    ('7','Maestria'),
    ('8','Doctorado'),
    ('9','Otros'),
)

OPC_PARENTESCO = (
    ('0','No Aplica'),
    ('1','Esposo(a)'),
    ('2','Hijo(a)'),
    ('3','Padre o Madre'),
    ('4','Abuelo(a)'),
    ('5','Nieto(a)'),
    ('6','Tio(a)'),
    ('7','Sobrino(a)'),
    ('8','Primo(a)'),
    ('9','Otro'),
) 

OPC_CANALES  = (
        ('ATM', 'Red de Cajeros'),
        ('POS', 'Compras en Comercios'),
        ('IVR', 'Audio Respuesta'),
        ('TRA', 'Transferencia'),
        ('CON', 'Consignacion'),
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

OPC_MODALIDAD_CRE = (
    ('A','Admisible'),
    ('C','Comercial'),
    ('M','MicroCredito'),
    ('V','Vivienda')
)

OPC_GARANTIA = (
    ('A','Admisible'),
    ('H','Hipotecaria'),
    ('D','Deudor Solidario'),
    ('Otros'),
)

OPC_OCUPACION = (
    ('1','Asalariado'),
    ('2','Pensionado'),
    ('3','Rentista'),
    ('4','Trabajador asociado'),
    ('5','Profesional independiente'),
    ('6','Empleado informal'),
    ('7','Independiente formal'),
    ('8','Independiente informal'),
    ('9','Independiente agro'),
    ('10','Empleado doméstico'),
    ('11','Estudiante'),
)

OPC_TIPO_VIVIENDA = (
	('1','Propia'),
	('2','Familiar'),	
	('3','Arrendada'),
)

class CLIENTES(models.Model):
    id = models.SmallAutoField(primary_key=True)
    codigo = models.CharField(max_length=1, null=False)
    doc_ide = models.CharField(max_length=12,
        validators=[validate_numeric],
        help_text='el documento de identidad debe ser numerico.',
        null=True
    )
    sigla = models.CharField(max_length=36)
    nombre = models.CharField(max_length=120)
    celular = models.CharField(
        max_length=10,
        validators=[validate_numeric],
        help_text='El número de celular debe contener exactamente 10 dígitos numéricos.',
        null=True
    )
    email = models.EmailField()
    dominio = models.URLField()
    class Meta:
        unique_together = [['codigo']]
        db_table = 'clientes'

class OFICINAS(models.Model):
    id = models.SmallAutoField(primary_key=True)
    cliente = models.ForeignKey(CLIENTES, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=5, null=False)
    @property
    def CodigoCliente(self):
       return self.Codigo[0]
    contabiliza = models.CharField(max_length=1, choices=OPC_BOOL)
    nombre_oficina = models.TextField()
    responsable = models.TextField()
    celular = models.CharField(
        max_length=10,
        validators=[validate_numeric],
        help_text='El número de celular debe contener exactamente 10 dígitos numéricos.',
        null=True
    )
    email = models.EmailField()
    class Meta:
        unique_together = [['cliente','codigo']]
        db_table = 'oficinas'


class LOCALIDADES(models.Model):
    # id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(CLIENTES, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=8, null=False)
    ciudad = models.CharField(max_length=1, choices=OPC_BOOL)
    nombre = models.CharField(max_length=36, null=False)
    class Meta:
        unique_together = [['cliente','codigo']]
        db_table = 'localidades'

class TERCEROS(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(CLIENTES, on_delete=models.CASCADE)
    cla_doc = models.CharField(max_length=1, choices=OPC_CLASEDOC)
    doc_ide  = models.CharField(max_length=12,null = False)
    dig_ver   = models.CharField(max_length=1,null = True)
    nit_rap  = models.CharField(max_length=12,null = True)
    cod_ciu_exp  = models.ForeignKey(LOCALIDADES, on_delete=models.CASCADE, related_name='ciu_exp')
    cod_ciu_res = models.ForeignKey(LOCALIDADES, on_delete=models.CASCADE, related_name='ciu_res')
    regimen = models.CharField(max_length=12, choices=OPC_REGIMEN)
    fec_exp_ced = models.DateField()
    tip_ter = models.CharField(max_length=12, choices=OPC_TIPTER)  
    pri_ape = models.CharField(max_length=22,null = True)
    seg_ape = models.CharField(max_length=22,null = True)
    pri_nom = models.CharField(max_length=22,null = True)
    seg_nom  = models.CharField(max_length=22,null = True)
    raz_soc  = models.CharField(max_length=96,null = True)
    direccion = models.CharField(max_length=68,null = True)
    cod_pos = models.CharField(max_length=8,null = True)
    tel_ofi  = models.CharField(max_length=10,null = True)
    tel_res = models.CharField(max_length=10,null = True)  
    celular1 = models.CharField(
        max_length=10,
        validators=[validate_numeric],
        help_text='El número de celular debe contener exactamente 10 dígitos numéricos.',
        null=True
    )
    celular2 = models.CharField(max_length=10,null = True) 
    fax = models.CharField(max_length=10,null = True)     
    email = models.EmailField()
    nombre = models.IntegerField(blank=True, null=True)
    def save(self, *args, **kwargs):
        if self.REGIMEN == "N":
            self.NOMBRE = self.PRI_APE+self.SEG_APE+self.PRI_NOM+self.SEG_NOM
        else:
            self.NOMBRE = self.RAZ_SOC
        super().save(*args, **kwargs)    
    fec_act = models.DateField()
    observacion = models.CharField(max_length=68,null = True)  
    per_pub_exp = models.CharField(max_length=1, choices=OPC_BOOL)
    nit_interno = models.CharField(max_length=1, choices=OPC_BOOL)
    class Meta:
        unique_together = [['cliente','cla_doc','doc_ide']]
        db_table = 'terceros'

class ASOCIADOS(models.Model):
    id = models.AutoField(primary_key=True)
    cod_aso = models.CharField(max_length=12,null = False) 
    oficina = models.OneToOneField(OFICINAS, on_delete=models.CASCADE, null=True)
    tercero = models.OneToOneField(TERCEROS, on_delete=models.CASCADE, null=True)
    sexo = models.CharField(max_length=1,null = False)
    class Meta:
        unique_together = [['oficina','cod_aso']]
        db_table = 'asociados'



class DOCTO_CONTA(models.Model):
    id = models.AutoField(primary_key=True)
    oficina = models.ForeignKey(OFICINAS, on_delete=models.CASCADE)
    per_con = models.IntegerField()
    nom_cto = models.CharField(max_length=8,null = False)
    nombre = models.CharField(max_length=24,null = False)
    inicio_nuevo_per = models.CharField(max_length=1, choices=OPC_BOOL)
    consecutivo = models.IntegerField()
    class Meta:
        unique_together = [['oficina','per_con','nom_cto']]
        db_table = 'docto_conta'

class HECHO_ECONO(models.Model):
    id = models.BigAutoField(primary_key=True)
    docto_conta = models.ForeignKey(DOCTO_CONTA, on_delete=models.CASCADE)
    numero = models.IntegerField()
    fecha = models.DateField()
    descripcion = models.CharField(max_length=64,null = True)
    anulado = models.CharField(max_length=1, choices=OPC_BOOL)
    protegido = models.CharField(max_length=1, choices=OPC_BOOL)
    fecha_prot = models.DateTimeField(auto_now = True)
    usuario = models.CharField(max_length=12,null = True)
    canal = models.CharField(max_length=3, choices=OPC_CANALES)
    class Meta:
        unique_together = [['docto_conta','numero']]
        db_table = 'hecho_econo'

class PLAN_CTAS(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(CLIENTES, on_delete=models.CASCADE)
    per_con = models.IntegerField()
    cod_cta = models.CharField(max_length=10,null = True)
    nom_cta = models.CharField(max_length=48,null = True)
    auxiliar = models.CharField(max_length=1, choices=OPC_BOOL)
    dinamica = models.TextField()
    naturaleza = models.CharField(max_length=1, choices=OPC_NAT)
    activa = models.CharField(max_length=1, choices=OPC_BOOL)
    por_tercero  = models.CharField(max_length=1, choices=OPC_BOOL)
    cta_act_fij  = models.CharField(max_length=1, choices=OPC_BOOL)
    cta_pre  = models.CharField(max_length=1, choices=OPC_BOOL)
    cta_bal  = models.CharField(max_length=1, choices=OPC_BOOL)
    cta_res = models.CharField(max_length=1, choices=OPC_BOOL)
    cta_ord = models.CharField(max_length=1, choices=OPC_BOOL)
    cta_ban  = models.CharField(max_length=1, choices=OPC_BOOL)
    cta_gan_per = models.CharField(max_length=1, choices=OPC_BOOL)
    cta_per_gan = models.CharField(max_length=1, choices=OPC_BOOL)
    cta_dep  = models.CharField(max_length=1, choices=OPC_BOOL)
    cta_ing_ret = models.CharField(max_length=1, choices=OPC_BOOL)
    cta_ret_iva  = models.CharField(max_length=1, choices=OPC_BOOL)
    cta_rec  = models.CharField(max_length=1, choices=OPC_BOOL)
    class Meta:
        unique_together = [['cliente','per_con','cod_cta']]
        db_table = 'plan_ctas'

class CENTROCOSTOS(models.Model):
    id = models.SmallAutoField(primary_key=True)
    cliente = models.ForeignKey(CLIENTES, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=5,null = False)
    class Meta:
        unique_together = [['cliente','codigo']]
        db_table = 'centro_costos'

class DETALLE_PROD(models.Model):
    id = models.BigAutoField(primary_key=True)
    hecho_econo = models.ForeignKey(HECHO_ECONO, on_delete=models.CASCADE)
    centro_costo = models.ForeignKey(CENTROCOSTOS, on_delete=models.CASCADE)
    producto = models.CharField(max_length=2, choices=OPC_PRODUCTO)
    subcuenta = models.CharField(max_length=12,null = True)
    concepto = models.CharField(max_length=8,null = True)
    valor = models.FloatField()
    usuario = models.CharField(max_length=12,null = True)
    fecha_creacion = models.DateTimeField(auto_now_add =True)
    fecha_actualizacion = models.DateTimeField(auto_now = True)
    class Meta:
        unique_together = [['hecho_econo','producto','subcuenta','concepto']]
        db_table = 'detalle_prod'
    
class DETALLE_ECONO(models.Model):
    id = models.BigAutoField(primary_key=True)
    hecho_econo = models.ForeignKey(HECHO_ECONO, on_delete=models.CASCADE)
    detalle_prod = models.ForeignKey(DETALLE_PROD, on_delete=models.CASCADE)
    cuenta = models.ForeignKey(PLAN_CTAS, on_delete=models.CASCADE)
    tercero = models.ForeignKey(TERCEROS, on_delete=models.CASCADE)
    item_concepto = models.CharField(max_length=6,null = True)
    detalle = models.TextField()
    debito = models.FloatField()
    credito = models.FloatField()
    class Meta:
        unique_together = [['hecho_econo','cuenta','tercero']]
        db_table = 'detalle_econo'

class DET_ECO_RET(models.Model):
    id = models.BigAutoField(primary_key=True)
    detalle_econo = models.ForeignKey(DETALLE_ECONO, on_delete=models.CASCADE)
    tip_ret = models.TextField()
    valor_base = models.FloatField()
    porcentaje = models.FloatField()
    class Meta:
        db_table = 'det_eco_ret'

class IMP_CON_LIN_AHO(models.Model):
    id = models.AutoField(primary_key=True)
    oficina = models.ForeignKey(OFICINAS, on_delete=models.CASCADE)
    cod_imp = models.CharField(max_length=2,null = True)
    cta_aho_act = models.CharField(max_length=10,null = True)
    cta_aho_ina = models.CharField(max_length=10,null = True)
    cta_ret_fue= models.CharField(max_length=10,null = True)
    class Meta:
        unique_together = [['oficina','cod_imp']]
        db_table = 'imp_con_lin_aho'

class LINEAS_AHORRO(models.Model):
    id = models.SmallAutoField(primary_key=True)
    oficina = models.ForeignKey(OFICINAS, on_delete=models.CASCADE)
    imp_con = models.ForeignKey(IMP_CON_LIN_AHO, on_delete=models.CASCADE)
    cod_lin_aho = models.CharField(max_length=2,null = True)
    termino = models.CharField(max_length=1, choices=OPC_TERMINO)
    per_liq_int = models.CharField(max_length=1, choices=OPC_PER_LIQ_INT)
    cta_por_pas = models.CharField(max_length=10,null = True)
    fec_ult_liq_int = models.DateField()
    saldo_minimo = models.FloatField()
    cod_lin_aho = models.CharField(max_length=2, choices=OPC_PRODUCTO)
    termino = models.CharField(max_length=1, choices=OPC_TERMINO)
    per_liq_int = models.CharField(max_length=1, choices=OPC_PER_LIQ_INT)
    cta_por_pas = models.CharField(max_length=10,null = True)
    fec_ult_liq_int = models.DateField()
    saldo_minimo = models.FloatField()
    class Meta:
        unique_together = [['oficina','cod_lin_aho']]
        db_table = 'lineas_ahorro'


class TAS_LIN_AHO(models.Model):
    id = models.AutoField(primary_key=True)
    lin_aho = models.ForeignKey(LINEAS_AHORRO, on_delete=models.CASCADE)
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()
    tiae = models.FloatField()
    class Meta:
        unique_together = [['lin_aho','fecha_inicial']]
        db_table = 'tas_lin_aho'


class CTAS_AHORRO(models.Model):
    id = models.AutoField(primary_key=True)
    oficina = models.ForeignKey(OFICINAS, on_delete=models.CASCADE)
    lin_aho = models.ForeignKey(LINEAS_AHORRO, on_delete=models.CASCADE)
    asociado = models.ForeignKey(ASOCIADOS, on_delete=models.CASCADE)
    num_cta = models.CharField(max_length=10,null = True)
    est_cta = models.CharField(max_length=1, choices=OPC_EST_CTA_AHO)
    fec_apertura = models.DateField()
    fec_cancela = models.DateField()
    exc_tas_mil = models.CharField(max_length=1, choices=OPC_BOOL)
    fec_ini_exc = models.DateField()
    class Meta:
        unique_together = [['oficina','num_cta']]
        db_table = 'ctas_ahorro'
     
class CTA_CDAT_AMP(models.Model):
    id = models.BigAutoField(primary_key=True)
    cta_aho = models.ForeignKey(CTAS_AHORRO, on_delete=models.CASCADE)
    ampliacion = models.IntegerField() 
    valor = models.FloatField()
    fecha = models.DateField()
    plazo_mes = models.IntegerField() 
    tiae = models.FloatField()
    Periodicidad = models.IntegerField()
    cta_int_ret = models.CharField(max_length=10,null = True)
    aplicado = models.CharField(max_length=1, choices=OPC_BOOL)
    class Meta:
        unique_together = [['cta_aho','ampliacion']]
        db_table = 'cta_cdat_amp'

class CTA_CDAT_INT(models.Model):
    id = models.BigAutoField(primary_key=True)
    cta_aho = models.ForeignKey(CTAS_AHORRO, on_delete=models.CASCADE)
    cta_amp = models.ForeignKey(CTA_CDAT_AMP, on_delete=models.CASCADE)
    fecha = models.DateField()
    cta_int_ret = models.CharField(max_length=10,null = True)
    Valor_int = models.FloatField()
    Valor_ret = models.FloatField()
    aplicado = models.CharField(max_length=1, choices=OPC_BOOL)
    docto = models.ForeignKey(HECHO_ECONO, on_delete=models.CASCADE)
    class Meta:
        unique_together = [['cta_aho','cta_amp','fecha']]
        db_table = 'cta_cdat_int'

class CTA_CDAT_INT_LIQ(models.Model):
    id = models.BigAutoField(primary_key=True)
    cta_aho = models.ForeignKey(CTAS_AHORRO, on_delete=models.CASCADE)
    cta_amp = models.ForeignKey(CTA_CDAT_AMP, on_delete=models.CASCADE)
    fecha = models.DateField()
    tip_liq = models.CharField(max_length=1, choices=OPC_LIQ_INT_AHO)
    Val_int = models.FloatField()
    Val_ret = models.FloatField()
    Val_int_nue = models.FloatField()
    Val_ret_nue = models.FloatField()
    aplicado = models.CharField(max_length=1, choices=OPC_BOOL)
    docto = models.ForeignKey(HECHO_ECONO, on_delete=models.CASCADE)
    aplicado = models.CharField(max_length=1, choices=OPC_BOOL)
    class Meta:
        unique_together = [['cta_aho','cta_amp','fecha','tip_liq']]
        db_table = 'cta_cdat_int_liq'

class IMP_CON_CRE(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(CLIENTES, on_delete=models.CASCADE)
    cod_imp = models.CharField(max_length=2,null = True)
    kcta_pte = models.CharField(max_length=10,null = True)
    kcta_pro_gen_adi = models.CharField(max_length=10,null = True)
    kcta_pro_gen = models.CharField(max_length=10,null = True)
    kcta_gas_pro_gen = models.CharField(max_length=10,null = True)
    kcta_rec_pro_gen = models.CharField(max_length=10,null = True)
    kcta_gas_pro_ind = models.CharField(max_length=10,null = True)
    kcta_rec_pro_ind = models.CharField(max_length=10,null = True)
    icta_des_int_pp = models.CharField(max_length=10,null = True)
    class Meta:
        unique_together = [['cliente','cod_imp']]
        db_table = 'imp_con_cre'

class IMP_CON_CRE_INT(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(CLIENTES, on_delete=models.CASCADE)
    cod_imp = models.CharField(max_length=2,null = True)
    categoria = models.CharField(max_length=1, choices=OPC_CRE_CATEGORIA)
    kcta_con = models.CharField(max_length=10,null = True)
    kcta_pro_ind = models.CharField(max_length=10,null = True)
    kporcentaje = models.FloatField()
    icta_pte = models.CharField(max_length=10,null = True)
    icxca = models.CharField(max_length=10,null = True)
    icxcb = models.CharField(max_length=10,null = True)
    icxcc = models.CharField(max_length=10,null = True)
    icxcd = models.CharField(max_length=10,null = True)
    icxce = models.CharField(max_length=10,null = True)
    icxcf = models.CharField(max_length=10,null = True)
    orden_c = models.CharField(max_length=10,null = True)
    orden_d = models.CharField(max_length=10,null = True)
    orden_e = models.CharField(max_length=10,null = True)
    orden_f = models.CharField(max_length=10,null = True)
    cta_por_pag = models.CharField(max_length=10,null = True)
    cta_val = models.CharField(max_length=10,null = True)
    class Meta:
        unique_together = [['cliente','cod_imp','categoria']]
        db_table = 'imp_con_cre_int'

class CREDITOS_CAUSA(models.Model):
    id = models.BigAutoField(primary_key=True)
    oficina = models.ForeignKey(OFICINAS, on_delete=models.CASCADE,related_name='cre_ofi')
    com_des =  models.ForeignKey(HECHO_ECONO, on_delete=models.CASCADE,related_name='cre_des')
    cod_cre = models.CharField(max_length=10,null = True)
    com_ult_cau = models.ForeignKey(HECHO_ECONO, on_delete=models.CASCADE,related_name='cre_cau')
    fecha =  models.DateField()
    cuota = models.IntegerField()
    capital = models.FloatField()
    int_cor = models.FloatField()
    pol_seg = models.FloatField()
    class Meta:
        unique_together = [['oficina','com_des','cod_cre','com_ult_cau','fecha']]
        db_table = 'creditos_causa'


class CREDITOS(models.Model):
    id = models.BigAutoField(primary_key=True)
    oficina = models.ForeignKey(OFICINAS, on_delete=models.CASCADE)
    imputacion = models.ForeignKey(IMP_CON_CRE, on_delete=models.CASCADE)
    com_des = models.ForeignKey(HECHO_ECONO, on_delete=models.CASCADE)
    cod_cre = models.CharField(max_length=10,null = True)
    com_ult_cau = models.ForeignKey(CREDITOS_CAUSA, on_delete=models.CASCADE)
    libranza = models.CharField(max_length=10,null = True)
    pagare = models.CharField(max_length=10,null = True)
    termino = models.CharField(max_length=1, choices=OPC_CRE_TERMINO)
    for_pag = models.CharField(max_length=1, choices=OPC_CRE_FOR_PAG)
    fec_des = models.DateField()
    fec_pag_ini = models.DateField()
    fec_ree = models.DateField()
    fec_ven = models.DateField()
    val_cuo_ini = models.FloatField()
    val_cuo_act = models.FloatField()
    num_cuo_ini = models.IntegerField()
    num_cuo_act = models.IntegerField()
    num_cuo_gra = models.IntegerField()
    per_ano = models.IntegerField()
    tian_ic_ini = models.FloatField()
    tian_ic_act = models.FloatField()
    tian_im = models.FloatField()
    tian_pol_seg = models.FloatField()
    por_des_pro_pag = models.FloatField()
    decreciente = models.CharField(max_length=1, choices=OPC_BOOL)
    estado = models.CharField(max_length=1, choices=OPC_EST_CRE)
    est_jur = models.CharField(max_length=1, choices=OPC_CRE_EST_JUR)
    cat_nue = models.CharField(max_length=1, choices=OPC_CRE_CATEGORIA)
    rep_cen_rie = models.CharField(max_length=1, choices=OPC_BOOL)
    val_gar_hip = models.FloatField()
    mat_inm_gar = models.CharField(max_length=12,null = True)
    num_pol_gar_hip =  models.CharField(max_length=10,null = True)
    figarantias = models.CharField(max_length=1, choices=OPC_BOOL)
    class Meta:
        unique_together = [['oficina','com_des','cod_cre']]
        db_table = 'creditos'
