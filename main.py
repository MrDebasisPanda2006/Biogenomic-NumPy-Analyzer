import numpy as np
import time as t

def Genomic_analysis():
    print("---Initializing genomic analysis---")
    start = t.time()

    # DNA GENERATION
    DNA = np.random.choice(['A','T','G','C'] , size=3*10**8)

    # GC CONTENT
    GC_mask = ((DNA== 'G') | (DNA == 'C'))
    GC_content = ((np.count_nonzero(GC_mask))/len(DNA))*100
    
    #CODON ANALYSIS
    codons = DNA.reshape(-1,3)
    #START CODON(ATG)
    start_mask = np.all(codons == ['A', 'T', 'G'], axis=1)
    ATG = np.count_nonzero(start_mask)
    #END CODON(TAA,TAG,TGA)
    end_mask = np.all((codons == ['T','A','A']) | 
                     (codons == ['T','G','A']) | 
                     (codons == ['T','A','G']) , axis =1)
    END = np.count_nonzero(end_mask)

    #TOTAL TIME TAKEN DURING THE PROCESS
    Duration = t.time()-start

    #THE OUTPUT
    print(f"The percentage of GC content in DNA is : {GC_content:.2f}")
    print(f"The number of start codons in DNA is : {ATG:,}")
    print(f"The number of end codons is {END:,}")
    print(f"tThe total time during this process : {Duration:.4f} seconds")

if __name__ == "__main__" :
    Genomic_analysis()