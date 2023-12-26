# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Activosfijos(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    id_age = models.IntegerField()
    codigo = models.CharField(max_length=16)
    descripcion = models.CharField(max_length=128, blank=True, null=True)
    fec_alt = models.DateField(blank=True, null=True)
    id_com_ite = models.BigIntegerField(blank=True, null=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    mes_dep = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    val_sal = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    depacuvigant = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    detacuvigant = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    valacuvigant = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    id_ctadep = models.ForeignKey('Cuentas', models.DO_NOTHING, db_column='id_ctadep', blank=True, null=True)
    id_ctadepgas = models.ForeignKey('Cuentas', models.DO_NOTHING, db_column='id_ctadepgas', blank=True, null=True)
    id_ctadet = models.BigIntegerField(blank=True, null=True)
    id_ctadetgas = models.BigIntegerField(blank=True, null=True)
    de_baja = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'activosfijos'
        unique_together = (('id_age', 'codigo'),)


class AdmItem(models.Model):
    id = models.BigIntegerField(primary_key=True)
    id_com = models.ForeignKey('Comprobantes', models.DO_NOTHING, db_column='id_com')
    cod_con = models.CharField(max_length=6)
    subcuenta = models.CharField(max_length=12)
    val_deb = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    val_cre = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    borrar = models.CharField(max_length=1, blank=True, null=True)
    val_bas = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    por_bas = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adm_item'
        unique_together = (('id_com', 'cod_con', 'subcuenta'),)


class Agencias(models.Model):
    id_cl = models.ForeignKey('Clientes', models.DO_NOTHING, db_column='id_cl')
    id = models.IntegerField(primary_key=True)  # AutoField?
    cod_age = models.CharField(max_length=5)
    nombre = models.CharField(max_length=32, blank=True, null=True)
    nit_ger = models.CharField(max_length=12, blank=True, null=True)
    nom_ger = models.CharField(max_length=64, blank=True, null=True)
    co_ciu_loc = models.CharField(max_length=8, blank=True, null=True)
    direccion = models.CharField(max_length=128, blank=True, null=True)
    telefono = models.CharField(max_length=12, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agencias'
        unique_together = (('id_cl', 'cod_age'),)


class Aportes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    id_age = models.ForeignKey('Socios', models.DO_NOTHING, db_column='id_age')
    id_com = models.ForeignKey('Comprobantes', models.DO_NOTHING, db_column='id_com')
    codsoc = models.ForeignKey('Socios', models.DO_NOTHING, db_column='codsoc')
    fecha = models.DateField(blank=True, null=True)
    ll_tip_apo = models.CharField(max_length=2, blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    validado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aportes'
        unique_together = (('id_age', 'id_com', 'codsoc', 'll_tip_apo'),)


class Autorizados(models.Model):
    id_cl = models.IntegerField()
    id = models.IntegerField(primary_key=True)  # AutoField?
    cuenta = models.CharField(max_length=20)
    nombre = models.CharField(max_length=32)
    cargo = models.CharField(max_length=32, blank=True, null=True)
    tipo = models.CharField(max_length=1)
    clave = models.CharField(max_length=20, blank=True, null=True)
    fec_ing = models.DateTimeField(blank=True, null=True)
    activo = models.CharField(max_length=1)
    cod_suc = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'autorizados'
        unique_together = (('id_cl', 'cuenta'),)


class Avances(models.Model):
    id_age = models.ForeignKey('Creditos', models.DO_NOTHING, db_column='id_age')
    id = models.BigIntegerField(primary_key=True)
    id_com_ava = models.BigIntegerField()
    cod_cre = models.ForeignKey('Creditos', models.DO_NOTHING, db_column='cod_cre')
    fecha = models.DateField()
    val_cuo = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    val_ava = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    num_cuo = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    titdn = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    ticdn = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    timdn = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    scapital = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    sint_cor = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    sint_mor = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    spol_seg = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    fec_ult_pag = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'avances'
        unique_together = (('id_age', 'id_com_ava', 'cod_cre'),)


class Botones(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    id_for = models.ForeignKey('Formularios', models.DO_NOTHING, db_column='id_for')
    orden = models.SmallIntegerField()
    boton = models.CharField(max_length=16, blank=True, null=True)
    descripcion = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'botones'


class Cajeros(models.Model):
    id_cl = models.IntegerField()
    id = models.IntegerField(primary_key=True)  # AutoField?
    cuenta = models.CharField(max_length=20, blank=True, null=True)
    cod_caj = models.CharField(max_length=2)
    id_us = models.ForeignKey(Autorizados, models.DO_NOTHING, db_column='id_us')
    nit = models.CharField(max_length=12, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    sal_cap = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    codcta = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'cajeros'


class CarteCau(models.Model):
    id_age = models.ForeignKey('Creditos', models.DO_NOTHING, db_column='id_age')
    id = models.BigIntegerField(primary_key=True)
    id_com = models.ForeignKey('Comprobantes', models.DO_NOTHING, db_column='id_com')
    cod_cre = models.ForeignKey('Creditos', models.DO_NOTHING, db_column='cod_cre')
    cuota = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    capital = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    int_cor = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carte_cau'
        unique_together = (('id_age', 'id_com', 'cod_cre', 'cuota'),)


class CarteCauHis(models.Model):
    id_age = models.ForeignKey(Agencias, models.DO_NOTHING, db_column='id_age')
    id = models.BigIntegerField(primary_key=True)
    id_com = models.ForeignKey('Comprobantes', models.DO_NOTHING, db_column='id_com')
    id_com_mov = models.ForeignKey('Comprobantes', models.DO_NOTHING, db_column='id_com_mov')
    cod_cre = models.CharField(max_length=12)
    cuota = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    capital = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    int_cor = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carte_cau_his'
        unique_together = (('id_age', 'id_com', 'id_com_mov', 'cod_cre', 'cuota'),)


class CartePag(models.Model):
    id_age = models.ForeignKey('Creditos', models.DO_NOTHING, db_column='id_age')
    id = models.BigIntegerField(primary_key=True)
    id_com = models.BigIntegerField()
    cod_cre = models.ForeignKey('Creditos', models.DO_NOTHING, db_column='cod_cre')
    id_com_mov = models.BigIntegerField(blank=True, null=True)
    tip_pag = models.CharField(max_length=1, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    capital = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    int_cor = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    int_mor = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    pol_seg = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    acreedor = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    ic_cau_fra = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    ic_des_pp = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    ic_ajuste = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    im_cau = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    im_descto = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    ps_cau = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carte_pag'
        unique_together = (('id_age', 'id_com', 'cod_cre', 'id_com_mov', 'tip_pag'),)


class CatDesCre(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    id_des_cre = models.ForeignKey('DestinoCre', models.DO_NOTHING, db_column='id_des_cre')
    cod_cat = models.CharField(max_length=2)
    dia_min = models.DecimalField(max_digits=9, decimal_places=0, blank=True, null=True)
    dia_max = models.DecimalField(max_digits=9, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_des_cre'
        unique_together = (('id_des_cre', 'cod_cat'),)


class Categorias(models.Model):
    id_cl = models.IntegerField()
    id = models.IntegerField(primary_key=True)  # AutoField?
    cod_cat = models.CharField(max_length=2)
    descripcion = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'categorias'


class Centrocostos(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    id_age = models.ForeignKey(Agencias, models.DO_NOTHING, db_column='id_age', blank=True, null=True)
    codcencos = models.CharField(max_length=5, blank=True, null=True)
    nombre = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'centrocostos'
        unique_together = (('id_age', 'codcencos'),)


class Cierremes(models.Model):
    id_cl = models.IntegerField()
    id = models.IntegerField(primary_key=True)  # AutoField?
    cod_age = models.CharField(max_length=5)
    per_con = models.DecimalField(max_digits=4, decimal_places=0)
    mes = models.CharField(max_length=2)
    cerrado = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cierremes'


class Ciiu(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    codigo = models.CharField(max_length=8)
    actividad = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ciiu'


class Clientes(models.Model):
    id_cl = models.IntegerField(primary_key=True)
    sigla = models.CharField(unique=True, max_length=32, blank=True, null=True)
    nombre = models.CharField(max_length=128, blank=True, null=True)
    nit = models.CharField(max_length=12, blank=True, null=True)
    dv = models.CharField(max_length=1, blank=True, null=True)
    direccion = models.CharField(max_length=128, blank=True, null=True)
    telefono = models.CharField(max_length=12, blank=True, null=True)
    celular = models.CharField(max_length=12, blank=True, null=True)
    nit_ger = models.CharField(max_length=12, blank=True, null=True)
    nom_ger = models.CharField(max_length=64, blank=True, null=True)
    nit_con = models.CharField(max_length=12, blank=True, null=True)
    nom_con = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    dominio = models.CharField(max_length=128, blank=True, null=True)
    age_ret = models.CharField(max_length=1)
    ret_iva = models.CharField(max_length=1)
    aut_ret = models.CharField(max_length=1)
    mascara = models.CharField(max_length=32, blank=True, null=True)
    com_dep = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    nit_rev_fis = models.CharField(max_length=12, blank=True, null=True)
    nom_rev_fis = models.CharField(max_length=64, blank=True, null=True)
    tp_con = models.CharField(max_length=16, blank=True, null=True)
    tp_rev_fis = models.CharField(max_length=16, blank=True, null=True)
    id_loc = models.IntegerField(blank=True, null=True)
    ciudad = models.CharField(max_length=32, blank=True, null=True)
    logo = models.TextField(blank=True, null=True)
    licencia = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes'


class Codeudores(models.Model):
    id = models.BigIntegerField(primary_key=True)
    id_cre = models.ForeignKey('Creditos', models.DO_NOTHING, db_column='id_cre')
    id_ter = models.ForeignKey('Terceros', models.DO_NOTHING, db_column='id_ter')

    class Meta:
        managed = False
        db_table = 'codeudores'
        unique_together = (('id_cre', 'id_ter'),)


class Comprobantes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    id_doc = models.ForeignKey('Documentos', models.DO_NOTHING, db_column='id_doc')
    numero = models.DecimalField(max_digits=9, decimal_places=0)
    fecha = models.DateField()
    ll_tip_doc = models.CharField(max_length=2, blank=True, null=True)
    concepto = models.CharField(max_length=255)
    protegido = models.CharField(max_length=1)
    anulado = models.CharField(max_length=1)
    balance = models.CharField(max_length=1, blank=True, null=True)
    val_caj = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    banco = models.CharField(max_length=10)
    cheque = models.CharField(max_length=12, blank=True, null=True)
    nit_ben = models.CharField(max_length=12, blank=True, null=True)
    fec_gra = models.DateField(blank=True, null=True)
    cuenta = models.CharField(max_length=20, blank=True, null=True)
    ll_fuente = models.CharField(max_length=2, blank=True, null=True)
    ll_jornada = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comprobantes'
        unique_together = (('id_doc', 'numero'),)


class Conceptos(models.Model):
    id_cl = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_cl')
    id = models.IntegerField(primary_key=True)  # AutoField?
    cod_con = models.CharField(max_length=6, blank=True, null=True)
    descripcion = models.CharField(max_length=64)
    ll_clase = models.CharField(max_length=2, blank=True, null=True)
    ll_tip_apo = models.CharField(max_length=2, blank=True, null=True)
    con_deb = models.CharField(max_length=1, blank=True, null=True)
    con_cre = models.CharField(max_length=1, blank=True, null=True)
    cta_con = models.CharField(max_length=10, blank=True, null=True)
    cta_pas = models.CharField(max_length=10)
    cta_nii = models.CharField(max_length=10)
    cta_pas_nii = models.CharField(max_length=10)
    com_por_ter = models.CharField(max_length=1, blank=True, null=True)
    ret_fue = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conceptos'


class CreditoHis(models.Model):
    id = models.BigIntegerField(primary_key=True)
    id_cod_cre = models.ForeignKey('Creditos', models.DO_NOTHING, db_column='id_cod_cre')
    cod_nov = models.CharField(max_length=1)
    fecha = models.DateField(blank=True, null=True)
    ant_val_tas = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    ant_valor = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'credito_his'
        unique_together = (('id_cod_cre', 'fecha', 'cod_nov'),)


class Creditos(models.Model):
    id_age = models.ForeignKey('Socios', models.DO_NOTHING, db_column='id_age')
    id = models.BigIntegerField(primary_key=True)
    cod_cre = models.CharField(max_length=12)
    id_com = models.BigIntegerField(blank=True, null=True)
    codsoc = models.ForeignKey('Socios', models.DO_NOTHING, db_column='codsoc', blank=True, null=True)
    ll_for_pag = models.CharField(max_length=2, blank=True, null=True)
    id_imp = models.ForeignKey('ImpConCre', models.DO_NOTHING, db_column='id_imp', blank=True, null=True)
    id_lc = models.ForeignKey('LineaCre', models.DO_NOTHING, db_column='id_lc', blank=True, null=True)
    id_dc = models.ForeignKey('DestinoCre', models.DO_NOTHING, db_column='id_dc', blank=True, null=True)
    libranza = models.CharField(max_length=12, blank=True, null=True)
    ll_garanti = models.CharField(max_length=2, blank=True, null=True)
    pagare = models.CharField(max_length=12, blank=True, null=True)
    ll_termino = models.CharField(max_length=2, blank=True, null=True)
    fec_des = models.DateField(blank=True, null=True)
    fec_pag_ini = models.DateField(blank=True, null=True)
    fec_ult_pag = models.DateField(blank=True, null=True)
    cap_ini = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    ll_per_ano = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    num_cuo = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    num_cuo_gra = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    tian_ic = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    tian_im = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    por_pol = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    val_cuo = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    por_pro_pag = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    con_dia_mor = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    decreciente = models.CharField(max_length=1, blank=True, null=True)
    reestructura = models.CharField(max_length=1, blank=True, null=True)
    cod_cre_res = models.CharField(max_length=12, blank=True, null=True)
    nue_cat = models.CharField(max_length=1, blank=True, null=True)
    rep_cen_rie = models.CharField(max_length=1, blank=True, null=True)
    ll_estado = models.CharField(max_length=2, blank=True, null=True)
    ll_est_jur = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'creditos'
        unique_together = (('id_age', 'cod_cre'),)


class Ct(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    id_age = models.IntegerField(blank=True, null=True)
    cod_cre = models.IntegerField(blank=True, null=True)
    capaoct = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    salcapoct = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    salintcoroct = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    diamoroct = models.IntegerField(blank=True, null=True)
    intmoroct = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    salpoloct = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    diames = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ct'


class Ctasporter(models.Model):
    id_cl = models.IntegerField()
    id = models.BigIntegerField(primary_key=True)
    tip_con = models.SmallIntegerField()
    id_cta = models.BigIntegerField()
    id_ter = models.BigIntegerField()
    per_con = models.DecimalField(max_digits=4, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'ctasporter'
        unique_together = (('id_cl', 'per_con', 'id_cta', 'id_ter'),)


class Cuentas(models.Model):
    id_cl = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_cl')
    id = models.BigIntegerField(primary_key=True)
    per_con = models.DecimalField(max_digits=4, decimal_places=0)
    tip_con = models.SmallIntegerField()
    cod_cta = models.CharField(max_length=10)
    nombre = models.CharField(max_length=128, blank=True, null=True)
    tip_cta = models.CharField(max_length=1)
    dinamica = models.CharField(max_length=255, blank=True, null=True)
    naturaleza = models.CharField(max_length=1, blank=True, null=True)
    activa = models.CharField(max_length=1)
    por_ter = models.CharField(max_length=1)
    cta_act_fij = models.CharField(max_length=1)
    cta_pre = models.CharField(max_length=1)
    cta_bal = models.CharField(max_length=1)
    cta_res = models.CharField(max_length=1)
    cta_ord = models.CharField(max_length=1)
    cta_ban = models.CharField(max_length=1)
    cta_ganper = models.CharField(max_length=1)
    cta_pergan = models.CharField(max_length=1)
    cta_dep = models.CharField(max_length=1)
    cta_ingret = models.CharField(max_length=1)
    cta_retiva = models.CharField(max_length=1)
    cta_rec = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cuentas'
        unique_together = (('id_cl', 'tip_con', 'per_con', 'cod_cta'),)


class Derechos(models.Model):
    id_cl = models.IntegerField()
    id = models.IntegerField(primary_key=True)  # AutoField?
    id_au = models.ForeignKey(Autorizados, models.DO_NOTHING, db_column='id_au')
    id_bt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'derechos'
        unique_together = (('id_au', 'id_bt', 'id_cl'),)


class DestinoCre(models.Model):
    id_cl = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_cl')
    id = models.IntegerField(primary_key=True)  # AutoField?
    cod_des_cre = models.CharField(max_length=2)
    descripcion = models.CharField(max_length=32, blank=True, null=True)
    codigo = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'destino_cre'
        unique_together = (('id_cl', 'cod_des_cre'),)


class DetallesCom(models.Model):
    id = models.BigIntegerField(primary_key=True)
    id_com = models.ForeignKey(Comprobantes, models.DO_NOTHING, db_column='id_com')
    id_cta = models.BigIntegerField()
    id_ter = models.ForeignKey('Terceros', models.DO_NOTHING, db_column='id_ter')
    id_cencos = models.ForeignKey(Centrocostos, models.DO_NOTHING, db_column='id_cencos')
    detalle = models.CharField(max_length=128)
    referencia = models.CharField(max_length=12, blank=True, null=True)
    val_bas = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    debito = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    credito = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    id_dc = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'detalles_com'


class Documentos(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    id_age = models.ForeignKey(Agencias, models.DO_NOTHING, db_column='id_age')
    per_con = models.DecimalField(max_digits=4, decimal_places=0)
    cod_doc = models.DecimalField(max_digits=8, decimal_places=0)
    consecutivo = models.DecimalField(max_digits=9, decimal_places=0, blank=True, null=True)
    nombre = models.CharField(max_length=32)
    ini_nue_vig = models.CharField(max_length=1)
    doc_adm = models.CharField(max_length=1, blank=True, null=True)
    nom_cto = models.CharField(max_length=8, blank=True, null=True)
    de_caja = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documentos'
        unique_together = (('id_age', 'per_con', 'cod_doc'),)


class Entidades(models.Model):
    id_cl = models.ForeignKey('Terceros', models.DO_NOTHING, db_column='id_cl')
    id = models.IntegerField(primary_key=True)  # AutoField?
    cod_ent = models.CharField(max_length=4)
    nit_pro = models.ForeignKey('Terceros', models.DO_NOTHING, db_column='nit_pro', blank=True, null=True)
    nombre = models.CharField(max_length=32, blank=True, null=True)
    nom_pag = models.CharField(max_length=64, blank=True, null=True)
    celular = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entidades'
        unique_together = (('id_cl', 'cod_ent'),)


class Equivalencia(models.Model):
    id_cl = models.IntegerField()
    id = models.IntegerField(primary_key=True)  # AutoField?
    id_us = models.ForeignKey(Autorizados, models.DO_NOTHING, db_column='id_us')
    id_gr = models.ForeignKey(Autorizados, models.DO_NOTHING, db_column='id_gr')

    class Meta:
        managed = False
        db_table = 'equivalencia'
        unique_together = (('id_cl', 'id_us', 'id_gr'),)


class EstFin(models.Model):
    id_nit = models.ForeignKey('Terceros', models.DO_NOTHING, db_column='id_nit')
    id = models.IntegerField(primary_key=True)  # AutoField?
    fec_mod = models.DateField(blank=True, null=True)
    ing_sal_fij = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    ing_ext = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    ing_pen = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    ing_hon = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    ing_ser = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    ing_com = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    ing_arr = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    ing_otr = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    tot_ing = models.BigIntegerField(blank=True, null=True)
    egr_gas_fam = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    egr_arr = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    egr_cuo_hip = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    egr_sec_fin = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    egr_otr_cre = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    egr_des_nom = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    egr_otr_gas = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    tot_egr = models.BigIntegerField(blank=True, null=True)
    act_fin_rai = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    act_vei = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    act_otr = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    tot_act = models.BigIntegerField(blank=True, null=True)
    pas_fin = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    pas_otr = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    tot_pas = models.BigIntegerField(blank=True, null=True)
    ref_com = models.CharField(max_length=32, blank=True, null=True)
    ref_com_cel = models.CharField(max_length=12, blank=True, null=True)
    ref_com_tel = models.CharField(max_length=32, blank=True, null=True)
    ref_ban = models.CharField(max_length=32, blank=True, null=True)
    ref_ban_cel = models.CharField(max_length=12, blank=True, null=True)
    ref_ban_tel = models.CharField(max_length=32, blank=True, null=True)
    ref_per = models.CharField(max_length=32, blank=True, null=True)
    ref_per_cel = models.CharField(max_length=12, blank=True, null=True)
    ref_per_tel = models.CharField(max_length=32, blank=True, null=True)
    dec_ren = models.CharField(max_length=1, blank=True, null=True)
    tie_cas = models.CharField(max_length=1, blank=True, null=True)
    escritura = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'est_fin'


class ExoCuentas(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    id_con = models.ForeignKey('Exoconceptos', models.DO_NOTHING, db_column='id_con', blank=True, null=True)
    codcta = models.CharField(max_length=10)
    num_val_inf = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'exo_cuentas'
        unique_together = (('id_con', 'codcta'),)


class Exoconceptos(models.Model):
    id_cl = models.IntegerField()
    id = models.IntegerField(primary_key=True)  # AutoField?
    id_for = models.ForeignKey('Exoformatos', models.DO_NOTHING, db_column='id_for', blank=True, null=True)
    codigo = models.CharField(max_length=4)
    detalle = models.CharField(max_length=64, blank=True, null=True)
    max_valores = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'exoconceptos'
        unique_together = (('id_cl', 'id_for', 'codigo'),)


class Exoformatos(models.Model):
    id_cl = models.IntegerField()
    id = models.IntegerField(primary_key=True)  # AutoField?
    codigo = models.CharField(max_length=4)
    nombre = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exoformatos'
        unique_together = (('id_cl', 'codigo'),)


class Formularios(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(unique=True, max_length=32)
    descripcion = models.CharField(max_length=64, blank=True, null=True)
    variable = models.CharField(max_length=32, blank=True, null=True)
    aplicacion = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'formularios'


class GcItem(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    id_gc = models.ForeignKey('GruposCuentas', models.DO_NOTHING, db_column='id_gc')
    tip_con = models.SmallIntegerField()
    cod_cta = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gc_item'
        unique_together = (('id_gc', 'tip_con', 'cod_cta'),)


class GruposCuentas(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    id_cl = models.IntegerField()
    codigo = models.CharField(max_length=8)
    descripcion = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grupos_cuentas'
        unique_together = (('id_cl', 'codigo'),)


class Homologacion(models.Model):
    id_cl = models.IntegerField()
    id = models.BigIntegerField(primary_key=True)
    id_cta_2649 = models.ForeignKey(Cuentas, models.DO_NOTHING, db_column='id_cta_2649', blank=True, null=True)
    id_cta_niif = models.ForeignKey(Cuentas, models.DO_NOTHING, db_column='id_cta_niif', blank=True, null=True)
    per_con = models.DecimalField(max_digits=4, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'homologacion'
        unique_together = (('id_cl', 'per_con', 'id_cta_2649'), ('id_cl', 'per_con', 'id_cta_niif'),)


class Huellas(models.Model):
    id = models.BigIntegerField(primary_key=True)
    id_nit = models.BigIntegerField()
    dedo = models.DecimalField(max_digits=2, decimal_places=0)
    serial = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'huellas'
        unique_together = (('id_nit', 'dedo'),)


class IcCreCat(models.Model):
    id_icc = models.ForeignKey('ImpConCre', models.DO_NOTHING, db_column='id_icc')
    id = models.IntegerField(primary_key=True)  # AutoField?
    ll_cat = models.CharField(max_length=2, blank=True, null=True)
    dias_max = models.DecimalField(max_digits=9, decimal_places=0, blank=True, null=True)
    dias_min = models.DecimalField(max_digits=9, decimal_places=0, blank=True, null=True)
    cta_k1 = models.CharField(max_length=12, blank=True, null=True)
    cta_k2 = models.CharField(max_length=12, blank=True, null=True)
    c_kpro_ind = models.CharField(max_length=12, blank=True, null=True)
    por_kp_ind = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    cta_pro_ic1 = models.CharField(max_length=12, blank=True, null=True)
    cta_pro_ic2 = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ic_cre_cat'


class ImpConCre(models.Model):
    id_cl = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_cl')
    id = models.IntegerField(primary_key=True)  # AutoField?
    cod_imp = models.CharField(max_length=2)
    descripcion = models.CharField(max_length=64, blank=True, null=True)
    ll_for_pag = models.CharField(max_length=2, blank=True, null=True)
    ll_modali = models.CharField(max_length=2, blank=True, null=True)
    ll_garanti = models.CharField(max_length=2, blank=True, null=True)
    ci_ic = models.CharField(max_length=12, blank=True, null=True)
    ci_im = models.CharField(max_length=12, blank=True, null=True)
    ci_pol = models.CharField(max_length=12, blank=True, null=True)
    cirp_k_gen = models.CharField(max_length=12, blank=True, null=True)
    cirp_k_ind = models.CharField(max_length=12, blank=True, null=True)
    cirp_ic = models.CharField(max_length=12, blank=True, null=True)
    cp_k_gen = models.CharField(max_length=12, blank=True, null=True)
    cp_k_ind = models.CharField(max_length=12, blank=True, null=True)
    cp_ic = models.CharField(max_length=12, blank=True, null=True)
    cgp_k_gen = models.CharField(max_length=12, blank=True, null=True)
    cgp_k_ind = models.CharField(max_length=12, blank=True, null=True)
    cgp_ic = models.CharField(max_length=12, blank=True, null=True)
    cg_des_int = models.CharField(max_length=12, blank=True, null=True)
    cta_cxp = models.CharField(max_length=12, blank=True, null=True)
    cta_acre = models.CharField(max_length=12, blank=True, null=True)
    cta_pte_cap = models.CharField(max_length=12, blank=True, null=True)
    cta_pte_ic = models.CharField(max_length=12, blank=True, null=True)
    cta_ord_i = models.CharField(max_length=12, blank=True, null=True)
    cta_ord_c = models.CharField(max_length=12, blank=True, null=True)
    cta_ord_d = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imp_con_cre'
        unique_together = (('id_cl', 'cod_imp'),)


class LineaCre(models.Model):
    id_cl = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_cl')
    id = models.IntegerField(primary_key=True)  # AutoField?
    cod_lc = models.CharField(max_length=1)
    descripcion = models.CharField(max_length=50)
    tican = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    timan = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    tisan = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    titae = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    por_des_pp = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    dias_con_im = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    lin_cre = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'linea_cre'
        unique_together = (('id_cl', 'cod_lc'),)


class Localidades(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    codigo = models.CharField(unique=True, max_length=8)
    nombre = models.CharField(max_length=32)
    codpos = models.CharField(unique=True, max_length=12, blank=True, null=True)
    dpto = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'localidades'


class MoviCaja(models.Model):
    id_age = models.ForeignKey(Agencias, models.DO_NOTHING, db_column='id_age')
    id = models.IntegerField(primary_key=True)  # AutoField?
    cod_caj = models.CharField(max_length=2)
    fecha = models.DateField(blank=True, null=True)
    jornada = models.CharField(max_length=1, blank=True, null=True)
    sal_ant = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    debitos = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    creditos = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    che_dev = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    sal_fin = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    difer = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    cheques = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    vales = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    moneda = models.BinaryField(blank=True, null=True)
    cerrado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movi_caja'


class NucFamSoc(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    id_soc = models.ForeignKey('Socios', models.DO_NOTHING, db_column='id_soc')
    orden = models.DecimalField(max_digits=3, decimal_places=0)
    nombre = models.CharField(max_length=32)
    ll_tip_fam = models.CharField(max_length=2)
    agno_nac = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    aporta = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'nuc_fam_soc'
        unique_together = (('id_soc', 'orden'),)


class RefItem(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    tabla = models.CharField(max_length=16)
    campo = models.CharField(max_length=16)
    descripcion = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ref_item'
        unique_together = (('tabla', 'campo'),)


class RefSoc(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    id_soc = models.ForeignKey('Socios', models.DO_NOTHING, db_column='id_soc')
    orden = models.DecimalField(max_digits=3, decimal_places=0)
    ll_tip_ref = models.CharField(max_length=2)
    nombre = models.CharField(max_length=32)
    ciudad = models.CharField(max_length=32, blank=True, null=True)
    direccion = models.CharField(max_length=64, blank=True, null=True)
    celular = models.CharField(max_length=12, blank=True, null=True)
    telefono = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ref_soc'
        unique_together = (('id_soc', 'orden'),)


class RefTercero(models.Model):
    id = models.BigIntegerField(primary_key=True)
    id_nit = models.ForeignKey('Terceros', models.DO_NOTHING, db_column='id_nit')
    ubicacion = models.DecimalField(max_digits=2, decimal_places=0)
    tip_ref = models.CharField(max_length=1, blank=True, null=True)
    nombre = models.CharField(max_length=64, blank=True, null=True)
    id_mun = models.IntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=64, blank=True, null=True)
    cargo = models.CharField(max_length=32, blank=True, null=True)
    celular = models.CharField(max_length=12, blank=True, null=True)
    telefono = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ref_tercero'
        unique_together = (('id_nit', 'ubicacion'),)


class Referencias(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    cod_ref = models.CharField(max_length=2, blank=True, null=True)
    nombre = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'referencias'


class RiItem(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    id_ri = models.ForeignKey(RefItem, models.DO_NOTHING, db_column='id_ri')
    orden = models.DecimalField(max_digits=9, decimal_places=0)
    llave = models.CharField(max_length=2)
    item = models.CharField(max_length=32)
    val_rep1 = models.CharField(max_length=5, blank=True, null=True)
    val_rep2 = models.CharField(max_length=5, blank=True, null=True)
    borrable = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ri_item'
        unique_together = (('id_ri', 'llave'),)


class Socios(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    id_cl = models.ForeignKey(Entidades, models.DO_NOTHING, db_column='id_cl', blank=True, null=True)
    id_age = models.ForeignKey(Agencias, models.DO_NOTHING, db_column='id_age')
    codsoc = models.CharField(max_length=12)
    nit_soc = models.CharField(max_length=12, blank=True, null=True)
    num_afi = models.CharField(max_length=5, blank=True, null=True)
    ll_sexo = models.CharField(max_length=2, blank=True, null=True)
    fec_nac = models.DateField(blank=True, null=True)
    lug_nac = models.CharField(max_length=32, blank=True, null=True)
    ll_ocupa = models.CharField(max_length=2, blank=True, null=True)
    ll_est_civ = models.CharField(max_length=2, blank=True, null=True)
    profesion = models.CharField(max_length=32, blank=True, null=True)
    cargo = models.CharField(max_length=32, blank=True, null=True)
    co_entidad = models.ForeignKey(Entidades, models.DO_NOTHING, db_column='co_entidad', blank=True, null=True)
    co_mun_lab = models.CharField(max_length=8, blank=True, null=True)
    fec_ing_lab = models.DateField(blank=True, null=True)
    per_a_cargo = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    ll_niv_est = models.CharField(max_length=2, blank=True, null=True)
    edu_coo = models.CharField(max_length=1, blank=True, null=True)
    apo_men = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    mot_vin = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    fec_ing_coo = models.DateField(blank=True, null=True)
    reingreso = models.CharField(max_length=1, blank=True, null=True)
    ll_estado = models.CharField(max_length=2, blank=True, null=True)
    fec_ret_coo = models.DateField(blank=True, null=True)
    activo = models.CharField(max_length=1, blank=True, null=True)
    ll_estrato = models.CharField(max_length=2, blank=True, null=True)
    muj_cab_fam = models.CharField(max_length=1, blank=True, null=True)
    ll_sec_eco = models.CharField(max_length=2, blank=True, null=True)
    fec_ult_act = models.DateField(blank=True, null=True)
    ano_ini_res = models.CharField(max_length=4, blank=True, null=True)
    preexistencia = models.CharField(max_length=1, blank=True, null=True)
    pol_vid = models.CharField(max_length=1, blank=True, null=True)
    pol_deu = models.CharField(max_length=1, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    fec_act = models.DateField(blank=True, null=True)
    not_ema = models.CharField(max_length=1, blank=True, null=True)
    not_cel = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socios'
        unique_together = (('id_age', 'codsoc'),)


class Terceros(models.Model):
    id_cl = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_cl')
    id = models.BigIntegerField(primary_key=True)
    nit = models.CharField(max_length=12)
    dv = models.CharField(max_length=1, blank=True, null=True)
    co_ciu_exp = models.ForeignKey(Localidades, models.DO_NOTHING, db_column='co_ciu_exp', blank=True, null=True)
    ll_tip_doc = models.CharField(max_length=2, blank=True, null=True)
    nit_rap = models.CharField(max_length=8, blank=True, null=True)
    co_ciu_res = models.ForeignKey(Localidades, models.DO_NOTHING, db_column='co_ciu_res', blank=True, null=True)
    ll_regimen = models.CharField(max_length=2, blank=True, null=True)
    fec_exp_ced = models.DateField(blank=True, null=True)
    ll_tip_ter = models.CharField(max_length=2, blank=True, null=True)
    pri_ape = models.CharField(max_length=32, blank=True, null=True)
    seg_ape = models.CharField(max_length=32, blank=True, null=True)
    pri_nom = models.CharField(max_length=32, blank=True, null=True)
    seg_nom = models.CharField(max_length=32, blank=True, null=True)
    raz_soc = models.CharField(max_length=128, blank=True, null=True)
    direccion = models.CharField(max_length=64, blank=True, null=True)
    co_codpos = models.CharField(max_length=12, blank=True, null=True)
    tel_ofi = models.CharField(max_length=12, blank=True, null=True)
    tel_res = models.CharField(max_length=12, blank=True, null=True)
    celular1 = models.CharField(max_length=12, blank=True, null=True)
    celular2 = models.CharField(max_length=12, blank=True, null=True)
    fax = models.CharField(max_length=12, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    nombre = models.CharField(max_length=131, blank=True, null=True)
    fec_act = models.DateField(blank=True, null=True)
    observacion = models.CharField(max_length=255, blank=True, null=True)
    per_pub_exp = models.CharField(max_length=1, blank=True, null=True)
    nit_interno = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'terceros'
        unique_together = (('id_cl', 'nit'),)


class Vigencia(models.Model):
    id_cl = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_cl')
    id = models.IntegerField(primary_key=True)  # AutoField?
    per_con = models.DecimalField(max_digits=4, decimal_places=0)
    formato = models.CharField(max_length=16, blank=True, null=True)
    sal_min_men = models.DecimalField(max_digits=9, decimal_places=0, blank=True, null=True)
    aux_tra_men = models.DecimalField(max_digits=9, decimal_places=0, blank=True, null=True)
    uvt = models.DecimalField(max_digits=9, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vigencia'
        unique_together = (('id_cl', 'per_con'),)


class ZmovCre(models.Model):
    id_age = models.IntegerField(blank=True, null=True)
    docto = models.CharField(max_length=10, blank=True, null=True)
    numero = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    codcre = models.CharField(max_length=12, blank=True, null=True)
    desem = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    capital = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    intcor = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    intmor = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    polseg = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    im_cau = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    ps_cau = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    aporte = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    ndoc = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    ncodcre = models.CharField(max_length=12, blank=True, null=True)
    copiado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zmov_cre'


class ZmovCreCum(models.Model):
    docto = models.CharField(max_length=10, blank=True, null=True)
    numero = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    codcre = models.CharField(max_length=12, blank=True, null=True)
    desem = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    capital = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    intcor = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    intmor = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    polseg = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    im_cau = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    ps_cau = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    aporte = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    ndoc = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    ncodcre = models.CharField(max_length=12, blank=True, null=True)
    copiado = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zmov_cre_cum'


class ZmovCreGra(models.Model):
    docto = models.CharField(max_length=10, blank=True, null=True)
    numero = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    codcre = models.CharField(max_length=12, blank=True, null=True)
    desem = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    capital = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    intcor = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    intmor = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    polseg = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    im_cau = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    ps_cau = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    aporte = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    ndoc = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    ncodcre = models.CharField(max_length=12, blank=True, null=True)
    copiado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zmov_cre_gra'


class ZmovCreGua(models.Model):
    docto = models.CharField(max_length=10, blank=True, null=True)
    numero = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    codcre = models.CharField(max_length=12, blank=True, null=True)
    desem = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    capital = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    intcor = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    intmor = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    polseg = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    im_cau = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    ps_cau = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    aporte = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    ndoc = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    ncodcre = models.CharField(max_length=12, blank=True, null=True)
    copiado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zmov_cre_gua'


class ZmovCreVil(models.Model):
    id_age = models.IntegerField(blank=True, null=True)
    docto = models.CharField(max_length=10, blank=True, null=True)
    numero = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    codcre = models.CharField(max_length=12, blank=True, null=True)
    desem = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    capital = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    intcor = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    intmor = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    polseg = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    im_cau = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    ps_cau = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    aporte = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    ndoc = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    ncodcre = models.CharField(max_length=12, blank=True, null=True)
    copiado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zmov_cre_vil'
