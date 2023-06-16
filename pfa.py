import secrets
import hashlib


def gen_seed():
    seed = secrets.token_hex(16)
    return seed


def generate_num(p_seed, s_seed, min, max):
    seed = str(p_seed) + str(s_seed)
    res_hash = hashlib.sha256(seed.encode()).hexdigest()
    number = int(res_hash, 16)
    rnd_num = number % (max - min + 1) + min
    return rnd_num


if __name__ == '__main__':
    player_seed = gen_seed()
    server_seed = gen_seed()
    rand = generate_num(player_seed, server_seed, 1, 50)
    print(rand)