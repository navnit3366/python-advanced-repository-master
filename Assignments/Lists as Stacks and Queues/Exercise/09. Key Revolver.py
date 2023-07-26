from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = deque([int(x) for x in input().split()])
locks = deque([int(x) for x in input().split()])
intelligence_value = int(input())
total_bullets_shot = 0
bullets_shot = 0

while True:
    current_bullet = bullets.pop()
    current_lock = locks[0]

    if current_bullet <= current_lock:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")

    bullets_shot += 1
    total_bullets_shot += 1

    if bullets_shot == gun_barrel_size and bullets:
        print("Reloading!")
        bullets_shot = 0

    if not locks:
        money_earned = intelligence_value - (total_bullets_shot * bullet_price)
        print(f"{len(bullets)} bullets left. Earned ${money_earned}")
        break

    elif not bullets:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        break
