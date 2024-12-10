from django import template

register = template.Library()

@register.filter
def currency(value):
    try:
        value = int(value)  # Convertir a entero para eliminar los decimales
    except (ValueError, TypeError):
        return value
    # Formatear con separador de miles usando punto
    return f"${value:,}".replace(",", ".")
