from pandas_ods_reader import read_ods

ruta = "ejemplo.ods"
df = read_ods(ruta)

if 'process' not in df.columns:
    df['process'] = ''

# Función para procesar cada fila
def procesar_fila(fila):
    suma = fila['A'] + fila['B'] + fila['C']
    print(f"Suma de la fila: {suma}")
    return 'OK'

# Actualizar la columna 'process' en el DataFrame original
for index in df.index:
    if df.at[index, 'process'] != 'OK':  # Usamos .at para modificar directamente
        df.at[index, 'process'] = procesar_fila(df.loc[index])


# Guardar el DataFrame actualizado en el archivo ODS
df.to_excel(ruta, engine="odf", index=False)

print("Procesamiento completado y archivo actualizado.")