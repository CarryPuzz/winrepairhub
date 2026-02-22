#!/usr/bin/env python3
# WinRepairHub.es – Portal español de reparación de Windows

AFFILIATE = "https://adtrack2.click/go.php?a_aid=699832ed8bc20"
SITE = "WinRepairHub"

PAGES = [
    ("index.html", "WinRepairHub – Reparar Windows 10/11 | Guías Gratis en Español", "home",
     "Guías gratuitas en español para reparar Windows 10 y 11. Soluciona errores del sistema, pantallazos azules, PC lento y optimiza tu ordenador fácilmente."),
    ("pages/pantalla-azul-bsod.html", "Pantalla azul de la muerte (BSOD) – Cómo reparar Windows 10/11", "bsod",
     "¿Cómo solucionar la pantalla azul de la muerte (BSOD) en Windows 10 y 11? Guía completa con todos los códigos de error."),
    ("pages/windows-no-arranca.html", "Windows no arranca – Soluciones paso a paso", "arranque",
     "¿Windows 10/11 no arranca? Descubre todos los métodos probados para reparar el inicio de Windows."),
    ("pages/pc-lento-acelerar.html", "PC lento – Cómo acelerar Windows 10/11", "optimizacion",
     "¿Tu PC va lento? Aprende a acelerar Windows 10 y 11 con nuestros consejos de expertos."),
    ("pages/errores-windows-update.html", "Errores de Windows Update – Todos los códigos resueltos", "actualizaciones",
     "¿Cómo solucionar errores de Windows Update? Soluciones para todos los problemas de actualización en Windows 10 y 11."),
    ("pages/sin-sonido-windows.html", "Sin sonido en Windows 10/11 – Reparar el audio", "audio",
     "¿Sin sonido en Windows? 10 métodos probados para restaurar el audio en Windows 10 y 11."),
    ("pages/problemas-wifi-windows.html", "Problemas de WiFi en Windows 10/11 – Reparar conexión", "red",
     "¿El WiFi no funciona en Windows? Guía completa para reparar la conexión inalámbrica."),
    ("pages/errores-disco-duro.html", "Errores de disco duro – Diagnóstico y reparación Windows", "disco",
     "¿Cómo solucionar errores de disco duro en Windows 10 y 11? Diagnóstico y reparación paso a paso."),
    ("pages/reparar-registro-windows.html", "Reparar el registro de Windows 10/11 – Guía segura", "registro",
     "¿Cómo reparar el registro de Windows de forma segura? Guía para Windows 10 y 11."),
    ("pages/windows-se-congela.html", "Windows se congela y no responde – Soluciones", "bloqueos",
     "¿Qué hacer cuando Windows 10/11 se congela o no responde? Todas las soluciones."),
    ("pages/error-0x80070005.html", "Error 0x80070005 – Acceso denegado Windows Fix", "codigos-error",
     "¿Cómo solucionar el error Windows 0x80070005 (Acceso denegado)? Guía completa."),
    ("pages/error-0xc0000185.html", "Error 0xc0000185 – Datos de configuración de arranque", "codigos-error",
     "Soluciona el error Windows 0xc0000185. Guía de reparación de los datos de arranque."),
    ("pages/error-0x80004005.html", "Error 0x80004005 – Error no especificado Windows Fix", "codigos-error",
     "¿Cómo solucionar el error Windows 0x80004005? Todas las soluciones."),
    ("pages/restablecer-windows.html", "Restablecer Windows 10/11 – Restaurar configuración de fábrica", "reset",
     "¿Cómo restablecer Windows 10 y 11 a la configuración de fábrica? Guía paso a paso con copia de seguridad."),
    ("pages/modo-seguro-windows.html", "Modo seguro Windows 10/11 – Cómo iniciarlo", "diagnostico",
     "¿Cómo iniciar Windows 10/11 en modo seguro? Todos los métodos explicados."),
    ("pages/sfc-scannow-windows.html", "SFC /scannow – Reparar archivos del sistema Windows 10/11", "diagnostico",
     "¿Cómo usar SFC /scannow para reparar archivos del sistema Windows? Guía completa."),
    ("pages/dism-reparacion.html", "DISM – Reparar la imagen del sistema Windows 10/11", "diagnostico",
     "¿Cómo usar DISM para reparar la imagen del sistema Windows dañada?"),
    ("pages/problemas-impresora.html", "Problemas de impresora Windows 10/11 – Reparación completa", "dispositivos",
     "¿La impresora no funciona en Windows? Guía de reparación paso a paso."),
    ("pages/errores-controladores.html", "Errores de controladores Windows – Actualizar y reparar", "controladores",
     "¿Cómo solucionar errores de controladores en Windows 10 y 11? Guía completa de actualización."),
    ("pages/problemas-pantalla.html", "Problemas de pantalla Windows – Resolución y parpadeo", "pantalla",
     "¿Cómo reparar problemas de pantalla en Windows 10 y 11? Resolución, parpadeo, pantalla negra."),
    ("pages/eliminar-virus-malware.html", "Eliminar virus y malware – Windows 10/11", "seguridad",
     "¿Cómo eliminar virus y malware de Windows 10 y 11? Guía de seguridad completa."),
    ("pages/optimizar-ram.html", "Optimizar la RAM en Windows 10/11 – Consejos de expertos", "optimizacion",
     "¿Cómo optimizar el uso de la RAM en Windows 10 y 11? Métodos probados."),
    ("pages/limpiar-disco-windows.html", "Limpiar el disco en Windows 10/11 – Liberar espacio", "optimizacion",
     "¿Cómo limpiar el disco duro en Windows 10 y 11? Libera espacio fácilmente."),
    ("pages/ethernet-sin-internet.html", "Ethernet no funciona – Sin Internet Windows Fix", "red",
     "¿La conexión Ethernet no funciona en Windows 10/11? Reparación paso a paso."),
    ("pages/desactivar-actualizaciones.html", "Desactivar actualizaciones automáticas Windows 10/11", "actualizaciones",
     "¿Cómo desactivar o controlar las actualizaciones automáticas de Windows?"),
    ("pages/reparar-sistema-archivos.html", "Reparar el sistema de archivos NTFS – Windows 10/11", "disco",
     "¿Cómo reparar el sistema de archivos NTFS dañado en Windows 10 y 11?"),
    ("pages/usb-no-reconocido.html", "USB no reconocido en Windows 10/11 – Reparación", "dispositivos",
     "¿El dispositivo USB no es reconocido por Windows? Todas las soluciones."),
    ("pages/windows-11-requisitos.html", "Windows 11 – Requisitos del sistema y actualización", "windows11",
     "¿Cuáles son los requisitos de Windows 11? ¿Cómo comprobar la compatibilidad del PC?"),
    ("pages/recuperar-datos-windows.html", "Recuperar datos perdidos – Windows 10/11", "recuperacion",
     "¿Cómo recuperar archivos perdidos en Windows 10 y 11? Herramientas y métodos probados."),
    ("pages/optimizar-ssd.html", "Optimizar un SSD en Windows 10/11 – Guía completa", "optimizacion",
     "¿Cómo optimizar un SSD en Windows 10 y 11? Activar TRIM, desactivar desfragmentación."),
]

