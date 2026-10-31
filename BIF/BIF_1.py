# DNA Sequence Analysis

# 1. Input DNA
dna = input("Enter DNA sequence: ").upper()

if dna == "" or any(b not in "ATGC" for b in dna):
    print("Invalid DNA sequence")

else:
    print("DNA Sequence:", dna)
    print("Length:", len(dna))

    # 2. GC Content
    g = dna.count("G")
    c = dna.count("C")
    gc = (g + c) / len(dna) * 100

    print("GC Content:", round(gc, 2), "%")

    # 3. Find Motif
    motif = input("Enter motif: ").upper()
    count = 0

    for i in range(len(dna)):
        if dna[i:i+len(motif)] == motif:
            print("Motif found at position:", i+1)
            count = count + 1

    print("Total Motif Occurrences:", count)

    # 4. Reverse Complement
    comp = ""
    for b in dna:
        if b == "A":
            comp = "T" + comp
        elif b == "T":
            comp = "A" + comp
        elif b == "G":
            comp = "C" + comp
        else:
            comp = "G" + comp

    print("Reverse Complement:", comp)

    # 5. Find Coding Region
    start = dna.find("ATG")
    found = False

    if start != -1:
        for i in range(start+3, len(dna)-2, 3):
            codon = dna[i:i+3]

            if codon == "TAA" or codon == "TAG" or codon == "TGA":
                print("Coding Region:", dna[start:i+3])
                found = True
                break

    if not found:
        print("No complete coding region found")

    # 6. Summary
    print("\n--- Summary ---")
    print("Total Bases:", len(dna))
    print("GC Content:", round(gc, 2), "%")
    print("Motif Count:", count)