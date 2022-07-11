from Alumno.models import Alumnos
from import_export import resources
from import_export.fields import Field

# Archivo resources.py para el manejo de importar y exportar la tabla de alumnos en la base de datos.

class AlumnoResource(resources.ModelResource):
    # Todos los "Field" son cada campo en el excel, como el nombre de las columnas en el archivo son 
    # de formatos variados e innapropiados para la base de datos, se indica manualmente que columna
    # pertenece a que valor.
    nombre_programa = Field(
        attribute="nombre_programa",
        column_name="NOMBRE PROGRAMA"
    )
    clave_programa = Field(
        attribute="clave_programa",
        column_name="CLAVE PROGRAMA"
    )
    plan = Field(
        attribute="plan",
        column_name="PLAN"
    )
    expediente = Field(
        attribute="expediente",
        column_name="EXPEDIENTE"
    )
    nombre = Field(
        attribute="nombre",
        column_name="NOMBRE"
    )
    status = Field(
        attribute="status",
        column_name="STATUS ALUMNO"
    )
    cred_pasante = Field(
        attribute="cred_pasante",
        column_name="CRED.PASANTE"
    )
    cred_aprob = Field(
        attribute="cred_aprob",
        column_name="CRED.APROB."
    )
    prom_kdxs = Field(
        attribute="prom_kdxs",
        column_name="PROM.KDXS"
    )
    prom_periodo = Field(
        attribute="prom_periodo",
        column_name="PROM.PERIODO"
    )
    mat_aprob = Field(
        attribute="mat_aprob",
        column_name="MAT.APROB."
    )
    materias_acreditadas = Field(
        attribute="materias_acreditadas",
        column_name="MATERIAS ACREDITADAS"
    )
    materias_inscritas = Field(
        attribute="materias_inscritas",
        column_name="MATERIAS INSCRITAS"
    )
    materias_segunda_inscr = Field(
        attribute="materias_segunda_inscr",
        column_name="MATERIAS SEGUNDA INSCR"
    )
    materias_tercera_inscr = Field(
        attribute="materias_tercera_inscr",
        column_name="MATERIAS TERCERA INSCR"
    )
    materias_reprobadas = Field(
        attribute="materias_reprobadas",
        column_name="MATERIAS REPROBADAS"
    )
    materias_bajas_voluntarias = Field(
        attribute="materias_bajas_voluntarias",
        column_name="MATERIAS BAJAS VOLUNTARIAS"
    )
    cred_inscr = Field(
        attribute="cred_inscr",
        column_name="CRED.INSC."
    )
    nivel_y_ciclo_ingles = Field(
        attribute="nivel_y_ciclo_ingles",
        column_name="NIVEL Y CICLO INGLÉS"
    )
    correo = Field(
        attribute="correo",
        column_name="CORREO"
    )
    cred_cult = Field(
        attribute="cred_cult",
        column_name="CRED CULT"
    )
    cred_dep = Field(
        attribute="cred_dep",
        column_name="CRED DEP"
    )
    practica_profesional_estatus_y_ciclo = Field(
        attribute="practica_profesional_estatus_y_ciclo",
        column_name="PRACTICA PROFESIONAL ESTATUS Y CICLO"
    )
    serviciosocialmateriaestatus_ciclo = Field(
        attribute="serviciosocialmateriaestatus_ciclo",
        column_name="SERVICIOSOCIALMATERIAESTATUS-CICLO"
    )
    estatusproyectoserviciosocial_cicloregistro = Field(
        attribute="estatusproyectoserviciosocial_cicloregistro",
        column_name="ESTATUSPROYECTOSERVICIOSOCIAL-CICLOREGISTRO"
    )
    egel_testimonio = Field(
        attribute="egel_testimonio",
        column_name="EGEL-TESTIMONIO"
    )
    inscrito = Field(
        attribute="inscrito",
        column_name="INSCRITO"
    )

    class Meta:
        model = Alumnos
    
    #Plantilla de como potencialmente leer el excel de una manera mas automatica.

    # def before_import(self, dataset, using_transactions, dry_run, **kwargs):
    #     template_headers = [h for h in dataset.headers]
    #     bool_inscr = [True if d == "SI" else False for d in dataset[template_headers[26]]]
    #     del dataset[-1]
    #     print(bool_inscr)
    #     dataset.append_col(bool_inscr, header='INSCRITO')
    
    #     # for id, col in enumerate(template_headers):
    #     #     dataset.headers[id] = col.replace(' ','_')
    #     #     dataset.headers[id] = col.replace('.','_')
    #     #     dataset.headers[id] = col.replace('-','_')
    #     #     dataset.headers[id] = col.lower()
    #     #     if col == "NIVEL_Y_CICLO_INGLÉS": dataset.headers[id] = "NIVEL_Y_CICLO_INGLES"
    #     #     if col == "CRED_APROB_": dataset.headers[id] = "CRED_APROB"
    #     #     if col == "MAT_APROB_": dataset.headers[id] = "MAT_APROB"
    #     #     print(dataset.headers[id])
    #     return super().before_import(dataset, using_transactions, dry_run, **kwargs)