NAV = [
    ("Inicio", "index.html"),
    ("Pantalla azul", "pages/pantalla-azul-bsod.html"),
    ("Actualizaciones", "pages/errores-windows-update.html"),
    ("Optimización", "pages/pc-lento-acelerar.html"),
    ("WiFi/Red", "pages/problemas-wifi-windows.html"),
    ("Diagnóstico", "pages/sfc-scannow-windows.html"),
    ("Códigos de error", "pages/error-0x80070005.html"),
]

def rel(f, t):
    if f == "index.html": return t
    if t == "index.html": return "../index.html"
    if t.startswith("pages/"): return t[6:]
    return t

def nav_html(current):
    return "".join(f'<a href="{rel(current, h)}">{l}</a>\n' for l, h in NAV)

def flag_bar():
    return '<div class="flag-bar"></div>'

def trust_bar():
    items = [("✅","Guías gratuitas"),("🔒","Métodos seguros"),("🇪🇸","100% en español"),("⚡","Soluciones rápidas"),("🔄","Actualizado regularmente")]
    inner = "".join(f'<div class="trust-item"><span class="ico">{i}</span><span>{t}</span></div>' for i,t in items)
    return f'<div class="trust-bar"><div class="trust-inner">{inner}</div></div>'

def footer_html(current):
    base = "../" if current.startswith("pages/") else ""
    cats = {
        "Errores del sistema": [
            ("Pantalla azul (BSOD)", "pages/pantalla-azul-bsod.html"),
            ("Windows no arranca", "pages/windows-no-arranca.html"),
            ("Windows se congela", "pages/windows-se-congela.html"),
            ("Error 0x80070005", "pages/error-0x80070005.html"),
            ("Error 0xc0000185", "pages/error-0xc0000185.html"),
        ],
        "Optimización": [
            ("PC lento", "pages/pc-lento-acelerar.html"),
            ("Limpiar el disco", "pages/limpiar-disco-windows.html"),
            ("Optimizar RAM", "pages/optimizar-ram.html"),
            ("Optimizar SSD", "pages/optimizar-ssd.html"),
        ],
        "Diagnóstico": [
            ("SFC /scannow", "pages/sfc-scannow-windows.html"),
            ("DISM Reparación", "pages/dism-reparacion.html"),
            ("Modo seguro", "pages/modo-seguro-windows.html"),
            ("Reparar registro", "pages/reparar-registro-windows.html"),
        ],
    }
    cols = ""
    for cat, items in cats.items():
        li = "".join(f'<li><a href="{rel(current,h)}">{t}</a></li>' for t,h in items)
        cols += f'<div><h4>{cat}</h4><ul>{li}</ul></div>'

    return f"""
<footer>
  <div class="footer-flag"></div>
  <div class="footer-inner">
    <div class="footer-grid">
      <div>
        <div class="footer-logo">WinRepair<span>Hub</span></div>
        <p style="font-size:13px;color:#3d3830;margin-bottom:16px;line-height:1.7;">Tu portal experto para reparar Windows 10 y 11 en español. Guías gratuitas, herramientas de diagnóstico y soluciones probadas para todos los problemas de Windows.</p>
        <a href="{AFFILIATE}" class="btn-dl" style="font-size:13px;padding:10px 20px;" target="_blank" rel="nofollow">⬇ Descargar gratis</a>
      </div>
      {cols}
    </div>
    <div class="footer-bottom">
      <p>© 2024 WinRepairHub – Todos los derechos reservados | <a href="{rel(current,'index.html')}" style="color:#3d3830;">Inicio</a> | Este sitio es de carácter informativo.</p>
      <p>Windows es una marca registrada de Microsoft Corporation. WinRepairHub no está afiliado a Microsoft.</p>
    </div>
  </div>
</footer>
<script src="{base}js/main.js"></script>"""

def sidebar_html(current):
    import random
    random.seed(abs(hash(current)) % 99999)
    others = [p for p in PAGES if p[0] != current and p[0] != "index.html"]
    selected = random.sample(others, min(8, len(others)))
    li = "".join(f'<li><a href="{rel(current,p[0])}">{p[1].split(" – ")[0][:52]}</a></li>' for p in selected)
    return f"""
<aside class="sidebar">
  <div class="sidebar-card sidebar-cta">
    <h3>🔧 Reparar ahora</h3>
    <p>La herramienta detecta y corrige errores de Windows automáticamente en minutos.</p>
    <a href="{AFFILIATE}" class="btn-dl" style="font-size:13px;padding:10px 16px;display:block;margin:0;" target="_blank" rel="nofollow">⬇ Descargar gratis</a>
  </div>
  <div class="sidebar-card">
    <h3>📋 Artículos populares</h3>
    <ul>{li}</ul>
  </div>
  <div class="sidebar-card" style="background:#fffbeb;border:1px solid #f59e0b;border-left:4px solid #f59e0b;">
    <h3 style="color:#92400e;border-color:#f59e0b30;">💡 Consejo experto</h3>
    <p style="font-size:13px;color:#78350f;font-weight:600;text-transform:none;letter-spacing:0;">Antes de reparar el sistema, crea un punto de restauración: <strong>Win + R → sysdm.cpl → Protección del sistema → Crear</strong></p>
  </div>
</aside>"""

def head_html(title, meta_desc, current, canonical):
    base = "" if current == "index.html" else "../"
    schema = "WebSite" if current == "index.html" else "Article"
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{meta_desc}">
  <meta name="robots" content="index, follow">
  <meta name="author" content="WinRepairHub">
  <meta name="language" content="es">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{meta_desc}">
  <meta property="og:type" content="{'website' if current == 'index.html' else 'article'}">
  <meta property="og:locale" content="es_ES">
  <meta property="og:site_name" content="WinRepairHub">
  <link rel="canonical" href="https://winrepairhub.es/{canonical}">
  <link rel="stylesheet" href="{base}css/style.css">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🖥️</text></svg>">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "{schema}",
    "name": "{title}",
    "description": "{meta_desc}",
    "inLanguage": "es-ES",
    "publisher": {{"@type": "Organization", "name": "WinRepairHub", "url": "https://winrepairhub.es"}}
  }}
  </script>
</head>
<body>
{flag_bar()}
<div class="header-top">
  🔴 ¿Problema con Windows? → <a href="{AFFILIATE}" target="_blank" rel="nofollow">Descarga la herramienta de reparación gratis</a> y resuélvelo en 3 minutos
</div>
<header>
  <div class="header-inner">
    <a href="{base}index.html" class="logo">
      <div class="logo-icon">🛠️</div>
      WinRepair<span class="hub">Hub</span>
    </a>
    <nav>{nav_html(current)}</nav>
  </div>
