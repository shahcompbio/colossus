"""Holds constants for the core app.

Note: don't expect to find *all* constants in here, only some of them
(this was a late addition to the app).
"""

# Enumeration for TenxLibraryConstructionInformation library_type
# choices
FIVE_PRIME = "5'"
THREE_PRIME = "3'"
VDJ = "V(D)J"
CNV = "CNV"

pathology_occurrence_choices = (
    ('PR', 'Primary'),
    ('RC', 'Recurrent or Relapse'),
    ('ME', 'Metastatic'),
    ('RM', 'Remission'),
    ('UN', 'Undetermined'),
    ('US', 'Unspecified'),
)

sex_choices = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('X', 'Mixed'),
    ('U', 'Unknown'),
)

tissue_type_choices = (
    ('N', 'Normal'),
    ('B', 'Benign'),
    ('PM', 'Pre-malignant'),
    ('M', 'Malignant'),
    ('NNP', 'Non-neoplastic Disease'),
    ('U', 'Undetermined'),
    ('HP', 'Hyperplasia'),
    ('MP', 'Metaplasia'),
    ('DP', 'Dysplasia'),
)

treatment_status_choices = (
    ('PR', 'Pre-treatment'),
    ('IN', 'In-treatment'),
    ('PO', 'Post-treatment'),
    ('NA', 'N/A'),
    ('UN', 'Unknown'),
)
TISSUE_STATES = (
    ('NONE', 'None'),
    ('FROZ', 'Frozen'),
    ('FRES', 'Fresh'),
    ('DIG-FRES', 'Digested-Fresh'),

)

CHIP_WELL = (
    (0, 'NOT SET'), (1, 'WELL_1'), (2, 'WELL_2'), (3, 'WELL_3'), (4, 'WELL_4'),
    (5, 'WELL_5'), (6, 'WELL_6'), (7, 'WELL_7'), (8, 'WELL_8')
)

TENX_LIBRARY_TYPE_CHOICES = (
    (FIVE_PRIME, FIVE_PRIME),
    (THREE_PRIME, THREE_PRIME),
    (VDJ, VDJ),
)

CHEMISTRY_VERSION_CHOICES = (
    ("VERSION_2", "v2"),
    ("VERSION_3", "v3")
)

spotting_location_choices = (
    ('AD', 'Aparicio Lab - Deckard'),
    ('AR', 'Aparicio Lab - Rachael'),
    ('H', 'Hansen Lab'),
    ('G', 'GSC'),
)

# choices
cell_state_choices = (
    ('C', 'Cells'),
    ('N', 'Nuclei'),
    ('M', 'Mixed'),
    ('U', 'Unknown'),
)

# choices
chip_format_choices = (
    ('W', 'Wafergen'),
    ('M', 'Microfluidic'),
    ('B', 'Bulk'),
    ('O', 'Other'),
)

qc_check_choices = (
    ('P', 'Will sequence'),
    ('N', 'Will not sequence'),
)

# fields
rev_comp_override_choices = (
    ('i7,i5', 'No Reverse Complement'),
    ('i7,rev(i5)', 'Reverse Complement i5'),
    ('rev(i7),i5', 'Reverse Complement i7'),
    ('rev(i7),rev(i5)', 'Reverse Complement i7 and i5'),
)

# choices
sequencing_instrument_choices = (
    ('HX', 'HiSeqX'),
    ('H2500', 'HiSeq2500'),
    ('N500', 'NextSeq500'),
    ('N550', 'NextSeq550'),
    ('MI', 'MiSeq'),
    ('O', 'other'),
)

sequencing_output_mode_choices = (
    ('L', 'Low'),
    ('M', 'Medium'),
    ('H', 'High'),
)

read_type_choices = (
    ('P', 'PET'),
    ('S', 'SET'),
)

SEQ_CENTER = (
    ('BCCAGSC', 'BCCAGSC'),
    ('UBCBRC', 'UBCBRC'),
)

# choices
plate_type_choices = (
    ('submitted', 'submitted'),
    ('sequenced', 'sequenced'),
    ('stored', 'stored'),
)

