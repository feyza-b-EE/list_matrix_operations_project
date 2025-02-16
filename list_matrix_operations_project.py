# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 20:33:46 2023

@author: Feyza
"""
my_name = "Ayse Feyza Birer"
my_id = "220102002033"
my_email = "a.birer2022@gtu.edu.tr"

def problem1(row=" ",column=" "):
    result = ""
    if row == 1 and column == 1:
        result = 1 
        return result
    elif column == 1 and row > 1:
        result = 3
        return result
    elif row == column and row > 1:
        result = 2
        return result
    else:
        if column < row: 
            result = problem1(row-1, column-1) + problem1(row-1,column)
            return result

def problem2(s1=" ", s2=" "):
   x = 0 
   length = ""
   if len(s1) < len(s2):
       length = len(s1)
   else:
       length = len(s2)
   for i in range(length):
       if s1[i] == s2[i]:
           x += 1  
   return x      
        
        
def problem3(accounts=" ", source=" ", destination=" ", lira=" ", kurus=" ",fee= True):
    if source < 0  or destination < 0:
        return accounts
    elif source > len(accounts) or destination > len(accounts):
        return accounts
    elif source == destination:
        return accounts
    else:
        if fee == True:
            if (float(lira) + float(kurus*1/100)) < 10:
                if float(accounts[source]) < float(lira) + float((kurus*1/100)) + 0.1:
                    return accounts
                else:
                    accounts[source] =   str(round(float(accounts[source]) - float(lira) - float((kurus*1/100)) - 0.1, 2))
                    accounts[destination] = str(round(float(accounts[destination]) + float(lira) + float((kurus*1/100)), 2))
            elif (float(lira) + float((kurus*1/100))) > 10:
                x = 1/100 * (float(lira) + float(kurus*1/100))
                y = round(x,2)
                if float(accounts[source]) < float(lira) + float((kurus*1/100)) + y:
                    return accounts
                else:
                    accounts[source] =   str(round(float(accounts[source]) - float(lira) - float((kurus*1/100)) - y, 2))
                    accounts[destination] = str(round(float(accounts[destination]) + float(lira) + float((kurus*1/100)), 2))
        
        elif fee == False:
            accounts[source] = str(round(float(accounts[source]) - float(lira) - float((kurus*1/100)), 2))
            accounts[destination] = str(round(float(accounts[destination]) + float(lira) + float((kurus*1/100)), 2))

    return accounts
                
                