</header>
"""

import os
BASE = "/home/claude/winrepairhub-es"

# ========== ARTICLES ==========

ARTICLES = {

"pages/pantalla-azul-bsod.html": {
"h1": "Pantalla azul de la muerte (BSOD) – Cómo reparar Windows 10 y 11",
"intro": "La pantalla azul de la muerte (Blue Screen of Death, BSOD) es uno de los errores más temidos en Windows. Aparece de repente, congela el ordenador y puede provocar la pérdida de datos no guardados. Esta guía te explica cómo identificar la causa y reparar definitivamente el BSOD en Windows 10 y Windows 11.",
"sections": [
("¿Qué es una pantalla azul y por qué aparece?", """<p>El BSOD es un mecanismo de protección de Windows. Cuando el sistema detecta un error crítico que podría corromper datos, se detiene automáticamente y muestra esta pantalla azul con un código de error.</p>
<p><strong>Causas más frecuentes del BSOD:</strong></p>
<ul>
<li>Controladores corruptos u obsoletos – especialmente los de la tarjeta gráfica</li>
<li>RAM defectuosa – errores de memoria o módulos dañados</li>
<li>Sobrecalentamiento del procesador o tarjeta gráfica</li>
<li>Archivos del sistema Windows corruptos</li>
<li>Problemas de disco duro – sectores defectuosos</li>
<li>Virus y software malicioso</li>
<li>Hardware incompatible tras una actualización</li>
</ul>"""),
("Leer e interpretar el código de error", """<p>Cada pantalla azul muestra un código de error que identifica la causa del problema. Anota este código:</p>
<div class="code-block">DRIVER_IRQL_NOT_LESS_OR_EQUAL
SYSTEM_THREAD_EXCEPTION_NOT_HANDLED
CRITICAL_PROCESS_DIED
PAGE_FAULT_IN_NONPAGED_AREA</div>
<p><strong>Códigos BSOD más comunes:</strong></p>
<ul>
<li><strong>DRIVER_IRQL_NOT_LESS_OR_EQUAL</strong> – problema de controlador</li>
<li><strong>PAGE_FAULT_IN_NONPAGED_AREA</strong> – problema de RAM</li>
<li><strong>NTFS_FILE_SYSTEM</strong> – error del sistema de archivos</li>
<li><strong>CRITICAL_PROCESS_DIED</strong> – proceso crítico terminado</li>
<li><strong>MEMORY_MANAGEMENT</strong> – gestión de memoria defectuosa</li>
</ul>
<div class="tip-box"><strong>💡 Consejo:</strong> Busca el código exacto en Google – normalmente encontrarás la causa precisa y la solución para tu configuración.</div>"""),
("Método 1: Actualizar los controladores", """<ol class="steps">
<li>Pulsa <strong>Win + X</strong> y abre el <strong>Administrador de dispositivos</strong></li>
<li>Busca dispositivos con un signo de exclamación amarillo</li>
<li>Clic derecho → <strong>Actualizar controlador</strong></li>
<li>Elige <strong>Buscar controladores automáticamente</strong></li>
<li>Reinicia el ordenador tras la actualización</li>
</ol>
<div class="warning-box"><strong>⚠️ Importante:</strong> Descarga siempre los controladores de tarjeta gráfica directamente del sitio del fabricante: NVIDIA GeForce Experience o AMD Radeon Software.</div>"""),
("Método 2: Verificar archivos del sistema (SFC)", """<p>Los archivos del sistema corruptos causan frecuentemente BSOD. La herramienta SFC los repara automáticamente:</p>
<ol class="steps">
<li>Pulsa <strong>Win + X</strong> y elige <strong>Terminal (Administrador)</strong></li>
<li>Escribe el siguiente comando y pulsa Intro:</li>
</ol>
<div class="code-block">sfc /scannow</div>
<p>El análisis dura entre 5 y 30 minutos. Windows repara automáticamente los errores encontrados. Reinicia el PC al terminar.</p>"""),
("Método 3: Comprobar la memoria RAM", """<ol class="steps">
<li>Pulsa <strong>Win + R</strong>, escribe <strong>mdsched.exe</strong> y pulsa Intro</li>
<li>Elige <strong>Reiniciar ahora y buscar problemas</strong></li>
<li>Windows reinicia y realiza una prueba completa de memoria</li>
<li>Los resultados se muestran al iniciar sesión</li>
</ol>
<div class="tip-box"><strong>💡 Consejo:</strong> Si la prueba detecta errores de memoria, deberás reemplazar el módulo RAM defectuoso – los errores de RAM no se pueden corregir por software.</div>"""),
("Método 4: Reparar con DISM", f"""<p>Si SFC no es suficiente, usa DISM para restaurar la imagen del sistema:</p>
<div class="code-block">DISM /Online /Cleanup-Image /RestoreHealth</div>
<p>Este comando descarga los archivos que faltan de Internet y restaura la imagen de Windows. Duración: 15-45 minutos.</p>
<div class="cta-box">
  <h3>🔧 Reparar el BSOD automáticamente</h3>
  <p>Nuestra herramienta analiza la causa de la pantalla azul y la corrige de forma completamente automática.</p>
  <a href="{AFFILIATE}" class="btn-dl" target="_blank" rel="nofollow">⬇ Descargar gratis</a>
</div>"""),
],
"related": ["pages/errores-controladores.html","pages/sfc-scannow-windows.html","pages/optimizar-ram.html","pages/windows-se-congela.html"],
},

"pages/windows-no-arranca.html": {
"h1": "Windows no arranca – Guía completa de reparación",
"intro": "¿Windows 10 o 11 no arranca? Pantalla negra, bucle de arranque o mensaje de error al iniciar – son situaciones estresantes pero reparables. Esta guía presenta todos los métodos probados para volver a iniciar Windows.",
"sections": [
("Identificar el tipo de problema", """<p>Primero determina qué ves en la pantalla:</p>
<ul>
<li><strong>Pantalla negra con cursor</strong> – problema de visualización o archivos de arranque corruptos</li>
<li><strong>«No se encontró sistema operativo»</strong> – error MBR/GPT o disco no detectado</li>
<li><strong>Bucle de arranque</strong> – Windows intenta repararse en bucle sin éxito</li>
<li><strong>Círculo de carga detenido</strong> – archivos del sistema o controladores corruptos</li>
<li><strong>Pantalla azul al arrancar</strong> – ver la <a href="pantalla-azul-bsod.html">guía de BSOD</a></li>
</ul>"""),
("Método 1: Reparación automática de inicio", """<ol class="steps">
<li>Fuerza 3 reinicios (mantén pulsado el botón de encendido 5 segundos)</li>
<li>Windows lanza automáticamente el <strong>Entorno de recuperación de Windows (WinRE)</strong></li>
<li>Elige <strong>Solucionar problemas → Opciones avanzadas → Reparación de inicio</strong></li>
<li>Espera a que finalice el proceso y reinicia</li>
</ol>
<div class="tip-box"><strong>💡 Consejo:</strong> La reparación automática corrige la mayoría de errores BCD y problemas de arranque comunes en pocos minutos.</div>"""),
("Método 2: Reconstruir el BCD manualmente", """<p>Si la reparación automática falla, reconstruye manualmente la configuración de arranque:</p>
<ol class="steps">
<li>Arranca desde un medio de instalación de Windows (USB/DVD)</li>
<li>Elige <strong>Reparar el equipo → Solucionar problemas → Símbolo del sistema</strong></li>
<li>Introduce estos comandos uno a uno:</li>
</ol>
<div class="code-block">bootrec /fixmbr
bootrec /fixboot
bootrec /scanos
bootrec /rebuildbcd</div>
<p>Escribe después <strong>exit</strong> y reinicia el ordenador.</p>"""),
("Método 3: Restaurar el sistema", f"""<ol class="steps">
<li>Accede a WinRE (3 reinicios forzados)</li>
<li>Elige <strong>Solucionar problemas → Opciones avanzadas → Restaurar sistema</strong></li>
<li>Selecciona un punto de restauración anterior al problema</li>
<li>Sigue las instrucciones y espera a que finalice</li>
</ol>
<div class="cta-box">
  <h3>🚀 Reparar el arranque automáticamente</h3>
  <p>La herramienta detecta problemas de arranque y los corrige sin conocimientos técnicos.</p>
  <a href="{AFFILIATE}" class="btn-dl" target="_blank" rel="nofollow">⬇ Descargar gratis</a>
