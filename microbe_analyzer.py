# ==========================================
# Project: Global Microbiology Standard Tool
# Lead Scientist: Ahmad Kamaal Pasha
# Standard: Based on WHO & IGNOU Page-21
# ==========================================

def identify_microbe():
    print("--------------------------------------------------")
    print("      PASHA GLOBAL BIO-SAFETY CONSULTANCY         ")
    print("   Microbial Identification Tool (Version 1.0)    ")
    print("--------------------------------------------------")
    
    print("\n[STEP 1] Select the Culture Media used (Based on Page-21):")
    print("1. EMB (Eosin Methylene Blue Agar)")
    print("2. PEA (Phenylethyl Alcohol Agar)")
    print("3. Blood Agar")
    
    choice = input("\nEnter choice (1/2/3): ")

    # Logic for EMB Agar (Selection and Differentiation)
    if choice == '1':
        print("\nChecking for Gram-Negative Bacteria (Coliforms)...")
        appearance = input("Enter Colony Appearance (e.g., Green Metallic Sheen / Pink / Clear): ").lower()
        
        if "green" in appearance:
            print("\n>>> ANALYSIS BY A.K. PASHA: Strong Lactose Fermentation.")
            print(">>> RESULT: High probability of Escherichia coli (E. coli).")
            print(">>> GLOBAL COMPLIANCE: Fecal contamination suspected. Action required.")
        elif "pink" in appearance:
            print("\n>>> ANALYSIS BY A.K. PASHA: Weak Lactose Fermenter.")
            print(">>> RESULT: Likely Klebsiella or Enterobacter species.")
        else:
            print("\n>>> ANALYSIS BY A.K. PASHA: Non-Lactose Fermenter.")
            print(">>> RESULT: Non-fecal coliform detected.")

    # Logic for PEA Agar (Selective Media)
    elif choice == '2':
        print("\n>>> ANALYSIS BY A.K. PASHA: PEA is a Purely Selective Medium.")
        print(">>> RESULT: Promoting Gram-Positive Growth / Suppressing Gram-Negative.")

    # Logic for Blood Agar (Differential & Complex Media)
    elif choice == '3':
        print("\nChecking for Hemolysis patterns...")
        hemolysis = input("Enter Hemolysis type (Alpha/Beta/Gamma): ").lower()
        print(f"\n>>> ANALYSIS BY A.K. PASHA: Differential analysis for {hemolysis} hemolysis completed.")
        print(">>> RESULT: Based on hemoglobin degradation standards.")

    else:
        print("\nERROR: Invalid selection. Please refer to WHO Lab Manual.")

if __name__ == "__main__":
    identify_microbe()
