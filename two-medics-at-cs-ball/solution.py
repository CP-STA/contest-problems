from fractions import Fraction

def find_eq(p1, p2):
    x, y = p1
    s, t = p2
    a = y - t
    b = s - x
    c = s * y - x * t
    # equation of the line is ax + by = c
    return (a, b, c)

def is_parallel(eq1, eq2):
    a, b, c = eq1
    s, t, u = eq2
    return a * t == s * b

def inverse_matrix(matrix):
    # matrix is     a b
    #               c d
    a, b, c, d = matrix
    det = a * d - b * c
    return (d / det, -b / det, -c / det, a / det)

def multiply_matrix(matrix, vector):
    a, b, c, d = matrix
    x, y = vector
    return (a * x + b * y, c * x + d * y)

def find_intersect(e, f, g, h):
    # find the intersection of the lines formed by point e, f and line fromed by g, h
    a, b, c = find_eq(e, f)
    s, t, u = find_eq(g, h)
    if is_parallel((a, b, c), (s, t, u)):
        raise ValueError('Lines are parallel')
    matrix = inverse_matrix((a, b, s, t))
    return multiply_matrix(matrix, (c, u))

def is_point_on_line_segment(p, e, f):
    x, y = p
    a, b, c = find_eq(e, f)
    return min(e[0], f[0]) <= x <= max(e[0], f[0]) \
        and min(e[1], f[1]) <= y <= max(e[1], f[1]) \
        and a * x + b * y == c

def seg_intersect(e, f, g, h):
    # check if the line segments intersect
    if is_parallel(find_eq(e, f), find_eq(g, h)):
        # We know that the lines are parallel, so we can check if the line segments overlap
        return is_point_on_line_segment(e, g, h) or is_point_on_line_segment(f, g, h) or is_point_on_line_segment(g, e, f) or is_point_on_line_segment(h, e, f)
    p = find_intersect(e, f, g, h)
    return is_point_on_line_segment(p, e, f) and is_point_on_line_segment(p, g, h)

def main():
    N = int(input())
    a, b, c, d = map(int, input().split())
    # use fraction to avoid floating point errors
    X = (Fraction(a), Fraction(b))
    Y = (Fraction(c), Fraction(d))
    points = []
    for _ in range(N):
        a, b = map(int, input().split())
        points.append((Fraction(a), Fraction(b)))
    count = 0
    for i, E in enumerate(points):
        for j, F in enumerate(points):
            if E != F and seg_intersect(X, Y, E, F):
                count += 1
    print(count // 2)

if __name__ == '__main__':
    main()