</div>"""),
],
"related": ["pages/pantalla-azul-bsod.html","pages/modo-seguro-windows.html","pages/restablecer-windows.html","pages/sfc-scannow-windows.html"],
},

"pages/pc-lento-acelerar.html": {
"h1": "PC lento – Cómo acelerar Windows 10 y 11",
"intro": "Un PC lento con Windows es uno de los problemas más comunes. Con el tiempo, el sistema acumula archivos innecesarios, ejecuta demasiados programas al inicio y se ralentiza progresivamente. Aquí están los métodos más efectivos para recuperar el rendimiento original.",
"sections": [
("¿Por qué se ralentiza Windows?", """<ul>
<li>Demasiados programas que se ejecutan al inicio</li>
<li>Disco duro casi lleno (menos del 15% de espacio libre)</li>
<li>Controladores obsoletos o defectuosos</li>
<li>Malware y adware en segundo plano</li>
<li>RAM insuficiente para las aplicaciones actuales</li>
<li>Efectos visuales activados que consumen CPU innecesariamente</li>
<li>Fragmentación del disco duro (no en SSD)</li>
</ul>"""),
("Paso 1: Desactivar programas de inicio", """<ol class="steps">
<li>Pulsa <strong>Ctrl + Mayús + Esc</strong> para abrir el Administrador de tareas</li>
<li>Haz clic en la pestaña <strong>Inicio</strong></li>
<li>Ordena por <strong>Impacto de inicio</strong> (Alto primero)</li>
<li>Clic derecho en los programas innecesarios → <strong>Deshabilitar</strong></li>
</ol>
<div class="tip-box"><strong>💡 ¿Qué se puede deshabilitar?</strong> OneDrive, Spotify, Discord, Skype, Teams (si no se usan). Nunca deshabilites: antivirus, controladores del sistema.</div>"""),
("Paso 2: Limpieza de disco", """<ol class="steps">
<li>Pulsa <strong>Win + S</strong> y busca <strong>Liberador de espacio en disco</strong></li>
<li>Selecciona la unidad C: y haz clic en Aceptar</li>
<li>Marca todas las categorías de archivos</li>
<li>Haz clic en <strong>Limpiar archivos del sistema</strong> para una limpieza más profunda</li>
<li>Confirma la eliminación</li>
</ol>"""),
("Paso 3: Reducir los efectos visuales", """<ol class="steps">
<li>Pulsa <strong>Win + R</strong>, escribe <strong>sysdm.cpl</strong> y pulsa Intro</li>
<li>Pestaña <strong>Opciones avanzadas → Rendimiento → Configuración</strong></li>
<li>Elige <strong>Ajustar para obtener el mejor rendimiento</strong></li>
<li>Haz clic en Aplicar y Aceptar</li>
</ol>"""),
("Paso 4: Plan de energía de alto rendimiento", f"""<ol class="steps">
<li>Ve a <strong>Configuración → Sistema → Energía y suspensión</strong></li>
<li>En <strong>Modo de energía</strong>, elige <strong>Mejor rendimiento</strong></li>
<li>Reinicia el ordenador para aplicar los cambios</li>
</ol>
<div class="cta-box">
  <h3>⚡ Optimizar el PC automáticamente</h3>
  <p>La herramienta analiza tu sistema y corrige todos los problemas de rendimiento automáticamente.</p>
  <a href="{AFFILIATE}" class="btn-dl" target="_blank" rel="nofollow">⬇ Descargar gratis</a>
</div>"""),
],
"related": ["pages/limpiar-disco-windows.html","pages/optimizar-ram.html","pages/optimizar-ssd.html","pages/errores-controladores.html"],
},

"pages/sfc-scannow-windows.html": {
"h1": "SFC /scannow – Reparar archivos del sistema Windows 10/11",
"intro": "El comando SFC (System File Checker) es la herramienta integrada más potente para reparar archivos del sistema Windows corruptos. Analiza la integridad de todos los archivos del sistema protegidos y reemplaza automáticamente los archivos dañados. Aquí todo lo que necesitas saber sobre SFC.",
"sections": [
("¿Para qué sirve SFC /scannow?", """<p>SFC comprueba todos los archivos del sistema Windows protegidos y los reemplaza por versiones correctas desde una caché local. Esta herramienta está integrada en Windows 10 y 11 – no requiere instalación.</p>
<p><strong>SFC puede resolver:</strong></p>
<ul>
<li>Pantallas azules (BSOD)</li>
<li>Problemas de arranque de Windows</li>
<li>Bloqueos y cuelgues frecuentes</li>
<li>Mensajes de error al abrir programas</li>
<li>Funciones de Windows que no responden</li>
</ul>"""),
("Paso a paso: Ejecutar SFC", """<ol class="steps">
<li>Pulsa <strong>Win + X</strong> y elige <strong>Terminal (Administrador)</strong></li>
<li>Confirma el aviso de UAC haciendo clic en <strong>Sí</strong></li>
<li>Escribe el siguiente comando:</li>
</ol>
<div class="code-block">sfc /scannow</div>
<ol class="steps" style="counter-reset:steps 3">
<li>Pulsa Intro y espera – el análisis dura entre 5 y 30 minutos</li>
<li>Lee atentamente el mensaje de resultado</li>
</ol>"""),
("Interpretar los resultados de SFC", """<p>Al finalizar el análisis, aparece uno de estos mensajes:</p>
<ul>
<li>✅ <strong>«No se encontraron infracciones»</strong> – los archivos del sistema están bien</li>
<li>✅ <strong>«Se encontraron y repararon infracciones»</strong> – errores corregidos, reinicia</li>
<li>⚠️ <strong>«Se encontraron infracciones pero no se pudieron reparar»</strong> – usa DISM después</li>
</ul>"""),
("Cuando SFC no puede reparar los errores", f"""<p>Si SFC no logra reparar los errores, primero ejecuta DISM:</p>
<div class="code-block">DISM /Online /Cleanup-Image /RestoreHealth</div>
<p>Vuelve a ejecutar <strong>sfc /scannow</strong> después. En la gran mayoría de casos, los errores se corregirán esta vez.</p>
<div class="cta-box">
  <h3>🔧 Reparar archivos del sistema automáticamente</h3>
  <p>La herramienta ejecuta SFC, DISM y otras reparaciones de forma automática.</p>
  <a href="{AFFILIATE}" class="btn-dl" target="_blank" rel="nofollow">⬇ Descargar gratis</a>
