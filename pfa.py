import secrets
import hashlib


def gen_seed():
    seed = secrets.token_hex(16)
    return seed


def generate_num(p_seed, s_seed, min, max):
    seed = str(p_seed) + str(s_seed)
    res_hash = hashlib.sha256(seed.encode()).hexdigest()
    number = int(res_hash, 16)
    rnd_num = number % (max - min) + min
    return rnd_num


def generate_weighted_random_number(p_seed, s_seed, min, max):
    number_range = [*range(min, max + 1)]
    weights = [1 / (x**2) for x in number_range]  # Example weights: 100, 99, 98, ..., 1
    cumulative_weights = [sum(weights[:i+1]) for i in range(len(weights))]

    random_value = generate_num(p_seed, s_seed, 0, cumulative_weights[-1])
    selected_number = None

    for i, cumulative_weight in enumerate(cumulative_weights):
        if random_value <= cumulative_weight:
            selected_number = number_range[i]
            break

    return selected_number


if __name__ == '__main__':
    player_seed = gen_seed()
    server_seed = gen_seed()
    rand = generate_weighted_random_number(player_seed, server_seed, 1, 50)
    print(rand)