INPUT_TYPE = (
    ('DLP', "DLP"),
    ('PBAL', "PBAL"),
    ('TENX', "TenX")
)

##########
#SISYPHUS#
##########
# Choices for the run status
IDLE = 'idle'
ERROR = 'error'
RUNNING = 'running'
ARCHIVING = 'archiving'
COMPLETE = 'complete'
ALIGN_COMPLETE = 'align_complete'
HMMCOPY_COMPLETE = 'hmmcopy_complete'

RUN_STATUS_CHOICES = (
    (IDLE, 'Idle'),
    (ERROR, 'Error'),
    (RUNNING, 'Running'),
    (ARCHIVING, 'Archiving'),
    (COMPLETE, 'Complete'),
    (ALIGN_COMPLETE, 'Align Complete'),
    (HMMCOPY_COMPLETE, 'Hmmcopy Complete'),
)

# Aligner choices
aligner_choices = (
    ('A', 'bwa-aln'),
    ('M', 'bwa-mem'),
)

# Smoothing choices
smoothing_choices = (
    ('M', 'modal'),
    ('L', 'loess'),
)

# choices
priority_level_choices = (
    ('L', 'Low'),
    ('M', 'Medium'),
    ('H', 'High'),
)

verified_choices = (
    ('T', 'True'),
    ('F', 'False'),
)

MONTAGE_STATUS_CHOICES = (
    ('Success', 'Success'),
    ('Error', 'Error'),
    ('Ignore', 'Ignore'),
    ('Pending', 'Pending')
)


# Enumeration for TenxLibraryConstructionInformation library_type
# choices