</div>"""),
],
"related": ["pages/dism-reparacion.html","pages/pantalla-azul-bsod.html","pages/windows-no-arranca.html","pages/reparar-registro-windows.html"],
},

"pages/problemas-wifi-windows.html": {
"h1": "Problemas de WiFi en Windows 10/11 – Guía de reparación",
"intro": "Los problemas de conexión WiFi en Windows son muy frecuentes. Ya sea que la red no se detecte, la conexión se interrumpa constantemente o Internet no funcione a pesar de estar conectado – aquí encontrarás todas las soluciones.",
"sections": [
("Problemas de WiFi comunes en Windows", """<ul>
<li>La tarjeta WiFi no detecta ninguna red</li>
<li>Conectado al WiFi pero sin acceso a Internet</li>
<li>La conexión WiFi se corta regularmente</li>
<li>Conexión WiFi muy lenta</li>
<li>Mensaje «Red no identificada»</li>
<li>El icono de WiFi ha desaparecido de la barra de tareas</li>
</ul>"""),
("Método 1: Restablecer la pila de red TCP/IP", """<div class="code-block">netsh winsock reset
netsh int ip reset
ipconfig /release
ipconfig /flushdns
ipconfig /renew</div>
<p>Introduce cada comando en el Símbolo del sistema (Administrador) y pulsa Intro. Reinicia el PC después.</p>"""),
("Método 2: Reinstalar el controlador WiFi", """<ol class="steps">
<li>Abre el <strong>Administrador de dispositivos</strong> (Win + X)</li>
<li>Expande <strong>Adaptadores de red</strong></li>
<li>Clic derecho en el adaptador WiFi → <strong>Desinstalar dispositivo</strong></li>
<li>Marca la casilla para eliminar el controlador</li>
<li>Reinicia – Windows reinstala el controlador automáticamente</li>
</ol>"""),
("Método 3: Restablecer la configuración de red", f"""<ol class="steps">
<li>Ve a <strong>Configuración → Red e Internet</strong></li>
<li>Desplázate hasta <strong>Restablecimiento de red</strong></li>
<li>Haz clic en <strong>Restablecer ahora</strong></li>
<li>Confirma y espera el reinicio</li>
</ol>
<div class="warning-box"><strong>⚠️ Atención:</strong> El restablecimiento de red elimina todas las contraseñas WiFi guardadas y las configuraciones VPN.</div>
<div class="cta-box">
  <h3>📶 Reparar el WiFi automáticamente</h3>
  <p>La herramienta diagnostica y repara problemas de red automáticamente.</p>
  <a href="{AFFILIATE}" class="btn-dl" target="_blank" rel="nofollow">⬇ Descargar gratis</a>
</div>"""),
],
"related": ["pages/ethernet-sin-internet.html","pages/errores-controladores.html","pages/sfc-scannow-windows.html","pages/restablecer-windows.html"],
},

"pages/errores-windows-update.html": {
"h1": "Errores de Windows Update – Todos los códigos resueltos",
"intro": "Las actualizaciones de Windows son esenciales para la seguridad y estabilidad del sistema. Cuando el proceso de actualización falla con un código de error, necesitas saber cómo reaccionar. Esta guía cubre todos los problemas comunes de Windows Update.",
"sections": [
("Códigos de error de Windows Update más frecuentes", """<ul>
<li><strong>0x80070422</strong> – servicio Windows Update desactivado</li>
<li><strong>0x80240034</strong> – problema al descargar las actualizaciones</li>
<li><strong>0x8007000E</strong> – memoria insuficiente durante la actualización</li>
<li><strong>0x80073712</strong> – archivos de actualización corruptos</li>
<li><strong>0x800F081F</strong> – archivo de origen no encontrado</li>
<li><strong>0xC1900101</strong> – error de controlador durante la actualización</li>
</ul>"""),
("Método 1: Solucionador de problemas de Windows Update", """<ol class="steps">
<li>Ve a <strong>Configuración → Sistema → Solucionar problemas</strong></li>
<li>Haz clic en <strong>Otros solucionadores de problemas</strong></li>
<li>Encuentra <strong>Windows Update</strong> y haz clic en <strong>Ejecutar</strong></li>
<li>Sigue las instrucciones y aplica las correcciones sugeridas</li>
</ol>"""),
("Método 2: Vaciar la caché de Windows Update", """<div class="code-block">net stop wuauserv
net stop cryptSvc
net stop bits
ren C:\\Windows\\SoftwareDistribution SoftwareDistribution.old
net start wuauserv
net start cryptSvc
net start bits</div>
<p>Introduce estos comandos en el Símbolo del sistema (Administrador). Reinicia y vuelve a intentar instalar las actualizaciones.</p>"""),
("Método 3: DISM para reparar la imagen del sistema", f"""<div class="code-block">DISM /Online /Cleanup-Image /RestoreHealth</div>
<p>Ejecuta después <strong>sfc /scannow</strong> y vuelve a iniciar Windows Update.</p>
<div class="cta-box">
  <h3>🔄 Reparar Windows Update automáticamente</h3>
  <p>La herramienta detecta y corrige los problemas de actualización de Windows automáticamente.</p>
  <a href="{AFFILIATE}" class="btn-dl" target="_blank" rel="nofollow">⬇ Descargar gratis</a>
</div>"""),
],
"related": ["pages/sfc-scannow-windows.html","pages/dism-reparacion.html","pages/restablecer-windows.html","pages/desactivar-actualizaciones.html"],
},

"pages/windows-se-congela.html": {
"h1": "Windows se congela y no responde – Causas y soluciones",
"intro": "Windows que se congela es un problema muy extendido. Ya sea que el sistema se bloquee al arrancar, durante el uso o en tareas específicas – esta guía te presenta todas las soluciones eficaces.",
"sections": [
("Causas principales del congelamiento de Windows", """<ul>
<li>RAM insuficiente para las aplicaciones en ejecución</li>
<li>Controladores obsoletos o defectuosos</li>
<li>Sobrecalentamiento del procesador o la tarjeta gráfica</li>
<li>Virus y malware activos en segundo plano</li>
<li>Archivos del sistema corruptos</li>
<li>Uso del disco al 100%</li>
<li>Conflictos entre programas en segundo plano</li>
</ul>"""),
("Acción inmediata: Desbloquear el sistema congelado", """<ul>
<li>Pulsa <strong>Ctrl + Alt + Supr</strong> y abre el Administrador de tareas</li>
<li>Finaliza los programas que muestren «No responde»</li>
<li>Si es imposible, mantén pulsado el botón de encendido 5-10 segundos</li>
</ul>"""),
("Diagnóstico: Corregir el uso del disco al 100%", """<ol class="steps">
<li>Abre el Administrador de tareas (<strong>Ctrl + Mayús + Esc</strong>)</li>
<li>Pestaña <strong>Rendimiento → Disco</strong> – si el uso está al 100% constantemente, esa es la causa</li>
<li>Desactiva el servicio <strong>SysMain</strong> en services.msc</li>
<li>Desactiva también <strong>Búsqueda de Windows</strong> temporalmente para probar</li>
</ol>"""),
("Solución: Desactivar SysMain (Superfetch)", f"""<ol class="steps">
<li>Pulsa <strong>Win + R</strong>, escribe <strong>services.msc</strong></li>
<li>Encuentra <strong>SysMain</strong> y haz doble clic</li>
<li>Cambia el <strong>Tipo de inicio</strong> a <strong>Deshabilitado</strong></li>
<li>Haz clic en <strong>Detener</strong> y luego en Aceptar</li>
</ol>
<div class="cta-box">
  <h3>🔧 Reparar los bloqueos automáticamente</h3>
  <p>La herramienta identifica la causa de los bloqueos y la corrige de forma completamente automática.</p>
  <a href="{AFFILIATE}" class="btn-dl" target="_blank" rel="nofollow">⬇ Descargar gratis</a>
