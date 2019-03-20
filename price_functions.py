

def calc_salary_julia(month_df):
	from calendar import monthrange
	from datetime import date
	from datetime import datetime
	# julia
	month = month_df.head(1).index.month[0]
	year = month_df.head(1).index.year[0]
	num_days_in_month = monthrange(year,month)[1]
	julia_salary_monthly = 31800
	sgi_year = 31800*12
	julia_p_kr_per_day = ((sgi_year*0.8*0.97))/365
	julia_pwc_bonus_kr_per_day = ((sgi_year*0.2*0.5))/365
	vacation_bonus_kr_per_day = (julia_salary_monthly*0.0043)
	
	## variables
	num_vacation_days = sum(month_df['vacation_j']*month_df['workday'])
	all_parent_days_j = month_df[['work_bonus_day_j','parent_day_j']].max(axis=1)
	num_total_parent_days = sum(all_parent_days_j.multiply(month_df['multi_j']))
	num_work_bonus_days = sum(month_df['work_bonus_day_j'])
	num_p_julia = sum(month_df['parent_day_j'])
	
	# decide removal of salary
	if (sum(all_parent_days_j)==num_days_in_month):
		remove_from_salary_julia = julia_salary_monthly
	else:
		remove_from_salary_julia = ((31800*12)/365)*sum(all_parent_days_j)
	#decide money from FK
	salary_from_work = julia_salary_monthly - remove_from_salary_julia
	from_fk_julia = julia_p_kr_per_day*num_total_parent_days
	from_pwc_bonus = num_work_bonus_days*julia_pwc_bonus_kr_per_day
	from_vacation_bonus = num_vacation_days*vacation_bonus_kr_per_day
	total_salary = from_fk_julia +from_pwc_bonus+ salary_from_work + from_vacation_bonus
	output = {}
	output['total_salary'] = total_salary
	output['month'] = date(year,month,1)
	output['num_vacation_days'] = num_vacation_days
	output['num_total_parent_days'] = num_total_parent_days
	output['num_work_bonus_days'] = num_work_bonus_days
	output['salary_from_work'] = salary_from_work
	return output

def calc_salary_filip(month_df):
	from calendar import monthrange
	from datetime import date
	from datetime import datetime
	# filip
	month = month_df.head(1).index.month[0]
	year = month_df.head(1).index.year[0]
	num_days_in_month = monthrange(year,month)[1]
	filip_salary_monthly = 42000
	bb_10 = 46500*10
	salary_over_10bb_yearly = (filip_salary_monthly*12)-bb_10
	salary_below_10bb_yearly = filip_salary_monthly*12 - salary_over_10bb_yearly
	filip_klarna_bonus_kr_per_day = ((salary_below_10bb_yearly*0.2)+ (salary_over_10bb_yearly))/365
	filip_p_kr_per_day = ((salary_below_10bb_yearly*0.8*0.97))/365
	vacation_bonus_kr_per_day = (filip_salary_monthly*0.0043)
	## variables
	num_vacation_days = sum(month_df['vacation_f']*month_df['workday'])
	all_parent_days_filip = month_df[['work_bonus_day_f','parent_day_f','10d_f']].max(axis=1)
	num_total_parent_days = sum(all_parent_days_filip.multiply(month_df['multi_f']))
	num_work_bonus_days = sum(month_df['work_bonus_day_f'])
	#num_p_filip = sum(month_df[['parent_day_f','10d_f']].max(axis=1))
	# decide removal of salary
	remove_from_salary_filip=0
	if (sum(all_parent_days_filip)==num_days_in_month):
		remove_from_salary_filip = filip_salary_monthly
	else:
		remove_from_salary_filip = ((filip_salary_monthly*12)/365)*sum(all_parent_days_filip)

	salary_from_work = filip_salary_monthly - remove_from_salary_filip
	from_fk_filip = filip_p_kr_per_day*num_total_parent_days
	from_klarna_bonus = num_work_bonus_days*filip_klarna_bonus_kr_per_day
	from_vacation_bonus = num_vacation_days*vacation_bonus_kr_per_day
	total_salary = from_fk_filip + from_klarna_bonus + salary_from_work + num_vacation_days*vacation_bonus_kr_per_day	
	## store output
	output = {}
	output['total_salary'] = total_salary
	output['month'] = date(year,month,1)
	output['num_vacation_days'] = num_vacation_days
	output['num_total_parent_days'] = num_total_parent_days
	output['num_work_bonus_days'] = num_work_bonus_days
	output['salary_from_work'] = salary_from_work
	return output
