def expected_goals(r_h, r_a):

    base = 1.3

    strength = r_h / r_a

    return base * strength, base / strength