</div>"""),
],
"related": ["pages/optimizar-ram.html","pages/pantalla-azul-bsod.html","pages/pc-lento-acelerar.html","pages/errores-controladores.html"],
},

"pages/errores-disco-duro.html": {
"h1": "Errores de disco duro – Diagnóstico y reparación Windows 10/11",
"intro": "Los errores de disco duro son serios y pueden provocar pérdida de datos. Windows ofrece varias herramientas integradas para diagnosticar y reparar discos. Aquí te explicamos cómo usarlas eficazmente.",
"sections": [
("Síntomas de un disco duro defectuoso", """<ul>
<li>Ruidos extraños (chasquidos, arañazos)</li>
<li>Tiempos de carga muy largos para archivos y programas</li>
<li>Pantallas azules con códigos relacionados con el disco</li>
<li>Archivos que desaparecen o no se pueden abrir</li>
<li>Errores al copiar archivos</li>
<li>Windows reporta sectores defectuosos</li>
</ul>"""),
("Herramienta 1: CHKDSK – Verificar el disco", """<div class="code-block">chkdsk C: /f /r /x</div>
<p>Ejecuta en el Símbolo del sistema (Administrador). Parámetros:</p>
<ul>
<li><strong>/f</strong> – corrige errores del sistema de archivos</li>
<li><strong>/r</strong> – localiza sectores defectuosos y recupera datos</li>
<li><strong>/x</strong> – desmonta el volumen antes del análisis</li>
</ul>"""),
("Herramienta 2: Comprobar el estado S.M.A.R.T.", f"""<p>S.M.A.R.T. supervisa la salud del disco. Compruébalo en PowerShell:</p>
<div class="code-block">Get-WmiObject -Namespace root\\wmi -Class MSStorageDriver_FailurePredictStatus</div>
<p>Si aparece <strong>PredictFailure: True</strong>, el disco puede fallar pronto – ¡haz una copia de seguridad inmediatamente!</p>
<div class="cta-box">
  <h3>💾 Diagnosticar el disco automáticamente</h3>
  <p>La herramienta comprueba el estado del disco, corrige errores y avisa de posibles fallos.</p>
  <a href="{AFFILIATE}" class="btn-dl" target="_blank" rel="nofollow">⬇ Descargar gratis</a>
