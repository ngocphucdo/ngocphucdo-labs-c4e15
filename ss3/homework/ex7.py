import string
st = input("Write down st here: ")
def remove_dollar_sign(st):
    prettier_str = st.replace("$","")
    return prettier_str
s = remove_dollar_sign(st)
print(s)
