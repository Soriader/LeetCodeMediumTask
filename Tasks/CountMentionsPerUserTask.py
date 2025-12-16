def countMentions(self, number_of_users: int, events: list[list[str]]) -> list[int]:
    count_users = {i: 0 for i in range(number_of_users)}
    offline_users: dict[int, int] = {}
    events.sort(key=lambda e: (int(e[1]), 0 if e[0] == "OFFLINE" else 1))

    for message in events:
        info = message[0]
        actual_time = int(message[1])
        users = message[2]

        offline_users = expireOffline(actual_time, offline_users)

        if info == "OFFLINE":
            offlineUsers(actual_time, users, offline_users)

        elif info == "MESSAGE":
            count_users = messageToUser(users, offline_users, count_users, number_of_users)

    result = [count_users[i] for i in range(number_of_users)]
    return result


def messageToUser(payload: str,
                  offline_users: dict[int, int],
                  count_users: dict[int, int],
                  number_of_users: int) -> dict[int, int]:

    if payload == "ALL":
        for key in count_users:
            count_users[key] += 1
        return count_users

    if payload == "HERE":
        for user in range(number_of_users):
            if user not in offline_users:
                count_users[user] += 1
        return count_users

    for token in payload.split():
        if token.startswith("id"):
            user = int(token.removeprefix("id"))
            count_users[user] += 1

    return count_users


def offlineUsers(actual_time: int, user_id_str: str, offline_users: dict[int, int]) -> None:
    user_id = int(user_id_str)
    offline_users[user_id] = actual_time + 60

def expireOffline(actual_time: int, offline_users: dict[int, int]) -> dict[int, int]:
    to_remove = [u for u, until in offline_users.items() if until <= actual_time]
    for u in to_remove:
        del offline_users[u]

    return offline_users

#https://leetcode.com/problems/count-mentions-per-user/description/?envType=daily-question&envId=2025-12-12