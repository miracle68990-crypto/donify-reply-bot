# ---------------------------------------------------------
# EDIT THIS FILE to set up your bot's canned replies.
# No need to touch bot.py at all.
# ---------------------------------------------------------

# MATCH_MODE controls how triggers are matched against incoming messages:
#   "contains" -> replies if the trigger word/phrase appears ANYWHERE in the message
#   "exact"    -> replies only if the message EXACTLY matches the trigger (ignoring case/spacing)
MATCH_MODE = "contains"

# ---------------------------------------------------------
# Reply text, written once per topic.
# ---------------------------------------------------------
REFERRAL_REPLY = (
    "Por ahora no hay ningún programa de rewards por referidos confirmado "
    "oficialmente. Lo único documentado en la web oficial (donifyapp.com/faq) "
    "es el sistema de Points, que mide actividad dentro del ecosistema pero "
    "no es dinero ni criptomoneda. Si sale algo oficial sobre referidos, se "
    "anunciará en los canales oficiales de Donify."
)

REFERRAL_REWARD_MECHANIC_REPLY = (
    "Los rewards por referido funcionan a través de la donación: si la "
    "persona que referiste hace una donación en la app, tanto tú como esa "
    "persona reciben un reward. (Esto aún no está publicado en la web "
    "oficial de Donify — es info confirmada directamente por el equipo "
    "del proyecto.)"
)

WHAT_IS_DONIFY_REPLY = (
    "DONIFY es un ecosistema descentralizado de donaciones cripto. Permite "
    "apoyar proyectos directamente a través de blockchain, sin registro "
    "complicado ni intermediarios centralizados. Más info: https://donifyapp.com"
)

POINTS_REPLY = (
    "Los Points muestran tu actividad dentro del ecosistema Donify. No son "
    "dinero ni criptomoneda: sirven para que el sistema identifique quién "
    "participó activamente apoyando proyectos e interactuando con Donify."
)

GETTING_STARTED_REPLY = (
    "Para empezar: 1) abre DONIFY en Telegram, 2) elige un proyecto, "
    "3) confirma la donación desde tu wallet, 4) revisa que la transacción "
    "quedó registrada. Bot oficial: https://t.me/donify_app_bot"
)

ALREADY_STARTED_REPLY = (
    "No hay confirmación oficial de que un programa de rewards por "
    "referidos ya haya empezado. Si ves algo en tu cuenta, probablemente "
    "sea el conteo de Points o el status de tus referidos, no un reward "
    "confirmado. Para info oficial, revisa los canales verificados de Donify."
)

CONDITIONS_REPLY = (
    "No hay un número mínimo de referidos requerido — cuentan tantos como "
    "hayas hecho. Y sí, los referidos anteriores también cuentan, ya que "
    "vienen de tu enlace de referido. (Esto aún no está publicado en la "
    "web oficial de Donify — es info confirmada directamente por el "
    "equipo del proyecto.)"
)

PUBLISH_PROJECT_REPLY = (
    "No, actualmente no cualquiera puede publicar un proyecto. Los "
    "proyectos los crea y gestiona el dueño de Donify. (Esto aún no está "
    "publicado en la web oficial de Donify — es info confirmada "
    "directamente por el equipo del proyecto.)"
)

DONATION_REPLY = (
    "Para donar: abre DONIFY en Telegram, elige un proyecto y confirma la "
    "donación desde tu wallet. Para verificar que salió bien: 1) revisa que "
    "tu wallet mostró confirmación exitosa, 2) chequea la dirección del "
    "proyecto y el monto, 3) confirma que el registro aparece en la "
    "blockchain — puedes usar el enlace \"Check transaction in explorer\" "
    "si aparece en la interfaz."
)

PROJECT_REPLY = (
    "DONIFY es un ecosistema descentralizado de donaciones cripto donde "
    "puedes apoyar proyectos directamente por blockchain. Actualmente está "
    "en etapa de lanzamiento, así que los primeros proyectos los crea el "
    "propio ecosistema Donify, para mostrar cómo funciona el sistema de "
    "donaciones y transacciones."
)

WHO_REVIEWS_REPLY = (
    "El dueño de Donify revisa los proyectos. (Esto aún no está publicado "
    "en la web oficial de Donify — es info confirmada directamente por el "
    "equipo del proyecto.)"
)

SHARE_REFERRAL_LINK_REPLY = (
    "Para compartir tu enlace de referido: publícalo en tus redes sociales "
    "para que tenga visibilidad y otras personas se unan a través de tu "
    "enlace. (Esto aún no está publicado en la web oficial de Donify — es "
    "info confirmada directamente por el equipo del proyecto.)"
)

# ---------------------------------------------------------
# Trigger words/phrases -> which reply they should fire.
# Add as many variations as you want on the left; the bot checks
# them top to bottom and uses the first match per message.
# ---------------------------------------------------------
REPLIES = {}

