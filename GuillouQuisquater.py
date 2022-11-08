from caculate import *


# chon tham so cho trung tam uy thac
def TA_generator():
    # p and q is secret and n is public
    p = prime_generator(pow(2, 50), pow(2, 51))
    q = prime_generator(pow(2, 50), pow(2, 51))
    n = p * q
    b = prime_generator(pow(2, 40), pow(2, 41))

    params = {
        "n": n,
        "p": p,
        "q": q,
        "b": b
    }
    return params


# tao khoa cua A
def key_generator(params: dict):
    # A chon bi mat u va tinh v roi gui v cho TA
    private_key = {
        "u": random.randrange(0, params["n"] - 1),
    }
    public_key = {
        "b": params["b"],
        "v": pow(private_key["u"], -params["b"], params["n"])  # v = u^(-b) mod n
    }
    out_put = {
        "sk": private_key,
        "pk": public_key
    }
    return out_put


def identification(params: dict, keys: dict):
    p: int = params["p"]
    q: int = params["q"]
    u: int = keys["sk"]["u"]
    v: int = keys["pk"]["v"]
    n: int = params["n"]
    b: int = params["b"]

    # A chooses a random number k and compute gamma = k^b mod n then sends to B C(A) and gamma.
    k = random.randrange(0, n - 1)
    gamma = pow(k, b, n)
    # B kiem thu chu ki cua TA trong C(A) bang thuat toan verTA.
    # B chon so ngau nhien r va gui r cho A
    r = random.randrange(1, b - 1)
    # A tinh y = kr + a (mod n) va gui y cho B
    y = k * pow(u, r) % n
    # B kiem tra  gamma = v^r * y^ b (mod n)
    gamma1 = pow(v, r, n) * pow(y, b, n) % n
    if gamma1 == gamma:
        print("p: ", p)
        print("q: ", q)
        print("n: ", n)
        print("b: ", b)
        print("u: ", u)
        print("v: ", v)
        print("k: ", k)
        print("gamma: ", gamma)
        print("r: ", r)
        print("y: ", y)
        print("gamma1: ", gamma1)
        print("Accepted")
    else:
        print("Reject")


if __name__ == "__main__":
    parameters = TA_generator()
    keys = key_generator(parameters)
    identification(parameters, keys)