</div>"""),
],
"related": ["pages/reparar-sistema-archivos.html","pages/limpiar-disco-windows.html","pages/optimizar-ssd.html","pages/recuperar-datos-windows.html"],
},
}

# Generic articles
GENERIC = {
"pages/sin-sonido-windows.html": ("Sin sonido en Windows 10/11 – Reparar el audio", "Sin sonido en Windows es un problema frustrante con muchas causas posibles. Esta guía presenta 10 métodos probados para restaurar el audio.", "Primero comprueba que el volumen no esté silenciado en la barra de tareas. Clic derecho en el icono del altavoz → Configuración de sonido → verifica el dispositivo de salida. Reinicia el servicio Windows Audio en services.msc. Actualiza el controlador de audio en el Administrador de dispositivos."),
"pages/reparar-registro-windows.html": ("Reparar el registro de Windows 10/11 – Guía segura", "El registro de Windows es una base de datos central con todos los parámetros del sistema. Las entradas corruptas pueden causar diversos problemas.", "Antes que nada, haz una copia de seguridad del registro: regedit → Archivo → Exportar → Todo. Usa sfc /scannow para una reparación automática segura. Para errores persistentes, usa DISM /Online /Cleanup-Image /RestoreHealth. Evita los limpiadores de registro de terceros."),
"pages/error-0x80070005.html": ("Error 0x80070005 – Acceso denegado Windows Fix", "El error 0x80070005 significa 'Acceso denegado' y aparece al instalar aplicaciones, actualizar Windows o cambiar configuraciones del sistema.", "Ejecuta sfc /scannow como Administrador. Verifica los permisos de las carpetas afectadas (Propiedades → Seguridad). Desactiva temporalmente el antivirus y vuelve a intentarlo. Comprueba la configuración del Control de cuentas de usuario (UAC)."),
"pages/error-0xc0000185.html": ("Error 0xc0000185 – Datos de configuración de arranque", "El error 0xc0000185 indica que los datos de configuración de arranque (BCD) están corruptos. Windows no puede iniciar.", "Arranca desde un medio de instalación de Windows. Elige Reparar el equipo → Símbolo del sistema e introduce: bootrec /rebuildbcd, luego bootrec /fixmbr y bootrec /fixboot. Reinicia el ordenador."),
"pages/error-0x80004005.html": ("Error 0x80004005 – Error no especificado Windows Fix", "El error 0x80004005 es un error general de Windows que puede aparecer al copiar archivos, instalar programas o acceder a recursos de red.", "Verifica los permisos de la carpeta afectada. Ejecuta SFC /scannow. Para errores de red, restablece la pila TCP/IP con netsh. Desactiva temporalmente el antivirus para probar."),
"pages/restablecer-windows.html": ("Restablecer Windows 10/11 – Restaurar configuración de fábrica", "Cuando otros métodos de reparación fallan, restablecer Windows a la configuración de fábrica puede resolver todos los problemas persistentes.", "Ve a Configuración → Sistema → Recuperación → Restablecer este PC. Elige 'Mantener mis archivos' (elimina apps, conserva documentos) o 'Quitar todo' para un restablecimiento completo. Sigue las instrucciones en pantalla."),
"pages/modo-seguro-windows.html": ("Modo seguro Windows 10/11 – Cómo iniciarlo", "El modo seguro inicia Windows con un conjunto mínimo de controladores y servicios. Es imprescindible para diagnosticar problemas y eliminar malware.", "Método 1: Configuración → Sistema → Recuperación → Inicio avanzado → Reiniciar ahora → Solucionar problemas → Opciones avanzadas → Configuración de inicio → Reiniciar → Tecla 4 (Modo seguro). Método 2: Mantén Mayús pulsado al reiniciar desde el menú Inicio."),
"pages/dism-reparacion.html": ("DISM – Reparar la imagen del sistema Windows 10/11", "DISM (Deployment Image Servicing and Management) es una herramienta avanzada para reparar la imagen del sistema Windows. Se usa cuando SFC no puede corregir los errores.", "Ejecuta sucesivamente: DISM /Online /Cleanup-Image /CheckHealth, luego /ScanHealth y finalmente /RestoreHealth. El último comando descarga los archivos faltantes de Internet. Duración: 15-45 minutos. Vuelve a ejecutar sfc /scannow después."),
"pages/problemas-impresora.html": ("Problemas de impresora Windows 10/11 – Reparación completa", "¿La impresora no funciona en Windows? Ya sea que no se reconozca, que los trabajos queden atascados o que aparezcan errores – aquí están todas las soluciones.", "Quita y vuelve a agregar la impresora: Configuración → Bluetooth y dispositivos → Impresoras y escáneres → quitar y volver a agregar. Vacía la cola de impresión: en services.msc, detén el servicio Cola de impresión, elimina los archivos en C:\\Windows\\System32\\spool\\PRINTERS y reinicia el servicio."),
"pages/errores-controladores.html": ("Errores de controladores Windows – Actualizar y reparar", "Los controladores son la interfaz entre el hardware y el sistema operativo. Los controladores obsoletos o corruptos provocan BSOD, problemas de sonido, errores gráficos y muchos otros problemas.", "Abre el Administrador de dispositivos (Win + X). Los dispositivos con errores están marcados con un signo de exclamación amarillo. Clic derecho → Actualizar controlador. Para controladores importantes (tarjeta gráfica, chipset), descarga siempre la versión más reciente del sitio del fabricante."),
"pages/problemas-pantalla.html": ("Problemas de pantalla Windows – Resolución, parpadeo, pantalla negra", "Los problemas de pantalla se manifiestan de diversas formas: resolución incorrecta, imagen parpadeante, pantalla negra o colores distorsionados. Aquí las soluciones.", "Clic derecho en el Escritorio → Configuración de pantalla. Establece la resolución recomendada y al menos 60Hz de frecuencia de actualización. Actualiza el controlador de la tarjeta gráfica. En caso de parpadeo, comprueba el cable HDMI/DisplayPort."),
"pages/eliminar-virus-malware.html": ("Eliminar virus y malware – Windows 10/11", "Virus, troyanos, spyware y ransomware pueden dañar gravemente Windows. Síntomas: PC lento, publicidad emergente, programas desconocidos, archivos cifrados.", "Inicia un análisis completo con Windows Defender: Seguridad de Windows → Protección contra virus y amenazas → Opciones de análisis → Análisis completo. Para casos difíciles, usa el modo seguro o Windows Defender sin conexión."),
"pages/optimizar-ram.html": ("Optimizar la RAM en Windows 10/11 – Consejos de expertos", "La RAM es un recurso crítico para el rendimiento de Windows. Cuando las aplicaciones consumen demasiada memoria, el sistema se ralentiza enormemente.", "Cierra las aplicaciones innecesarias y las pestañas del navegador. Desactiva los programas de inicio innecesarios (Administrador de tareas → Inicio). Aumenta el tamaño del archivo de paginación: Propiedades del sistema → Avanzado → Rendimiento → Configuración → Avanzado → Memoria virtual."),
"pages/limpiar-disco-windows.html": ("Limpiar el disco en Windows 10/11 – Liberar espacio", "Con el tiempo, el disco de Windows se llena de archivos temporales, residuos de actualizaciones y aplicaciones no utilizadas. La falta de espacio ralentiza considerablemente Windows.", "Usa el Liberador de espacio en disco (Win + S → Liberador de espacio en disco → Unidad C → marca todas las categorías → Limpiar archivos del sistema). Desinstala los programas no utilizados en Configuración → Aplicaciones."),
"pages/ethernet-sin-internet.html": ("Ethernet no funciona – Sin Internet Windows Fix", "Los problemas con la conexión Ethernet pueden ser tan frustrantes como los problemas de WiFi. ¿Cable conectado pero sin Internet? Aquí están las soluciones.", "Restablece la pila de red: netsh winsock reset e ipconfig /flushdns. Actualiza el controlador de la tarjeta Ethernet en el Administrador de dispositivos. Verifica la configuración del adaptador de red y desactiva IPv6 temporalmente para probar."),
"pages/desactivar-actualizaciones.html": ("Desactivar actualizaciones automáticas Windows 10/11", "Las actualizaciones automáticas pueden ser molestas – consumen ancho de banda, ralentizan el PC y reinician el sistema en el peor momento.", "Pausa temporalmente las actualizaciones: Configuración → Windows Update → Pausar actualizaciones (hasta 5 semanas). Para Windows 10 Pro: gpedit.msc → Configuración del equipo → Plantillas administrativas → Componentes de Windows → Windows Update → Configurar actualizaciones automáticas → Deshabilitado."),
"pages/reparar-sistema-archivos.html": ("Reparar el sistema de archivos NTFS – Windows 10/11", "Un sistema de archivos NTFS dañado puede imposibilitar el acceso a los datos y causar diversos errores del sistema. Windows ofrece herramientas de reparación integradas.", "Ejecuta CHKDSK: chkdsk C: /f /r en el Símbolo del sistema (Administrador). Confirma la programación en el próximo inicio escribiendo S. Alternativa: Propiedades del disco → Herramientas → Comprobar."),
"pages/usb-no-reconocido.html": ("USB no reconocido en Windows 10/11 – Reparación", "Dispositivos USB no reconocidos por Windows – un problema común con pendrives, discos externos, teclados y ratones.", "Prueba con otro puerto USB. Desinstala los controladores USB en el Administrador de dispositivos (Controladores de bus serie universal) y reinicia – Windows los reinstala automáticamente. Desactiva la administración de energía para los puertos USB en las propiedades del dispositivo."),
"pages/windows-11-requisitos.html": ("Windows 11 – Requisitos del sistema y actualización", "Windows 11 impone requisitos de hardware más estrictos que Windows 10. Muchos PCs no cumplen los requisitos por falta de TPM 2.0 o un procesador no compatible.", "Requisitos mínimos: procesador de 1 GHz con 2+ núcleos (64 bits), 4 GB RAM, 64 GB almacenamiento, TPM 2.0, Secure Boot, tarjeta gráfica DirectX 12. Comprueba la compatibilidad con la herramienta Comprobación de estado del PC de Microsoft."),
"pages/recuperar-datos-windows.html": ("Recuperar datos perdidos – Windows 10/11", "Eliminación accidental, formateo del disco o fallo del sistema – estas situaciones pueden provocar pérdida de datos. Sin embargo, existen métodos eficaces para recuperarlos.", "Comprueba primero la Papelera de reciclaje. Usa la función 'Versiones anteriores' (clic derecho en la carpeta → Propiedades → Versiones anteriores). Usa el Historial de archivos si estaba activado. Para una recuperación más profunda, usa la herramienta gratuita Recuva."),
"pages/optimizar-ssd.html": ("Optimizar un SSD en Windows 10/11 – Guía completa", "Los SSD requieren una configuración diferente a los discos duros tradicionales. Una buena configuración de Windows prolonga la vida útil del SSD y mantiene su rendimiento.", "Comprueba que TRIM esté activo: fsutil behavior query DisableDeleteNotify (0 = activo). Desactiva la desfragmentación para SSDs. Activa el modo AHCI en la BIOS. Desactiva la indexación del contenido del disco."),
}

def gen_article(filename, h1, intro, fix=None, sections=None, related=None):
    p = next(x for x in PAGES if x[0] == filename)
    title, meta_desc = p[1], p[3]
    base = "../" if filename.startswith("pages/") else ""

    breadcrumb = f'<div class="container"><div class="breadcrumb"><a href="../index.html">Inicio</a> <span>›</span> <span>{title.split(" – ")[0][:55]}</span></div></div>'

    if sections:
        toc_items = "".join(f'<li><a href="#{i+1}">{s[0]}</a></li>' for i, s in enumerate(sections))
        toc = f'<div class="toc"><h4>Índice de contenidos</h4><ol>{toc_items}</ol></div>'
        body = f"<p>{intro}</p>{toc}"
        for i, (h2, sec) in enumerate(sections):
            body += f'<h2 id="{i+1}">{h2}</h2>{sec}'
    else:
        body = f"""<p>{intro}</p>
<div class="toc"><h4>Índice de contenidos</h4><ol><li><a href="#1">Causas y síntomas</a></li><li><a href="#2">Solución paso a paso</a></li><li><a href="#3">Reparación automática</a></li></ol></div>
<h2 id="1">Causas y síntomas</h2>
<p>Este problema puede tener varios orígenes. Un diagnóstico preciso es importante antes de comenzar la reparación para elegir el método más eficaz.</p>
<div class="warning-box"><strong>⚠️ Antes de comenzar:</strong> Crea un punto de restauración del sistema: <strong>Win + R → sysdm.cpl → Protección del sistema → Crear</strong></div>
<h2 id="2">Solución paso a paso</h2>
<p>{fix}</p>
<div class="tip-box"><strong>💡 Consejo pro:</strong> Tras cualquier reparación, ejecuta <strong>sfc /scannow</strong> en el Símbolo del sistema (Administrador) para asegurarte de que ningún archivo del sistema ha sido dañado.</div>
<div class="code-block">sfc /scannow</div>
<h2 id="3">Reparación automática</h2>
<p>Si los métodos manuales resultan demasiado complejos o no dan resultado, nuestra herramienta de diagnóstico automático puede ayudarte.</p>
<div class="cta-box">
  <h3>🔧 Reparar automáticamente</h3>
  <p>La herramienta analiza tu sistema y corrige todos los errores detectados con un solo clic.</p>
  <a href="{AFFILIATE}" class="btn-dl" target="_blank" rel="nofollow">⬇ Descargar gratis</a>
