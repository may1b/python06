print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")

from alchemy.grimoire.dark_spellbook import dark_spell_record  # noqa: E402

print(
    "Testing record dark spell: "
    f"{dark_spell_record('Forbidden', 'Bats, frogs and arsenic')}"
)
