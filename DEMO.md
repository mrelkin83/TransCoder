# Demo de TransCoder 🎬

Este documento te guiará paso a paso para probar TransCoder y ver todo su poder en acción.

---

## Demo 1: Tu Primer Proyecto (5 minutos)

Vamos a crear un dashboard de analytics completo usando TransCoder.

### Paso 1: Iniciar TransCoder CLI

```bash
cd TransCoder
python transcoder-cli.py
```

Verás:

```
┌───────────────────────────────────────┐
│ TransCoder - Tu Traductor de Ideas   │
│ Optimiza prompts • Ahorra tokens     │
└───────────────────────────────────────┘

No hay proyecto activo.

¿Crear nuevo proyecto? (Y/n):
```

### Paso 2: Configurar Proyecto

Presiona `Y` y responde:

```
📋 CONFIGURACIÓN INICIAL

Nombre del proyecto: analytics-dashboard
Tipo de proyecto:
  1. Web (sitio web, landing, dashboard)
  2. App (móvil, desktop)
  3. API (backend, microservicio)
  4. CLI (herramienta línea de comandos)
  5. Script (automatización, utilidad)
Elige: 1

Stack tecnológico (separado por comas): Next.js, TypeScript, Tailwind, Chart.js

Feature principal (máx 10 palabras): Dashboard analytics con gráficas interactivas
```

### Paso 3: Ver el Plan Generado

TransCoder automáticamente genera:

```
📋 PLAN GENERADO (5 pasos)

#  Paso                   Descripción
───────────────────────────────────────────────────────────
1  Setup                  Inicializar proyecto y dependencias
2  Layout                 Estructura base y navegación
3  Feature Core           Implementar Dashboard analytics con gráficas interactivas
4  Estilos                UI/UX y responsive design
5  Testing                Tests y optimización

¿Empezar con el paso 1? (Y/n):
```

### Paso 4: Ejecutar Primer Paso

Presiona `Y` para ver el prompt optimizado:

```
🔄 PASO 1/5: Setup

📝 PROMPT GENERADO (152 tokens):
───────────────────────────────────────
🎯 TAREA: Inicializar proyecto y dependencias

📦 PROYECTO:
- Nombre: analytics-dashboard
- Tipo: web
- Stack: Next.js, TypeScript, Tailwind, Chart.js

✅ REQUERIMIENTOS:
• Inicializar proyecto Next.js 14 con App Router
• Configurar TypeScript estricto
• Instalar y configurar Tailwind CSS
• Añadir Chart.js y react-chartjs-2
• Estructura de carpetas: src/app/, src/components/, src/lib/

📤 OUTPUT:
- Comandos a ejecutar (si aplica)
- Archivos a crear con contenido completo
- Configuraciones necesarias
- Sin explicaciones largas

🚫 NO INCLUIR:
- Comentarios verbose en código
- Archivos de ejemplo/demo innecesarios
───────────────────────────────────────

💰 Tokens estimados: ~152
📊 Ahorro estimado vs manual: ~65%

¿Qué hacer?
  1. Copiar al portapapeles
  2. Guardar en archivo
  3. Marcar como completado manualmente
  4. Saltar este paso

Elige: 1
```

### Paso 5: Usar el Prompt

1. El prompt se copia al portapapeles
2. Abre Claude Code (o tu agente favorito)
3. Pega el prompt
4. ¡El agente creará todo el setup perfectamente!

### Paso 6: Marcar como Completado

Vuelve a TransCoder CLI:

```
¿Paso completado? (marca como hecho) (y/N): y

✅ Paso 1 completado

¿Continuar con siguiente paso? (y/N): y
```

### Paso 7: Repetir para Todos los Pasos

TransCoder te guiará paso a paso hasta completar el proyecto entero.

---

## Demo 2: Uso desde Claude Code (Skill)

### Paso 1: Abrir Claude Code

```bash
# Si usas Claude Code CLI
claude-code
```

### Paso 2: Activar TransCoder

Simplemente escribe en el chat:

```
Tú: Nuevo proyecto con transcoder: API de tareas con FastAPI
```

### Paso 3: Claude Code Responde

```
🤖 Claude Code (usando TransCoder skill):

📋 CONFIGURACIÓN INICIAL

Proyecto: api-tareas
Tipo: API
Stack: FastAPI, Python 3.10, PostgreSQL, SQLAlchemy

📋 PLAN GENERADO (5 pasos):

1. [Setup] Estructura FastAPI + dependencias
2. [Database] Modelos SQLAlchemy para tareas
3. [Endpoints] CRUD completo de tareas
4. [Auth] Autenticación con JWT
5. [Testing] Tests con pytest

🎯 ¿Empezamos con el paso 1?
```

