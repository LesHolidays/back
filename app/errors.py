# Exceptions métier personnalisées
# 
# Pourquoi des exceptions custom ?
# Flask, par défaut, renvoie du HTML quand une exception non attrapée remonte.
# En créant nos propres classes, on peut :
# 1. Lever des erreurs explicites dans les services (ex: NotFoundError("Post introuvable"))
# 2. Les attraper automatiquement dans main.py avec des @app.errorhandler
# 3. Renvoyer du JSON propre avec le bon code HTTP, sans try/catch dans chaque route
#
# C'est le pattern "exception-based error handling" : on laisse les erreurs remonter
# naturellement dans la call stack, et on les intercepte à un seul endroit (le controller).

class NotFoundError(Exception):
    """Ressource introuvable → HTTP 404"""
    pass

class ForbiddenError(Exception):
    """Action non autorisée (pas le propriétaire) → HTTP 403"""
    pass

class ConflictError(Exception):
    """Conflit (ex: compte déjà activé) → HTTP 409"""
    pass

class BadRequestError(Exception):
    """Requête invalide (paramètres manquants/invalides) → HTTP 400"""
    pass

class UnauthorizedError(Exception):
    """Authentification échouée → HTTP 401"""
    pass
