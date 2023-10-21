import streamlit as st
from PIL import Image
import pickle


model = pickle.load(open('ML_Model1.pkl','rb'))

def run():
    img1 = Image.open('bank.png')
    img1 = img1.resize((156,145))
    st.image(img1,use_column_width=False)
    st.title("Bank Loan Prediction ")

    ## Loan_id
    loan_id = st.text_input('Loan_ID')

    ## For Marital Status
    mar_display = ('No','Yes')
    mar_options = list(range(len(mar_display)))
    mar = st.selectbox("Marital Status", mar_options, format_func=lambda x: mar_display[x])

    ## For Gender
    gen_display = ('Male','Female')
    gen_options = list(range(len(gen_display)))
    gen = st.selectbox("Gender",gen_options, format_func=lambda x: gen_display[x])

    ## No of dependets
    dep_display = ('No','One','Two','More than Two')
    dep_options = list(range(len(dep_display)))
    dep = st.selectbox("Dependents",  dep_options, format_func=lambda x: dep_display[x])

    ## For Education
    edu_display = ('Not Graduate','Graduate')
    edu_options = list(range(len(edu_display)))
    edu = st.selectbox("Education",edu_options, format_func=lambda x: edu_display[x])

    ## For Self Employed
    emp_display = ('No','Yes')
    emp_options = list(range(len(emp_display)))
    emp = st.selectbox("Employment Status",emp_options, format_func=lambda x: emp_display[x])

    ## Applicant Monthly Income
    mon_income = st.number_input("Applicant's Monthly Income($)",value=0)

    ## Co-Applicant Monthly Income
    co_mon_income = st.number_input("Co-Applicant's Monthly Income($)",value=0)

    ## Loan Amount
    loan_amt = st.number_input("Loan Amount",value=0)

    ## Loan Duration Term
    dur_display = ['2 Month','6 Month','8 Month','1 Year','16 Month']
    dur_options = range(len(dur_display))
    dur = st.selectbox("Loan Duration Term",dur_options, format_func=lambda x: dur_display[x])

    ## For Property status
    prop_display = ('Urban','Rural','Semiurban')
    prop_options = list(range(len(prop_display)))
    prop = st.selectbox("Property Area",prop_options, format_func=lambda x: prop_display[x])

    ## For Credit History
    cred_display = ('0','1')
    cred_options = list(range(len(cred_display)))
    cred = st.selectbox("Credit History",cred_options, format_func=lambda x: cred_display[x])


    if st.button("Submit"):
        duration = 0
        if dur == 0:
            duration = 60
        if dur == 1:
            duration = 180
        if dur == 2:
            duration = 240
        if dur == 3:
            duration = 360
        if dur == 4:
            duration = 480
        income_sum = mon_income + co_mon_income    
        features = [[mar, mon_income, co_mon_income, loan_amt, duration, cred, prop,income_sum]]
        print(features)
        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        if ans == 0:
            st.error(
                
                "Account number: "+loan_id +' || '
                'According to our Calculations, you can not give this loan to the customer'
            )
        else:
            st.success(
                
                "Account number: "+loan_id +' || '
                'Good news!! you can give this loan to the customer'
            )

run()