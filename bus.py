import random;

col = 10;
row = 10;
array = list();
dp = list();
route = list();

def init_route():
    x = 0;
    y = 0;
    while y < row:
        route.append(list());
        x = 0;
        while x < col:
            route[y].append(0);
            x += 1;
        y += 1;
    route[0][0] = 1;
    route[row - 1][col - 1] = 1;  

def init_array():
    x = 0;
    y = 0;
    while y < row:
        array.append(list());
        x = 0;
        while x < col:
            array[y].append(random.randint(0, 100));
            x += 1;
        y += 1;

def init_dp_cache():
    x = 0;
    y = 0;
    while y < row:
        dp.append(list());
        x = 0;
        while x < col:
            dp[y].append(-1);
            x += 1;
        y += 1;
    dp[row - 1][col - 1] = array[row - 1][col - 1];


def get_biggist_score(x1, y1):
    if dp[y1][x1] != -1:
        return dp[y1][x1];
    score = array[y1][x1];
    if x1 == col - 1:
        dp[y1][x1] = get_biggist_score(x1, y1 + 1) + score;
    elif y1 == row - 1:
        dp[y1][x1] = get_biggist_score(x1 + 1, y1) + score;
    else:
        dp[y1][x1] = max(get_biggist_score(x1 + 1, y1) + score, get_biggist_score(x1, y1 + 1) + score);
    return dp[y1][x1];

def find_route():
    step = row + col - 2;
    x = 0;
    y = 0;
    while step > 0:
        if x == col - 1:
            route[y + 1][x] = 1;
            y = y + 1;
        elif y == row - 1:
            route[y][x + 1] = 1;
            x = x + 1;
        else:
            if dp[y + 1][x] > dp[y][x + 1]:
                route[y + 1][x] = 1;
                y = y + 1;
            else:
                route[y][x + 1] = 1;
                x = x + 1;
        step -= 1;

def print_route():
    x = 0;
    y = 0;
    while y < row:
        x = 0;
        while x < col:
            if route[y][x] == 0:
                print " %2d "%(array[y][x]),
            else:
                print "[%2d]"%(array[y][x]),
            x += 1;
        y += 1;
        print "";

init_array();
init_route();
init_dp_cache();
get_biggist_score(0, 0);
find_route();
print_route();
