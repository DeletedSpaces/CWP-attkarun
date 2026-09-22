#!/usr/bin/env python3
table = 0
while table <= 10:
    line = f"Table de {table}:"
    factor = 0
    while factor <= 10:
        line += f" {factor * table}"
        factor += 1
    print(line)
    table += 1
