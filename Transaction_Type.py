Debit_ATM_Green = ['Interest'] + ['Cash Advance - ATM'] * 2 + ['Purchase'] * 19
Debit_ATM_Yellow = ['Interest'] + ['Cash Advance - ATM'] * 5 + ['Purchase'] * 19
Debit_ATM_Red = ['Interest'] + ['Cash Advance - ATM'] * 7 + ['Purchase'] * 10
Merchant_Credits_Green = ['Merchant Credit'] + ['ACH Payment','Paper Check'] * 9
Merchant_Credits_Yellow = ['Merchant Credit'] + ['ACH Payment','Paper Check'] * 3
Merchant_Credits_Red = ['Merchant Credit','ACH Payment','Paper Check']
Payments= ['Cash Payment','Wire Payment','ACH Payment','Paper Check','e-Check Check','Online Transfer','ATM Payment']
Credits = ['Payment','Reversal','Award']
Debit = ['Purchase','Fee','Interest Charge','Penalty','Refund']
Debit_Ovpmt_Green = ['Fee','Interest Charge','Penalty','Refund'] + ['Purchase'] * 23
Debit_Ovpmt_Yellow = ['Fee','Interest Charge','Penalty','Refund'] + ['Purchase'] * 7
Debit_Ovpmt_Red = ['Purchase','Fee','Interest Charge','Penalty','Refund']
Debit_Refund_Green = ['Cash Payment','Wire Payment','Paper Check','e-Check','Online Transfer','ATM Payment','Reversal','Award'] + ['ACH Payment'] * 2 + ['Refund'] * 6
Debit_Refund_Yellow = ['Cash Payment','Wire Payment','Paper Check','e-Check','Online Transfer','ATM Payment','Reversal','Award'] + ['ACH Payment'] * 2 + ['Refund'] * 15
Debit_Refund_Red = ['Cash Payment','Wire Payment','Paper Check','e-Check','Online Transfer','ATM Payment','Reversal','Award'] + ['ACH Payment'] * 2 + ['Refund'] * 21
Debit_Payments_Green = ['Interest Charge'] * 8 + ['Purchase'] * 10
Debit_Payments_Yellow = ['Interest Charge'] * 4 + ['Purchase'] * 5
Debit_Payments_Red = ['Purchase','Interest Charge'] * 2
Debit_10_41No19_21No25_27 = ['Fee','Interest Charge','Penalty','Refund'] + ['Purchase'] * 35
Credits_ATM = ['Cash Payment','Wire Payment','ACH Payment','Paper Check','e-Check']
Merchant_Debit = ['Interest'] + ['Purchase'] * 9
Credits_Ovpmt_Refund = ['Cash Payment','Wire Payment','Paper Check','e-Check','Online Transfer','ATM Payment','Reversal','Award'] + ['ACH Payment'] * 2
Credits_Payments = ['Cash Payment','Wire Payment'] * 2 + ['ACH Payment'] * 4
Credits_Refund_Red = ['Refund','Refund','Refund','Refund','Refund','Refund','Refund','Refund','Refund','Refund','Refund','Refund','Refund','Refund','Refund','Refund','Refund','Refund','Refund','Refund','Refund','Cash Payment','Wire Payment','ACH Payment','ACH Payment','Paper Check','e-Check','Online Transfer','ATM Payment','Reversal','Award']
Credits_Refund_Yellow = ['Refund','Refund','Refund','Refund','Refund','Refund','Refund','Refund','Refund','Refund','Refund','Refund','Refund','Refund','Refund','Cash Payment','Wire Payment','ACH Payment','ACH Payment','Paper Check','e-Check','Online Transfer','ATM Payment','Reversal','Award']
Credits_Refund_Green = ['Refund','Refund','Refund','Refund','Refund','Refund','Cash Payment','Wire Payment','ACH Payment','ACH Payment','Paper Check','e-Check','Online Transfer','ATM Payment','Reversal','Award']
Credits_10_41No19_21No25_27 = ['Cash Payment','Wire Payment','ACH Payment','ACH Payment','Paper Check','e-Check','Online Transfer','ATM Payment','Reversal','Award']
