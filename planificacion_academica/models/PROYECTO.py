# -*- coding: utf-8 -*-
##############################################################################
#
#    ODOO, Solución ERP de código abierto
#
#    Este programa es software libre: se puede redistribuir y / o modificar
#    bajo los términos de la GNU Affero General Public License
#
#    Debería haber recibido una copia de la Licencia Pública General GNU Affero
#    Junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.
#
##############################################################################
# Generado por el plugin Odoo V10 para Dia!

from odoo import api, fields, models
import math
class Estudiante(models.Model):
    """(NULL)"""
    _name = 'estudiante'
    #_rec_name = ''
    idestudiante = fields.Integer()
    uc1 = fields.Integer()
    uc2 = fields.Integer()
    uc3 = fields.Integer()
    uc4 = fields.Integer()
    uc5 = fields.Integer()
    uc6 = fields.Integer()
    uc7 = fields.Integer()
    uc8 = fields.Integer()
    uc9 = fields.Integer()
    uc10 = fields.Integer()
    uc11 = fields.Integer()
    uc12 = fields.Integer()
    uc13 = fields.Integer()
    uc14 = fields.Integer()
    uc15 = fields.Integer()
    uc16 = fields.Integer()
    uc17 = fields.Integer()
    uc18 = fields.Integer()
    uc19 = fields.Integer()

class Docente(models.Model):
    """(NULL)"""
    _name = 'docente'
    #_rec_name = ''
    iddocente = fields.Integer()
    ucdocente = fields.Integer()

