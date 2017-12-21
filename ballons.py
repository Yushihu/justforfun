import random;

n = 4;
ballons = list();
for i in range(n + 2):
    ballons.append(random.randint(1, 10))
ballons[0] = 1;
ballons[-1] = 1;
print ballons[1:n + 1];

dp = list();
for i in range(n + 2):
    dp.append(list());
    for j in range(n + 2):
        dp[i].append(None);

dp[0][0] = 1;
dp[n + 1][n + 1] = 1;

def get_score(x):
    if x == len(ballons) or x < 1:
        return None;
    return ballons[x - 1] * ballons[x] * ballons[x + 1];

def get_biggest_score(left, right):
    if left > right :
        return 0;
    if dp[left][right] != None:
        return dp[left][right];

    if left == right:
        dp[left][right] = get_score(left);
        return dp[left][right];

    maxn = 1;
    for k in range(left, right + 1):
        left_value = get_biggest_score(left, k - 1);
        right_value = get_biggest_score(k + 1, right);
        this_value = ballons[left - 1] * ballons[k] * ballons[right + 1];
        sumn = left_value + this_value + right_value;
        maxn =max(maxn, sumn);
    dp[left][right] = maxn;
    return maxn;

print get_biggest_score(1, n);