</div>"""

    if not related:
        others = [x for x in PAGES if x[0] != filename and x[0] != "index.html"][:4]
    else:
        others = [x for x in PAGES if x[0] in related][:4]

    rc = "".join(f'<a href="{rel(filename,x[0])}" class="related-card"><h4>{x[1].split(" – ")[0]}</h4><p>{x[3][:65]}...</p></a>' for x in others)
    body += f'<div class="related-articles"><h3>Artículos relacionados</h3><div class="related-grid">{rc}</div></div>'

    html = head_html(title, meta_desc, filename, filename)
    html += trust_bar()
    html += breadcrumb
    html += f"""
<div class="container">
  <div class="layout">
    <article class="main">
      <h1>{h1}</h1>
      <div class="meta">
        <span class="tag">Guía</span>
        <span>📅 Actualizado: 2024</span>
        <span>⏱ Lectura: ~5 min</span>
        <span>🖥️ Windows 10 &amp; 11</span>
      </div>
      {body}
    </article>
    {sidebar_html(filename)}
  </div>
</div>
{footer_html(filename)}
</body></html>"""

    os.makedirs(f"{BASE}/pages", exist_ok=True)
    with open(f"{BASE}/{filename}", 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✓ {filename}")

def gen_index():
    icons = {"bsod":"💀","arranque":"🔄","optimizacion":"⚡","actualizaciones":"🔄","audio":"🔊",
             "red":"📶","disco":"💾","registro":"📋","bloqueos":"⚠️","codigos-error":"🔴",
             "reset":"♻️","diagnostico":"🔍","dispositivos":"🖨️","controladores":"🎛️",
             "pantalla":"🖥️","seguridad":"🛡️","windows11":"🪟","recuperacion":"📂"}
    cards = ""
    for p in PAGES[1:]:
        icon = icons.get(p[2], "🔧")
        cards += f"""
<a href="{p[0]}" class="card">
  <div class="card-icon">{icon}</div>
  <h3>{p[1].split(" – ")[0]}</h3>
  <p>{p[3][:88]}...</p>
  <span class="read-more">Leer la guía →</span>
</a>"""

    features = """
<div class="features">
  <div class="feature"><div class="icon">✅</div><h4>Métodos verificados</h4><p>Cada guía se prueba en sistemas Windows 10 y 11 reales</p></div>
  <div class="feature"><div class="icon">🇪🇸</div><h4>En español</h4><p>Todas las guías en español claro, sin jerga técnica</p></div>
  <div class="feature"><div class="icon">🔒</div><h4>100% seguro</h4><p>Solo métodos seguros sin riesgo de pérdida de datos</p></div>
  <div class="feature"><div class="icon">🆓</div><h4>Gratis</h4><p>Todas las guías y herramientas básicas completamente gratuitas</p></div>
</div>"""

    html = head_html(PAGES[0][1], PAGES[0][3], "index.html", "")
    html += trust_bar()
    html += f"""
<main>
  <section class="hero">
    <div class="hero-orb1"></div>
    <div class="hero-orb2"></div>
    <div class="hero-inner">
      <div class="hero-label">🛠️ Portal de reparación Windows 10 &amp; 11</div>
      <h1>Repara Windows<br><span class="highlight">rápido</span> y sin<br><span class="red">complicaciones</span></h1>
      <p>Más de 30 guías detalladas en español para resolver todos los problemas de Windows – gratuitas, verificadas por expertos, actualizadas regularmente.</p>
      <div class="hero-btns">
        <a href="{AFFILIATE}" class="btn-dl" target="_blank" rel="nofollow">⬇ Descargar herramienta de reparación gratis</a>
        <a href="#guias" class="btn-outline">📋 Ver todas las guías</a>
      </div>
      <div class="hero-numbers">
        <div class="hero-num"><span class="n">30+</span><span class="l">Guías gratuitas</span></div>
        <div class="hero-num"><span class="n">100%</span><span class="l">En español</span></div>
        <div class="hero-num"><span class="n">Win 10/11</span><span class="l">Compatible</span></div>
      </div>
    </div>
  </section>

  <div class="container">
    <div class="section-header" id="guias">
      <h2>Problemas de Windows más frecuentes</h2>
      <p>Elige tu problema y sigue nuestra guía detallada.</p>
    </div>
    <div class="card-grid">{cards}</div>

    <div class="cta-box">
      <h3>¿No encuentras tu problema?</h3>
      <p>Nuestra herramienta de diagnóstico automático analiza tu sistema y detecta todos los errores.</p>
      <a href="{AFFILIATE}" class="btn-dl" target="_blank" rel="nofollow">⬇ WinRepairHub Tool – Descargar gratis</a>
    </div>

    <div class="section-header">
      <h2>¿Por qué WinRepairHub?</h2>
    </div>
    {features}
  </div>
</main>
{footer_html("index.html")}
</body></html>"""

    with open(f"{BASE}/index.html", 'w', encoding='utf-8') as f:
        f.write(html)
    print("✓ index.html")

gen_index()
for filename, data in ARTICLES.items():
    gen_article(filename, data["h1"], data["intro"],
                sections=data.get("sections"), related=data.get("related"))
for filename, (h1, intro, fix) in GENERIC.items():
    gen_article(filename, h1, intro, fix=fix)

# robots.txt + sitemap + .htaccess
with open(f"{BASE}/robots.txt", 'w') as f:
    f.write("User-agent: *\nAllow: /\nSitemap: https://winrepairhub.es/sitemap.xml\n")

with open(f"{BASE}/.htaccess", 'w') as f:
    f.write("""AddType application/xml .xml
AddType text/html .html

<IfModule mod_headers.c>
    Header set X-Robots-Tag "index, follow"
</IfModule>

<IfModule mod_expires.c>
    ExpiresActive On
    ExpiresByType application/xml "access plus 1 day"
    ExpiresByType text/html "access plus 1 hour"
</IfModule>

<Files "sitemap.xml">
    Header set Content-Type "application/xml; charset=UTF-8"
</Files>

<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteCond %{HTTP_USER_AGENT} (Googlebot|bingbot|Slurp|DuckDuckBot|Baiduspider|YandexBot) [NC]
    RewriteRule .* - [L]
</IfModule>

Options -Indexes
""")

urls = "\n".join(f"""  <url>
    <loc>https://winrepairhub.es/{p[0] if p[0]!='index.html' else ''}</loc>
    <changefreq>monthly</changefreq>
    <priority>{'1.0' if p[0]=='index.html' else '0.8'}</priority>
    <lastmod>2024-01-15</lastmod>
  </url>""" for p in PAGES)

with open(f"{BASE}/sitemap.xml", 'w', encoding='utf-8') as f:
    f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>')

print(f"\n✅ ¡Listo! {len(PAGES)} páginas generadas.")