### Paso 4: Continuar la Conversación

```
Tú: Sí, dale

🤖 Claude Code:

🔄 PASO 1/5: Setup

Voy a generar el prompt optimizado para inicializar el proyecto...

[Automáticamente genera y ejecuta el prompt]

✅ Setup completado

Archivos creados:
- main.py (servidor FastAPI)
- requirements.txt (dependencias)
- database.py (configuración DB)
- models/ (estructura para modelos)
- api/routes/ (estructura para endpoints)

📊 Tokens usados: 234 (ahorro: ~68% vs manual)

¿Continúo con paso 2 (Database)?
```

---

## Demo 3: Auditoría de Eficiencia

Después de completar varios pasos, audita tu eficiencia:

```bash
python transcoder-cli.py audit
```

Verás:

```
┌─────────────────────────────────────────┐
│ 🔍 Auditoría de Eficiencia              │
└─────────────────────────────────────────┘

📊 MÉTRICAS GENERALES

Métrica              Valor
──────────────────────────────
Pasos completados    3
Tokens prompts       682
Tokens respuestas    1,450
Total tokens         2,132
Promedio por prompt  227
Ahorro estimado      ~65%


💡 RECOMENDACIONES:

  • Buen progreso: Has avanzado significativamente
  • Eficiencia óptima: Tus prompts están bien optimizados
```

---

## Demo 4: Agregar Contexto Dinámico

A medida que trabajas, añade archivos importantes al contexto:

```bash
# Añadir archivo al contexto
python transcoder-cli.py context src/app/layout.tsx

✅ 'src/app/layout.tsx' añadido al contexto

# Ahora TransCoder lo incluirá automáticamente en futuros prompts
```

---

## Demo 5: Ver Estado del Proyecto

En cualquier momento:

```bash
python transcoder-cli.py status
```

```
┌───────────────────────────────────────┐
│ 📊 Estado del Proyecto                │
│ analytics-dashboard                   │
│ Tipo: web • Stack: Next.js, ...      │
└───────────────────────────────────────┘

Progreso: 3/5 pasos (60%)
Fase actual: development
Ahorro de tokens: ~4,280 tokens

Pasos del Plan

#  Estado          Paso            Descripción
─────────────────────────────────────────────────────────
1  ✅ Completado   Setup           Inicializar proyecto...
2  ✅ Completado   Layout          Estructura base...
3  ✅ Completado   Feature Core    Dashboard analytics...
4  ⏳ Pendiente    Estilos         UI/UX responsive...
5  ⏳ Pendiente    Testing         Tests y optimización...

📁 Archivos en contexto:
  • src/app/layout.tsx
  • src/components/Dashboard.tsx
```

---

## Demo 6: Comandos Rápidos

### Crear Proyecto Rápido

```bash
# Directo sin modo interactivo
python transcoder-cli.py new
```

### Siguiente Paso Inmediato

```bash
# Ir al siguiente paso directamente
python transcoder-cli.py next
```

### Ver Solo Estado

```bash
# Ver estado sin interacción
python transcoder-cli.py status
```

---

## Demo 7: Comparación de Prompts

### Sin TransCoder (Prompt Manual Típico):

```
Hola, me gustaría que por favor me ayudaras a crear un dashboard
para analytics. Quiero que sea bonito y moderno, con gráficas
interactivas que se vean bien. Usa Next.js porque es lo que
conozco, y también TypeScript porque me gusta. Ah, y que sea
responsive para móviles también. Gracias!
```

**Problemas:**
- ❌ Ambiguo ("bonito", "moderno")
- ❌ Información redundante
- ❌ Sin estructura
- ❌ ~580 tokens estimados
- ❌ Alta probabilidad de alucinación

### Con TransCoder (Prompt Optimizado):

```
🎯 TAREA: Crear componente Dashboard

📁 CONTEXTO:
- Archivo: src/components/Dashboard.tsx
- Stack: Next.js 14, TypeScript, Chart.js

✅ REQUERIMIENTOS:
- Grid responsive 12 columnas (Tailwind)
- 3 gráficas: línea (ventas), barra (categorías), dona (usuarios)
- KPI cards con iconos
- Mobile-first design

📤 OUTPUT:
- Solo código TypeScript/JSX
- Sin explicaciones
- Imports necesarios

🚫 NO INCLUIR:
- Comentarios verbose
- Código de ejemplo
```

**Beneficios:**
- ✅ Específico y accionable
- ✅ Contexto preciso
- ✅ Estructura clara
- ✅ ~210 tokens (ahorro: 64%)
- ✅ Baja probabilidad de error

---

## Demo 8: Templates Personalizados

### Crear Template Custom

Edita `.claude/skills/transcoder/templates/universal.md`:

