#data is coming in down way

#
# import pickle
# import streamlit as st
#
# with open('Loan_model.pkl','rb') as f:
#     model = pickle.load(f)
#
#
# # Define the user interface
# st.title('Predict if person fully paid or not')
# feature_names = ['credit.policy', 'int.rate', 'installment', 'log.annual.inc', 'dti',
#        'fico', 'days.with.cr.line', 'revol.bal', 'revol.util',
#        'inq.last.6mths', 'delinq.2yrs', 'pub.rec',
#        'purpose_credit_card', 'purpose_debt_consolidation',
#        'purpose_educational', 'purpose_home_improvement',
#        'purpose_major_purchase', 'purpose_small_business']
#
# inputs = []
#
# credits_val = st.selectbox(feature_names[0],[0,1])
# inputs.append(credits_val)
#
# for feature_name in feature_names[1:9]:
#     value = st.number_input(feature_name)
#     inputs.append(value)
#
# feature_slider={feature_names[9]:(0,32),feature_names[10]:(0,11),feature_names[11]:(0,5)}
#
# for feature_name, feature_range in feature_slider.items():
#     value = st.slider(feature_name, feature_range[0], feature_range[1])
#     inputs.append(value)
#
# for feature_name in feature_names[-6:]:
#     value = st.selectbox(feature_name,[0,1])
#     inputs.append(value)
#
# # Make predictions and show the results
# if st.button('Predict'):
#     inputs_array = [inputs]
#     prediction = model.predict(inputs_array)[0]
#     if prediction == 0:
#         st.write('The person did not fully pay.')
#     else:
#         st.write('The person fully paid.')


#Data shown in the side by side manner
import pickle
import streamlit as st

with open('Loan_model.pkl','rb') as f:
    model = pickle.load(f)


# Define the user interface
st.title('Loan Repayment Status')
feature_names = ['credit.policy', 'int.rate', 'installment', 'log.annual.inc', 'dti',
       'fico', 'days.with.cr.line', 'revol.bal', 'revol.util',
       'inq.last.6mths', 'delinq.2yrs', 'pub.rec',
       'purpose_credit_card', 'purpose_debt_consolidation',
       'purpose_educational', 'purpose_home_improvement',
       'purpose_major_purchase', 'purpose_small_business']

inputs = []

col1, col2, col3 = st.columns(3)

credits_val = col1.selectbox(feature_names[0],[0,1])
inputs.append(credits_val)

for feature_name in feature_names[1:9]:
    value = col1.number_input(feature_name)
    inputs.append(value)

feature_slider={feature_names[9]:(0,100),feature_names[10]:(0,100),feature_names[11]:(0,10)}

for feature_name, feature_range in feature_slider.items():
    value = col2.slider(feature_name, feature_range[0], feature_range[1])
    inputs.append(value)

for feature_name in feature_names[-6:]:
    value = col3.selectbox(feature_name,[0,1])
    inputs.append(value)



# Define the user interface
st.sidebar.title('Menu')

if st.sidebar.button('View Feature Information'):
    # Display the tax information in point format
    st.sidebar.markdown('All the Data is used of Lending club website 2016-2017 data')
    st.sidebar.markdown('* credit.policy: 1 if the customer meets the credit underwriting criteria of '
                        'LendingClub.com, and 0 otherwise.')
    st.sidebar.markdown('* int.rate: The interest rate of the loan, as a proportion (a rate of 11% would be stored as '
                        '0.11). Borrowers judged by LendingClub.com to be more risky are assigned higher interest '
                        'rates.')
    st.sidebar.markdown('* installment: The monthly installments owed by the borrower if the losan is funded.')
    st.sidebar.markdown('* log.annual.inc: The natural log of the self-reported annual income of the borrower.')
    st.sidebar.markdown('* dti: The debt-to-income ratio of the borrower (amount of debt divided by annual income')
    st.sidebar.markdown('* days.with.cr.line: The number of days the borrower has had a credit line.')
    st.sidebar.markdown('* revol.bal: The borrowers revolving balance (amount unpaid at the end of the credit card '
                        'billing cycle')
    st.sidebar.markdown('* revol.util: The borrowers revolving line utilization rate (the amount of the credit line '
                        'used relative to total credit available.')
    st.sidebar.markdown('* inq.last.6mths: The borrower number of inquiries by creditors in the last 6 months.')
    st.sidebar.markdown('* delinq.2yrs: The number of times the borrower had been 30+ days past due on a payment in '
                        'the past 2 years.')
    st.sidebar.markdown('* pub.rec: The borrowers number of derogatory public records (bankruptcy filings, tax liens, '
                        'or judgments)')

#Make predictions and show the results
if st.button('Predict'):
    inputs_array = [inputs]
    prediction = model.predict(inputs_array)[0]
    if prediction == 0:
        st.error('The person did not fully pay.')
    else:
        st.success('The person fully paid.')


# Make predictions and show the results
# if st.button('Predict'):
#     inputs_array = [inputs]
#     prediction = model.predict(inputs_array)[0]
#     if prediction == 0:
#         result = 'The person did not fully pay.'
#     else:
#         result = 'The person fully paid.'
#
#     # create a popup window to show the result
#     st.write('<span style="font-size:30px"><b>Result:</b></span>', unsafe_allow_html=True)
#     st.write('')
#     st.write(result,font_size=60,unsafe_allow_html=True)


