from django.db import models
import re
from django.core.exceptions import ValidationError
from justo_app.models import validate_numeric
from justo_app.opciones import OPC_BOOL, OPC_REGIMEN, OPC_CLASEDOC, OPC_TIPTER
from clientes_app.models import CLIENTES
from localidades_app.models import LOCALIDADES

class TERCEROS(models.Model):
    cliente = models.ForeignKey(CLIENTES, on_delete=models.CASCADE)
    cla_doc = models.CharField(max_length=1, choices=OPC_CLASEDOC)
    doc_ide = models.CharField(max_length=12, null=False)
    dig_ver = models.CharField(max_length=1, null=True)
    nit_rap = models.CharField(max_length=12, null=True)
    cod_ciu_exp = models.ForeignKey(
        LOCALIDADES, on_delete=models.CASCADE, related_name='ciu_exp', null=True, blank=True)
    cod_ciu_res = models.ForeignKey(
        LOCALIDADES, on_delete=models.CASCADE, related_name='ciu_res', null=True, blank=True)
    regimen = models.CharField(max_length=12, choices=OPC_REGIMEN)
    fec_exp_ced = models.DateField(null=True, blank=True)
    tip_ter = models.CharField(max_length=12, choices=OPC_TIPTER)
    pri_ape = models.CharField(max_length=28, null=True)
    seg_ape = models.CharField(max_length=28, null=True)
    pri_nom = models.CharField(max_length=28, null=True)
    seg_nom = models.CharField(max_length=28, null=True)
    raz_soc = models.CharField(max_length=120, null=True)
    direccion = models.CharField(max_length=80, null=True)
    cod_pos = models.CharField(max_length=8, null=True)
    tel_ofi = models.CharField(max_length=10, null=True)
    tel_res = models.CharField(max_length=10, null=True)
    id_ds = models.BigIntegerField(null=True, db_index=True)
    celular1 = models.CharField(
        max_length=10,
        validators=[validate_numeric],
        help_text='El número de celular debe contener exactamente 10 dígitos numéricos.',
        null=True
    )
    celular2 = models.CharField(max_length=10, null=True)
    fax = models.CharField(max_length=10, null=True)
    email = models.EmailField()
    nombre = models.CharField(max_length=120, blank=True, null=True)
    fec_act = models.DateField(null=True, blank=True)
    observacion = models.CharField(max_length=255, null=True)
    per_pub_exp = models.CharField(max_length=1, choices=OPC_BOOL)
    nit_interno = models.CharField(max_length=1, choices=OPC_BOOL)

    def save(self, *args, **kwargs):
        if self.tip_ter == "N":
            self.nombre = """%s %s %s %s""" % (
                self.pri_ape, self.seg_ape, self.pri_nom, self.seg_nom)
        else:
            self.nombre = self.raz_soc
        super().save(*args, **kwargs)

    class Meta:
        unique_together = [['cliente', 'cla_doc', 'doc_ide']]
        db_table = 'terceros'
