#https://stackoverflow.com/questions/33159518/collapse-cell-in-jupyter-notebook
#https://peopledoc.github.io/workalendar/basic.html
from datetime import date
from datetime import timedelta
from datetime import datetime
from calendar import monthrange
from calendra.europe import Sweden
import pandas as pd 
# exec(open("calendar_test.py").read())





## find month
data = pd.read_csv("input_py.csv",sep=';')
data = data.fillna(0)
data['date_'] = data.apply(lambda x: datetime.strptime(x['date'], '%Y-%m-%d'), axis=1)
data = data.set_index('date_')
#data[(data.index.year==2019)&(data.index.month==5)]

#for d in all_months:
#	month_df = data[(data.index.year==d.year)&(data.index.month==d.month)]
#month_df = data[(data.index.year==2019)&(data.index.month==6)]
startyear = 2019
startmonth = 5
endyear = 2021
endmonth = 1
all_months = [date(m//12, m%12+1, 1) for m in range(startyear*12+startmonth-1, endyear*12+endmonth)]



month_df = data[(data.index.year==2019)&(data.index.month==7)]
calc_salary_julia(month_df)
calc_salary_filip(month_df)



list_of_output = []
for i in all_months:
	month_df = data[(data.index.year==i.year)&(data.index.month==i.month)]
	filip_output = calc_salary_filip(month_df)
	filip_output['name'] = 'filip'
	julia_output = calc_salary_julia(month_df)
	julia_output['name'] = 'julia'
	list_of_output.append(filip_output)
	list_of_output.append(julia_output)
	#print(i,",",calc_salary_julia(month_df),",",calc_salary_filip(month_df),",",get_num_parent_days_julia(month_df),",",get_num_parent_days_filip(month_df))

pd_output = pd.DataFrame(list_of_output)
pd_output.to_csv('out.csv',index=False)

