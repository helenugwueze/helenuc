def display_posts(titles, bodies):
    if len(titles) == 0:
        print("No posts yet.")
        return

    for index in range(len(titles)):
        print(f"\n{index + 1}. {titles[index]}")
        print(bodies[index])


def add_post(titles, bodies):
    title = input("Post title: ")
    body = input("Post content: ")
    titles.append(title)
    bodies.append(body)
    print("Post added.")


titles = []
bodies = []

while True:
    print("\n1. View posts")
    print("2. Add a post")
    print("3. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        display_posts(titles, bodies)
    elif choice == "2":
        add_post(titles, bodies)
    elif choice == "3":
        break
    else:
        print("Invalid choice.")