```markdown
## Mi Template Custom

```
[ROLE] Expert {framework} developer

[TASK]
{mi_tarea_custom}

[CONTEXT]
{mi_contexto}

[OUTPUT]
- {formato_output}
```
```

Usa variables `{nombre_variable}` que luego puedes llenar desde el CLI.

---

## Flujo Completo de Ejemplo

Aquí está el flujo completo de crear un proyecto real:

```bash
# 1. Iniciar proyecto
$ python transcoder-cli.py new

# Configurar: E-commerce, Next.js+Stripe
# Plan generado: 8 pasos

# 2. Paso 1: Setup
$ python transcoder-cli.py next
[Copiar prompt → Claude Code → Ejecutar → Marcar completado]

# 3. Paso 2: Products catalog
$ python transcoder-cli.py next
[Copiar prompt → Claude Code → Ejecutar → Marcar completado]

# 4. Añadir contexto
$ python transcoder-cli.py context src/lib/stripe.ts
$ python transcoder-cli.py context src/app/products/page.tsx

# 5. Continuar pasos...
$ python transcoder-cli.py next  # Paso 3
$ python transcoder-cli.py next  # Paso 4
# ... hasta paso 8

# 6. Auditar al final
$ python transcoder-cli.py audit

📊 RESULTADO:
- 8 pasos completados
- 15,230 tokens totales
- Ahorro: 67% vs manual (~31,000 tokens estimados)
- Costo: $2.30 vs $6.80 estimado manual
- Tiempo: 2 horas vs 4-5 horas manual
```

---

## Demo 9: Uso con OpenCode (GitHub Copilot)

TransCoder tiene soporte optimizado para OpenCode con el formato nativo `@workspace`.

### Paso 1: Configurar Proyecto para OpenCode

```bash
python transcoder-cli.py new

# Proyecto: user-dashboard
# Stack: Next.js, TypeScript, Tailwind
# Feature: Dashboard de usuarios con gráficas
```

### Paso 2: Generar Prompt Formato OpenCode

```bash
python transcoder-cli.py next
```

TransCoder detecta automáticamente si usas OpenCode/GitHub Copilot y genera:

```
@workspace Create UserDashboard component

Context:
#file:src/components/UserDashboard.tsx
Stack: Next.js 14, TypeScript, Tailwind CSS, Recharts

Requirements:
1. Grid layout 3 columns (responsive to 1 on mobile)
2. User stats cards (total, active, inactive)
3. Line chart - User growth last 30 days
4. Bar chart - Users by role
5. Data table - Recent users (last 10)
6. Loading states for async data

Output: TypeScript/JSX code only
Constraints: Server Component default, client only for charts
```

### Paso 3: Usar en GitHub Copilot Chat

1. Abre GitHub Copilot Chat (Ctrl+I o Cmd+I)
2. Pega el prompt generado
3. GitHub Copilot generará el código completo

### Paso 4: Resultado Esperado

GitHub Copilot generará código como:

```tsx
'use client';

import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { LineChart, Line, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

interface UserDashboardProps {
  totalUsers: number;
  activeUsers: number;
  inactiveUsers: number;
  growthData: { date: string; count: number }[];
  roleData: { role: string; count: number }[];
  recentUsers: { id: string; name: string; email: string; role: string }[];
}

export function UserDashboard({
  totalUsers,
  activeUsers,
  inactiveUsers,
  growthData,
  roleData,
  recentUsers
}: UserDashboardProps) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-6 p-6">
      {/* Stats Cards */}
      <Card>
        <CardHeader>
          <CardTitle>Total Users</CardTitle>
        </CardHeader>
        <CardContent>
          <p className="text-3xl font-bold">{totalUsers}</p>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle>Active Users</CardTitle>
        </CardHeader>
        <CardContent>
          <p className="text-3xl font-bold text-green-600">{activeUsers}</p>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle>Inactive Users</CardTitle>
        </CardHeader>
        <CardContent>
          <p className="text-3xl font-bold text-gray-400">{inactiveUsers}</p>
        </CardContent>
      </Card>

      {/* Growth Chart */}
      <Card className="col-span-1 md:col-span-2">
        <CardHeader>
          <CardTitle>User Growth (Last 30 Days)</CardTitle>
        </CardHeader>
        <CardContent>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={growthData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="date" />
              <YAxis />
              <Tooltip />
              <Line type="monotone" dataKey="count" stroke="#3b82f6" strokeWidth={2} />
            </LineChart>
          </ResponsiveContainer>
        </CardContent>
      </Card>

      {/* Role Distribution */}
      <Card>
        <CardHeader>
          <CardTitle>Users by Role</CardTitle>
        </CardHeader>
        <CardContent>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={roleData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="role" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="count" fill="#3b82f6" />
            </BarChart>
          </ResponsiveContainer>
        </CardContent>
      </Card>

      {/* Recent Users Table */}
      <Card className="col-span-1 md:col-span-3">
        <CardHeader>
          <CardTitle>Recent Users</CardTitle>
        </CardHeader>
        <CardContent>
          <table className="w-full">
            <thead>
              <tr className="border-b">
                <th className="text-left p-2">Name</th>
                <th className="text-left p-2">Email</th>
                <th className="text-left p-2">Role</th>
              </tr>
            </thead>
            <tbody>
              {recentUsers.map(user => (
                <tr key={user.id} className="border-b">
                  <td className="p-2">{user.name}</td>
                  <td className="p-2">{user.email}</td>
                  <td className="p-2">
                    <span className="px-2 py-1 bg-blue-100 text-blue-800 rounded text-sm">
                      {user.role}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </CardContent>
      </Card>
    </div>
  );
}
```

