print(
    *list(
        map(lambda a, b: (a + b) % 2,
            list(
                map(
                    lambda x: int(x),
                    list(input().split()))),
            list(
                map(
                    lambda x: int(x),
                    list(input().split()
                    )
                )
            )
        )
    )
)
