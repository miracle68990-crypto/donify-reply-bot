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
    "Las condiciones de un posible programa de rewards por referidos "
    "(cuántos referidos hacen falta, si cuentan los anteriores, etc.) no "
    "están documentadas oficialmente todavía. No te bases en rumores del "
    "grupo — espera el anuncio oficial de Donify para los detalles exactos."
)

# ---------------------------------------------------------
# Trigger words/phrases -> which reply they should fire.
# Add as many variations as you want on the left; the bot checks
# them top to bottom and uses the first match per message.
# ---------------------------------------------------------
REPLIES = {}

# Anything referral/reward related
for trigger in [
    "referral", "referrals", "referido", "referidos", "invitar", "invite",
    "reward", "rewards", "recompensa", "recompensas",
]:
    REPLIES[trigger] = REFERRAL_REPLY

# "What is Donify" / general project questions
for trigger in [
    "que es donify", "qué es donify", "que es esto", "de que trata",
    "de qué trata", "what is donify", "sobre el proyecto", "sobre donify",
]:
    REPLIES[trigger] = WHAT_IS_DONIFY_REPLY

# Points system
for trigger in ["points", "puntos"]:
    REPLIES[trigger] = POINTS_REPLY

# Getting started / how to use it
for trigger in [
    "como empiezo", "cómo empiezo", "como funciona", "cómo funciona",
    "como uso", "cómo uso", "how to start", "how does it work",
]:
    REPLIES[trigger] = GETTING_STARTED_REPLY

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

# Add more topics below the same way, or add one-off entries directly:
# REPLIES["your trigger word"] = "your ready response here"

# ---------------------------------------------------------
# Optional fallback reply.
# Sent ONLY when the message doesn't match any trigger above,
# but seems to be about Donify (contains "donify" or the project name).
# Leave DEFAULT_REPLY as None to stay silent on unmatched messages instead.
# ---------------------------------------------------------
DEFAULT_REPLY = None