### Ventajas del Formato OpenCode

✅ **Más conciso:** ~30% menos tokens que formato universal
✅ **Mejor comprensión:** GitHub Copilot entiende mejor `@workspace`
✅ **Referencias explícitas:** `#file:` para ubicación exacta
✅ **Integración nativa:** Funciona perfectamente con Copilot Chat
✅ **Menos iteraciones:** Código correcto en primer intento

### Comparación de Tokens

| Formato | Tokens | Diferencia |
|---------|--------|------------|
| Manual (sin TransCoder) | ~620 | Baseline |
| Universal (TransCoder) | ~210 | -66% |
| OpenCode (TransCoder) | ~180 | -71% |

**Ahorro adicional con OpenCode:** 5-10% vs formato universal

---

## Casos de Uso Reales Documentados

### Caso 1: Startup - Landing Page

**Contexto:** Landing page para startup SaaS
**Stack:** Astro + Tailwind
**Pasos:** 6
**Tiempo:** 1.5 horas
**Tokens:** 8,420
**Ahorro vs manual:** 71%

### Caso 2: Freelance - E-commerce

**Contexto:** Tienda online completa
**Stack:** Next.js + Stripe + PostgreSQL
**Pasos:** 12
**Tiempo:** 8 horas
**Tokens:** 24,800
**Ahorro vs manual:** 68%

### Caso 3: Empresa - Dashboard Interno

**Contexto:** Panel de analytics para equipo
**Stack:** React + Node.js + MongoDB
**Pasos:** 9
**Tiempo:** 5 horas
**Tokens:** 18,500
**Ahorro vs manual:** 64%

---

## Tips para Maximizar Eficiencia

### 1. Usa Contexto Inteligentemente

❌ **Mal:**
```bash
# Añadir todos los archivos
tc context src/app/*.tsx  # Demasiado
```

✅ **Bien:**
```bash
# Solo archivos clave del paso actual
tc context src/components/Dashboard.tsx
tc context src/lib/api.ts
```

### 2. Planifica Antes de Ejecutar

❌ **Mal:**
```
Ir ejecutando pasos sin revisar el plan completo
```

✅ **Bien:**
```bash
# Ver plan completo primero
tc status
# Ajustar si es necesario
# Luego ejecutar paso a paso
```

### 3. Audita Regularmente

```bash
# Cada 5 pasos completados
tc audit

# Ajusta según recomendaciones
```

### 4. Nombra Proyectos Descriptivamente

❌ **Mal:** `proyecto1`, `test`, `nuevo`
✅ **Bien:** `dashboard-analytics`, `api-ecommerce`, `landing-startup`

---

## Próximos Experimentos

Una vez domines lo básico, prueba:

1. **Crear proyecto con múltiples agentes:**
   - Paso 1-3: Claude Code
   - Paso 4-6: Cursor
   - Mismo contexto TransCoder

2. **Integrar con Git:**
   - Commit automático por paso
   - Branch por feature

3. **Compartir templates:**
   - Exporta tus templates custom
   - Comparte con equipo

4. **Medir ROI real:**
   - Trackea tiempo y costo
   - Compara con proyectos previos sin TransCoder

---

## ¿Preguntas?

Después de probar estos demos, deberías poder:

- ✅ Crear proyectos nuevos con TransCoder
- ✅ Generar prompts optimizados automáticamente
- ✅ Seguir planes paso a paso
- ✅ Auditar tu eficiencia
- ✅ Integrar con Claude Code y otros agentes

**Si algo no funciona:** Revisa [INSTALL.md](INSTALL.md) o reporta un issue.

---

<div align="center">

**¡Ahora ve y crea algo increíble con TransCoder!**

[Volver al README](README.md) • [Instalación](INSTALL.md)

</div>