SI_GA_A1 = "SI_GA-A1,GGTTTACT,CTAAACGG,TCGGCGTC,AACCGTAA"
SI_GA_A2 = "SI-GA-A2,TTTCATGA,ACGTCCCT,CGCATGTG,GAAGGAAC"
SI_GA_A3 = "SI-GA-A3,CAGTACTG,AGTAGTCT,GCAGTAGA,TTCCCGAC"
SI_GA_A4 = "SI-GA-A4,TATGATTC,CCCACAGT,ATGCTGAA,GGATGCCG"
SI_GA_A5 = "SI-GA-A5,CTAGGTGA,TCGTTCAG,AGCCAATT,GATACGCC"
SI_GA_A6 = "SI-GA-A6,CGCTATGT,GCTGTCCA,TTGAGATC,AAACCGAG"
SI_GA_A7 = "SI-GA-A7,ACAGAGGT,TATAGTTG,CGGTCCCA,GTCCTAAC"
SI_GA_A8 = "SI-GA-A8,GCATCTCC,TGTAAGGT,CTGCGATG,AACGTCAA"
SI_GA_A9 = "SI-GA-A9,TCTTAAAG,CGAGGCTC,GTCCTTCT,AAGACGGA"
SI_GA_A10 = "SI-GA-A10,GAAACCCT,TTTCTGTC,CCGTGTGA,AGCGAAAG"
SI_GA_A11 = "SI-GA-A11,GTCCGGTC,AAGATCAT,CCTGAAGG,TGATCTCA"
SI_GA_A12 = "SI-GA-A12,AGTGGAAC,GTCTCCTT,TCACATCA,CAGATGGG"
SI_GA_B1 = "SI-GA-B1,GTAATCTT,TCCGGAAG,AGTTCGGC,CAGCATCA"
SI_GA_B2 = "SI-GA-B2,TACTCTTC,CCTGTGCG,GGACACGT,ATGAGAAA"
SI_GA_B3 = "SI-GA-B3,GTGTATTA,TGTGCGGG,ACCATAAC,CAACGCCT"
SI_GA_B4 = "SI-GA-B4,ACTTCATA,GAGATGAC,TGCCGTGG,CTAGACCT"
SI_GA_B5 = "SI-GA-B5,AATAATGG,CCAGGGCA,TGCCTCAT,GTGTCATC"
SI_GA_B6 = "SI-GA-B6,CGTTAATC,GCCACGCT,TTACTCAG,AAGGGTGA"
SI_GA_B7 = "SI-GA-B7,AAACCTCA,GCCTTGGT,CTGGACTC,TGTAGAAG"
SI_GA_B8 = "SI-GA-B8,AAAGTGCT,GCTACCTG,TGCTGTAA,CTGCAAGC"
SI_GA_B9 = "SI-GA-B9,CTGTAACT,TCTAGCGA,AGAGTGTG,GACCCTAC"
SI_GA_B10 = "SI-GA-B10,ACCGTATG,GATTAGAT,CTGACTGA,TGACGCCC"
SI_GA_B11 = "SI-GA-B11,GTTCCTCA,AGGTACGC,TAAGTATG,CCCAGGAT"
SI_GA_B12 = "SI-GA-B12,TACCACCA,CTAAGTTT,GGGTCAAG,ACTGTGGC"
SI_GA_C1 = "SI-GA-C1,CCACTTAT,AACTGGCG,TTGGCATA,GGTAACGC"
SI_GA_C2 = "SI-GA-C2,CCTAGACC,ATCTCTGT,TAGCTCTA,GGAGAGAG"
SI_GA_C3 = "SI-GA-C3,TCAGCCGT,CAGAGGCC,GGTCAATA,ATCTTTAG"
SI_GA_C4 = "SI-GA-C4,ACAATTCA,TGCGCAGC,CATCACTT,GTGTGGAG"
SI_GA_C5 = "SI-GA-C5,CGACTTGA,TACAGACT,ATTGCGTG,GCGTACAC"
SI_GA_C6 = "SI-GA-C6,ATTACTTC,TGCGAACT,GCATTCGG,CAGCGGAA"
SI_GA_C7 = "SI-GA-C7,GTCTCTCG,AATCTCTC,CGGAGGGA,TCAGAAAT"
SI_GA_C8 = "SI-GA-C8,GTTGAGAA,AGATCTGG,TCGATACT,CACCGCTC"
SI_GA_C9 = "SI-GA-C9,GCGCAGAA,ATCTTACC,TATGGTGT,CGAACCTG"
SI_GA_C10 = "SI-GA-C10,TCTCAGTG,GAGACTAT,CGCTTAGC,ATAGGCCA"
SI_GA_C11 = "SI-GA-C11,GAGGATCT,AGACCATA,TCCTGCGC,CTTATGAG"
SI_GA_C12 = "SI-GA-C12,TCTCGTTT,GGCTAGCG,ATGACCGC,CAAGTAAA"
SI_GA_D1 = "SI-GA-D1,CACTCGGA,GCTGAATT,TGAAGTAC,ATGCTCCG"
SI_GA_D2 = "SI-GA-D2,TAACAAGG,GGTTCCTC,ATCATGCA,CCGGGTAT"
SI_GA_D3 = "SI-GA-D3,ACATTACT,TTTGGGTA,CAGCCCAC,GGCAATGG"
SI_GA_D4 = "SI-GA-D4,CCCTAACA,ATTCCGAT,TGGATTGC,GAAGGCTG"
SI_GA_D5 = "SI-GA-D5,CTCGTCAC,GATCAGCA,ACAACAGG,TGGTGTTT"
SI_GA_D6 = "SI-GA-D6,CATGCGAT,TGATATTC,GTGATCGA,ACCCGACG"
SI_GA_D7 = "SI-GA-D7,ATTTGCTA,TAGACACC,CCACAGGG,GGCGTTAT"
SI_GA_D8 = "SI-GA-D8,GCAACAAA,TAGTTGTC,CGCCATCG,ATTGGCGT"
SI_GA_D9 = "SI-GA-D9,AGGAGATG,GATGTGGT,CTACATCC,TCCTCCAA"
SI_GA_D10 = "SI-GA-D10,CAATACCC,TGTCTATG,ACCACGAA,GTGGGTGT"
SI_GA_D11 = "SI-GA-D11,CTTTGCGG,TGCACAAA,AAGCAGTC,GCAGTTCT"
SI_GA_D12 = "SI-GA-D12,GCACAATG,CTTGGTAC,TGCACCGT,AAGTTGCA"
SI_GA_E1 = "SI-GA-E1,TGGTAAAC,GAAAGGGT,ACTGCTCG,CTCCTCTA"
SI_GA_E2 = "SI-GA-E2,GTGGTACC,TACTATAG,ACAAGGTA,CGTCCCGT"
SI_GA_E3 = "SI-GA-E3,AGGTATTG,CTCCTAGT,TCAAGGCC,GATGCCAA"
SI_GA_E4 = "SI-GA-E4,TTCGCCCT,GGATGGGC,AATCAATG,CCGATTAA"
SI_GA_E5 = "SI-GA-E5,CATTAGCG,TTCGCTGA,ACAAGAAT,GGGCTCTC"
SI_GA_E6 = "SI-GA-E6,CTGCGGCT,GACTCAAA,AGAAACTC,TCTGTTGG"
SI_GA_E7 = "SI-GA-E7,CACGCCTT,GTATATAG,TCTCGGGC,AGGATACA"
SI_GA_E8 = "SI-GA-E8,ATAGTTAC,TGCTGAGT,CCTACGTA,GAGCACCG"
SI_GA_E9 = "SI-GA-E9,TTGTTTCC,GGAGGAGG,CCTAACAA,AACCCGTT"
SI_GA_E10 = "SI-GA-E10,AAATGTGC,GGGCAAAT,TCTATCCG,CTCGCGTA"
SI_GA_E11 = "SI-GA-E11,AAGCGCTG,CGTTTGAT,GTAGCACA,TCCAATGC"
SI_GA_E12 = "SI-GA-E12,ACCGGCTC,GAGTTAGT,CGTCCTAG,TTAAAGCA"
SI_GA_F1 = "SI-GA-F1,GTTGCAGC,TGGAATTA,CAATGGAG,ACCCTCCT"
SI_GA_F2 = "SI-GA-F2,TTTACATG,CGCGATAC,ACGCGGGT,GAATTCCA"
SI_GA_F3 = "SI-GA-F3,TTCAGGTG,ACGGACAT,GATCTTGA,CGATCACC"
SI_GA_F4 = "SI-GA-F4,CCCAATAG,GTGTCGCT,AGAGTCGC,TATCGATA"
SI_GA_F5 = "SI-GA-F5,GACTACGT,CTAGCGAG,TCTATATC,AGGCGTCA"
SI_GA_F6 = "SI-GA-F6,CGGAGCAC,GACCTATT,ACTTAGGA,TTAGCTCG"
SI_GA_F7 = "SI-GA-F7,CGTGCAGA,AACAAGAT,TCGCTTCG,GTATGCTC"
SI_GA_F8 = "SI-GA-F8,CATGAACA,TCACTCGC,AGCTGGAT,GTGACTTG"
SI_GA_F9 = "SI-GA-F9,CAAGCTCC,GTTCACTG,TCGTGAAA,AGCATGGT"
SI_GA_F10 = "SI-GA-F10,GCTTGGCT,AAACAAAC,CGGGCTTA,TTCATCGG"
SI_GA_F11 = "SI-GA-F11,GCGAGAGT,TACGTTCA,AGTCCCAC,CTATAGTG"
SI_GA_F12 = "SI-GA-F12,TGATGCAT,GCTACTGA,CACCTGCC,ATGGAATG"
SI_GA_G1 = "SI-GA-G1,ATGAATCT,GATCTCAG,CCAGGAGC,TGCTCGTA"
SI_GA_G2 = "SI-GA-G2,TGATTCTA,ACTAGGAG,CAGCCACT,GTCGATGC"
SI_GA_G3 = "SI-GA-G3,CCTCATTC,AGCATCCG,GTGGCAAT,TAATGGGA"
SI_GA_G4 = "SI-GA-G4,GCGATGTG,AGATACAA,TTTCCACT,CACGGTGC"
SI_GA_G5 = "SI-GA-G5,GAGCAAGA,TCTGTGAT,CGCAGTTC,ATATCCCG"
SI_GA_G6 = "SI-GA-G6,CTGACGCG,GGTCGTAC,TCCTTCTT,AAAGAAGA"
SI_GA_G7 = "SI-GA-G7,GGTATGCA,CTCGAAAT,ACACCTTC,TAGTGCGG"
SI_GA_G8 = "SI-GA-G8,TATGAGCT,CCGATAGC,ATACCCAA,GGCTGTTG"
SI_GA_G9 = "SI-GA-G9,TAGGACGT,ATCCCACA,GGAATGTC,CCTTGTAG"
SI_GA_G10 = "SI-GA-G10,TCGCCAGC,AATGTTAG,CGATAGCT,GTCAGCTA"
SI_GA_G11 = "SI-GA-G11,TTATCGTT,AGCAGAGC,CATCTCCA,GCGGATAG"
SI_GA_G12 = "SI-GA-G12,ATTCTAAG,CCCGATTA,TGGAGGCT,GAATCCGC"
SI_GA_H1 = "SI-GA-H1,GTATGTCA,TGTCAGAC,CACGTCGG,ACGACATT"
SI_GA_H2 = "SI-GA-H2,TAATGACC,ATGCCTTA,GCCGAGAT,CGTATCGG"
SI_GA_H3 = "SI-GA-H3,CCAAGATG,AGGCCCGA,TACGTGAC,GTTTATCT"
SI_GA_H4 = "SI-GA-H4,GCCATTCC,CAAGAATT,TTGCCGGA,AGTTGCAG"
SI_GA_H5 = "SI-GA-H5,CCACTACA,GATTCTGG,TGCGGCTT,ATGAAGAC"
SI_GA_H6 = "SI-GA-H6,TAGGATAA,CCTTTGTC,GTACGCGG,AGCACACT"
SI_GA_H7 = "SI-GA-H7,AGCTATCA,CATATAAC,TCAGGGTG,GTGCCCGT"
SI_GA_H8 = "SI-GA-H8,TTGTTGAT,GCTCAACC,CAAAGTGG,AGCGCCTA"
SI_GA_H9 = "SI-GA-H9,ACACTGTT,CAGGATGG,GGCTGAAC,TTTACCCA"
SI_GA_H10 = "SI-GA-H10,GTAATTGC,AGTCGCTT,CACGAGAA,TCGTCACG"
SI_GA_H11 = "SI-GA-H11,GGCGAGTA,ACTTCTAT,CAAATACG,TTGCGCGC"
SI_GA_H12 = "SI-GA-H12,GACAGCAT,TTTGTACA,AGGCCGTG,CCATATGC"

