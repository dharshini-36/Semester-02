class Calculate:
    def cal_final_price(self,base_price,dis_per,tax_per):
        if base_price<=0 or dis_per<=0 or tax_per<=0:
            raise ValueError ("Amount, discount and tax percentage cannot be zero or negative")
        discounted_price=base_price*(dis_per/100)
        tax=base_price*(tax_per/100)
        total_amt=base_price-discounted_price+tax
        print(f"Final price: {total_amt:.2f}")

calc=Calculate()
try:
    base_price=float(input("Enter the price of the product"))
    dis_per=float(input("Enter the discount percentage: "))
    tax_per=float(input("Enter the tax percentage: "))
    calc.cal_final_price(base_price,dis_per,tax_per)
except ValueError as ve:
    print(ve)


