from caculate import *


# generate a number alpha which have order = q (mod p).
# chọn alpha bằng cách lấy x^( (p-1)/q) với x là 1 căn nguyên thủy của p
def number_generator(p, q):
    while True:
        k = (p - 1) // q
        x = primitive_root(p)
        alpha = pow(x, k, p)
        return alpha


def TA_generator():
    p = prime_generator(pow(2, 30), pow(2, 35))
    q = divisor_number(p)
    params = {
        "p": p,
        "q": q,
        "alpha1": number_generator(p, q),
        "alpha2": number_generator(p, q),
        "t": random.randrange(1, 20)
    }
    return params


def key_generator(params: dict):
    private_key = {
        "a1": random.randrange(0, params["q"] - 1),
        "a2": random.randrange(0, params["q"] - 1)
    }
    public_key = {
        "alpha1": params["alpha1"],
        "alpha2": params["alpha2"],
    }
    output = {
        "sk": private_key,
        "pk": public_key
    }
    return output


def identification(params: dict, keys: dict):
    alpha1: int = keys["pk"]["alpha1"]
    alpha2: int = keys["pk"]["alpha2"]
    a1: int = keys["sk"]["a1"]
    a2: int = keys["sk"]["a2"]
    p: int = params["p"]
    q: int = params["q"]
    t: int = params["t"]
    # A sends v to TA
    v = (pow(alpha1, -a1, p) * pow(alpha2, -a2, p)) % p
    # A chooses  random k1 and k2  and compute gamma then sends gamma to B
    k1 = random.randrange(1, params["q"])
    k2 = random.randrange(1, params["q"])
    gamma = (pow(alpha1, k1, p) * pow(alpha2, k2, p)) % p
    # B choose a random r
    r = random.randrange(0, 2 ** t - 1)

    y1 = k1 + r * a1 % q
    y2 = k2 + r * a2 % q
    gamma1 = pow(alpha1, y1, p) * pow(alpha2, y2, p) * pow(v, r) % p

    if gamma1 == gamma:
        print(f"p: {p} \nq: {q} \nalpha1: {alpha1} \nalpha2: {alpha2} \na1: {a1} \n"
              f"a2: {a2} \nt: {t} \nv: {v} \nk1: {k1} \nk2: {k2} \n"
              f"gamma: {gamma} \nr: {r} \ny1: {y1} \ny2: {y2} \ngamma: {gamma1}")
        print("Accepted")
    else:
        print("Rejected")


if __name__ == "__main__":
    parameters = TA_generator()
    keys = key_generator(parameters)
    identification(parameters, keys)