class Estadistica(models.Model):

    _name = 'estadistica'

    idestudiante = fields.Many2one('estudiante', String='Estudiante')
    iddocente = fields.Many2one('docente', String='Docente')
    programaestadistica = fields.Char(string='Programa', default = 'PNFI - 2014')
    nucleoestadistica = fields.Char(string='Nucleo', default = 'La Urbina')
    turnoestadistica = fields.Char(string='Turno', default = 'Nocturno')

    """UNIDADES CURRICULARES PNFI 2014"""
    ucestadistica1 = fields.Char(string='Unidad Curricular', default = 'MATEMÁTICA APLICADA')
    ucestadistica2 = fields.Char(string='Unidad Curricular', default = 'FORMACIÓN CRÍTICA III')
    ucestadistica3 = fields.Char(string='Unidad Curricular', default = 'SISTEMAS OPERATIVOS')
    ucestadistica4 = fields.Char(string='Unidad Curricular', default = 'INGENIERÍA DEL SOFTWARE III')
    ucestadistica5 = fields.Char(string='Unidad Curricular', default = 'PROYECTO SOCIO TECNOLÓGICO III')
    ucestadistica6 = fields.Char(string='Unidad Curricular', default = 'MODELADO DE BASE DE DATOS')
    ucestadistica7 = fields.Char(string='Unidad Curricular', default = 'ELECTIVA III')
    ucestadistica8 = fields.Char(string='Unidad Curricular', default = 'INVESTIGACIÓN DE OPERACIONES III')
    ucestadistica9 = fields.Char(string='Unidad Curricular', default = 'INGLÉS')
    ucestadistica10 = fields.Char(string='Unidad Curricular', default = 'FORMACIÓN CRÍTICA IV')
    ucestadistica11 = fields.Char(string='Unidad Curricular', default = 'GESTIÓN DE PROYECTOS INFORMÁTICOS')
    ucestadistica12 = fields.Char(string='Unidad Curricular', default = 'ADMINISTRACIÓN DE BASES DE DATOS')
    ucestadistica13 = fields.Char(string='Unidad Curricular', default = 'REDES AVANZADAS')
    ucestadistica14 = fields.Char(string='Unidad Curricular', default = 'SEGURIDAD INFORMÁTICA')
    ucestadistica15 = fields.Char(string='Unidad Curricular', default = 'INGENIERÍA DEL SOFTWARE IV')
    ucestadistica16 = fields.Char(string='Unidad Curricular', default = 'INVESTIGACIÓN DE OPERACIONES IV')
    ucestadistica17 = fields.Char(string='Unidad Curricular', default = 'ELECTIVA IV')
    ucestadistica18 = fields.Char(string='Unidad Curricular', default = 'AUDITORÍA INFORMÁTICA')
    ucestadistica19 = fields.Char(string='Unidad Curricular', default = 'PROYECTO IV')

    """ESTADISTICAS ESTUDIANTES MATEMÁTICA APLICADA"""
    estudiantes1 = fields.Integer(string='Estudiantes que no han cursado', compute='_compute_estudiantes1', store=False)

    """DOCENTES"""
    docente1 = fields.Integer(string='Docentes disponibles', compute='_compute_docente1', store=False)

    """GRUPOS"""
    grupo1 = fields.Integer(string='Grupos', compute='_compute_grupo1', store=False)

    """FUNCIONES"""

    """ESTUDIANTES"""
    @api.depends('idestudiante')
    def _compute_estudiantes1(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc1 = '0'")
        resultestudiantes1 = self.env.cr.fetchone()
        countestudiantes1 = resultestudiantes1[0] if resultestudiantes1 else 0
        self.estudiantes1 = countestudiantes1

    def update_estudiantes1(self):
        self._compute_estudiantes1()

    """DOCENTES"""
    @api.depends('iddocente')
    def _compute_docente1(self):
        self.env.cr.execute("SELECT COUNT(*) FROM docente WHERE ucdocente = '1'")
        resultdocente1 = self.env.cr.fetchone()
        countdocente1 = resultdocente1[0] if resultdocente1 else 0
        self.docente1 = countdocente1

    def update_docente1(self):
        self._compute_docente1()

    """GRUPOS"""
    @api.depends('idestudiante')
    def _compute_grupo1(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc1 = '0'")
        resultgrupo1 = self.env.cr.fetchone()
        countgrupo1 = resultgrupo1[0] if resultgrupo1 else 0
        resultado_dividido1 = math.ceil((countgrupo1 / 30))
        self.grupo1 = resultado_dividido1

    def update_grupo1(self):
        self._compute_grupo1()

    """ESTADISTICAS ESTUDIANTES FORMACIÓN CRÍTICA III"""
    estudiantes2 = fields.Integer(string='Estudiantes que no han cursado', compute='_compute_estudiantes2', store=False)

    """DOCENTES"""
    docente2 = fields.Integer(string='Docentes disponibles', compute='_compute_docente2', store=False)

    """GRUPOS"""
    grupo2 = fields.Integer(string='Grupos', compute='_compute_grupo2', store=False)

    """FUNCIONES"""

    """ESTUDIANTES"""
    @api.depends('idestudiante')
    def _compute_estudiantes2(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc2 = '0'")
        resultestudiantes2 = self.env.cr.fetchone()
        countestudiantes2 = resultestudiantes2[0] if resultestudiantes2 else 0
        self.estudiantes2 = countestudiantes2

    def update_estudiantes2(self):
        self._compute_estudiantes2()

    """DOCENTES"""
    @api.depends('iddocente')
    def _compute_docente2(self):
        self.env.cr.execute("SELECT COUNT(*) FROM docente WHERE ucdocente = '2'")
        resultdocente2 = self.env.cr.fetchone()
        countdocente2 = resultdocente2[0] if resultdocente2 else 0
        self.docente2 = countdocente2

    def update_docente2(self):
        self._compute_docente2()

    """GRUPOS"""
    @api.depends('idestudiante')
    def _compute_grupo2(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc2 = '0'")
        resultgrupo2 = self.env.cr.fetchone()
        countgrupo2 = resultgrupo2[0] if resultgrupo2 else 0
        resultado_dividido2 = math.ceil((countgrupo2 / 30))
        self.grupo2 = resultado_dividido2

    def update_grupo2(self):
        self._compute_grupo2()


    """ESTADISTICAS ESTUDIANTES SISTEMAS OPERATIVOS"""
    estudiantes3 = fields.Integer(string='Estudiantes que no han cursado', compute='_compute_estudiantes3', store=False)

    """DOCENTES"""
    docente3 = fields.Integer(string='Docentes disponibles', compute='_compute_docente3', store=False)

    """GRUPOS"""
    grupo3 = fields.Integer(string='Grupos', compute='_compute_grupo3', store=False)

    """FUNCIONES"""

    """ESTUDIANTES"""
    @api.depends('idestudiante')
    def _compute_estudiantes3(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc3 = '0'")
        resultestudiantes3 = self.env.cr.fetchone()
        countestudiantes3 = resultestudiantes3[0] if resultestudiantes3 else 0
        self.estudiantes3 = countestudiantes3

    def update_estudiantes3(self):
        self._compute_estudiantes3()

    """DOCENTES"""
    @api.depends('iddocente')
    def _compute_docente3(self):
        self.env.cr.execute("SELECT COUNT(*) FROM docente WHERE ucdocente = '3'")
        resultdocente3 = self.env.cr.fetchone()
        countdocente3 = resultdocente3[0] if resultdocente3 else 0
        self.docente3 = countdocente3

    def update_docente3(self):
        self._compute_docente3()

    """GRUPOS"""
    @api.depends('idestudiante')
    def _compute_grupo3(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc3 = '0'")
        resultgrupo3 = self.env.cr.fetchone()
        countgrupo3 = resultgrupo3[0] if resultgrupo3 else 0
        resultado_dividido3 = math.ceil((countgrupo3 / 30))
        self.grupo3 = resultado_dividido3

    def update_grupo3(self):
        self._compute_grupo3()


    """ESTADISTICAS ESTUDIANTES INGENIERÍA DEL SOFTWARE III"""
    estudiantes4 = fields.Integer(string='Estudiantes que no han cursado', compute='_compute_estudiantes4', store=False)

    """DOCENTES"""
    docente4 = fields.Integer(string='Docentes disponibles', compute='_compute_docente4', store=False)

    """GRUPOS"""
    grupo4 = fields.Integer(string='Grupos', compute='_compute_grupo4', store=False)

    """FUNCIONES"""

    """ESTUDIANTES"""
    @api.depends('idestudiante')
    def _compute_estudiantes4(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc4 = '0'")
        resultestudiantes4 = self.env.cr.fetchone()
        countestudiantes4 = resultestudiantes4[0] if resultestudiantes4 else 0
        self.estudiantes4 = countestudiantes4

    def update_estudiantes4(self):
        self._compute_estudiantes4()

    """DOCENTES"""
    @api.depends('iddocente')
    def _compute_docente4(self):
        self.env.cr.execute("SELECT COUNT(*) FROM docente WHERE ucdocente = '4'")
        resultdocente4 = self.env.cr.fetchone()
        countdocente4 = resultdocente4[0] if resultdocente4 else 0
        self.docente4 = countdocente4

    def update_docente4(self):
        self._compute_docente4()

    """GRUPOS"""
    @api.depends('idestudiante')
    def _compute_grupo4(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc4 = '0'")
        resultgrupo4 = self.env.cr.fetchone()
        countgrupo4 = resultgrupo4[0] if resultgrupo4 else 0
        resultado_dividido4 = math.ceil((countgrupo4 / 30))
        self.grupo4 = resultado_dividido4

    def update_grupo4(self):
        self._compute_grupo4()


    """ESTADISTICAS ESTUDIANTES PROYECTO SOCIOTECNOLÓGICO III"""
    estudiantes5 = fields.Integer(string='Estudiantes que no han cursado', compute='_compute_estudiantes5', store=False)

    """DOCENTES"""
    docente5 = fields.Integer(string='Docentes disponibles', compute='_compute_docente5', store=False)

    """GRUPOS"""
    grupo5 = fields.Integer(string='Grupos', compute='_compute_grupo5', store=False)

    """FUNCIONES"""

    """ESTUDIANTES"""
    @api.depends('idestudiante')
    def _compute_estudiantes5(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc5 = '0'")
        resultestudiantes5 = self.env.cr.fetchone()
        countestudiantes5 = resultestudiantes5[0] if resultestudiantes5 else 0
        self.estudiantes5 = countestudiantes5

    def update_estudiantes5(self):
        self._compute_estudiantes5()

    """DOCENTES"""
    @api.depends('iddocente')
    def _compute_docente5(self):
        self.env.cr.execute("SELECT COUNT(*) FROM docente WHERE ucdocente = '5'")
        resultdocente5 = self.env.cr.fetchone()
        countdocente5 = resultdocente5[0] if resultdocente5 else 0
        self.docente5 = countdocente5

    def update_docente5(self):
        self._compute_docente5()

    """GRUPOS"""
    @api.depends('idestudiante')
    def _compute_grupo5(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc5 = '0'")
        resultgrupo5 = self.env.cr.fetchone()
        countgrupo5 = resultgrupo5[0] if resultgrupo5 else 0
        resultado_dividido5 = math.ceil((countgrupo5 / 30))
        self.grupo5 = resultado_dividido5

    def update_grupo5(self):
        self._compute_grupo5()

    """ESTADISTICAS ESTUDIANTES MODELADO DE BASE DE DATOS"""
    estudiantes6 = fields.Integer(string='Estudiantes que no han cursado', compute='_compute_estudiantes6', store=False)

    """DOCENTES"""
    docente6 = fields.Integer(string='Docentes disponibles', compute='_compute_docente6', store=False)

    """GRUPOS"""
    grupo6 = fields.Integer(string='Grupos', compute='_compute_grupo6', store=False)

    """FUNCIONES"""

    """ESTUDIANTES"""
    @api.depends('idestudiante')
    def _compute_estudiantes6(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc6 = '0'")
        resultestudiantes6 = self.env.cr.fetchone()
        countestudiantes6 = resultestudiantes6[0] if resultestudiantes6 else 0
        self.estudiantes6 = countestudiantes6

    def update_estudiantes6(self):
        self._compute_estudiantes6()

    """DOCENTES"""
    @api.depends('iddocente')
    def _compute_docente6(self):
        self.env.cr.execute("SELECT COUNT(*) FROM docente WHERE ucdocente = '6'")
        resultdocente6 = self.env.cr.fetchone()
        countdocente6 = resultdocente6[0] if resultdocente6 else 0
        self.docente6 = countdocente6

    def update_docente6(self):
        self._compute_docente6()

    """GRUPOS"""
    @api.depends('idestudiante')
    def _compute_grupo6(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc6 = '0'")
        resultgrupo6 = self.env.cr.fetchone()
        countgrupo6 = resultgrupo6[0] if resultgrupo6 else 0
        resultado_dividido6 = math.ceil((countgrupo6 / 30))
        self.grupo6 = resultado_dividido6

    def update_grupo6(self):
        self._compute_grupo6()

    """ESTADISTICAS ESTUDIANTES ELECTIVA III"""
    estudiantes7 = fields.Integer(string='Estudiantes que no han cursado', compute='_compute_estudiantes7', store=False)

    """DOCENTES"""
    docente7 = fields.Integer(string='Docentes disponibles', compute='_compute_docente7', store=False)

    """GRUPOS"""
    grupo7 = fields.Integer(string='Grupos', compute='_compute_grupo7', store=False)

    """FUNCIONES"""

    """ESTUDIANTES"""
    @api.depends('idestudiante')
    def _compute_estudiantes7(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc7 = '0'")
        resultestudiantes7 = self.env.cr.fetchone()
        countestudiantes7 = resultestudiantes7[0] if resultestudiantes7 else 0
        self.estudiantes7 = countestudiantes7

    def update_estudiantes7(self):
        self._compute_estudiantes7()

    """DOCENTES"""
    @api.depends('iddocente')
    def _compute_docente7(self):
        self.env.cr.execute("SELECT COUNT(*) FROM docente WHERE ucdocente = '7'")
        resultdocente7 = self.env.cr.fetchone()
        countdocente7 = resultdocente7[0] if resultdocente7 else 0
        self.docente7 = countdocente7

    def update_docente7(self):
        self._compute_docente7()

    """GRUPOS"""
    @api.depends('idestudiante')
    def _compute_grupo7(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc7 = '0'")
        resultgrupo7 = self.env.cr.fetchone()
        countgrupo7 = resultgrupo7[0] if resultgrupo7 else 0
        resultado_dividido7 = math.ceil((countgrupo7 / 30))
        self.grupo7 = resultado_dividido7

    def update_grupo7(self):
        self._compute_grupo7()


    """ESTADISTICAS ESTUDIANTES INVESTIGACIÓN DE OPERACIONES"""
    estudiantes8 = fields.Integer(string='Estudiantes que no han cursado', compute='_compute_estudiantes8', store=False)

    """DOCENTES"""
    docente8 = fields.Integer(string='Docentes disponibles', compute='_compute_docente8', store=False)

    """GRUPOS"""
    grupo8 = fields.Integer(string='Grupos', compute='_compute_grupo8', store=False)

    """FUNCIONES"""

    """ESTUDIANTES"""
    @api.depends('idestudiante')
    def _compute_estudiantes8(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc8 = '0'")
        resultestudiantes8 = self.env.cr.fetchone()
        countestudiantes8 = resultestudiantes8[0] if resultestudiantes8 else 0
        self.estudiantes8 = countestudiantes8

    def update_estudiantes8(self):
        self._compute_estudiantes8()

    """DOCENTES"""
    @api.depends('iddocente')
    def _compute_docente8(self):
        self.env.cr.execute("SELECT COUNT(*) FROM docente WHERE ucdocente = '8'")
        resultdocente8 = self.env.cr.fetchone()
        countdocente8 = resultdocente8[0] if resultdocente8 else 0
        self.docente8 = countdocente8

    def update_docente8(self):
        self._compute_docente8()

    
    """GRUPOS"""
    @api.depends('idestudiante')
    def _compute_grupo8(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc8 = '0'")
        resultgrupo8 = self.env.cr.fetchone()
        countgrupo8 = resultgrupo8[0] if resultgrupo8 else 0
        resultado_dividido8 = math.ceil((countgrupo8 / 30))
        self.grupo8 = resultado_dividido8

    def update_grupo8(self):
        self._compute_grupo8()

    """ESTADISTICAS ESTUDIANTES INGLÉS"""
    estudiantes9 = fields.Integer(string='Estudiantes que no han cursado', compute='_compute_estudiantes9', store=False)

    """DOCENTES"""
    docente9 = fields.Integer(string='Docentes disponibles', compute='_compute_docente9', store=False)

    """GRUPOS"""
    grupo9 = fields.Integer(string='Grupos', compute='_compute_grupo9', store=False)

    """FUNCIONES"""

    """ESTUDIANTES"""
    @api.depends('idestudiante')
    def _compute_estudiantes9(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc9 = '0'")
        resultestudiantes9 = self.env.cr.fetchone()
        countestudiantes9 = resultestudiantes9[0] if resultestudiantes9 else 0
        self.estudiantes9 = countestudiantes9

    def update_estudiantes9(self):
        self._compute_estudiantes9()

    """DOCENTES"""
    @api.depends('iddocente')
    def _compute_docente9(self):
        self.env.cr.execute("SELECT COUNT(*) FROM docente WHERE ucdocente = '9'")
        resultdocente9 = self.env.cr.fetchone()
        countdocente9 = resultdocente9[0] if resultdocente9 else 0
        self.docente9 = countdocente9

    def update_docente9(self):
        self._compute_docente9()

    """GRUPOS"""
    @api.depends('idestudiante')
    def _compute_grupo9(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc9 = '0'")
        resultgrupo9 = self.env.cr.fetchone()
        countgrupo9 = resultgrupo9[0] if resultgrupo9 else 0
        resultado_dividido9 = math.ceil((countgrupo9 / 30))
        self.grupo9 = resultado_dividido9

    def update_grupo9(self):
        self._compute_grupo9()

    """ESTADISTICAS ESTUDIANTES FORMACIÓN CRÍTICA IV"""
    estudiantes10 = fields.Integer(string='Estudiantes que no han cursado', compute='_compute_estudiantes10', store=False)

    """DOCENTES"""
    docente10 = fields.Integer(string='Docentes disponibles', compute='_compute_docente10', store=False)

    """GRUPOS"""
    grupo10 = fields.Integer(string='Grupos', compute='_compute_grupo10', store=False)

    """FUNCIONES"""

    """ESTUDIANTES"""
    @api.depends('idestudiante')
    def _compute_estudiantes10(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc10 = '0'")
        resultestudiantes10 = self.env.cr.fetchone()
        countestudiantes10 = resultestudiantes10[0] if resultestudiantes10 else 0
        self.estudiantes10 = countestudiantes10

    def update_estudiantes10(self):
        self._compute_estudiantes10()

    """DOCENTES"""
    @api.depends('iddocente')
    def _compute_docente10(self):
        self.env.cr.execute("SELECT COUNT(*) FROM docente WHERE ucdocente = '10'")
        resultdocente10 = self.env.cr.fetchone()
        countdocente10 = resultdocente10[0] if resultdocente10 else 0
        self.docente10 = countdocente10

    def update_docente10(self):
        self._compute_docente10()

    """GRUPOS"""
    @api.depends('idestudiante')
    def _compute_grupo10(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc10 = '0'")
        resultgrupo10 = self.env.cr.fetchone()
        countgrupo10 = resultgrupo10[0] if resultgrupo10 else 0
        resultado_dividido10 = math.ceil((countgrupo10 / 30))
        self.grupo10 = resultado_dividido10

    def update_grupo10(self):
        self._compute_grupo10()

    """ESTADISTICAS ESTUDIANTES GESTIÓN DE PROYECTOS INFORMÁTICOS"""
    estudiantes11 = fields.Integer(string='Estudiantes que no han cursado', compute='_compute_estudiantes11', store=False)

    """DOCENTES"""
    docente11 = fields.Integer(string='Docentes disponibles', compute='_compute_docente11', store=False)

    """GRUPOS"""
    grupo11 = fields.Integer(string='Grupos', compute='_compute_grupo11', store=False)

    """FUNCIONES"""

    """ESTUDIANTES"""
    @api.depends('idestudiante')
    def _compute_estudiantes11(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc11 = '0'")
        resultestudiantes11 = self.env.cr.fetchone()
        countestudiantes11 = resultestudiantes11[0] if resultestudiantes11 else 0
        self.estudiantes11 = countestudiantes11

    def update_estudiantes11(self):
        self._compute_estudiantes11()

    """DOCENTES"""
    @api.depends('iddocente')
    def _compute_docente11(self):
        self.env.cr.execute("SELECT COUNT(*) FROM docente WHERE ucdocente = '11'")
        resultdocente11 = self.env.cr.fetchone()
        countdocente11 = resultdocente11[0] if resultdocente11 else 0
        self.docente11 = countdocente11

    def update_docente11(self):
        self._compute_docente11()

    """GRUPOS"""
    @api.depends('idestudiante')
    def _compute_grupo11(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc11 = '0'")
        resultgrupo11 = self.env.cr.fetchone()
        countgrupo11 = resultgrupo11[0] if resultgrupo11 else 0
        resultado_dividido11 = math.ceil((countgrupo11 / 30))
        self.grupo11 = resultado_dividido11

    def update_grupo11(self):
        self._compute_grupo11()

    """ESTADISTICAS ESTUDIANTES ADMINISTRACIÓN DE BASES DE DATOS"""
    estudiantes12 = fields.Integer(string='Estudiantes que no han cursado', compute='_compute_estudiantes12', store=False)

    """DOCENTES"""
    docente12 = fields.Integer(string='Docentes disponibles', compute='_compute_docente12', store=False)

    """GRUPOS"""
    grupo12 = fields.Integer(string='Grupos', compute='_compute_grupo12', store=False)

    """FUNCIONES"""

    """ESTUDIANTES"""
    @api.depends('idestudiante')
    def _compute_estudiantes12(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc12 = '0'")
        resultestudiantes12 = self.env.cr.fetchone()
        countestudiantes12 = resultestudiantes12[0] if resultestudiantes12 else 0
        self.estudiantes12 = countestudiantes12

    def update_estudiantes12(self):
        self._compute_estudiantes12()

    """DOCENTES"""
    @api.depends('iddocente')
    def _compute_docente12(self):
        self.env.cr.execute("SELECT COUNT(*) FROM docente WHERE ucdocente = '12'")
        resultdocente12 = self.env.cr.fetchone()
        countdocente12 = resultdocente12[0] if resultdocente12 else 0
        self.docente12 = countdocente12

    def update_docente12(self):
        self._compute_docente12()

    """GRUPOS"""
    @api.depends('idestudiante')
    def _compute_grupo12(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc12 = '0'")
        resultgrupo12 = self.env.cr.fetchone()
        countgrupo12 = resultgrupo12[0] if resultgrupo12 else 0
        resultado_dividido12 = math.ceil((countgrupo12 / 30))
        self.grupo12 = resultado_dividido12

    def update_grupo12(self):
        self._compute_grupo12()

    """ESTADISTICAS ESTUDIANTES REDES AVANZADAS"""
    estudiantes13 = fields.Integer(string='Estudiantes que no han cursado', compute='_compute_estudiantes13', store=False)

    """DOCENTES"""
    docente13 = fields.Integer(string='Docentes disponibles', compute='_compute_docente13', store=False)

    """GRUPOS"""
    grupo13 = fields.Integer(string='Grupos', compute='_compute_grupo13', store=False)

    """FUNCIONES"""

    """ESTUDIANTES"""
    @api.depends('idestudiante')
    def _compute_estudiantes13(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc13 = '0'")
        resultestudiantes13 = self.env.cr.fetchone()
        countestudiantes13 = resultestudiantes13[0] if resultestudiantes13 else 0
        self.estudiantes13 = countestudiantes13

    def update_estudiantes13(self):
        self._compute_estudiantes13()

    """DOCENTES"""
    @api.depends('iddocente')
    def _compute_docente13(self):
        self.env.cr.execute("SELECT COUNT(*) FROM docente WHERE ucdocente = '13'")
        resultdocente13 = self.env.cr.fetchone()
        countdocente13 = resultdocente13[0] if resultdocente13 else 0
        self.docente13 = countdocente13

    def update_docente13(self):
        self._compute_docente13()

    """GRUPOS"""
    @api.depends('idestudiante')
    def _compute_grupo13(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc13 = '0'")
        resultgrupo13 = self.env.cr.fetchone()
        countgrupo13 = resultgrupo13[0] if resultgrupo13 else 0
        resultado_dividido13 = math.ceil((countgrupo13 / 30))
        self.grupo13 = resultado_dividido13

    def update_grupo13(self):
        self._compute_grupo13()

    """ESTADISTICAS ESTUDIANTES SEGURIDAD INFORMÁTICA"""
    estudiantes14 = fields.Integer(string='Estudiantes que no han cursado', compute='_compute_estudiantes14', store=False)

    """DOCENTES"""
    docente14 = fields.Integer(string='Docentes disponibles', compute='_compute_docente14', store=False)

    """GRUPOS"""
    grupo14 = fields.Integer(string='Grupos', compute='_compute_grupo14', store=False)

    """FUNCIONES"""

    """ESTUDIANTES"""
    @api.depends('idestudiante')
    def _compute_estudiantes14(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc14 = '0'")
        resultestudiantes14 = self.env.cr.fetchone()
        countestudiantes14 = resultestudiantes14[0] if resultestudiantes14 else 0
        self.estudiantes14 = countestudiantes14

    def update_estudiantes14(self):
        self._compute_estudiantes14()

    """DOCENTES"""
    @api.depends('iddocente')
    def _compute_docente14(self):
        self.env.cr.execute("SELECT COUNT(*) FROM docente WHERE ucdocente = '14'")
        resultdocente14 = self.env.cr.fetchone()
        countdocente14 = resultdocente14[0] if resultdocente14 else 0
        self.docente14 = countdocente14

    def update_docente14(self):
        self._compute_docente14()

    """GRUPOS"""
    @api.depends('idestudiante')
    def _compute_grupo14(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc14 = '0'")
        resultgrupo14 = self.env.cr.fetchone()
        countgrupo14 = resultgrupo14[0] if resultgrupo14 else 0
        resultado_dividido14 = math.ceil((countgrupo14 / 30))
        self.grupo14 = resultado_dividido14

    def update_grupo14(self):
        self._compute_grupo14()


    """ESTADISTICAS ESTUDIANTES INGENIERÍA DEL SOFTWARE IV"""
    estudiantes15 = fields.Integer(string='Estudiantes que no han cursado', compute='_compute_estudiantes15', store=False)

    """DOCENTES"""
    docente15 = fields.Integer(string='Docentes disponibles', compute='_compute_docente15', store=False)

    """GRUPOS"""
    grupo15 = fields.Integer(string='Grupos', compute='_compute_grupo15', store=False)

    """FUNCIONES"""

    """ESTUDIANTES"""
    @api.depends('idestudiante')
    def _compute_estudiantes15(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc15 = '0'")
        resultestudiantes15 = self.env.cr.fetchone()
        countestudiantes15 = resultestudiantes15[0] if resultestudiantes15 else 0
        self.estudiantes15 = countestudiantes15

    def update_estudiantes15(self):
        self._compute_estudiantes15()

    """DOCENTES"""
    @api.depends('iddocente')
    def _compute_docente15(self):
        self.env.cr.execute("SELECT COUNT(*) FROM docente WHERE ucdocente = '15'")
        resultdocente15 = self.env.cr.fetchone()
        countdocente15 = resultdocente15[0] if resultdocente15 else 0
        self.docente15 = countdocente15

    def update_docente15(self):
        self._compute_docente15()

    """GRUPOS"""
    @api.depends('idestudiante')
    def _compute_grupo15(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc15 = '0'")
        resultgrupo15 = self.env.cr.fetchone()
        countgrupo15 = resultgrupo15[0] if resultgrupo15 else 0
        resultado_dividido15 = math.ceil((countgrupo15 / 30))
        self.grupo15 = resultado_dividido15

    def update_grupo15(self):
        self._compute_grupo15()

    """ESTADISTICAS ESTUDIANTES INVESTIGACIÓN DE OPERACIONES"""
    estudiantes16 = fields.Integer(string='Estudiantes que no han cursado', compute='_compute_estudiantes16', store=False)

    """DOCENTES"""
    docente16 = fields.Integer(string='Docentes disponibles', compute='_compute_docente16', store=False)

    """GRUPOS"""
    grupo16 = fields.Integer(string='Grupos', compute='_compute_grupo16', store=False)

    """FUNCIONES"""

    """ESTUDIANTES"""
    @api.depends('idestudiante')
    def _compute_estudiantes16(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc16 = '0'")
        resultestudiantes16 = self.env.cr.fetchone()
        countestudiantes16 = resultestudiantes16[0] if resultestudiantes16 else 0
        self.estudiantes16 = countestudiantes16

    def update_estudiantes16(self):
        self._compute_estudiantes16()

    """DOCENTES"""
    @api.depends('iddocente')
    def _compute_docente16(self):
        self.env.cr.execute("SELECT COUNT(*) FROM docente WHERE ucdocente = '16'")
        resultdocente16 = self.env.cr.fetchone()
        countdocente16 = resultdocente16[0] if resultdocente16 else 0
        self.docente16 = countdocente16

    def update_docente16(self):
        self._compute_docente16()

    """GRUPOS"""
    @api.depends('idestudiante')
    def _compute_grupo16(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc16 = '0'")
        resultgrupo16 = self.env.cr.fetchone()
        countgrupo16 = resultgrupo16[0] if resultgrupo16 else 0
        resultado_dividido16 = math.ceil((countgrupo16 / 30))
        self.grupo16 = resultado_dividido16

    def update_grupo16(self):
        self._compute_grupo16()

    """ESTADISTICAS ESTUDIANTES ELECTIVA IV"""
    estudiantes17 = fields.Integer(string='Estudiantes que no han cursado', compute='_compute_estudiantes17', store=False)

    """DOCENTES"""
    docente17 = fields.Integer(string='Docentes disponibles', compute='_compute_docente17', store=False)

    """GRUPOS"""
    grupo17 = fields.Integer(string='Grupos', compute='_compute_grupo17', store=False)

    """FUNCIONES"""

    """ESTUDIANTES"""
    @api.depends('idestudiante')
    def _compute_estudiantes17(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc17 = '0'")
        resultestudiantes17 = self.env.cr.fetchone()
        countestudiantes17 = resultestudiantes17[0] if resultestudiantes17 else 0
        self.estudiantes17 = countestudiantes17

    def update_estudiantes17(self):
        self._compute_estudiantes17()

    """DOCENTES"""
    @api.depends('iddocente')
    def _compute_docente17(self):
        self.env.cr.execute("SELECT COUNT(*) FROM docente WHERE ucdocente = '17'")
        resultdocente17 = self.env.cr.fetchone()
        countdocente17 = resultdocente17[0] if resultdocente17 else 0
        self.docente17 = countdocente17

    def update_docente17(self):
        self._compute_docente17()

        
    """GRUPOS"""
    @api.depends('idestudiante')
    def _compute_grupo17(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc17 = '0'")
        resultgrupo17 = self.env.cr.fetchone()
        countgrupo17 = resultgrupo17[0] if resultgrupo17 else 0
        resultado_dividido17 = math.ceil((countgrupo17 / 30))
        self.grupo17 = resultado_dividido17

    def update_grupo17(self):
        self._compute_grupo17()

    """ESTADISTICAS ESTUDIANTES AUDITORÍA INFORMÁTICA"""
    estudiantes18 = fields.Integer(string='Estudiantes que no han cursado', compute='_compute_estudiantes18', store=False)

    """DOCENTES"""
    docente18 = fields.Integer(string='Docentes disponibles', compute='_compute_docente18', store=False)

    """GRUPOS"""
    grupo18 = fields.Integer(string='Grupos', compute='_compute_grupo18', store=False)

    """FUNCIONES"""

    """ESTUDIANTES"""
    @api.depends('idestudiante')
    def _compute_estudiantes18(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc18 = '0'")
        resultestudiantes18 = self.env.cr.fetchone()
        countestudiantes18 = resultestudiantes18[0] if resultestudiantes18 else 0
        self.estudiantes18 = countestudiantes18

    def update_estudiantes18(self):
        self._compute_estudiantes18()

    """DOCENTES"""
    @api.depends('iddocente')
    def _compute_docente18(self):
        self.env.cr.execute("SELECT COUNT(*) FROM docente WHERE ucdocente = '18'")
        resultdocente18 = self.env.cr.fetchone()
        countdocente18 = resultdocente18[0] if resultdocente18 else 0
        self.docente18 = countdocente18

    def update_docente18(self):
        self._compute_docente18() 

    
    """GRUPOS"""
    @api.depends('idestudiante')
    def _compute_grupo18(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc18 = '0'")
        resultgrupo18 = self.env.cr.fetchone()
        countgrupo18 = resultgrupo18[0] if resultgrupo18 else 0
        resultado_dividido18 = math.ceil((countgrupo18 / 30))
        self.grupo18 = resultado_dividido18

    def update_grupo18(self):
        self._compute_grupo18()

    """ESTADISTICAS ESTUDIANTES PROYECTO"""
    estudiantes19 = fields.Integer(string='Estudiantes que no han cursado', compute='_compute_estudiantes19', store=False)

    """DOCENTES"""
    docente19 = fields.Integer(string='Docentes disponibles', compute='_compute_docente19', store=False)

    """GRUPOS"""
    grupo19 = fields.Integer(string='Grupos', compute='_compute_grupo19', store=False)

    """FUNCIONES"""

    """ESTUDIANTES"""
    @api.depends('idestudiante')
    def _compute_estudiantes19(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc19 = '0'")
        resultestudiantes19 = self.env.cr.fetchone()
        countestudiantes19 = resultestudiantes19[0] if resultestudiantes19 else 0
        self.estudiantes19 = countestudiantes19

    def update_estudiantes19(self):
        self._compute_estudiantes19()

    """DOCENTES"""
    @api.depends('iddocente')
    def _compute_docente19(self):
        self.env.cr.execute("SELECT COUNT(*) FROM docente WHERE ucdocente = '19'")
        resultdocente19 = self.env.cr.fetchone()
        countdocente19 = resultdocente19[0] if resultdocente19 else 0
        self.docente19 = countdocente19

    def update_docente19(self):
        self._compute_docente19() 

    """GRUPOS"""
    @api.depends('idestudiante')
    def _compute_grupo19(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE uc19 = '0'")
        resultgrupo19 = self.env.cr.fetchone()
        countgrupo19 = resultgrupo19[0] if resultgrupo19 else 0
        resultado_dividido19 = math.ceil((countgrupo19 / 30))
        self.grupo19 = resultado_dividido19

    def update_grupo19(self):
        self._compute_grupo19()