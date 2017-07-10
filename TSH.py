print ("Welcome to the Thyroid Testing Pathway Program")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
sTSH= float(input("Please enter your sTSH value in mU/L: "))
if sTSH <= 5.0 and sTSH >=0.4:
    print ("TSH value is consistent with a normal state. Further thryoid testing is not recommended.")
elif sTSH > 5.0:
    print ("Please run an FT4 test")
    FT4= float(input("Enter FT4 results here in pmol/L: "))
    if FT4 > 28 :
        print("Results are consistent with secondary pituitary hypothyroidism.")
    elif FT4 < 10:
        print("Results are consistent with primary pituitary hypothyroidism.")
    else:
        print("Results are consistent with subclinical hypothyroidism.")
elif sTSH < 0.40:
    print("Please run an FT4 test")
    FT4 = float(input("Enter FT4 results here in pmol/L: "))
    if FT4 > 28:
        print("Results are consistent with primary hyperthyroidism.")
    elif FT4 < 10:
        print("Results are consistent with secondary pituitary hypothyroidism.")
    else:
        print("Please perform an FT3.")
        FT3 = input("Please enter if your FT3 is Low, Normal or High according to your reference range. Please use the terms here: ")
        FT3 = FT3.lower()
        if FT3 == "normal" or FT3 == "low":
            print("Results indicate a probable euthyroid condition. It is recommended to repeat the TSH later when the patient is well")
        else:
            print("Results are consistent with T3 Thyrotoxicosis")