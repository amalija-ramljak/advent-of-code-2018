from copy import deepcopy


def fight(groups, part):
    """stats - 0: weaknesses, 1: immunities"""
    original = groups
    attempt = 0
    while True:
        if part == 2:
            groups = deepcopy(original)
            attempt += 1
            for group in groups:
                if group.spec == 'imm':
                    group.damage[0] += attempt
        # print(attempt)
        while True:
            inf_count = len([g for g in groups if g.spec == 'inf' and g.count > 0])
            imm_count = len([g for g in groups if g.spec == 'imm' and g.count > 0])
            # print("  Counts: inf", inf_count, "imm", imm_count)
            if inf_count == 0 or imm_count == 0:
                break
            targets = dict()
            groups.sort()
            # selection phase
            for group in groups:
                if group.count <= 0:
                    continue
                opp = [grp for grp in groups if grp.spec != group.spec and grp.count > 0]
                if len(opp) == 0:
                    continue
                opp.sort()
                weak = []
                normal = []
                taken = set(targets.values())
                for tgt in opp:
                    if tgt in taken:
                        continue
                    if group.damage[1] in tgt.weakness:
                        weak.append(tgt)
                    elif group.damage[1] not in tgt.immunity:
                        normal.append(tgt)
                if len(weak) == 0 and len(normal) == 0:
                    continue
                if len(weak) == 0:
                    normal.sort()
                    targets[group] = normal[0]
                else:
                    weak.sort()
                    targets[group] = weak[0]

            # attacking phase
            attackers = list(targets.keys())
            if len(attackers) == 0:
                break
            attackers.sort(key=lambda g: g.initiative, reverse=True)  # new sort!
            for attacker in attackers:
                if attacker.count <= 0:
                    continue
                effective = attacker.damage[0] * attacker.count
                if attacker.damage[1] in targets[attacker].weakness:
                    effective *= 2
                target_loss = effective // targets[attacker].health  # how many units it loses
                targets[attacker].count -= target_loss

        specs = set([g.spec for g in groups if g.count > 0])
        if len(specs) > 1:
            continue
        winners = [g for g in groups if g.count > 0]
        units = [g.count for g in winners]
        winner = winners[0].spec
        if part == 1:
            break
        if winner == 'imm' and part == 2:
            break
    print("Part", part, winner, sum(units))
    if part == 2:
        print("For fun, the increment is", attempt)
