# Dynamic Array

def dynamicArray(N, queries):
    # Write your code here
    lastans = 0
    result = []
    Seqs = [ [] for _ in range( N ) ]
    for i in queries:
        if i[0] == 1:
            Seqs[ ( i[1] ^ lastans ) % N ].append( i[2] )
        elif i[0] == 2:
            arr = Seqs[ ( i[1] ^ lastans ) % N ]
            val = arr[ i[2] % len(arr) ]
            result.append(val)
            lastans = val
    return result
