class BattleField:
    def fight(self, attacker, enemy):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")

        if attacker.__class__.__name__ == "Beginner":
            attacker.health += 40
            for card in attacker.card_repository.cards:
                card.damage_points += 30

        if enemy.__class__.__name__ == "Beginner":
            enemy.health += 40
            for card in enemy.card_repository.cards:
                card.damage_points += 30

        attacker.health += sum([c.health_points for c in attacker.card_repository.cards])
        enemy.health += sum([c.health_points for c in enemy.card_repository.cards])

        for card in attacker.card_repository.cards:
            if enemy.is_dead or attacker.is_dead:
                return
            enemy.take_damage(card.damage_points)
            #attacker.card_repository.remove(card.name)

        for card in enemy.card_repository.cards:
            if enemy.is_dead or attacker.is_dead:
                return
            attacker.take_damage(card.damage_points)
            #enemy.card_repository.remove(card.name)