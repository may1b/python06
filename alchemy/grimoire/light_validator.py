def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    lower_ingredients = ingredients.lower()
    is_valid = any(
        ingredient in lower_ingredients
        for ingredient in light_spell_allowed_ingredients()
    )
    if is_valid:
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
