from app.models.acceso_model import existe_usuario_por_correo, registrar_usuario

def normalizar_texto(texto: str) -> str:
    return (texto or "").strip()

def validar_datos_registro(nombre: str, correo: str, clave: str) -> tuple[bool, str]:
    nombre = normalizar_texto(nombre)
    correo = normalizar_texto(correo)
    clave = normalizar_texto(clave)

    if nombre == "":
        return False, "Debe ingresar el nombre"

    if correo == "":
        return False, "Debe ingresar el correo"

    if clave == "":
        return False, "Debe ingresar la contraseña"

    if existe_usuario_por_correo(correo):
        return False, "Ya existe un usuario registrado con ese correo"

    return True, "Datos válidos"

def crear_usuario(nombre: str, correo: str, clave: str, rol: str = "empleado") -> tuple[bool, str]:
    valido, mensaje = validar_datos_registro(nombre, correo, clave)

    if not valido:
        return False, mensaje

    registrar_usuario(nombre, correo, clave, rol)
    return True, "Usuario registrado correctamente"