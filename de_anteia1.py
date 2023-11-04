from datetime import date
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Justo_proy.settings')

# Initialize django application
import django
django.setup()
from datetime import datetime
import requests
import justo_app.models as justoAppModels

url = "https://dev.api.anteia.co/auth"

payload = {}
headers = {
  'Accept': 'application/json',
  'Authorization': 'Basic NjM2MTJhNzQwY2YwYWE0MzVhNjhmMjdmOmVlNWQ0MWM4ZGUwZjE1MDk4NDE2ZjQ2ODkzZmE0NzMxOWYwMWFkMDE5ZTU5ZWQ5ZDFhMDI0ODZmODQzYTEzYjg=',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
token = response.json()['token']

url = "https://dev.hyperflow.anteia.co/api/v2/hyperflow/getPendingSync/6527fd228cda1257e2422a73"

payload = {}
headers = {
  'Accept': 'application/json, application/xml',
  'Authorization': 'Bearer '+token
}
def init():
    response = requests.request("GET", url, headers=headers, data=payload)
    nom_arc = "c:/aaa/archivo"
    anteia1 = response.json()
    with open(nom_arc, 'w') as archivo:
        archivo.write(str(anteia1))

    Cliente = justoAppModels.CLIENTES.objects.filter(codigo='A').first()
    if Cliente == None:
        Cliente=justoAppModels.CLIENTES.objects.create(codigo="A",doc_ide='123456',sigla="COORINOQUIA")     
   
    for idsocio in anteia1['flows']:
        tipTra = anteia1['flows'][idsocio]['tipoTramite']       # Nv 
        #  Terceros 
        nombre = anteia1['flows'][idsocio]['user.fullName']     # Terceros Nombre
        ciuExpDoc =  anteia1['flows'][idsocio]['user.document.expeditionCity2']  # no tiene codigo
        print("ciuExpDoc",ciuExpDoc)
        direccion = anteia1['flows'][idsocio]['user.manualAdress.concat']
        #  Direcciones   
        dirTot = anteia1['flows'][idsocio]['user.manualAdress.numVia']
        dirTot = dirTot + ' '+anteia1['flows'][idsocio]['user.manualAdress.segundoNumero']
        dirTot = dirTot + ' '+anteia1['flows'][idsocio]['user.manualAdress.numViaDos']
        tipVia = anteia1['flows'][idsocio]['user.manualAdress.tipoVia']
        direccion = tipVia+' '+dirTot
        telefono = anteia1['flows'][idsocio]['user.phone']
        lacalizacion = anteia1['flows'][idsocio]['user.manualAdress.extra']
        dirRur = anteia1['flows'][idsocio]['user.manualAdress.rural']

        fec_Exp_Doc = anteia1['flows'][idsocio]['user.document.expeditionDate']
        
        email = anteia1['flows'][idsocio]['user.email']
        cod_ciu = anteia1['flows'][idsocio]['user.city.cod']
        Cliente = justoAppModels.CLIENTES.objects.filter(codigo='A').first()
        Localidad = justoAppModels.LOCALIDADES.objects.filter(cliente=Cliente,codigo='50001').first()
        Tercero = justoAppModels.TERCEROS.objects.filter(cliente=Cliente,
            cla_doc = 'C',
            doc_ide = anteia1['flows'][idsocio]['user.document.number']).first()
        if Tercero == None:
            Tercero = justoAppModels.TERCEROS.objects.create(
                cliente = Cliente,
                cla_doc = 'C',  # cla_doc = anteia1['flows'][idsocio]['user.document.type.cod'],
                doc_ide = anteia1['flows'][idsocio]['user.document.number']
            )
        Tercero.tip_ter = 'N'
        Tercero.pri_ape = anteia1['flows'][idsocio]['user.firstLastName']
        Tercero.seg_ape = anteia1['flows'][idsocio]['user.secondLastName']
        Tercero.pri_nom = anteia1['flows'][idsocio]['user.firstNameFirst']
        Tercero.seg_nom = anteia1['flows'][idsocio]['user.middleName']
        Tercero.direccion = direccion
        Tercero.nombre = nombre
        Tercero.dig_ver = ' '
        Tercero.nit_rap = ''
        Tercero.tel_res = telefono
        Tercero.celular1 = telefono
        Tercero.cod_ciu_exp = Localidad
        Tercero.cod_ciu_res = Localidad
        Tercero.fec_exp_ced = datetime.strptime(fec_Exp_Doc, "%d-%b-%Y").strftime("%Y-%m-%d")
        Tercero.email = email
        Tercero.fec_act = date.today()
        Tercero.regimen = 49
        Tercero.save()

        #   Asociados    
        cod_aso = anteia1['flows'][idsocio]['user.document.number'] # Ok
        sexo = anteia1['flows'][idsocio]['user.document.sex']
        est_civ = anteia1['flows'][idsocio]['user.civilState']
        fec_nac = anteia1['flows'][idsocio]['user.document.birthDate']  # Ok
        cod_ciu_nac = anteia1['flows'][idsocio]['user.document.birthPlaceUpper']
        ciu_res = anteia1['flows'][idsocio]['user.workInfo.city.cod']
        print("ciu_res",ciu_res)
        zona = anteia1['flows'][idsocio]['user.zone']
        estrato = anteia1['flows'][idsocio]['user.estrato']
        niv_est = anteia1['flows'][idsocio]['user.studiesLevel.cod']
        ocupacion = anteia1['flows'][idsocio]['user.ocupation']
        print("ocupacion=",ocupacion)
        break

        ocupacion_cod = anteia1['flows'][idsocio]['user.ocupation.cod']
        profesion = anteia1['flows'][idsocio]['user.tituloProfesional']
        cab_fam = anteia1['flows'][idsocio]['user.houseHolder']  # asociados
        fec_afi = anteia1['flows'][idsocio]['form.date']
        cargo_emp = anteia1['flows'][idsocio]['user.workInfo.position']
        per_a_cargo = anteia1['flows'][idsocio]['user.personsInCharge']
        num_hij_men = anteia1['flows'][idsocio]['user.numsChildren.menores']
        num_hij_may = anteia1['flows'][idsocio]['user.numsChildren.mayores']
        tip_viv = anteia1['flows'][idsocio]['user.home.type.cod']
        tie_en_ciu = anteia1['flows'][idsocio]['user.home.time']
        med_con = anteia1['flows'][idsocio]['coorinoquia.medioContacto']
        fec_ing_tra = anteia1['flows'][idsocio]['user.workInfo.startDate']
        tel_tra = anteia1['flows'][idsocio]['user.workInfo.phone']
        tip_sal = anteia1['flows'][idsocio]['user.workInfo.salaryType']
        ciu_tra = anteia1['flows'][idsocio]['user.workInfo.city']
        act_eco = anteia1['flows'][idsocio]['user.workInfo.economicActivity'] 
        cod_ciiu = anteia1['flows'][idsocio]['user.workInfo.ciiu']
        tip_con = anteia1['flows'][idsocio]['user.workInfo.contractType']
        nom_emp = anteia1['flows'][idsocio]['user.workInfo.company']
        nit_emp = anteia1['flows'][idsocio]['user.workInfo.nit']
        dir_emp = anteia1['flows'][idsocio]['user.workInfo.address']
        email_emp = anteia1['flows'][idsocio]['user.workInfo.email']
        sector_emp = anteia1['flows'][idsocio]['user.workInfo.sector']
        empresa_ant = anteia1['flows'][idsocio]['user.workInfo.tiempo']
        emp_num_emp = anteia1['flows'][idsocio]['user.workInfo.hasEmployees.quantity']
        #    negocio_lug = anteia1['flows'][idsocio]['user.workInfo.location']
        #    ocuEmp = anteia1['flows'][idsocio]['user.workInfo.occupation']
        negocio_pro = anteia1['flows'][idsocio]['user.workInfo.hasBusiness']
        negocio_nom = anteia1['flows'][idsocio]['user.business.name']
        negocio_tel = anteia1['flows'][idsocio]['user.business.owner.phone']
        negocio_loc_pro = anteia1['flows'][idsocio]['user.business.rental']
        negocio_cam_com = anteia1['flows'][idsocio]['user.business.camaraComercio']
        negocio_ant = anteia1['flows'][idsocio]['user.business.time']
        pension_ent = anteia1['flows'][idsocio]['user.pensioner.entity']
        pension_tie = anteia1['flows'][idsocio]['user.pensioner.startDate']
        pension_otr = anteia1['flows'][idsocio]['user.pensioner.other']
        pension_ent_otr = anteia1['flows'][idsocio]['user.pensioner.other.entity']
        pep_es_fam = anteia1['flows'][idsocio]['user.pep.esFamiliar']
        pep_fam_par = anteia1['flows'][idsocio]['user.pep.fam.parentesco']
        pep_fam_nom = anteia1['flows'][idsocio]['user.pep.fam.nombre']
        pep_car_pub = anteia1['flows'][idsocio]['user.ostentaCargoPublico']
        pep_cargo = anteia1['flows'][idsocio]['user.pep.cargo']
        pep_eje_pod = anteia1['flows'][idsocio]['user.ejercePoder']
        pep_adm_rec_est = anteia1['flows'][idsocio]['user.administraRecursos']
        
        tie_gre_car = anteia1['flows'][idsocio]['coorinoquia.fatca2']
        recibe_pag_ext = anteia1['flows'][idsocio]['coorinoquia.fatca3']
        recide_ext_mas_186 = anteia1['flows'][idsocio]['coorinoquia.fatca1']
        recibe_ing_ext = anteia1['flows'][idsocio]['coorinoquia.fatca4']

        # Estados Financieros
        ing_sal_fij = anteia1['flows'][idsocio]['user.financial.salary']
        ing_hon = anteia1['flows'][idsocio]['user.financial.honoraries']
        ing_pen = anteia1['flows'][idsocio]['user.financial.pension']
        ing_arr = anteia1['flows'][idsocio]['user.financial.otherIncome.act']  # no esta
        ing_com = anteia1['flows'][idsocio]['user.financial.pension']  # no esta
        ing_ext = anteia1['flows'][idsocio]['user.financial.extra']
        ing_otr = anteia1['flows'][idsocio]['user.financial.agregarOtros']
        ing_tot = anteia1['flows'][idsocio]['user.financial.totalIncomes']

        egr_sec_fin = anteia1['flows'][idsocio]['user.financial.familyExpenses']
        egr_cuo_hip = anteia1['flows'][idsocio]['user.financial.otherIncome']
        egr_des_nom = anteia1['flows'][idsocio]['user.financial.hasOtherExpenses']
        egr_gas_fam = anteia1['flows'][idsocio]['user.financial.personalExpenses']
        egr_otr_cre = anteia1['flows'][idsocio]['user.financial.creditCards']
        egr_arr = anteia1['flows'][idsocio]['user.financial.leasing']
        egr_otr_gas = anteia1['flows'][idsocio]['user.financial.otherExpenses']
        egr_tot = anteia1['flows'][idsocio]['user.financial.totalExpenses']

        act_otr_egr = anteia1['flows'][idsocio]['user.financial.otherExpenses.act']
        act_tip_bien = anteia1['flows'][idsocio]['coorinoquia.activos.tipo2']
        act_vei = anteia1['flows'][idsocio]['coorinoquia.activos.valorComercial2']
        act_otr = anteia1['flows'][idsocio]['coorinoquia.agregarActivo']
        tot_act = anteia1['flows'][idsocio]['user.financial.totalAssets']
        act_fin_rai =anteia1['flows'][idsocio]['coorinoquia.activos.valorComercial']
        act_inv = anteia1['flows'][idsocio]['coorinoquia.inversiones']
        escritura = anteia1['flows'][idsocio]['coorinoquia.activos.tipo']
        pas_otr = anteia1['flows'][idsocio]['coorinoquia.agregarPasivo']
        pas_tip = anteia1['flows'][idsocio]['coorinoquia.pasivos.tipo']
        tot_pat = anteia1['flows'][idsocio]['user.financial.totalEquity']
        pas_val = anteia1['flows'][idsocio]['coorinoquia.pasivos.valorComercial2']
        tot_pas = anteia1['flows'][idsocio]['coorinoquia.totalLiability']

        pas_des = anteia1['flows'][idsocio]['coorinoquia.pasivos.descripcion2']
        dec_ren = anteia1['flows'][idsocio]['coorinoquia.declaraciones.renta']
        tip_pas = anteia1['flows'][idsocio]['coorinoquia.pasivos.tipo2']
        des_pas = anteia1['flows'][idsocio]['coorinoquia.pasivos.descripcion']
        val_pas = anteia1['flows'][idsocio]['coorinoquia.pasivos.valorComercial']
        ope_mon_ext = anteia1['flows'][idsocio]['coorinoquia.declaraciones.realizaOperaciones']
        nom_ban_ext = anteia1['flows'][idsocio]['coorinoquia.productosExtranjeros.nombreEntidad']
        ope_monto_ext = anteia1['flows'][idsocio]['coorinoquia.operExtranjeras.monto']
        ope_pais_ext = anteia1['flows'][idsocio]['coorinoquia.operExtranjeras.pais']
        num_cta_ext = anteia1['flows'][idsocio]['coorinoquia.productosExtranjeros.numCuenta']
        tip_ope_ext = anteia1['flows'][idsocio]['coorinoquia.operExtranjeras.tipoOperacion']
        mon_ope_ext = anteia1['flows'][idsocio]['coorinoquia.operExtranjeras.moneda']
        prod_mon_ext = anteia1['flows'][idsocio]['coorinoquia.declaraciones.productosExtranjeros']
        des_prod_ext = anteia1['flows'][idsocio]['coorinoquia.productosExtranjeros.descripcion']
        mon_prod_ext = anteia1['flows'][idsocio]['coorinoquia.productosExtranjeros.moneda']
        pais_prod_ext =anteia1['flows'][idsocio]['coorinoquia.productosExtranjeros.pais']
        ciu_prod_ext = anteia1['flows'][idsocio]['coorinoquia.productosExtranjeros.ciudad']
        prom_prod_ext = anteia1['flows'][idsocio]['coorinoquia.productosExtranjeros.monto']

        #   Solicitud de creditos    
        lin_cre = anteia1['flows'][idsocio]['coorinoquia.solicitudCredito.linea']				
        monto = anteia1['flows'][idsocio]['coorinoquia.solicitudCredito.monto']				
        plazo = anteia1['flows'][idsocio]['coorinoquia.solicitudCredito.plazo']				
        garCreSol = anteia1['flows'][idsocio]['coorinoquia.solicitudCredito.garantia.cod']
        linCreSol = anteia1['flows'][idsocio]['coorinoquia.solicitudCredito.linea.cod']
        modCreSol = anteia1['flows'][idsocio]['coorinoquia.solicitudCredito.modalidad.cod']

        
        #  print(idsocio,nombre,"\n"," Referencias Personales")
        for refPer in anteia1['arrayData'][idsocio]['coorinoquia.referenciasPersonales']['data']:
            refPerdir = refPer['data']['direccion']
            refPerNom = refPer['data']['nombreCompleto']
            refPerTel = refPer['data']['telefono']

        for reffam in anteia1['arrayData'][idsocio]['coorinoquia.referenciasFamiliares']['data']:
            refFamPar = reffam['data']['parentesco']
            refFamDir = reffam['data']['direccion']
            refFamCel = reffam['data']['celular']
            refFamOcu = reffam['data']['ocupacion']
            refFamNomCom = reffam['data']['nombreCompleto']

        for beneficiario in anteia1['arrayData'][idsocio]['coorinoquia.beneficiarios']['data']:
            benTipDoc = beneficiario['data']['docType']
            benParentesco = beneficiario['data']['parentesco']
            benNumDoc = beneficiario['data']['numDoc']
            benorcentaje = beneficiario['data']['porcentaje']
            benNomCom = beneficiario['data']['nombreCompleto']

init()