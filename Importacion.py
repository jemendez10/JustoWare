import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Justo_proy.settings')

# Initialize django application
import django
django.setup()

# Do what you want to debug and set breakpoints
import csv
from django.shortcuts import render
from django.http import HttpResponse
import justo_app.models as justoAppModels
from datetime import datetime

def asignar_fecha(fecha_str, formato='%d/%m/%Y'):
    try:
        fecha = datetime.strptime(fecha_str, formato)
        fecha_validada = fecha.strftime('%Y-%m-%d')
        return fecha_validada
    except ValueError:
        return None

def inicio():
    print('Inicial  ',datetime.now())
    Cliente = justoAppModels.CLIENTES.objects.filter(codigo = 'A').first()
    if Cliente == None:
        Cliente = justoAppModels.CLIENTES.objects.create(codigo = 'A')
    Cliente.doc_ide = '8947111111'
    Cliente.sigla = 'CORNOQUIA'
    Cliente.nombre = 'COOPERATIVA ESPECIALIZADA DE AHORRO Y CREDITO DE LA ORINOQUIA'
    Cliente.celular = '3153275734'
    Cliente.email = 'COORINOQUIA@HOTMAIL.COM'
    Cliente.dominio = 'COORINOQUIA.COOP'
    Cliente.save()
    Oficina = justoAppModels.OFICINAS.objects.filter(cliente = Cliente,codigo='A0001').first()
    if Oficina == None:
        Oficina=justoAppModels.OFICINAS.objects.create(cliente = Cliente,codigo = "A0001",
        contabiliza = 'S',
        nombre_oficina = 'Oficina Principal',
        responsable = 'Jose Guillermo Prieto López',
        celular = '3153263722',
    )
    CentroCosto = justoAppModels.CENTROCOSTOS.objects.filter(cliente=Cliente,codigo = 'A001').first()
    if CentroCosto==None:
        CentroCosto = justoAppModels.CENTROCOSTOS.objects.create(cliente=Cliente,codigo = 'A001')
    with open('c:/ajusto/csv/localidades.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            Localidad = justoAppModels.LOCALIDADES.objects.filter(cliente = Cliente,codigo = row['codigo']).first()
            if Localidad == None:
                Localidad = justoAppModels.LOCALIDADES.objects.create(cliente = Cliente,
                    codigo = row['codigo'])
            Localidad.nombre = row['nombre']
            Localidad.cod_pos = row['codpos']
            Localidad.departamento = row['dpto']
            Localidad.save()
    with open('c:/ajusto/csv/c00documentos.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            DocZep = justoAppModels.XDOC_ZEP.objects.filter(per_con=int(row['c00agno']),clase_zep=row['c00clase']).first()
            if DocZep == None:
                DocZep = justoAppModels.XDOC_ZEP.objects.create(per_con=int(row['c00agno']),clase_zep=row['c00clase'])
            DocZep.doc_ds =row['c00docds']
            DocZep.nombre =row['c00nombre']
            DocZep.descripcion =row['c00descripcion']
            DocZep.save()
    print('         ',datetime.now())

def usuarios():
    print('usuarios  ',datetime.now())
    Cliente = justoAppModels.CLIENTES.objects.filter(codigo = 'A').first()
    Oficina = justoAppModels.OFICINAS.objects.filter(cliente = Cliente,codigo='A0001').first()
    with open('c:/ajusto/csv/c06cajeros.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')  
        for row in csv_reader:
            Usuario = justoAppModels.USUARIOS.objects.filter(oficina=Oficina,login = row['c06usuario']).first()
            if Usuario == None:
                Usuario = justoAppModels.USUARIOS.objects.create(oficina=Oficina,login = row['c06usuario'])
            Usuario.nit = ''
            Usuario.nombre = ''
            Usuario.fec_ing = asignar_fecha('01/01/1900','%M-%D-%Y')
            Usuario.es_cajero = 'S'
            Usuario.cod_caj = row['c06codcaj']
            Usuario.fec_sal = asignar_fecha('01/01/1900','%M-%D-%Y')
            Usuario.cta_con_acr = row['c06ctacon']
            Usuario.activo = 'S'
            Usuario.save()
    print('          ',datetime.now())

def cierre_mes():
    print('cierres  ',datetime.now())
    Cliente = justoAppModels.CLIENTES.objects.filter(codigo = 'A').first()
    Oficina = justoAppModels.OFICINAS.objects.filter(cliente = Cliente,codigo='A0001').first()
    with open('c:/ajusto/csv/g10cierres.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')  
        for row in csv_reader:
            CierreMes = justoAppModels.cierre_mes.objects.filter(oficina=Oficina,fecha = asignar_fecha(row['g10feccie'],'%M-%D-%Y')).first()
            if CierreMes == None:
                CierreMes = justoAppModels.cierre_mes.objects.create(oficina=Oficina,fecha = asignar_fecha(row['g10feccie'],'%M-%D-%Y'))
            CierreMes.protegido = row['g10protegido']
            CierreMes.tot_deb = row['g10debitos']
            CierreMes.tot_cre = row['g10creditos']
            CierreMes.fec_cie = asignar_fecha(row['g10feccie'],'%M-%D-%Y')
            CierreMes.usuario = row['g10usuario']
            CierreMes.save()
    print('         ',datetime.now())

def mov_caja():
    print('Mov Caja   ',datetime.now())
    Cliente = justoAppModels.CLIENTES.objects.filter(codigo = 'A').first()
    Oficina = justoAppModels.OFICINAS.objects.filter(cliente = Cliente,codigo='A0001').first()
    with open('c:/ajusto/csv/c07movcaja.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')  
        for row in csv_reader:
            MovCaja = justoAppModels.MOV_CAJA.objects.filter(oficina=Oficina,cod_caj=row['c07codcaj'],
                    fecha=asignar_fecha(row['c07fecha'],'%M-%D-%Y'),jornada=row['c07jornada']).first()
            if MovCaja == None:
                MovCaja = justoAppModels.MOV_CAJA.objects.create(oficina=Oficina,cod_caj=row['c07codcaj'],
                    fecha=asignar_fecha(row['c07fecha'],'%M-%D-%Y'),jornada=row['c07jornada'])
                MovCaja.saldo_ini = row['c07salant']
                MovCaja.debitos = row['c07salant']
                MovCaja.creditos = row['c07salant']
                MovCaja.val_che_dev = row['c07chedev']
                MovCaja.saldo_fin =row['c07salfin']
                MovCaja.diferencia = row['c07difer']
                MovCaja.val_cheques = row['c07cheques']
                MovCaja.val_vales = row['c07vales']
                MovCaja.cerrado = 'S'
                MovCaja.monedas = row['c07moneda'].replace(';', ',')
                MovCaja.save()
    print('           ',datetime.now())

def docto_conta():    
    print('Documentos  ',datetime.now())
    Cliente = justoAppModels.CLIENTES.objects.filter(codigo = 'A').first()
    Oficina = justoAppModels.OFICINAS.objects.filter(cliente = Cliente,codigo='A0001').first()
    with open('c:/ajusto/csv/documentos.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            DoctoConta = justoAppModels.DOCTO_CONTA.objects.filter(oficina=Oficina,per_con=int(float(row['PER_CON'])),
                codigo=int(float(row['COD_DOC']))).first()
            if DoctoConta == None:
                DoctoConta = justoAppModels.DOCTO_CONTA.objects.create(oficina=Oficina,per_con=int(float(row['PER_CON'])),
                    codigo=int(float(row['COD_DOC'])))
            DoctoConta.nom_cto = row['NOM_CTO']
            DoctoConta.nombre = row['NOMBRE']
            DoctoConta.doc_admin = row['DOC_ADM']
            DoctoConta.doc_caja = row['DE_CAJA']
            DoctoConta.inicio_nuevo_per = row['INI_NUE_VIG']
            DoctoConta.consecutivo = int(float(row['CONSECUTIVO']))
            DoctoConta.id_ds = row['ID']
            DoctoConta.save()

    print('            ',datetime.now())

def plan_ctas():
    print('Plan Ctas  ',datetime.now())
    Cliente = justoAppModels.CLIENTES.objects.filter(codigo = 'A').first()
    with open('c:/ajusto/csv/plancuentas.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')  
        for row in csv_reader:
            if row['TIP_CON'] == '1':
                PlanCta = justoAppModels.PLAN_CTAS.objects.filter(cliente=Cliente,per_con=int(float(row['PER_CON'])),
                    cod_cta=row['COD_CTA']).first()
                if PlanCta == None:
                    PlanCta = justoAppModels.PLAN_CTAS.objects.create(cliente=Cliente,per_con=int(float(row['PER_CON'])),
                cod_cta=row['COD_CTA'])
                PlanCta.nom_cta = row['NOMBRE'][:64]
                PlanCta.tip_cta = row['TIP_CTA']
                PlanCta.dinamica = row['DINAMICA']
                PlanCta.naturaleza = row['NATURALEZA']
                PlanCta.activa = row['ACTIVA']
                PlanCta.por_tercero  = row['POR_TER']
                PlanCta.cta_act_fij  = row['CTA_ACT_FIJ']
                PlanCta.cta_pre  = row['CTA_PRE']
                PlanCta.cta_bal  = row['CTA_BAL']
                PlanCta.cta_res = row['CTA_RES']
                PlanCta.cta_ord = row['CTA_ORD']
                PlanCta.cta_ban  = row['CTA_BAN']
                PlanCta.cta_gan_per = row['CTA_GANPER']
                PlanCta.cta_per_gan = row['CTA_PERGAN']  
                PlanCta.cta_dep  = row['CTA_DEP']
                PlanCta.cta_ing_ret = row['CTA_INGRET']
                PlanCta.cta_ret_iva  = row['CTA_RETIVA']
                PlanCta.cta_rec  = row['CTA_REC']
                PlanCta.id_ds  = row['ID']
                PlanCta.save()
    print('           ',datetime.now())

def conceptos():
    print('Conceptos Justo ',datetime.now())
    Cliente = justoAppModels.CLIENTES.objects.filter(codigo = 'A').first()
    with open('c:/ajusto/csv/c02concepto.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')  
        for row in csv_reader:
            Concepto = justoAppModels.CONCEPTOS.objects.filter(cliente=Cliente,cod_con=row['c02codcon']).first()
            if Concepto == None:
                Concepto = justoAppModels.CONCEPTOS.objects.create(cliente=Cliente,cod_con=row['c02codcon'])
            Concepto.con_justo = 'S' if row['c02noborra']=='T' else 'N'
            Concepto.descripcion = row['c02descripcion']
            Concepto.tip_dev_ap = 'N' if row['c02tipdevapo'] else (row['c02tipdevapo'] if len(row['c02tipdevapo']) == 1 else ('N'))       
            Concepto.tip_con = 'S' if row['c02tipcon']=='T' else 'N'
            Concepto.tip_sis = row['c02tipsis']
            Concepto.cta_con = row['c02ctacon']
            Concepto.cta_con_pas = row['c02ctapas']
            Concepto.debito = 'S' if row['c02debito'] == 'T' else 'N'
            Concepto.credito = 'S' if row['c02credito'] == 'T' else 'N'
            Concepto.por_tercero =  'S' if row['c02conporter'] == 'T' else 'N'
            Concepto.por_ret_fue =  row['c02por_ret']
            Concepto.save()
    print('                ',datetime.now())    

def terceros():
    print('Terceros....  ',datetime.now())
    Cliente = justoAppModels.CLIENTES.objects.filter(codigo='A').first()
    with open('c:/ajusto/Terceros.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            Tercero = justoAppModels.TERCEROS.objects.filter(cliente=Cliente,
            cla_doc = row['LL_TIP_DOC'][0],
            doc_ide = row['NIT']).first()
            if Tercero == None:
                Tercero = justoAppModels.TERCEROS.objects.create(
                    cliente = Cliente,
                    cla_doc = row['LL_TIP_DOC'][0],
                    doc_ide = row['NIT']
                )
            Tercero.dig_ver = row['DV']
            Tercero.nit_rap = row['NIT_RAP']
            Tercero.cod_ciu_exp = justoAppModels.LOCALIDADES.objects.filter(cliente=Cliente,
                        codigo=row['CO_CIU_EXP']).first()
            Tercero.cod_ciu_res = justoAppModels.LOCALIDADES.objects.filter(cliente=Cliente,
                        codigo=row['CO_CIU_RES']).first()
            Tercero.regimen = row['LL_REGIMEN']
            Tercero.fec_exp_ced = asignar_fecha(row['FEC_EXP_CED'])
            Tercero.tip_ter = row['LL_TIP_TER']
            Tercero.pri_ape = row['PRI_APE'][:10]
            Tercero.seg_ape = row['SEG_APE'][:10]
            Tercero.pri_nom = row['PRI_NOM'][:10]
            Tercero.seg_nom  = row['SEG_NOM'][:10]
            Tercero.raz_soc  = row['RAZ_SOC']
            Tercero.direccion = row['DIRECCION']
            Tercero.cod_pos = row['CO_CODPOS']
            Tercero.tel_ofi  = row['TEL_OFI'][:10]
            Tercero.tel_res = row['TEL_RES'][:10]
            Tercero.celular1 = row['CELULAR1'][:10]
            Tercero.celular2 = row['CELULAR2'][:10]
            Tercero.fax = row['FAX']
            Tercero.email = row['EMAIL']
            #   fec_act = datetime.strptime("1900-01-1", "%Y-%m-%d")
            #   asignar_fecha(anteia1['flows'][idsocio]['form.date'])
            Tercero.observacion = row['OBSERVACION']
            Tercero.per_pub_exp = row['PER_PUB_EXP']
            Tercero.nit_interno = row['NIT_INTERNO']
            Tercero.id_ds = row['ID']
            Tercero.save()
    print('Fin Terceros  ',datetime.now())

def comprobantes():
    print('Comprobantes .... ',datetime.now())
    Cliente = justoAppModels.CLIENTES.objects.filter(codigo='A').first()
    with open('c:/ajusto/csv/comprobantes.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            Documento = justoAppModels.DOCTO_CONTA.objects.filter(id_ds = row['ID_DOC']).first()
            if Documento == None:
                continue
            Comprobante = justoAppModels.HECHO_ECONO.objects.filter(docto_conta=Documento,numero=int(float(row['NUMERO']))).first()
            if Comprobante == None:
                Comprobante = justoAppModels.HECHO_ECONO.objects.create(docto_conta=Documento,numero=int(float(row['NUMERO'])))
            Comprobante.fecha = asignar_fecha(row['FECHA'],'%d/%m/%Y')
            Comprobante.descripcion = row['CONCEPTO'][:64]
            Comprobante.anulado =  row['ANULADO']
            Comprobante.protegido = row['PROTEGIDO']
            Comprobante.fecha_prot = asignar_fecha(row['FEC_GRA'],'%d/%m/%Y')
            Comprobante.usuario = row['CUENTA'][:16]
            Comprobante.canal = row['LL_FUENTE']
            Comprobante.id_ds = row['ID']
            Comprobante.save()
    print('             .... ',datetime.now())

def detalle_prod():
    print('Detalle_prod ... ',datetime.now())
    Cliente = justoAppModels.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justoAppModels.OFICINAS.objects.filter(codigo='A0001').first()
    CentroCosto = justoAppModels.CENTROCOSTOS.objects.filter(cliente=Cliente,codigo = 'A001').first()
    with open('c:/ajusto/csv/c05movite.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            if row['c05concept'] in ('DESEM','CUOTA','ABOCA','CONDO','CASTI'):
                DocZep = justoAppModels.XDOC_ZEP.objects.filter(per_con=row['c05fecha'],clase_zep=row['c05clase']).first()
                if DocZep == None:
                    print('No Doc Zep',row['c05fecha'],row['c05clase'],row['c05documen'])
                    continue
                DocCon = justoAppModels.DOCTO_CONTA.objects.filter(oficina=Oficina,per_con=DocZep.per_con,
                      codigo=DocZep.doc_ds).first()
                if DocCon == None:
                    print('No Doc Justo',row['c05fecha'],row['c05clase'],row['c05documen'])
                    continue
                HechEco = justoAppModels.HECHO_ECONO.objects.filter(docto_conta=DocCon,numero=int(row['c05documen'])).first()
                if HechEco == None:
                    print('No Comp Justo',row['c05fecha'],row['c05clase'],row['c05documen'])
                    continue
                DetProd = justoAppModels.DETALLE_PROD.objects.filter(hecho_econo=HechEco,producto="CR",
                        concepto = row['c05concept'],subcuenta=row['c05subcuen']).first()
                if DetProd == None:
                    DetProd = justoAppModels.DETALLE_PROD.objects.create(hecho_econo=HechEco,producto="CR",
                        concepto = row['c05concept'],subcuenta=row['c05subcuen'])
                DetProd.valor = row['c05valor']
                DetProd.centro_costo = CentroCosto
                DetProd.save()
    print('             ... ',datetime.now())

def detalle_econo():
    print('Detalles Comp ... ',datetime.now())
    Cliente = justoAppModels.CLIENTES.objects.filter(codigo='A').first()
    CentroCosto = justoAppModels.CENTROCOSTOS.objects.filter(cliente=Cliente,codigo = 'A001').first()
    with open('c:/ajusto/csv/detalles_22.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            Comprobante = justoAppModels.HECHO_ECONO.objects.filter(id_ds = row['ID_COM']).first()
            if Comprobante == None:
                continue
            Tercero = justoAppModels.TERCEROS.objects.filter(id_ds = row['ID_TER']).first()
            if Tercero == None:
                continue
            Cuenta = justoAppModels.PLAN_CTAS.objects.filter(id_ds = row['ID_CTA']).first()
            if Cuenta == None:
                continue
            DetalleEcono = justoAppModels.DETALLE_ECONO.objects.filter(hecho_econo=Comprobante,cuenta=Cuenta,tercero=Tercero).first()
            if DetalleEcono == None:
                DetalleEcono = justoAppModels.DETALLE_ECONO.objects.create(hecho_econo=Comprobante,cuenta=Cuenta,tercero=Tercero)
            DetalleEcono.item_concepto = row['ID_DC']
            DetalleEcono.detalle = row['DETALLE']
            DetalleEcono.debito = row['DEBITO']
            DetalleEcono.credito = row['CREDITO']
            DetalleEcono.id_ds = row['ID']
            DetalleEcono.save()
    print('              ... ',datetime.now())

def est_fin():
    print('Estados_fin ..  ',datetime.now())
    Cliente = justoAppModels.CLIENTES.objects.filter(codigo='A').first()
    with open('c:/ajusto/csv/s02estfin.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')    
        for row in csv_reader:
            Tercero  = justoAppModels.TERCEROS.objects.filter(
                cliente = Cliente,
                doc_ide = row['s02nit']).first()
            if Tercero == None:
                continue
            Estfin = justoAppModels.estados_fin.objects.filter(
                cliente = Cliente,
                tercero = Tercero,
                fec_inf = asignar_fecha(row['s02fecmod'].strip(),'%m/%d/%Y')).first()
            if Estfin == None:
                Estfin = justoAppModels.estados_fin.objects.create(
                    cliente = Cliente,
                    tercero = Tercero,
                    fec_inf = asignar_fecha(row['s02fecmod'].strip(),'%m/%d/%Y'))
            ing_sal_fij = row['s02ingmen']
            Estfin.ing_hon = row['s02inghon']
            Estfin.ing_pen = row['s02ingpen']
            Estfin.ing_arr = row['s02ingarr']
            Estfin.ing_com = row['s02ingcom']
            Estfin.ing_ext = row['s02ingext']
            Estfin.ing_otr = 'S'
            Estfin.ing_tot = 0
            Estfin.egr_sec_fin = row['s02egrsecfin']
            Estfin.egr_cuo_hip = row['s02egrcuohip']
            Estfin.egr_des_nom = 'S'
            Estfin.egr_gas_fam = row['s02egrgasfam']
            Estfin.egr_otr_cre = row['s02egrotrcre']
            Estfin.egr_arr = row['s02egrarr']
            Estfin.egr_otr_gas = row['s02egrotrgas']
            Estfin.egr_tot = 0
            Estfin.act_otr_egr = 0
            Estfin.act_tip_bien = ''
            Estfin.act_vei = row['s02actveh']
            Estfin.act_otr = 'S'
            Estfin.tot_act = 0
            Estfin.act_fin_rai = row['s02actfinrai']
            Estfin.act_inv = 0
            Estfin.escritura = ''
            Estfin.pas_otr = 'S'
            Estfin.pas_tip = row['s02pasfin']
            Estfin.tot_pat = 0
            Estfin.pas_val = row['s02pasotr']
            Estfin.tot_pas = 0
            Estfin.pas_des = 0 
            Estfin.dec_ren = 'N'
            Estfin.tip_pas = ''
            Estfin.des_pas = ''
            Estfin.val_pas = 0
            Estfin.ope_mon_ext = 'N'
            Estfin.nom_ban_ext = ''
            Estfin.ope_pais_ext = 'S'
            Estfin.ope_monto_ext = 0
            Estfin.num_cta_ext = ''
            Estfin.tip_ope_ext = ''
            Estfin.mon_ope_ext = 'S'
            Estfin.prod_mon_ext = 0
            Estfin.des_prod_ext = 0
            Estfin.mon_prod_ext = 0
            Estfin.pais_prod_ext = 0
            Estfin.ciu_prod_ext = 0
            Estfin.prom_prod_ext = 0
            Estfin.save()
    print('Fin Estados_fin',datetime.now())

def pagadores():
    print('Pagadores..  ',datetime.now())
    Cliente = justoAppModels.CLIENTES.objects.filter(codigo='A').first()
    with open('c:/ajusto/csv/s07entidades.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')    
        for row in csv_reader:
            pagador = justoAppModels.pagadores.objects.filter(
                    cliente=Cliente,
                    codigo=row['s07codent']).first()
            if pagador == None:
                pagador=justoAppModels.pagadores.objects.create(cliente = Cliente,
                        codigo = row['s07codent'])
            pagador.nombre = row['s07nombre']
            pagador.ciudad = row['s07ciudad']
            pagador.pagador = row['s07nompag']
            pagador.tel_cel = row['s07telpag']
            pagador.save()
    print('Fin pagadores ',datetime.now())

def socios():
    print('Socios....  ',datetime.now())
    Cliente = justoAppModels.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justoAppModels.OFICINAS.objects.filter(codigo='A0001').first()
    if Oficina == None:
        Oficina=justoAppModels.OFICINAS.objects.create(cliente = Cliente,codigo = "A0001",
        contabiliza = 'S',
        nombre_oficina = 'Oficina Principal',
        responsable = 'Jose Guillermo Prieto López',
        celular = '3153263722',
    )
    with open('c:/ajusto/csv/s01socios.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            tercero = justoAppModels.TERCEROS.objects.filter(cliente=Cliente,
                        doc_ide = row['s01nit']).first()
            if tercero == None:
                continue
            Socio = justoAppModels.ASOCIADOS.objects.filter(
                    oficina=Oficina,
                    cod_aso = row['s01codsoc']).first()
            if Socio == None:    
                Socio = justoAppModels.ASOCIADOS.objects.create(
                        oficina = Oficina,
                        cod_aso = row['s01codsoc']
                    )    
            pagador = justoAppModels.pagadores.objects.filter(
                    cliente=Cliente,
                    codigo=row['s01codent']).first()
            Socio.sexo = row['s01sexo'][:1]
            Socio.est_civ = row['s01estciv']
            Socio.fec_nac = asignar_fecha(row['s01fecnac'])
            Socio.ciu_res = ''
            Socio.zona  = ''
            Socio.profesion = ''
            Socio.ocupacion =''
            Socio.ocupacion_cod = ''
            Socio.estrato = row['s01estrato']
            Socio.niv_est  = row['s01nivest']
            Socio.cab_fam = row['s01mujcabfam']
            Socio.id_pag = pagador
            Socio.fec_afi = asignar_fecha(row['s01mujcabfam'])
            Socio.cargo_emp = row['s01cargo']
            Socio.per_a_cargo = row['s01peracar']
            Socio.num_hij_men = 0
            Socio.num_hij_may = row['s01peracar']
            Socio.tip_viv = ''
            Socio.tie_en_ciu = '' 
            Socio.med_con = ''
            Socio.fec_ing_tra = asignar_fecha(row['s01fecinge'])
            Socio.tel_tra = ''
            Socio.tip_sal= ''
            Socio.ciu_tra = ''
            Socio.act_eco = ''
            Socio.cod_ciiu = ''
            Socio.tip_con = ''
            Socio.nom_emp = ''
            Socio.nit_emp = ''
            Socio.dir_emp = ''
            Socio.email_emp = ''
            Socio.sector_emp = ''
            Socio.empresa_ant = ''
            Socio.emp_num_emp = ''
            Socio.negocio_pro = ''
            Socio.negocio_nom = ''
            Socio.negocio_tel = ''
            Socio.negocio_loc_pro = '' 
            Socio.negocio_cam_com = ''
            Socio.negocio_ant = ''
            Socio.pension_ent = ''
            Socio.pension_tie = ''
            Socio.pension_otr = ''
            Socio.pension_ent_otr = '' 
            Socio.pep_es_fam = ''
            Socio.pep_fam_par = ''
            Socio.pep_fam_nom = ''
            Socio.pep_car_pub = ''
            Socio.pep_cargo = ''
            Socio.pep_eje_pod = '' 
            Socio.pep_adm_rec_est = '' 
            Socio.tie_gre_car = ''
            Socio.recibe_pag_ext = '' 
            Socio.recide_ext_mas_186 = '' 
            Socio.recibe_ing_ext = ''
            Socio.estado_anteia = ''
            Socio.save()
    print('Fin socios  ',datetime.now())

def bene_aso():
    print('Bene_aso  ',datetime.now())
    Oficina = justoAppModels.OFICINAS.objects.filter(codigo='A0001').first()
    with open('c:/ajusto/csv/s01compfami.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        idocide = 1
        for row in csv_reader:
            Socio = justoAppModels.ASOCIADOS.objects.filter(
                    oficina=Oficina,
                    cod_aso = row['s01xcodsoc']).first()
            if Socio == None:
                continue
            AsoBene = justoAppModels.ASO_BENEF.objects.filter(asociado  = Socio,
                    doc_ide = str(idocide)).first()
            if AsoBene == None:
                AsoBene = justoAppModels.ASO_BENEF.objects.create(asociado  = Socio,
                    doc_ide = str(idocide))
            AsoBene.nombre = row['s01xnombre']
            AsoBene.agno_nac = row['s01xagnnac']
            AsoBene.parentesco = row['s01xparentesco']
            AsoBene.porcentaje = 0
            AsoBene.save()
            idocide = idocide + 1
    print('Fin Bene ',datetime.now())

def referencias():
    print('Referencias  ',datetime.now())
    Oficina = justoAppModels.OFICINAS.objects.filter(codigo='A0001').first()
    with open('c:/ajusto/csv/s02referencias.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            Socio = justoAppModels.ASOCIADOS.objects.filter(
                    oficina = Oficina,
                    cod_aso = row['s02nit']).first()
            if Socio == None:
                continue
            Referencia = justoAppModels.ASO_REFERENCIAS.objects.filter(asociado = Socio,nombre = row['s02nombre']).first()
            if Referencia == None:
                Referencia = justoAppModels.ASO_REFERENCIAS.objects.create(asociado = Socio,nombre = row['s02nombre'])
            if row['s02tipref'] < '7':
                Referencia.tipo_ref = '1'
                if row['s02tipref'] == '1':
                    Referencia.parentesco = '3'
                elif row['s02tipref'] == '2':
                    Referencia.parentesco = '6' 
                elif row['s02tipref'] == '3':
                    Referencia.parentesco = '2' 
                else:
                    Referencia.parentesco = '9' 
            else:
                Referencia.parentesco = '0' 
                if row['s02tipref'] == '7':
                    Referencia.tipo_ref = '2'
                if row['s02tipref'] == '8':
                    Referencia.tipo_ref = '3'
            Referencia.ocupacion = row['s02cargo']
            Referencia.empresa = row['s02empresa']
            Referencia.direccion = row['s02direccion']
            Referencia.tel_fijo = row['s02telfij'][:10]
            Referencia.tel_cel = row['s02telcel'][:10]
            Referencia.tel_emp = row['s02telemp'][:10]
            Referencia.save()
    print('Fin Referen ',datetime.now())

def linaho():
    print('Lineas Ahorros  ',datetime.now())
    Cliente = justoAppModels.CLIENTES.objects.filter(codigo='A').first()
    with open('c:/ajusto/csv/s04linaho.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader: 
            LinAho = justoAppModels.LINEAS_AHORRO.objects.filter(cliente = Cliente,
                cod_lin_aho = row['s04tipcta']).first()
            if LinAho == None:
                LinAho = justoAppModels.LINEAS_AHORRO.objects.create(cliente = Cliente,
                cod_lin_aho = row['s04tipcta'])
            LinAho.nombre = row['s04nombre']    
            LinAho.termino = row['s04termino']
            LinAho.per_liq_int = row['s04perliqint']
            LinAho.cta_por_pas = row['s04ctaporpag']
            LinAho.fec_ult_liq_int =  asignar_fecha(row['s04fecultliqint'],'%m/%d/%Y')
            LinAho.saldo_minimo = row['s04monminliqint']
            LinAho.save()
    print('Fin Lin Ahorros ',datetime.now())

def plan_aportes():
    print('plan aportes     ',datetime.now())
    Oficina = justoAppModels.OFICINAS.objects.filter(codigo='A0001').first()
    with open('c:/ajusto/csv/S00APORTACION.CSV', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader: 
            PlanApor = justoAppModels.PLAN_APORTES.objects.filter(
                    oficina = Oficina,
                    agno = int(row['agno'])).first()
            if PlanApor == None:
                PlanApor = justoAppModels.PLAN_APORTES.objects.create(
                    oficina = Oficina,
                    agno = int(row['agno'])
                    )
            PlanApor.meses = row['agno']
            PlanApor.iniadu = row['s00iniadu']
            PlanApor.totadu = row['s00totadu']
            PlanApor.inichi1 = row['s00inichi1']
            PlanApor.totchi1 = row['s00totchi1']
            PlanApor.inichi2 = row['s00inichi2']
            PlanApor.totchi2 = row['s00totchi2']
            PlanApor.inijur = row['s00inijur']
            PlanApor.totjur = row['s00totjur']
            PlanApor.save()
        
    print('Fin Plan Aportes ',datetime.now())

def imp_con_lin_aho():
    print('Imp Lin Aho     ',datetime.now())
    Cliente = justoAppModels.CLIENTES.objects.filter(codigo='A').first()
    with open('c:/ajusto/csv/S22IMPCONLINAHO.CSV', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader: 
            LinAho = justoAppModels.LINEAS_AHORRO.objects.filter(cliente=Cliente,cod_lin_aho=row['s22tipcta']).first()
            if LinAho == None:
                continue
            Impconlinaho = justoAppModels.IMP_CON_LIN_AHO.objects.filter(linea_ahorro=LinAho,cod_imp = row['s22codimp']).first()
            if Impconlinaho == None:
                Impconlinaho = justoAppModels.IMP_CON_LIN_AHO.objects.create(linea_ahorro=LinAho,cod_imp = row['s22codimp'])
            Impconlinaho.descripcion = row['s22descripcion']
            Impconlinaho.ctaafeact = row['s22ctaafecap'] 
            Impconlinaho.ctaafeina = row['s22ctaafeina']
            Impconlinaho.ctaafeint = row['s22ctaafeint']
            Impconlinaho.ctaretfue = row['s22ctaaferetfue']
            Impconlinaho.save()
    print('Fin Imp Lin Aho ',datetime.now())        

def ctas_aho():
    print('Ctas Aho     ',datetime.now())
    Cliente = justoAppModels.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justoAppModels.OFICINAS.objects.filter(codigo='A0001').first()
    with open('c:/ajusto/csv/S05CTAAHO.CSV', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader: 
            Socio = justoAppModels.ASOCIADOS.objects.filter(
                oficina = Oficina,cod_aso = row['s05codsoc']).first()
            if Socio == None:
                continue
            LinAho = justoAppModels.LINEAS_AHORRO.objects.filter(cliente = Cliente,cod_lin_aho = row['s05tipcta']).first()
            if LinAho == None:
                continue
            CtaAho = justoAppModels.CTAS_AHORRO.objects.filter(
                oficina = Oficina,num_cta = row['s05numcta']).first()
            if CtaAho == None:
                CtaAho = justoAppModels.CTAS_AHORRO.objects.create(
                        oficina = Oficina,num_cta = row['s05numcta'],lin_aho = LinAho,asociado = Socio)
            CtaAho.est_cta = row['s05estado']
            CtaAho.fec_apertura = asignar_fecha(row['s05fecape'],'%m/%d/%Y')
            CtaAho.fec_cancela = asignar_fecha('01/01/1900','%m/%d/%Y')
            CtaAho.exc_tas_mil = row['s05exegmf']
            CtaAho.fec_ini_exc = asignar_fecha(row['s05feciniexc'],'%m/%d/%Y')
            CtaAho.save()
    print('Fin ctas aho  ',datetime.now())    

def int_lin_aho():
    print('int_lin_aho  ',datetime.now())    
    Cliente = justoAppModels.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justoAppModels.OFICINAS.objects.filter(codigo='A0001').first()
    with open('c:/ajusto/csv/s08intlinaho.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader: 
            LinAho = justoAppModels.LINEAS_AHORRO.objects.filter(cliente=Cliente,cod_lin_aho=row['s08tipcta']).first()
            if LinAho == None:
                continue
            TasLinAho = justoAppModels.TAS_LIN_AHO.objects.filter(lin_aho=LinAho,
                    fecha_inicial=asignar_fecha(row['s08fecini'],'%m/%d/%Y')).first()
            if TasLinAho == None:
                TasLinAho = justoAppModels.TAS_LIN_AHO.objects.create(lin_aho=LinAho,
                    fecha_inicial=asignar_fecha(row['s08fecini'],'%m/%d/%Y'),tiae=0)
            TasLinAho.fecha_final = asignar_fecha(row['s08fecfin'],'%m/%d/%Y')
            TasLinAho.tiae = row['s08tasintanu']
            TasLinAho.save()
    print('          ',datetime.now())    

def ret_fue_aho():
    print('ret_fue_aho  ',datetime.now())    
    Cliente = justoAppModels.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justoAppModels.OFICINAS.objects.filter(codigo='A0001').first()
    with open('c:/ajusto/csv/s11parretfue.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader: 
            LinAho = justoAppModels.LINEAS_AHORRO.objects.filter(cliente=Cliente,cod_lin_aho=row['s11tipcta']).first()
            if LinAho == None:
                continue
            RetFueAho = justoAppModels.RET_FUE_AHO.objects.filter(lin_aho=LinAho,
                    fecha_inicial=asignar_fecha(row['s11fecini'],'%m/%d/%Y')).first()
            if RetFueAho == None:
                RetFueAho = justoAppModels.RET_FUE_AHO.objects.create(lin_aho=LinAho,
                    fecha_inicial=asignar_fecha(row['s11fecini'],'%m/%d/%Y'))
            RetFueAho.fecha_final = asignar_fecha(row['s11fecfin'],'%m/%d/%Y')
            RetFueAho.bas_liq_int = row['s11basliqdia'] 
            RetFueAho.tas_liq_rf = row['s11tasintretfue']
            RetFueAho.save()
    print('              ',datetime.now())    

def cta_cdat():
    print('CDAT    ',datetime.now())    
    Cliente = justoAppModels.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justoAppModels.OFICINAS.objects.filter(codigo='A0001').first()
    with open('c:/ajusto/csv/s20cdat.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader: 
            CtaAho = justoAppModels.CTAS_AHORRO.objects.filter(
                oficina = Oficina,num_cta = row['s20numcta']).first()
            if CtaAho == None:
                continue
            CtaCdat = justoAppModels.CTA_CDAT.objects.filter(cta_aho = CtaAho,ampliacion=row['s20ampliacion']).first()
            if CtaCdat == None:
                CtaCdat = justoAppModels.CTA_CDAT.objects.create(cta_aho = CtaAho,ampliacion=row['s20ampliacion']) 
            CtaCdat.valor = row['s20monto']
            CtaCdat.fecha = asignar_fecha(row['s20fecha'],'%m/%d/%Y')
            CtaCdat.plazo_mes = row['s20plazomes']
            CtaCdat.tiae = row['s20tasintanuefe']
            CtaCdat.Periodicidad = row['s20periodicidad']
            CtaCdat.cta_int_ret = row['s20ctaafeint']
            CtaCdat.aplicado = row['s20aplicado']
            CtaCdat.save()
    print('              ',datetime.now())    

def cta_cdat_amp():
    print('CDAT AMP  ',datetime.now())    
    Cliente = justoAppModels.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justoAppModels.OFICINAS.objects.filter(codigo='A0001').first()
    with open('c:/ajusto/csv/s21liqintcda.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader: 
            CtaAho = justoAppModels.CTAS_AHORRO.objects.filter(
                oficina = Oficina,num_cta = row['s21numcta']).first()
            if CtaAho == None:
                continue
            CtaCda = justoAppModels.CTA_CDAT.objects.filter(cta_aho = CtaAho,ampliacion=row['s21ampliacion']).first()
            if CtaCda == None:
                CtaCda = justoAppModels.CTA_CDAT.objects.create(cta_aho = CtaAho,ampliacion=row['s21ampliacion']) 
            if CtaCda == None:
                continue
            CtaCdaAmp = justoAppModels.CTA_CDAT_AMP.objects.filter(cta_aho = CtaAho,cta_amp = CtaCda,fecha = asignar_fecha(row['s21fecha'],'%m/%d/%Y')).first()
            if CtaCdaAmp == None:
                CtaCdaAmp = justoAppModels.CTA_CDAT_AMP.objects.create(cta_aho = CtaAho,cta_amp = CtaCda,fecha = asignar_fecha(row['s21fecha'],'%m/%d/%Y'))
            CtaCdaAmp.num_liq = row['s21numliqint']
            CtaCdaAmp.valor = row['s21valor']
            CtaCdaAmp.cta_aho_afe = row['s21ctaafe']
            CtaCdaAmp.clase = row['s21clase']
            CtaCdaAmp.documento = row['s21documento']
            CtaCdaAmp.aplicado = row['s21aplicado']
            CtaCdaAmp.save()
    print('            ',datetime.now())    

def cta_cda_liq():
    print('CDAT liq   ',datetime.now())    
    Cliente = justoAppModels.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justoAppModels.OFICINAS.objects.filter(codigo='A0001').first()
    with open('c:/ajusto/csv/s39histcdat.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader: 
            CtaAho = justoAppModels.CTAS_AHORRO.objects.filter(
                oficina = Oficina,num_cta = row['s39numcta']).first()
            if CtaAho == None:
                continue
            CtaCda = justoAppModels.CTA_CDAT.objects.filter(cta_aho = CtaAho,ampliacion=row['s39ampliacion']).first()
            if CtaCda == None:
                continue
            CtaCdatAmp = justoAppModels.CTA_CDAT_AMP.objects.filter(cta_aho = CtaAho,cta_amp =CtaCda).first()
            if CtaCdatAmp == None:
                continue 
            CtaCdatLiq = justoAppModels.CTA_CDAT_LIQ.objects.filter(cta_aho = CtaAho,cta_amp = CtaCdatAmp,
                fecha = asignar_fecha(row['s39fecha'],'%m/%d/%Y'),tip_liq = row['s39tipo']).first()
            if CtaCdatLiq == None:
                CtaCdatLiq = justoAppModels.CTA_CDAT_LIQ.objects.create(cta_aho = CtaAho,cta_amp = CtaCdatAmp,
                    fecha = asignar_fecha(row['s39fecha'],'%m/%d/%Y'),tip_liq = row['s39tipo'])
            CtaCdatLiq.Val_int = row['s39interes']
            CtaCdatLiq.Val_ret = row['s39retfue']
            CtaCdatLiq.Val_ret_nue = row['s39retfuenue']
            CtaCdatLiq.aplicado = row['s39aplicado']
            CtaCdatLiq.save()
    print('              ',datetime.now())    

def imp_con_cre():
    print('Imp Creditos   ',datetime.now())    
    Cliente = justoAppModels.CLIENTES.objects.filter(codigo='A').first()
    with open('c:/ajusto/csv/s16impconcre.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            ImpConCre = justoAppModels.IMP_CON_CRE.objects.filter(cliente=Cliente,cod_imp = row['s16codimp']).first()
            if ImpConCre == None:
                ImpConCre = justoAppModels.IMP_CON_CRE.objects.create(cliente=Cliente,cod_imp = row['s16codimp'])
            ImpConCre.descripcion = row['s16descripcion']
            ImpConCre.kcta_pte = ''
            ImpConCre.kcta_pro_gen_adi = row['s16ctaprogenadi'] 
            ImpConCre.kcta_pro_gen = row['s16ctaprogen']
            ImpConCre.kcta_gas_pro_gen = row['s16ctagasprogen']
            ImpConCre.kcta_rec_pro_gen = row['s16ctarecprogen']
            ImpConCre.kcta_gas_pro_ind = row['s16ctagasproind']
            ImpConCre.kcta_rec_pro_ind = row['s16ctarecproind']
            ImpConCre.icta_des_int_pp = ''
            ImpConCre.save()
    print('             ',datetime.now())

def imp_con_cre_int():
    print('Imp Int Creditos',datetime.now())    
    Cliente = justoAppModels.CLIENTES.objects.filter(codigo='A').first()
    with open('c:/ajusto/csv/s18impconcrecapcat.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            ImpConCreInt = justoAppModels.IMP_CON_CRE_INT.objects.filter(cliente=Cliente,cod_imp = row['s18codimp'],categoria = row['s18codcat']).first()
            if ImpConCreInt == None:
                ImpConCreInt = justoAppModels.IMP_CON_CRE_INT.objects.create(cliente=Cliente,cod_imp = row['s18codimp'],categoria = row['s18codcat'])
            ImpConCreInt.kcta_con = row['s18ctacon']
            ImpConCreInt.kcta_pro_ind = row['s18ctapro']
            ImpConCreInt.kporcentaje = row['s18porpro']
            ImpConCreInt.save()
    print('   Continua  ',datetime.now())    
    with open('c:/ajusto/csv/s34asicatint.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            if row['s34cuenta'] not in ["Ingreso","CtaPte","CxP","Error","IngRec","OrdenI"]:
                if row['s34cuenta'] == 'OrdenC':
                    xCat = 'C'
                elif row['s34cuenta'] == 'OrdenD':
                    xCat = 'D'
                elif row['s34cuenta'] == 'OrdenE':
                    xCat = 'E'
                elif row['s34cuenta'] == 'OrdenF':
                    xCat = 'F'
                else:
                    xCat = row['s34cat']
                ImpConCreInt = justoAppModels.IMP_CON_CRE_INT.objects.filter(cliente=Cliente,cod_imp = row['s34codimpcon'],categoria = xCat).first()
                if ImpConCreInt == None:
                    ImpConCreInt = justoAppModels.IMP_CON_CRE_INT.objects.create(cliente=Cliente,cod_imp = row['s34codimpcon'],categoria = xCat)
                elif row['s34cuenta'] == 'CxCa':
                    ImpConCreInt.cta_int = row['s34codcta']
                elif row['s34cuenta'] == 'CxCb':
                    ImpConCreInt.cta_int = row['s34codcta']
                elif row['s34cuenta'] == 'CxCc':
                    ImpConCreInt.cta_int = row['s34codcta']
                elif row['s34cuenta'] == 'CxCd':
                    ImpConCreInt.cta_int = row['s34codcta']
                elif row['s34cuenta'] == 'CxCe':
                    ImpConCreInt.cta_int = row['s34codcta']
                elif row['s34cuenta'] == 'CxCe':
                    ImpConCreInt.cta_int = row['s34codcta']
                elif row['s34cuenta'] == 'CxCf':
                    ImpConCreInt.cta_int = row['s34codcta']
                elif row['s34cuenta'] == 'OrdenC':
                    ImpConCreInt.cta_ord_int = row['s34codcta']
                elif row['s34cuenta'] == 'OrdenD':
                    ImpConCreInt.cta_ord_int = row['s34codcta']
                elif row['s34cuenta'] == 'OrdenE':
                    ImpConCreInt.cta_ord_int = row['s34codcta']
                elif row['s34cuenta'] == 'OrdenF':
                    ImpConCreInt.cta_ord_int = row['s34codcta']
                ImpConCreInt.save()
            else:
                ImpConCre = justoAppModels.IMP_CON_CRE.objects.filter(cliente=Cliente,cod_imp = row['s34codimpcon']).first()
                if ImpConCre == None:
                    ImpConCre = justoAppModels.IMP_CON_CRE.objects.create(cliente=Cliente,cod_imp = row['s34codimpcon'])
                if row['s34cuenta'] == 'CtaPte':
                    ImpConCre.kcta_pte_int = row['s34codcta']
                elif row['s34cuenta'] == 'Ingreso':
                    ImpConCre.kcta_ingreso = row['s34codcta']
                elif row['s34cuenta'] == 'CxP':
                    ImpConCre.cta_por_pag = row['s34codcta']
                elif row['s34cuenta'] == 'OrdenI':
                    ImpConCre.orden_i = row['s34codcta']
                elif row['s34cuenta'] == 'Error':
                    ImpConCre.cta_val = row['s34codcta']
                ImpConCre.save()
    print('             ',datetime.now())

def destino_cre():
    print('des Creditos   ',datetime.now())    
    Cliente = justoAppModels.CLIENTES.objects.filter(codigo='A').first()
    with open('c:/ajusto/csv/s17descre.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            DesCre = justoAppModels.DESTINO_CRE.objects.filter(cliente=Cliente,codigo = ord(row['s17coddescre'])).first()
            if DesCre == None:
                DesCre = justoAppModels.DESTINO_CRE.objects.create(cliente=Cliente,codigo = ord(row['s17coddescre']))
            DesCre.descripcion = row['s17descripcion']
            DesCre.save()
    print('des Creditos   ',datetime.now())    

def cat_des_dia_cre():
    print('des Dia Creditos   ',datetime.now())    
    Cliente = justoAppModels.CLIENTES.objects.filter(codigo='A').first()
    with open('c:/ajusto/csv/s19catdescre.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            CatDesDiaCre = justoAppModels.CAT_DES_DIA_CRE.objects.filter(cliente=Cliente,codigo = ord(row['s19coddescre']),categoria = row['s19codcat']).first()
            if CatDesDiaCre == None:
                CatDesDiaCre = justoAppModels.CAT_DES_DIA_CRE.objects.create(cliente=Cliente,codigo = ord(row['s19coddescre']),categoria = row['s19codcat'])
            CatDesDiaCre.minimo_dias = row['s19diamin']
            CatDesDiaCre.maximo_dias = row['s19diamax']
            CatDesDiaCre.save()
    print('        ',datetime.now())    

def lineas_credito():
    print('Lineas Credito   ',datetime.now())    
    Cliente = justoAppModels.CLIENTES.objects.filter(codigo='A').first()
    with open('c:/ajusto/csv/s14lincre.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            LinCre = justoAppModels.LINEAS_CREDITO.objects.filter(cliente=Cliente,cod_lin_cre = ord(row['s14codlincre'])).first()
            if LinCre == None:
                LinCre = justoAppModels.LINEAS_CREDITO.objects.create(cliente=Cliente,cod_lin_cre = ord(row['s14codlincre']))
            LinCre.descripcion = row['s14descripcion']
            LinCre.tas_int_anu = row['s14tasintanu']
            LinCre.tas_int_mor = row['s14tasintmor']
            LinCre.por_pol = row['s14porpol']
            LinCre.por_des_pp = row['s14pordespropag']
            LinCre.dia_con_int_mor = row['s14diaconintmor']
            LinCre.save()
    print('Lineas Credito   ',datetime.now()) 

def creditos():
    print('Creditos....  ',datetime.now())
    Cliente = justoAppModels.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justoAppModels.OFICINAS.objects.filter(codigo='A0001').first()
    with open('c:/ajusto/csv/s12creditos.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            Socio = justoAppModels.ASOCIADOS.objects.filter(oficina=Oficina,cod_aso=row['s12codsoc']).first()
            if Socio == None:
                print('Socio con Docto ',row['s12codsoc'], ' No existe con el credito ',row['s12codcre'])
                continue
            Credito = justoAppModels.CREDITOS.objects.filter(oficina=Oficina,cod_cre=row['s12codcre']).first()
            if Credito == None:
                Credito = justoAppModels.CREDITOS.objects.create(oficina=Oficina,cod_cre=row['s12codcre'],socio=Socio)
            ImpConCre = justoAppModels.IMP_CON_CRE.objects.filter(cliente = Cliente,cod_imp = row['s12codimpcon']).first()
            if ImpConCre==None:
                ImpConCre = justoAppModels.IMP_CON_CRE.objects.create(cliente = Cliente,cod_imp = row['s12codimpcon'])
            Credito.imputacion = ImpConCre
    #   Credito.com_des = ''
    #   Credito.com_ult_cau = models.ForeignKey(CREDITOS_CAUSA, on_delete=models.CASCADE,null = True)
            Credito.libranza = row['s12libranza']
            Credito.pagare = row['s12pagare']
            Credito.termino = row['s12termino']
            Credito.for_pag = row['s12forpag']
            Credito.fec_des = asignar_fecha(row['s12fecdes'],'%m/%d/%Y')
            Credito.fec_pag_ini = asignar_fecha(row['s12fecpagini'],'%m/%d/%Y')
            Credito.fec_ree = asignar_fecha('01/01/1900','%m/%d/%Y')
            Credito.fec_ven = asignar_fecha(row['s12fecpagini'],'%m/%d/%Y')
            Credito.fec_ult_pag = asignar_fecha(row['s12fecultpag'],'%m/%d/%Y')
            Credito.val_cuo_ini = row['s12valcuo']
            Credito.val_cuo_act = row['s12valcuo']
            Credito.num_cuo_ini = row['s12numcuo']
            Credito.num_cuo_act = row['s12numcuo']
            Credito.num_cuo_gra = row['s12numcuogra']
            Credito.per_ano = row['s12perano']
            Credito.tian_ic_ini = row['s12tasintanuini']
            Credito.tian_ic_act = row['s12tasintanu']
            Credito.tian_im = row['s12tasintmor']
            Credito.tian_pol_seg = row['s12porpol']
            Credito.por_des_pro_pag = row['s12pordespropag']
            Credito.decreciente = row['s12decreciente']
            Credito.estado = row['s12estjur']
            Credito.est_jur = row['s12estjur']
            Credito.cat_nue = row['s12nvocat']
            Credito.rep_cen_rie = row['s12repcenrie']
            Credito.val_gar_hip = row['s12valcomgarhip']
            Credito.mat_inm_gar = row['s12matinmgarhip']
            Credito.num_pol_gar_hip = row['s12numpolgh']
            Credito.figarantias = row['s12figrantias']
            Credito.save()
#   s12percom;s12reestructura;s12codcreres;s12cosjud;s12valcosjud;s12diaconintmor;s12notmor;s12fecnotmor;s12fecpol;
#   s12fecava;s12codseg;s12costo;s12individual;s12enobs;s12aprobado; s12catevacar
    print('              ',datetime.now())

def codeudores():
    print('Codeudores...  ',datetime.now())
    Cliente = justoAppModels.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justoAppModels.OFICINAS.objects.filter(codigo='A0001').first()
    with open('c:/ajusto/csv/s10codeudor.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            Credito = justoAppModels.CREDITOS.objects.filter(oficina=Oficina,cod_cre=row['s10codcre']).first()
            if Credito == None:
                continue
            Tercero = justoAppModels.TERCEROS.objects.filter(cliente=Cliente,doc_ide=row['s10nit']).first()
            if Tercero == None:
                continue
            Codeudor = justoAppModels.CODEUDORES.objects.filter(oficina=Oficina,credito=Credito,tercero=Tercero).first()
            if Codeudor == None:
                Codeudor = justoAppModels.CODEUDORES.objects.create(oficina=Oficina,credito=Credito,tercero=Tercero)
            Codeudor.save()
    print('          ...  ',datetime.now())

def init():
    inicio()
    #   terceros()
    #   pagadores()
    #   usuarios()
    #   cierre_mes()
    #   mov_caja()
    #   docto_conta()
    #   plan_ctas()
    #   conceptos()
    #   comprobantes()
    detalle_prod()
    #   detalle_econo()
    #   est_fin()
    #   socios()
    #   bene_aso()
    #   referencias()
    #   plan_aportes()
    #   linaho()
    #   imp_con_lin_aho()
    #   ctas_aho()
    #   int_lin_aho()
    #   ret_fue_aho()
    #   cta_cdat()
    #   cta_cdat_amp()
    #   cta_cda_liq()
    #   imp_con_cre()
    #   imp_con_cre_int()
    #   destino_cre()
    #   lineas_credito()
    #   cat_des_dia_cre()
    #   creditos()
    #   codeudores()

init()