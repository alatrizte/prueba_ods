import ezodf
import pandas as pd

ruta = "ejemplo.ods"

# Abrir el documento ODS
doc = ezodf.opendoc(ruta)

# Obtener la primera hoja
sheet = doc.sheets[0]

# Convertir la hoja a un DataFrame de pandas
df = pd.DataFrame({col: [cell.value for cell in sheet.column(col)] for col in range(sheet.ncols())})
df.columns = [sheet[0, col].value for col in range(sheet.ncols())]

# Verificar si la columna 'process' existe, si no, crearla
if 'process' not in df.columns:
    df['process'] = ''
    # Añadir la columna 'process' al documento
    sheet.append_columns(1)
    sheet[0, sheet.ncols() - 1].set_value('process')

# Función para procesar cada fila
def procesar_fila(fila):
    suma = fila['A'] + fila['B'] + fila['C']
    print(f"Suma de la fila: {suma}")
    return 'OK'

# Actualizar la columna 'process' en el DataFrame y en el documento
for index in range(1, len(df)):  # Empezamos desde 1 para omitir la fila de encabezado
    if df.at[index, 'process'] != 'OK':
        resultado = procesar_fila(df.loc[index])
        df.at[index, 'process'] = resultado
        
        # Asegurarse de que la fila existe antes de escribir
        while sheet.nrows() <= index:
            sheet.append_rows(1)
        
        # Escribir el resultado en la última columna
        sheet[index, sheet.ncols() - 1].set_value(resultado)

# Guardar el documento actualizado
doc.save()

print("Procesamiento completado y archivo actualizado.")


