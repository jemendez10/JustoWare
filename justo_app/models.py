from django.db import models
import re
from django.core.exceptions import ValidationError

from django.core.exceptions import ValidationError
from django.db import models

class DefaultToZeroMixin(models.Model):
    def save(self, *args, **kwargs):
        for field in self._meta.fields:
            if (isinstance(field, models.IntegerField) or isinstance(field, models.FloatField)) and field.attname != 'id' :
                if getattr(self, field.name) is None or getattr(self, field.name) == '':
                    setattr(self, field.name, 0)

        super(DefaultToZeroMixin, self).save(*args, **kwargs)

    class Meta:
        abstract = True

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

OPC_EST_CIV  = (
        ('N', 'No Aplica'),
        ('S', 'Soltero'),
        ('C', 'Casado'),
        ('U', 'Union Libre'),
        ('V', 'Viudo'),
        ('E', 'Separado'),
        ('D', 'Divorciado'),
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
    ('6','PosGrado'),
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
    ('5','Nieto'),
    ('6','Tio'),
    ('7','Sobrino'),
    ('8','Primo'),
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
    nombre = models.CharField(max_length=36, null=False)
    cod_pos = models.CharField(max_length=12, null=True)
    departamento = models.CharField(max_length=36, null=True)
    class Meta:
        unique_together = [['cliente','codigo']]
        db_table = 'localidades'

class TERCEROS(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(CLIENTES, on_delete=models.CASCADE)
    cla_doc = models.CharField(max_length=1, choices=OPC_CLASEDOC)
    doc_ide = models.CharField(max_length=12,null = False)
    dig_ver = models.CharField(max_length=1,null = True)
    nit_rap = models.CharField(max_length=12,null = True)
    cod_ciu_exp  = models.ForeignKey(LOCALIDADES, on_delete=models.CASCADE, related_name='ciu_exp',null = True, blank=True)
    cod_ciu_res = models.ForeignKey(LOCALIDADES, on_delete=models.CASCADE, related_name='ciu_res',null = True, blank=True)
    regimen = models.CharField(max_length=12, choices=OPC_REGIMEN)
    fec_exp_ced = models.DateField(null = True,blank = True)
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
    nombre = models.CharField(max_length=68,blank=True, null=True)   
    fec_act = models.DateField(null=True,blank=True)
    observacion = models.CharField(max_length=68,null = True)  
    per_pub_exp = models.CharField(max_length=1, choices=OPC_BOOL)
    nit_interno = models.CharField(max_length=1, choices=OPC_BOOL)
    def save(self, *args, **kwargs):
        if self.tip_ter == "N":
            self.nombre = """%s %s %s %s"""%(self.pri_ape,self.seg_ape,self.pri_nom,self.seg_nom)
        else:
            self.nombre = self.raz_soc
        super().save(*args, **kwargs) 
    class Meta:
        unique_together = [['cliente','cla_doc','doc_ide']]
        db_table = 'terceros'

class estados_fin(DefaultToZeroMixin):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(CLIENTES, on_delete=models.CASCADE, null=False)
    tercero = models.OneToOneField(TERCEROS, on_delete=models.CASCADE, null=False)
    fec_inf = models.DateField(null=True,blank=True)
    ing_sal_fij = models.FloatField(blank=True, null=True)
    ing_hon = models.FloatField(blank=True, null=True)
    ing_pen = models.FloatField(blank=True, null=True)
    ing_arr = models.FloatField(blank=True, null=True)
    ing_com = models.FloatField(blank=True, null=True)
    ing_ext = models.FloatField(blank=True, null=True)
    ing_otr = models.CharField(max_length=1, choices=OPC_BOOL,null=True)
    ing_tot = models.FloatField(blank=True, null=True)
    egr_sec_fin = models.FloatField(blank=True, null=True)
    egr_cuo_hip = models.FloatField(blank=True, null=True)
    egr_des_nom = models.CharField(max_length=1, choices=OPC_BOOL,null=True)
    egr_gas_fam = models.FloatField(blank=True, null=True)
    egr_otr_cre = models.FloatField(blank=True, null=True)
    egr_arr = models.FloatField(blank=True, null=True)
    egr_otr_gas = models.FloatField(blank=True, null=True)
    egr_tot = models.FloatField(blank=True, null=True)
    act_otr_egr = models.FloatField(blank=True, null=True)
    act_tip_bien = models.CharField(max_length=20,null = True)  
    act_vei = models.FloatField(blank=True, null=True)
    act_otr = models.CharField(max_length=1, choices=OPC_BOOL,null=True)
    tot_act = models.FloatField(blank=True, null=True)
    act_fin_rai = models.FloatField(blank=True, null=True)
    act_inv = models.FloatField(blank=True, null=True)
    escritura = models.CharField(max_length=20,null = True)
    pas_otr = models.CharField(max_length=1, choices=OPC_BOOL,null=True)
    pas_tip = models.CharField(max_length=24,null = True)
    tot_pat = models.FloatField(blank=True, null=True)
    pas_val = models.FloatField(blank=True, null=True)
    tot_pas = models.FloatField(blank=True, null=True)
    pas_des = models.CharField(max_length=40,null = True)
    dec_ren = models.CharField(max_length=1, choices=OPC_BOOL)
    tip_pas = models.CharField(max_length=40,null = True)
    des_pas = models.CharField(max_length=40,null = True)
    val_pas = models.FloatField(blank=True, null=True)
    ope_mon_ext = models.CharField(max_length=1, choices=OPC_BOOL)
    nom_ban_ext = models.CharField(max_length=40,null = True)
    ope_pais_ext = models.CharField(max_length=1, choices=OPC_BOOL)
    ope_monto_ext = models.CharField(max_length=1, choices=OPC_BOOL)
    num_cta_ext = models.CharField(max_length=20,null = True)
    tip_ope_ext = models.CharField(max_length=20,null = True)
    mon_ope_ext = models.CharField(max_length=1, choices=OPC_BOOL)
    prod_mon_ext = models.CharField(max_length=1, choices=OPC_BOOL)
    des_prod_ext = models.CharField(max_length=40,null = True)
    mon_prod_ext = models.CharField(max_length=20,null = True)
    pais_prod_ext = models.CharField(max_length=20,null = True)
    ciu_prod_ext = models.CharField(max_length=20,null = True)
    prom_prod_ext = models.FloatField(blank=True, null=True)
    class Meta:
        unique_together = [['cliente','tercero']]
        db_table = 'estados_fin'

class pagadores(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40,null = False)

class ASOCIADOS(DefaultToZeroMixin):
    id = models.AutoField(primary_key=True)
    cod_aso = models.CharField(max_length=12,null = False) 
    oficina = models.OneToOneField(OFICINAS, on_delete=models.CASCADE, null=True)
    tercero = models.OneToOneField(TERCEROS, on_delete=models.CASCADE, null=True)
    sexo = models.CharField(max_length=1,null = True,blank = True)
    est_civ = models.CharField(max_length=1, choices=OPC_EST_CIV)
    fec_nac = models.DateField(null = True,blank = True)
    ciu_res = models.CharField(max_length=48,null = True,blank = True)
    zona  = models.CharField(max_length=16,null = True,blank = True)
    profesion = models.CharField(max_length=48,null = True,blank = True)
    ocupacion = models.CharField(max_length=40,null = True,blank = True)
    ocupacion_cod = models.CharField(max_length=3,null = True,blank = True)
    estrato = models.CharField(max_length=1,null = True,blank = True)
    niv_est  = models.CharField(max_length=1, choices=OPC_EDUCACION)
    cab_fam = models.CharField(max_length=1, choices=OPC_BOOL)
    id_pag = models.ForeignKey(pagadores, on_delete=models.CASCADE, null=True)
    fec_afi = models.DateField(null = True,blank = True)
    cargo_emp = models.CharField(max_length=36,null = True)
    per_a_cargo = models.IntegerField(null = True,blank = True)
    num_hij_men = models.IntegerField(blank=True, null=True)
    num_hij_may = models.IntegerField(blank=True, null=True)
    tip_viv = models.CharField(max_length=24,null = True)  
    tie_en_ciu = models.IntegerField(blank=True, null=True)
    med_con = models.CharField(max_length=48,null = True)  
    fec_ing_tra = models.DateField(null=True,blank=True)
    tel_tra = models.CharField(max_length=10,null = True)  
    tip_sal= models.CharField(max_length=18,null = True)  
    ciu_tra = models.CharField(max_length=30,null = True)  
    act_eco = models.CharField(max_length=24,null = True)  
    cod_ciiu = models.CharField(max_length=12,null = True) 
    tip_con = models.CharField(max_length=18,null = True)  
    nom_emp = models.CharField(max_length=40,null = True)  
    nit_emp = models.CharField(max_length=12,null = True)  
    dir_emp = models.CharField(max_length=50,null = True)  
    email_emp = models.EmailField(blank=True, null=True)
    sector_emp = models.CharField(max_length=12,null = True)  
    empresa_ant = models.IntegerField(blank=True, null=True)  
    emp_num_emp = models.IntegerField(blank=True, null=True)
    negocio_pro = models.CharField(max_length=1, choices=OPC_BOOL)
    negocio_nom = models.CharField(max_length=48,null = True)  
    negocio_tel = models.CharField(max_length=10,null = True)  
    negocio_loc_pro = models.CharField(max_length=1, choices=OPC_BOOL)
    negocio_cam_com = models.CharField(max_length=1, choices=OPC_BOOL)
    negocio_ant = models.IntegerField(blank=True, null=True)
    pension_ent = models.CharField(max_length=36,null = True)  
    pension_tie = models.IntegerField(blank=True, null=True)
    pension_otr = models.CharField(max_length=1, choices=OPC_BOOL)
    pension_ent_otr = models.CharField(max_length=36,null = True)  
    pep_es_fam = models.CharField(max_length=1, choices=OPC_BOOL)
    pep_fam_par = models.CharField(max_length=1, choices=OPC_PARENTESCO)  
    pep_fam_nom = models.CharField(max_length=36,null = True)  
    pep_car_pub = models.CharField(max_length=1, choices=OPC_BOOL)
    pep_cargo = models.CharField(max_length=36,null = True)  
    pep_eje_pod = models.CharField(max_length=1, choices=OPC_BOOL)
    pep_adm_rec_est = models.CharField(max_length=1, choices=OPC_BOOL)
    tie_gre_car = models.CharField(max_length=1, choices=OPC_BOOL)
    recibe_pag_ext = models.CharField(max_length=1, choices=OPC_BOOL)
    recide_ext_mas_186 = models.CharField(max_length=1, choices=OPC_BOOL)
    recibe_ing_ext = models.CharField(max_length=1, choices=OPC_BOOL)
    class Meta:
        unique_together = [['oficina','cod_aso']]
        db_table = 'asociados'

class ASO_BENEF(models.Model):
    id = models.AutoField(primary_key=True)
    asociado = models.ForeignKey(ASOCIADOS, on_delete=models.CASCADE)
    cla_doc = models.CharField(max_length=1, choices=OPC_CLASEDOC)
    doc_ide  = models.CharField(max_length=12,null = False)
    nombre = models.CharField(max_length=64,null = False)
    parentesco = models.CharField(max_length=1, choices=OPC_PARENTESCO) 
    porcentaje = models.FloatField(blank=True, null=True)
    class Meta:
        unique_together = [['asociado','doc_ide']]
        db_table = 'aso_banef'

class ASO_REF_FAM(models.Model):
    id = models.AutoField(primary_key=True)
    asociado = models.ForeignKey(ASOCIADOS, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=64,null = False)
    ocupacion = models.CharField(max_length=30,null = True)
    direccion = models.CharField(max_length=50,null = True)
    parentesco = models.CharField(max_length=1, choices=OPC_PARENTESCO) 
    telefono = models.CharField(max_length=10,null = False)
    class Meta:
        unique_together = [['asociado','nombre']]
        db_table = 'aso_ref_fam'

class ASO_REF_PER(models.Model):
    id = models.AutoField(primary_key=True)
    asociado = models.ForeignKey(ASOCIADOS, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=64,null = False)
    ocupacion = models.CharField(max_length=32,null = False)
    direccion = models.CharField(max_length=64,null = False)
    celular = models.CharField(max_length=10,null = False)
    telefono = models.CharField(max_length=10,null = False)
    class Meta:
        unique_together = [['asociado','nombre']]
        db_table = 'aso_ref_per'

class ORIGINACION(models.Model):
    asociado = models.ForeignKey(ASOCIADOS, on_delete=models.CASCADE)
    lin_cre = models.CharField(max_length=30,null = False)
    monto = models.FloatField(blank=True, null=True)
    plazo = models.IntegerField(blank=True, null=True)
    gar_cre_sol = models.CharField(max_length=1,null = False)
    lin_cre_sol = models.CharField(max_length=1,null = False)
    mod_cre_sol = models.CharField(max_length=1,null = False)
    class Meta:
        unique_together = [['asociado']]
        db_table = 'originacion'

class DOCTO_CONTA(models.Model):
    id = models.AutoField(primary_key=True)
    oficina = models.ForeignKey(OFICINAS, on_delete=models.CASCADE)
    per_con = models.IntegerField(blank=True, null=True)
    nom_cto = models.CharField(max_length=8,null = False)
    nombre = models.CharField(max_length=24,null = False)
    inicio_nuevo_per = models.CharField(max_length=1, choices=OPC_BOOL)
    consecutivo = models.IntegerField(blank=True, null=True)
    class Meta:
        unique_together = [['oficina','per_con','nom_cto']]
        db_table = 'docto_conta'

class HECHO_ECONO(models.Model):
    id = models.BigAutoField(primary_key=True)
    docto_conta = models.ForeignKey(DOCTO_CONTA, on_delete=models.CASCADE)
    numero = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(null=True,blank=True)
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
    per_con = models.IntegerField(blank=True, null=True)
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
    fec_ult_liq_int = models.DateField(null=True,blank=True)
    saldo_minimo = models.FloatField()
    cod_lin_aho = models.CharField(max_length=2, choices=OPC_PRODUCTO)
    termino = models.CharField(max_length=1, choices=OPC_TERMINO)
    per_liq_int = models.CharField(max_length=1, choices=OPC_PER_LIQ_INT)
    cta_por_pas = models.CharField(max_length=10,null = True)
    fec_ult_liq_int = models.DateField(null=True,blank=True)
    saldo_minimo = models.FloatField()
    class Meta:
        unique_together = [['oficina','cod_lin_aho']]
        db_table = 'lineas_ahorro'

class TAS_LIN_AHO(models.Model):
    id = models.AutoField(primary_key=True)
    lin_aho = models.ForeignKey(LINEAS_AHORRO, on_delete=models.CASCADE)
    fecha_inicial = models.DateField(null=True,blank=True)
    fecha_final = models.DateField(null=True,blank=True)
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
    fec_apertura = models.DateField(null=True,blank=True)
    fec_cancela = models.DateField(null=True,blank=True)
    exc_tas_mil = models.CharField(max_length=1, choices=OPC_BOOL)
    fec_ini_exc = models.DateField(null=True,blank=True)
    class Meta:
        unique_together = [['oficina','num_cta']]
        db_table = 'ctas_ahorro'
     
class CTA_CDAT_AMP(models.Model):
    id = models.BigAutoField(primary_key=True)
    cta_aho = models.ForeignKey(CTAS_AHORRO, on_delete=models.CASCADE)
    ampliacion = models.IntegerField() 
    valor = models.FloatField()
    fecha = models.DateField(null=True,blank=True)
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
    fecha = models.DateField(null=True,blank=True)
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
    fecha = models.DateField(null=True,blank=True)
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
    fecha =  models.DateField(null=True,blank=True)
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
    por_pag = models.CharField(max_length=1, choices=OPC_CRE_FOR_PAG)
    fec_des = models.DateField(null=True,blank=True)
    fec_pag_ini = models.DateField(null=True,blank=True)
    fec_ree = models.DateField(null=True,blank=True)
    fec_ven = models.DateField(null=True,blank=True)
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
