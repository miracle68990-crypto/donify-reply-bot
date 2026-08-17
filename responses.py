# ---------------------------------------------------------
# EDIT THIS FILE to set up your bot's canned replies.
# No need to touch bot.py at all.
# ---------------------------------------------------------

# MATCH_MODE controls how triggers are matched against incoming messages:
#   "contains" -> replies if the trigger word/phrase appears ANYWHERE in the message
#   "exact"    -> replies only if the message EXACTLY matches the trigger (ignoring case/spacing)
MATCH_MODE = "contains"

# Map of trigger -> reply.
# Add as many as you want. The bot checks these top to bottom and uses the first match.
REPLIES = {
    "referral": (
        "Por ahora no hay ningún programa de rewards por referidos confirmado "
        "oficialmente. Lo único documentado en la web oficial (donifyapp.com/faq) "
        "es el sistema de Points, que mide actividad dentro del ecosistema pero "
        "no es dinero ni criptomoneda. Si sale algo oficial sobre referidos, se "
        "anunciará en los canales oficiales de Donify."
    ),
    "reward": (
        "Por ahora no hay ningún programa de rewards por referidos confirmado "
        "oficialmente. Lo único documentado en la web oficial (donifyapp.com/faq) "
        "es el sistema de Points, que mide actividad dentro del ecosistema pero "
        "no es dinero ni criptomoneda. Si sale algo oficial sobre referidos, se "
        "anunciará en los canales oficiales de Donify."
    ),
    "que es donify": (
        "DONIFY es un ecosistema descentralizado de donaciones cripto. Permite "
        "apoyar proyectos directamente a través de blockchain, sin registro "
        "complicado ni intermediarios centralizados. Más info: https://donifyapp.com"
    ),
    "points": (
        "Los Points muestran tu actividad dentro del ecosistema Donify. No son "
        "dinero ni criptomoneda: sirven para que el sistema identifique quién "
        "participó activamente apoyando proyectos e interactuando con Donify."
    ),
    "como empiezo": (
        "Para empezar: 1) abre DONIFY en Telegram, 2) elige un proyecto, "
        "3) confirma la donación desde tu wallet, 4) revisa que la transacción "
        "quedó registrada. Bot oficial: https://t.me/donify_app_bot"
    ),
    # "your trigger word": "your ready response here",
}

# Optional: a fallback reply sent when NO trigger matches.
# Set to None (without quotes) if you don't want the bot replying to everything.
DEFAULT_REPLY = None