TENX_INDEX_CHOICES = (
    (SI_GA_A1, "SI-GA_A1"),
    (SI_GA_A2, "SI-GA-A2"),
    (SI_GA_A3, "SI-GA-A3"),
    (SI_GA_A4, "SI-GA-A4"),
    (SI_GA_A5, "SI-GA-A5"),
    (SI_GA_A6, "SI-GA-A6"),
    (SI_GA_A7, "SI-GA-A7"),
    (SI_GA_A8, "SI-GA-A8"),
    (SI_GA_A9, "SI-GA-A9"),
    (SI_GA_A10, "SI-GA-A10"),
    (SI_GA_A11, "SI-GA-A11"),
    (SI_GA_A12, "SI-GA-A12"),
    (SI_GA_B1, "SI-GA-B1"),
    (SI_GA_B2, "SI-GA-B2"),
    (SI_GA_B3, "SI-GA-B3"),
    (SI_GA_B4, "SI-GA-B4"),
    (SI_GA_B5, "SI-GA-B5"),
    (SI_GA_B6, "SI-GA-B6"),
    (SI_GA_B7, "SI-GA-B7"),
    (SI_GA_B8, "SI-GA-B8"),
    (SI_GA_B9, "SI-GA-B9"),
    (SI_GA_B10, "SI-GA-B10"),
    (SI_GA_B11, "SI-GA-B11"),
    (SI_GA_B12, "SI-GA-B12"),
    (SI_GA_C1, "SI-GA-C1"),
    (SI_GA_C2, "SI-GA-C2"),
    (SI_GA_C3, "SI-GA-C3"),
    (SI_GA_C4, "SI-GA-C4"),
    (SI_GA_C5, "SI-GA-C5"),
    (SI_GA_C6, "SI-GA-C6"),
    (SI_GA_C7, "SI-GA-C7"),
    (SI_GA_C8, "SI-GA-C8"),
    (SI_GA_C9, "SI-GA-C9"),
    (SI_GA_C10, "SI-GA-C10"),
    (SI_GA_C11, "SI-GA-C11"),
    (SI_GA_C12, "SI-GA-C12"),
    (SI_GA_D1, "SI-GA-D1"),
    (SI_GA_D2, "SI-GA-D2"),
    (SI_GA_D3, "SI-GA-D3"),
    (SI_GA_D4, "SI-GA-D4"),
    (SI_GA_D5, "SI-GA-D5"),
    (SI_GA_D6, "SI-GA-D6"),
    (SI_GA_D7, "SI-GA-D7"),
    (SI_GA_D8, "SI-GA-D8"),
    (SI_GA_D9, "SI-GA-D9"),
    (SI_GA_D10, "SI-GA-D10"),
    (SI_GA_D11, "SI-GA-D11"),
    (SI_GA_D12, "SI-GA-D12"),
    (SI_GA_E1, "SI-GA-E1"),
    (SI_GA_E2, "SI-GA-E2"),
    (SI_GA_E3, "SI-GA-E3"),
    (SI_GA_E4, "SI-GA-E4"),
    (SI_GA_E5, "SI-GA-E5"),
    (SI_GA_E6, "SI-GA-E6"),
    (SI_GA_E7, "SI-GA-E7"),
    (SI_GA_E8, "SI-GA-E8"),
    (SI_GA_E9, "SI-GA-E9"),
    (SI_GA_E10, "SI-GA-E10"),
    (SI_GA_E11, "SI-GA-E11"),
    (SI_GA_E12, "SI-GA-E12"),
    (SI_GA_F1, "SI-GA-F1"),
    (SI_GA_F2, "SI-GA-F2"),
    (SI_GA_F3, "SI-GA-F3"),
    (SI_GA_F4, "SI-GA-F4"),
    (SI_GA_F5, "SI-GA-F5"),
    (SI_GA_F6, "SI-GA-F6"),
    (SI_GA_F7, "SI-GA-F7"),
    (SI_GA_F8, "SI-GA-F8"),
    (SI_GA_F9, "SI-GA-F9"),
    (SI_GA_F10, "SI-GA-F10"),
    (SI_GA_F11, "SI-GA-F11"),
    (SI_GA_F12, "SI-GA-F12"),
    (SI_GA_G1, "SI-GA-G1"),
    (SI_GA_G2, "SI-GA-G2"),
    (SI_GA_G3, "SI-GA-G3"),
    (SI_GA_G4, "SI-GA-G4"),
    (SI_GA_G5, "SI-GA-G5"),
    (SI_GA_G6, "SI-GA-G6"),
    (SI_GA_G7, "SI-GA-G7"),
    (SI_GA_G8, "SI-GA-G8"),
    (SI_GA_G9, "SI-GA-G9"),
    (SI_GA_G10, "SI-GA-G10"),
    (SI_GA_G11, "SI-GA-G11"),
    (SI_GA_G12, "SI-GA-G12"),
    (SI_GA_H1, "SI-GA-H1"),
    (SI_GA_H2, "SI-GA-H2"),
    (SI_GA_H3, "SI-GA-H3"),
    (SI_GA_H4, "SI-GA-H4"),
    (SI_GA_H5, "SI-GA-H5"),
    (SI_GA_H6, "SI-GA-H6"),
    (SI_GA_H7, "SI-GA-H7"),
    (SI_GA_H8, "SI-GA-H8"),
    (SI_GA_H9, "SI-GA-H9"),
    (SI_GA_H10, "SI-GA-H10"),
    (SI_GA_H11, "SI-GA-H11"),
    (SI_GA_H12, "SI-GA-H12"),
)