# --- Specific / longer phrases first, so they're matched before the ---
# --- generic single-word triggers below (e.g. "referral link" before "referral") ---

# How referral rewards actually work (mechanic) - must come before
# "getting started" triggers since it can contain "como funciona..."
for trigger in [
    "como funcionan los rewards", "cómo funcionan los rewards",
    "como obtienen recompensas", "cómo obtienen recompensas",
    "como funciona el reward", "cómo funciona el reward",
    "como se ganan los rewards", "cómo se ganan los rewards",
    "how do rewards work", "how does the reward work",
    "how do they get reward",
]:
    REPLIES[trigger] = REFERRAL_REWARD_MECHANIC_REPLY

# How to share a referral link
for trigger in [
    "compartir enlace", "compartir mi enlace", "enlace de referido",
    "link de referido", "compartir referido", "share referral link",
    "share my referral", "referral link",
]:
    REPLIES[trigger] = SHARE_REFERRAL_LINK_REPLY

# "Has it already started" / "did anyone actually receive one"
for trigger in [
    "ya empezo", "ya empezó", "ya comenzo", "ya comenzó", "has started",
    "already started", "me aparecio", "me apareció", "recibio", "recibió",
    "recibi algo", "recibí algo", "notificacion", "notificación",
]:
    REPLIES[trigger] = ALREADY_STARTED_REPLY

# "How many referrals needed" / "do old referrals count" / conditions
for trigger in [
    "cuantos referidos", "cuántos referidos", "cuenta los anteriores",
    "referidos anteriores", "condiciones", "how many referrals",
    "count old referrals", "status active", "referral status",
]:
    REPLIES[trigger] = CONDITIONS_REPLY

# "Can anyone create/publish a project"
for trigger in [
    "publicar proyecto", "publicar un proyecto", "crear proyecto",
    "crear un proyecto", "quien puede publicar", "quién puede publicar",
    "cualquiera podra publicar", "cualquiera podrá publicar",
    "create a project", "publish a project",
]:
    REPLIES[trigger] = PUBLISH_PROJECT_REPLY

# Who reviews/approves projects
for trigger in [
    "quien revisa", "quién revisa", "quien aprueba", "quién aprueba",
    "revisa el proyecto", "who reviews", "who approves",
]:
    REPLIES[trigger] = WHO_REVIEWS_REPLY

# "What is Donify" / general project questions
for trigger in [
    "que es donify", "qué es donify", "que es esto", "de que trata",
    "de qué trata", "what is donify", "sobre el proyecto", "sobre donify",
]:
    REPLIES[trigger] = WHAT_IS_DONIFY_REPLY

# Getting started / how to use it
for trigger in [
    "como empiezo", "cómo empiezo", "como funciona", "cómo funciona",
    "como uso", "cómo uso", "how to start", "how does it work",
]:
    REPLIES[trigger] = GETTING_STARTED_REPLY

# Donation process
for trigger in [
    "donacion", "donación", "donation", "como dono", "cómo dono",
    "como donar", "cómo donar", "how to donate",
]:
    REPLIES[trigger] = DONATION_REPLY

# --- Generic single-word / broad triggers last, as fallback within their topic ---

# Anything referral/reward related
for trigger in [
    "referral", "referrals", "referido", "referidos", "invitar", "invite",
    "reward", "rewards", "recompensa", "recompensas",
]:
    REPLIES[trigger] = REFERRAL_REPLY

# Points system
for trigger in ["points", "puntos"]:
    REPLIES[trigger] = POINTS_REPLY

# What is a project / general project question
for trigger in ["proyecto", "project"]:
    REPLIES[trigger] = PROJECT_REPLY

# Add more topics below the same way, or add one-off entries directly:
# REPLIES["your trigger word"] = "your ready response here"

# ---------------------------------------------------------
# Optional fallback reply.
# Sent ONLY when the message doesn't match any specific trigger above,
# AND the message contains one of DEFAULT_REPLY_KEYWORDS below (so the
# bot doesn't reply to unrelated chit-chat, only Donify-related topics
# it doesn't have a specific answer for yet).
# Leave DEFAULT_REPLY as None to stay silent on unmatched messages instead.
# ---------------------------------------------------------
DEFAULT_REPLY = (
    "¡Hola! Todavía no tengo una respuesta específica para eso, pero puedo "
    "ayudarte con preguntas sobre donaciones, proyectos, Points o "
    "referidos en Donify — intenta reformular tu pregunta con esas "
    "palabras. Si necesitas algo más específico, un admin del grupo puede "
    "ayudarte."
)

# Any message containing one of these words/phrases is considered
# "about Donify" and will get DEFAULT_REPLY if no specific trigger matched.
DEFAULT_REPLY_KEYWORDS = [
    "donify",
]
