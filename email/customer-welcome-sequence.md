# Customer Welcome Sequence - Post-Purchase

## Overview
5-email sequence sent after purchase.
Goals: Reduce buyer's remorse, increase consumption, build community.

---

## Email 1: Welcome + Immediate Access
**Trigger:** Immediately after purchase
**Subject:** 🎉 ¡Bienvenido a CEO Autónomo! Tu acceso está aquí

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bienvenido a CEO Autónomo</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; color: #1f2937; margin: 0; padding: 0; background: #f9fafb; }
        .container { max-width: 600px; margin: 0 auto; background: #ffffff; }
        .header { background: linear-gradient(135deg, #2563eb 0%, #059669 100%); color: white; padding: 40px 30px; text-align: center; }
        .content { padding: 40px 30px; }
        .button { display: inline-block; background: #059669; color: white; padding: 16px 32px; border-radius: 8px; text-decoration: none; font-weight: 600; font-size: 18px; margin: 20px 0; }
        .download-box { background: #f0fdf4; border: 2px solid #059669; padding: 30px; border-radius: 8px; margin: 30px 0; text-align: center; }
        .framework { background: #f9fafb; border-left: 4px solid #2563eb; padding: 20px; margin: 20px 0; }
        .footer { background: #f3f4f6; padding: 30px; text-align: center; font-size: 14px; color: #6b7280; }
        .community { background: #fef3c7; padding: 20px; border-radius: 8px; margin: 20px 0; }
        @media only screen and (max-width: 600px) {
            .content { padding: 30px 20px; }
            .header { padding: 30px 20px; }
        }
    </style>
</head>
<body>
    <div class="container">

        <!-- Header -->
        <div class="header">
            <h1 style="margin: 0 0 10px 0; font-size: 28px;">🎉 ¡Bienvenido!</h1>
            <p style="margin: 0; font-size: 18px; opacity: 0.9;">Tu acceso a CEO Autónomo está listo</p>
        </div>

        <!-- Content -->
        <div class="content">

            <p>Hola {{first_name}},</p>

            <p><strong>Gracias por tu confianza.</strong></p>

            <p>Acabas de tomar una de las mejores decisiones para tu negocio (y tu vida).</p>

            <p>En los próximos 30 días vas a tener sistemas que te devuelven horas semanales.</p>

            <!-- Download Box -->
            <div class="download-box">
                <h3 style="margin: 0 0 10px 0; color: #059669;">📥 Descarga tu guía aquí:</h3>
                <p style="color: #374151; margin: 0 0 20px 0;">CEO Autonomo - Guia Maestra v3.0.pdf</p>
                <a href="{{download_url}}" class="button">Descargar Ahora →</a>
                <p style="font-size: 14px; color: #6b7280; margin: 15px 0 0 0;">El link es permanente. Guarda este email.</p>
            </div>

            <p><strong>Lo que acabas de obtener:</strong></p>

            <ul style="line-height: 2; color: #374151;">
                <li>✅ Guía completa (100+ páginas)</li>
                <li>✅ 5 frameworks detallados paso a paso</li>
                <li>✅ 20+ plantillas listas para usar</li>
                <li>✅ Toolkit de automatización</li>
                <li>✅ Acceso de por vida</li>
                <li>✅ Actualizaciones gratis</li>
            </ul>

            <p><strong>Recomendación: Empieza con esto</strong></p>

            <div class="framework">
                <strong>1. Framework #1: Máquina de Delegación</strong>
                <p style="margin: 10px 0 0 0;">Leelo primero. Es el que más impacto tiene inmediatamente.</p>
            </div>

            <div class="framework">
                <strong>2. El Checklist de 7 Días (incluido)</strong>
                <p style="margin: 10px 0 0 0;">Síguelo exactamente. Te lleva de la teoría a la acción.</p>
            </div>

            <div class="framework">
                <strong>3. Calcula Tu Costo Real</strong>
                <p style="margin: 10px 0 0 0;">Haz el ejercicio del costo de NO delegar. Es revelador.</p>
            </div>

            <div class="community">
                <strong>💬 Únete a la comunidad</strong>
                <p style="margin: 10px 0 0 0;">Tenemos un grupo privado de CEOs Autónomos. Pregunta, comparte, conecta:</p>
                <p style="margin: 15px 0 0 0;"><a href="{{community_link}}" style="color: #2563eb; font-weight: 600;">👉 Unirse al grupo privado</a></p>
            </div>

            <p><strong>Expectativas realistas:</strong></p>

            <p>Semana 1: Vas a sentir que "no tienes tiempo" de implementar.<br>
            <em>Esto es normal. Empieza con 30 minutos.</em></p>

            <p>Semana 2: Vas a documentar tu primera tarea.<br>
            <em>Pequeño win. Celebralo.</em></p>

            <p>Semana 3-4: Vas a delegar algo.<br>
            <em>Ahí es donde empieza la magia.</em></p>

            <p>Una pregunta antes de irme:</p>

            <p><em>¿Qué tarea odias hacer que podrías delegar primero?</em></p>

            <p>Responde a este email con tu respuesta. Leelo personalmente.</p>

            <p>Estoy aquí para ayudarte a implementar.</p>

            <p>Alfred</p>

            <p style="font-size: 14px; color: #6b7280; margin-top: 30px;">
                P.D. Guarda este email en una carpeta segura. Es el único lugar con tu link de descarga permanente.
            </p>

        </div>

        <!-- Footer -->
        <div class="footer">
            <p>¿Preguntas? Responde a este email.</p>
            <p style="margin: 10px 0;">
                <a href="mailto:support@ceoautonomo.com" style="color: #2563eb;">Soporte</a>
            </p>
        </div>

    </div>
</body>
</html>
```

---

## Email 2: Day 3 - First Win Check-in
**Trigger:** 72 hours post-purchase
**Subject:** Quick check: ¿Ya empezaste el Framework #1?

```
Hola {{first_name}},

Han pasado 3 días desde tu compra.

Pregunta honesta: ¿Ya leíste el Framework #1 (Máquina de Delegación)?

Si SÍ → Qué framework te pareció más útil? Responde y cuéntame.

Si NO → Totalmente normal. La vida interrumpe.

Pero aquí está el truco:

No necesitas "encontrar tiempo".
Necesitas robar 15 minutos.

Opciones:
• En lugar de Instagram en la cama → Leer Framework #1
• En lugar de Netflix → Leer Framework #1
• En lugar de responder ese email no urgente → Leer Framework #1

Las primeras 15 minutos son las más importantes.

Rompe la inercia.

[LINK DE DESCARGA]

P.D. Mañana te envío mi "Anti-Procrastinación Hack" que uso cuando no tengo ganas de hacer algo importante.
-Alfred
```

---

## Email 3: Day 7 - First Week Milestone
**Trigger:** 7 days post-purchase
**Subject:** Semana 1 completa: Tienes 3 la opciones

```
Hola {{first_name}},

Han pasado 7 días.

Estás en un punto decisivo:

Camino A: Leíste algo → Hiciste el ejercicio → Documentaste tu primera tarea
→ RESULTADO: Ya tienes momentum. Siguiente paso: encontrar a quien delegar.

Camino B: Leíste algo → No hiciste nada aún
→ RESULTADO: Información sin acción = entretenimiento. Pero gastaste $47, no $14 de Netflix.

Camino C: Ni siquiera abriste el PDF aún
→ RESULTADO: Estás validando tu creencia de que "no tienes tiempo". Ironía: exactamente por eso compraste esto.

(No soy duro por ser cruel. Soy directo porque es lo que necesitas.)

La buena noticia:

Da igual en qué camino estés.

Solo necesitas 1 acción hoy:

SI Camino A: Comenta en el grupo qué tarea vas a delegar primero.

SI Camino B: Abre el PDF AHORA y lee solo la página 1-5.

SI Camino C: Configura un timer de 25 minutos y abre el PDF. Nada más. Solo ábrelo.

[LINK A COMUNIDAD]

El 80% del éxito es empez