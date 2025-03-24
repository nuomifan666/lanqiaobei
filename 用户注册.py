def register_users(n, usernames):
    database = {}
    result = []

    for name in usernames:
        if name not in database:
            database[name] = 0
            result.append("OK")
        else:
            database[name] += 1
            new_name = f"{name}{database[name]}"
            result.append(new_name)

    # 输出结果
    print("\n".join(result))


# 输入处理
n = int(input().strip())
usernames = [input().strip() for _ in range(n)]

register_users(n, usernames)
